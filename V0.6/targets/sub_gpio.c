#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

// Original Binary for GPIO interface 

void init_gpio() {

    printf("GPIO Interface - SUBSYS\n");
    printf("Protected by IgniteAuth..\n");
    
    
}

int main(){

    init_gpio();
    int gpio_call = 43110; //  an indicator for driver call
    
    for(int i = 0;i<5;i++){

        printf(".");
        sleep(1);
        
    }

    printf("GPIO service Started at addr : %p", &gpio_call);
    
    
}
