#include <stdio.h>
#include <sys/stat.h>

int main()
{
    struct stat fileInfo;

    if (stat("sample.txt", &fileInfo) == 0)
    {
        printf("File Information:\n");
        printf("File size: %ld bytes\n", fileInfo.st_size);
        printf("File permission: %o\n", fileInfo.st_mode & 0777);
    }
    else
    {
        printf("Unable to get file information.\n");
    }
    return 0;
}