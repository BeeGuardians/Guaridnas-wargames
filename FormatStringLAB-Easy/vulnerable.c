#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char flag[100];

void vuln(char *leak_target) {
    char buf[256];
    puts("Tell me something:");
    fgets(buf, sizeof(buf), stdin);
    printf(buf);  // 포맷스트링 취약점 그대로
    puts("\nThanks!");
}

int main() {
    FILE *f = fopen("flag.txt", "r");
    if (!f) {
        perror("flag.txt");
        exit(1);
    }
    fread(flag, 1, sizeof(flag), f);
    fclose(f);

    // ✨ 플래그 주소를 명시적으로 스택에 올림
    vuln(flag);
    return 0;
}
