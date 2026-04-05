class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for i in strs:
            msg+=i+"|||"
        return msg
        
    def decode(self, s: str) -> List[str]:
        return s.split("|||")[:-1]