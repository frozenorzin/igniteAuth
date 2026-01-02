#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

// Original Binary for Driver interface 

void init_driver() {

    printf("Driver Interface - SUBSYS\n");
    printf("Protected by IgniteAuth..\n");
    
    
}

int main(){

    init_driver();
    int driver_call = 43119; //  an indicator for driver call
    
    for(int i = 0;i<5;i++){

        printf(".");
        sleep(1);
        
    }

    printf("Driver Started at addr : %p", &driver_call);
    
    
}