class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for st in s:
            if st.isalnum():
                string+=st.lower()
        return string == string[::-1]
        