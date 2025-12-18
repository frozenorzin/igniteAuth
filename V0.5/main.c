/* 
                            
                            Documentation - IgniteAuth plane MAIN system executable 

                           -> Main systems holds the architecture  
                           -> IA plane will act as control policy plane when  sub_system execution  triggered 
                           -> policy in IG_Policy.h => holds the policy model 
                           -> subsystem header map to call desired executabe using spawn(), fork(), system() anything for now .. 


                           Important operations :
                           subsystemcall ->  run_bin(SUBxPATH);


*/


// general headers ... 
#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>
#include<string.h>
#include<process.h> //spawnl()
#include<time.h>   // for logging timestamp
#include<unistd.h>

// the control plane policy ...
#include "./header/IG_Policy.h"        // consists of validate_command engine 
#include "./targets/sub_system_map.h" // subsystem holding map .... 


// request handling parameters - Client Plane to STDOUT API  
// handled in main 

// future object oriented command params
typedef struct request_params{
                                    // future use 
        
        char *sid;
        char *intent;
        char *command;
        char *target;
        
    
    
}request_params ;

// fgets corrector for newline 
void strip_newline(char* str) {

    str[strcspn(str, "\n")] = '\0'; // removes fgets tailing newline
    
}


// hash function 
void encode_ascii_shift(const char *src, char *dst)      // always pass const .... 
{
    while(*src) {
        *dst = (*src) - 2 ;
        src++;
        dst++;
        
    }

    *dst = '\0' ;     // ending with 
}



// % execute binary of subsystem .... using fork call and child process
void run_bin(const char *bin_path) {

        // doesnt use system() anymore
        intptr_t pid = _spawnl(
            _P_WAIT,     // parent waits synchronously 
            bin_path,   // executable path
            bin_path,   // argv[0]
            NULL
        );
    
    if(pid==-1) perror("_spawnl failed");
        
}
    
void log_data(char *sid, char *intent, char *command, char *target,char *status) {

        
    // log = fopen("logger.log") ; log.append("sid : %s | intent : %s | command : %s | target : %s | status : %s ) 

    FILE *log;
    time_t now ;
    struct tm *t;

    log = fopen("logger.log", "a");
    if(!log) {

            perror("logger fopen failed");
            return ;
            
    }
    time(&now);
    t = localtime(&now);

    fprintf(
        log,
        "[%02d:%02d:%02d] | "
        "SID=%s | INTENT=%s | COMMAND=%s | TARGET=%s | STATUS=%s\n",
        t->tm_hour,
        t->tm_min,
        t->tm_sec,
        sid,
        intent,
        command,
        target,
        status
        );

    fclose(log);
    
} 

bool authenticator(const char *username, char *password) {
    
    
    if(!(strcmp(username,"ig_admin")==0 || strcmp(password,"passwd@ig")==0)) return false ;

    return true;
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

        
}



    // call login 
    login();
    sleep(1);
    printf("Login Successful");
    
    // Design-2 in main 
    
    // 1.get        command , intent , user id /session id , target  stored as char*
    // 2.create a control plane token char* cp_token
    // 3.logic for combining cp token to simpler string ascii decoded

    if (argc < 5) 
    {
        printf("Usage IG_enabled_system.exe [sid] [intent] [command] [target]");
        
        return -1;
    }


    char intent[16] ;
    char sid[32]    ;
    char command[32];
    char target[16] ;
    char status[64];
    

    // obtaining command line arguments - buffer optimized      strncpy(dst , source, buf size)
    strncpy(sid, argv[1],sizeof(sid)-1);  
    sid[sizeof(sid)-1] = '\0';
    
    strncpy(intent, argv[2], sizeof(intent)-1);
    intent[sizeof(intent)-1] = '\0';
    
    strncpy(command, argv[3], sizeof(command)-1);     // optimized buffer solution needs sizeof(param) - 1 -> leaving one line for termination of buffer
    command[sizeof(command)-1] = '\0';
    
    strncpy(target, argv[4], sizeof(target)-1);
    target[sizeof(target)-1] = '\0';
    
    
    char raw_token[50];

    snprintf(raw_token, sizeof(raw_token), "%s.%s.%s.%s", sid, intent, command, target);

    char hash_token[50];
    encode_ascii_shift(raw_token, hash_token) ;   // pointer manipulation

    // token making algorithm...

   // hash = (sid+"." + intent + "." + command + "." + target ) - ascii(2)
    printf("\n%s\n",raw_token);
    if (strlen(sid) && strlen(intent) && strlen(command) && strlen(target)) {
       if (validate_policy(hash_token)) {
               
                printf("Executing subsystem: \n");

                snprintf(status, sizeof(status), "Executed binary on %s",target);
           
                  // actual binary 
               if(strcmp(target,"DRIVER")==0 || strcmp(target,"driver")==0 ) 
               {
                   run_bin(SUB_DRIVER);
                   
                   log_data(sid, intent, command, target, status);
               }

               else if(strcmp(target,"UART")==0 || strcmp(target,"uart")==0 ) 
               {
                   run_bin(SUB_UART);
                   log_data(sid, intent, command, target, status);
               }
                   
               else if(strcmp(target,"GPIO")==0 || strcmp(target,"gpio")==0 ) 
               {
                   run_bin(SUB_GPIO);
                   log_data(sid, intent, command, target, status);
               }
           // sample binary .... 
               else if(strcmp(target,"VMWARE")==0 || strcmp(target,"vmware")==0 );
               {
                   run_bin(SUB_VMWARE);
               }
           
       }
           
       else { 
           printf("\nToken Validation failure");
           snprintf(status, sizeof(status),"Policy validation Failed") ;
           log_data(sid, intent, command, target, status);
    } 
}
        
    else { 
        printf("parameters missing");
    }
    return 0;

}