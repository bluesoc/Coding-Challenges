/* 
    https://leetcode.com/problems/length-of-last-word


Test cases:
    "   fly me   to   the moon  "

    "Hello World"

*/

int lengthOfLastWord(char* s) {
    size_t sz = strlen(s);

    int lastw = 0;

    // Flag to validate if a word was found
    int LAST_SET = 0;

    for (int i = sz - 1 ; i >= 0; i--)
    {
        if ( isalpha(s[i]) )
        {
            if ( LAST_SET == 0)
            {
                LAST_SET = 1;
                lastw = 1;

            }
            else
            {
                lastw++;
            }
        }
        else if ( LAST_SET && !isalpha(s[i]) )
        {
            break;
        }
    }
    return lastw;
}
