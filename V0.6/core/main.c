//./core/main.c

/*
                        ===========================================================
                                 IgniteAuth Core Execution Controller
                        ===========================================================

Information:

1. This module represents the IgniteAuth core control-plane
   executor responsible for coordinating authentication,
   policy evaluation, and controlled subsystem execution.

2. It operates as the Policy Enforcement Point (PEP):
      - Collects execution intent and parameters
      - Sends requests to the external policy server
      - Enforces the returned authorization decision

3. All execution requests are evaluated remotely by the
   policy engine. This module NEVER makes authorization
   decisions locally.

4. Execution of subsystem binaries occurs only when an
   explicit ALLOW decision is received from the policy
   server, ensuring strict separation between:
      - Authorization (policy server)
      - Enforcement (this module)
      - Execution (subsystem binaries)

5. Communication with the policy server is performed using
   HTTP over libcurl with structured JSON payloads.

6. This design prevents direct command execution based on
   user input and enforces intent-based, policy-driven
   execution semantics.

Security Principles:
- Explicit authorization over implicit trust
- Control-plane and data-plane separation
- Least privilege execution via isolated binaries

===========================================================
*/


#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>
#include<unistd.h>

#include<curl/curl.h>

#include "IG_executor.h"
#include "../include/IG_targets.h"


/* =========================
   Authentication - basic and subtle 
   ========================= */

bool authenticator(const char *username, const char *password)
{

    if(strcmp(username, "ig_admin")!=0)  return false ;

    if(strcmp(password, "passwd")!=0)  return false ;

    return true ;
    
}

void strip_newline(char *str) {


        str[strcspn(str, "\n")] = 0; 
    
}


/* =========================
   CURL response buffer
   ========================= */

struct response_buffer {

    char *data;
    size_t size;

};

// response buffer 
size_t write_cb(void *contents, size_t size, size_t nmemb, void *userp) {
    size_t total = size * nmemb;
    struct response_buffer *buf = (struct response_buffer *)userp;

    char *tmp = realloc(buf->data, buf->size + total + 1);
    if (!tmp) return 0;

    buf->data = tmp;
    memcpy(buf->data + buf->size, contents, total);
    buf->size += total;
    buf->data[buf->size] = '\0';

    return total;
}


// main

int main (int argc, char *argv[])
{

    if(argc != 5)
    {

         printf("Usage: %s <sid> <intent> <command> <target>\n", argv[0]);
         return 1;
    
    }

    char username[32];
    char password[32];

    printf("IgniteAuth Login\n");
    printf("Username : ");
    fgets(username, sizeof(username), stdin);
    strip_newline(username);

    printf("Password : ");
    fgets(password, sizeof(password), stdin);
    strip_newline(password);

    if(!authenticator(username, password)){

        printf("Authentication Failure\n");
        return 1;
    }

    printf("Login Successful\n");
    
    // inputs 
    char sid[32];
    char intent[32];
    char command[32];
    char target[32];

    strncpy(sid, argv[1],sizeof(sid)-1);
    strncpy(intent, argv[2], sizeof(intent) - 1);
    strncpy(command, argv[3], sizeof(command) - 1);
    strncpy(target, argv[4], sizeof(target) - 1);


    sid[31] = intent[31] = command[31] = target[31] = '\0';




    /* -------- Temporary Policy Bypass (TEST ONLY) --------
   Direct execution path for vmware target.
   This bypasses IgniteAuth policy enforcement
   and is intended strictly for execution testing.
------------------------------------------------------ */

    if (strcmp(target, "vmware") == 0) {
        printf("[TEST MODE] Bypassing policy for VMware launch\n");
        execute_target_bin(SUB_VMWARE);
        return 0;
    }


    

    // policy request 

    CURL *curl = curl_easy_init();
        
    if(!curl) {

        printf("Failed to init curl\n");
        return 1;
    }

    struct response_buffer resp = {0} ; // response buffer set to NULL
    struct curl_slist *headers = NULL;

    headers = curl_slist_append(headers, "Content-Type: application/json");

    char payload[256];
    snprintf(payload, sizeof(payload),
            "{\"sid\":\"%s\",\"intent\":\"%s\",\"command\":\"%s\",\"target\":\"%s\"}",
            sid, intent, command, target
    );
        
    

    // code for curl request to server
    // stdin -> payload -> curl client -> server (Flask Policy engine) -> response from server (raw)-> capture buffer and send json
    // execution decision further .... with verification of target  on core     



    curl_easy_setopt(curl, CURLOPT_URL, "http://127.0.0.1:2000/policy_engine");
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, payload);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_cb);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &resp);

    CURLcode res = curl_easy_perform(curl);

    if(res!=CURLE_OK){

        fprintf(stderr, "curl error : %s\n", curl_easy_strerror(res));
        goto cleanup ;
        
    }

    printf("Policy Response : %s\n", resp.data);


    /* -------- Policy Enforcement -------- */
    if(resp.data && strstr(resp.data, "\"allow\": true")){

        if(strcmp(target, "gpio")==0)
            execute_target_bin(SUB_GPIO);

        else if (strcmp(target, "driver")==0)
            execute_target_bin(SUB_DRIVER);

        else if (strcmp(target, "uart")==0)
            execute_target_bin(SUB_UART);

         else 
            printf("Unknown target\n");
    
    }else {

            printf("Execution Denied by IgniteAuth Policy\n");
        
    }
    

// cleanup

cleanup : 
    curl_easy_cleanup(curl);
    curl_slist_free_all(headers);
    free(resp.data);


    return 0;

}











