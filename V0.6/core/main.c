// ./core/main.c

// main system source 

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>
#include<stdbool.h>
#include<curl/curl.h> // libcurl for API

// #include<curl/curl.h> HTTP requests are sent from here  - POST request to server : @ ../policy/server.py 

// includes 
#include "IG_executor.h"  // imports execute_target_bin()
// #include "../include/IG_targets.h" generally declared in IG_executor for target map import 


bool authenticator(char *username, char *password) {

    if(!(strcmp(username, "ig_admin")==0 || strcmp(password, "passwd@ig"))) return false;

    return true;
}



void strip_newline(char *str){


	str[strcspn,'\n'] = 0;
    
}

int main(int argc, char *argv[]) {
    
    void login() {
        
    printf("IgniteAuth Login: \n");
    char username[20];
    char password[30];

    printf("Username : ");
    fgets(username, sizeof(username), stdin);
    strip_newline(username);
        
    printf("\nPassword : ");
    fgets(password, sizeof(password),stdin);
    strip_newline(password);
        
    
    if(!(authenticator(username, password))) {

        printf("Username or Password Incorrect\n");
        login();   // recursion
    }

} //  end login 

    // call login 
    login();
    sleep(1);
    printf("Login Successful\n");
    printf("Welcome to IgniteAuth");
    
    //  sid, intent, command, target declaration

    char sid[32];
    char intent[16];
    char command[32];
    char target[16];
    
    // 4 params from stdin
    strncpy(sid, argv[1],sizeof(sid)-1);  
    sid[sizeof(sid)-1] = '\0';
    
    strncpy(intent, argv[2],sizeof(intent)-1);
    intent[sizeof(intent)-1] = '\0';
    
    strncpy(command, argv[3],sizeof()-1);  
    command[sizeof(command)-1] = '\0';
    
    strncpy(target, argv[4],sizeof(target)-1);
    target[sizeof(target)-1] = '\0';


    

    
    
    // POST request the parameters as json inputs 
    curl->POST('localhost:2000/policy_engine', (req,res) -> {

        jsonify({"sid":sid,  "intent":intent, "command":command, "target" : target});
        
    }
    
    int return_value = curl.res // response from 
}
    
    if(return_value) {

        if target == "driver" || target=="DRIVER"
        execute_target_bin(SUB_DRIVER)

        if target == "uart" || target=="UART"
        execute_target_bin(SUB_UART)

        if target == "MPU" || target=="mpu"
        execute_target_bin(SUB_MPU)

        
        
    }

    