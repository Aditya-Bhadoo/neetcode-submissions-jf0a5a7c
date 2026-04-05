class Solution:

    def encode(self, strs: List[str]) -> str:
        msg="|||".join(strs)
        if len(strs) == 0:
            return "None"
        print(msg)
        return msg
        
    def decode(self, s: str) -> List[str]:
        print(s)
        if s == "None":
            return []
        return s.split("|||")