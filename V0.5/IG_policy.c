// ./IG_Policy.c - source of the control plane
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// whitelisted params
const char valid_commands[3][20] = {
    "rebootF",
    "execPowDebug",
    "ResetSYS"
};

const char valid_intents[3][30] = {
    "firmware_reboot",
    "powerline_diagnostics",
    "firmware_reset"
};

const char valid_targets[3][10] = {
    "GPIO",
    "UART",
    "DRIVER"
};

/*
              *   Decode token: ascii +2
*/
void extract_cmd_params(const char *hashed_token, char *main_token) {
    while (*hashed_token) {
        *main_token = (*hashed_token) + 2;
        hashed_token++;
        main_token++;
    }
    *main_token = '\0';
}

/*
              * Control Plane Policy Validation
*/
bool validate_policy(const char *hashed_token) {

    char main_token[100];

    printf(" Welcome to IgniteAuth \n");

    printf("received token : %s\n", hashed_token);
    printf("sending command to execute...\n");

    // decode hashed → plaintext
    extract_cmd_params(hashed_token, main_token);

    // split token
    char *sid     = strtok(main_token, ".");
    char *intent  = strtok(NULL, ".");
    char *command = strtok(NULL, ".");
    char *target  = strtok(NULL, ".");

    // format safety
    if (!sid || !intent || !command || !target) {
        printf("POLICY ABORT: Invalid token format\n");
        return false;
    }

    printf("\nDecoded:\n");
    printf("SID     : %s\n", sid);
    printf("Intent  : %s\n", intent);
    printf("Command : %s\n", command);
    printf("Target  : %s\n", target);

    /*
     * ================================
     * INVERTED INTENT WHITELIST CHECK
     * ================================
   */

    bool intent_invalid = true;   // deny-by-default

    for (int i = 0; i < 3; i++) {
        if (strcmp(intent, valid_intents[i]) == 0) {
            intent_invalid = false;   // intent allowed
            break;
        }
    }

    if (intent_invalid) {
        printf("\nPOLICY ABORT: Intent not allowed -> %s\n", intent);
        return false;
    }

     /*
     * ================================
     * COMMAND INTENT WHITELIST CHECK
     * ================================
   */

    bool command_invalid = true ;

    for (int i = 0; i < 3;i++){
        if(strcmp(command, valid_commands[i])==0){

            command_invalid = false ;
            break;
        }
    }
    
    if(command_invalid) {
        printf("\nPOLICY ABORT: Command not allowed -> %s\n", command);
        return false ;
        
    }

    printf("\nPOLICY PASS: Intent and Command validated\n");
    

    printf("CONTROL PLANE: Execution permitted\n");
    printf("Executing command : %s on Target %s\n", command, target) ;
    return true;                                                   // more secure , we dont use stored value of intent 
}
