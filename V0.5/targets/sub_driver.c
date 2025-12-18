#include<stdio.h>
#include<unistd.h>

int main() {
    
    printf("Starting DRIVER on main system - child spawn\n") ;
    printf("Secured by IgniteAuth\n");

    for (int i = 0; i < 10; ++i){      // expected time for booting uart 
        
        printf(".");
        sleep(1) ;
        
    }

    printf("\n\t\t\t...DRIVER started at 0xADD3...\t\t\t\n");
    
    


    return 0;
}