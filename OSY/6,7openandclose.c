#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main()
{
    int fd;
    fd = open("sample.txt", O_CREAT | O_WRONLY, 0644);

    if (fd == -1)
    {
        printf("File opening failed.\n");
        return 1;
    }

    printf("File opened successfully.\n");
    printf("File descriptor = %d\n", fd);

    close(fd);
    printf("File closed successfully.\n");
    return 0;
}