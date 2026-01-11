#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

// Original Binary for UART interface 

void init_uart() {

    printf("UART Interface - SUBSYS\n");
    
    printf("Protected by IgniteAuth..\n");
    sleep(5);
    
}

int main(){

    init_uart();
    int uart_call = 43111; //  an indicator for driver call
    
    for(int i = 0;i<5;i++){

        printf(".");
        sleep(1);
        
    }

    printf("UART Service Started at addr : %p", &uart_call);
    
    
}
