#include<stdio.h>
#include<unistd.h>

int main() {
    
    printf("Starting GPIO on main system - child spawn \n") ;
    printf("Secured by IgniteAuth\n");

    for (int i = 0; i < 10; ++i){      // expected time for booting uart 
        
        printf(".");
        sleep(1) ;
        
    }

    printf("\n\t\t\t...GPIO started at 0xADD2...\t\t\t\n");
    
    


    return 0;
}