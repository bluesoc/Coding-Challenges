class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

        '''
        # Old method (33 ms):
        try:
            return haystack.index(needle)
        except:
            return -1
        '''

