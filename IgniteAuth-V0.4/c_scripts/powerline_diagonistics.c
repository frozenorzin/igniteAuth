// powerline_diagnostics.c -> command engine 



#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc < 4) {
        printf("\n❌ Missing arguments: target_node intent command\n");
        return 1;
    }

    char *target_node = argv[1];  // target to be executed
    char *intent = argv[2];       // intent of command
    char *command = argv[3];      // command to execute

    const char *intent_main = "criticality_testing";  // const cannot be modified ... 
    const char *command_main = "powerline_diagnostics";

    if (strcmp(intent, intent_main) == 0 && strcmp(command, command_main) == 0) {
        printf("✅ powerline_test triggered securely at node: %s\n", target_node);
    } else {
        printf("❌ Intent or Command not authorized.\n");
    }

    return 0;
}