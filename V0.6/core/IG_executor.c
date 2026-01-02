// ./core/IG_executor.c

#include<stdio.h>
#include<stdlib.h>
#include<process.h>

#include "../include/IG_targets.h" // paths for binaries 



void execute_target_bin(const char *path) {

    intptr_t pid = spawnl(
        _P_WAIT,
        path,
        path,
        NULL
    )

    if(pid==-1) perror("_spawnl Failed");

    
}



