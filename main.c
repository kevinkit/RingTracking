#include <datahold.h>
#include <filereader.h>
#include <stdlib.h>
#include <stdio.h>







int main(int argc, char** argv)
{
    Data my_data[100];

    int file_am;


 
    if(argc > 1)
        file_am = atoi(argv[1]);
    else
        file_am = 0;
   
   
     
    char* name; 
    
    printf("ARGC = %d\n",argc);
    int i=0;


    for(i=0;i<=file_am;i++){
          sprintf(name,"Results%d.txt",i);            
     
            if(read_data(my_data,name) == -1){
                printf("could not access file %d\n",i);
                return -1;
            }
    
    
    
    
    
    
    }
    
    return 1;
}
