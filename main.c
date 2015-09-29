#include <datahold.h>
#include <filereader.h>
#include <stdlib.h>
#include <stdio.h>







int main(char** argv, int argc)
{
    Data my_data[100];

    char name[100];

    switch(argc){
        case 0: name = "Results.txt"; break;
        case 1: name = argv[1]; break;
    }

    printf("argc = %d\n",argc);









    if(read_data(my_data,"hallo") == -1){
        printf("could not read file\n");
        return -1;
    }
     
    
    return 1;
}
