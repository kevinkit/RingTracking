#include <stdlib.h>
#include <stdio.h>






int read_data(Data* data, char* filename)
{
    FILE *file;
    file = fopen(filename,"r");
    if(file == NULL)
        return -1;
    
    unsigned i = 0;

    for(i=0; i < 10;i++)
    {
        data[i].pos = i;
        fscanf(file,"%d",&data[i].x);
        fscanf(file,"%d",&data[i].y);
        fscanf(file,"%f",&data[i].r);
        fscanf(file,"%f",&data[i].intensity);
        fscanf(file,"%f",&data[i].contrast);

    }

    fclose(file);
    return 1;
}
