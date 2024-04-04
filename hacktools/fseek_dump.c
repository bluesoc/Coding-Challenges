/*
 *	This program was created during a CTF hacking competition
 *
 *	bluesoc (c) 2024
 *
 */
#include <stdio.h>

#define TGT_FILE "Win10Home-20H2-64bit-memdump"

// skip 73132150 bytes
static int skip = 0x45BE876;

/*
 *	Read clear text password string 
 *	found at byte 0x45BE876 on the 
 *	'TGT_FILE' machine memory dump. 
 */
int main()
{
	unsigned char read[8];

	FILE* file = fopen(TGT_FILE, "rb");
	if (!file)
	{
		printf("File not found.\n");
		return(1);
	}

	fseek(file, skip , SEEK_SET);

	fread( read, 6, 1, file);

	fclose(file);
	printf("%s\n", read);

	return 0;
}