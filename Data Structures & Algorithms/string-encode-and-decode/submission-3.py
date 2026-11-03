class Solution:

    def encode(self, strs: List[str]) -> str:
        return 'r4nd0m_str1ng'.join(strs) if len(strs)>0 else 'empty'
    def decode(self, s: str) -> List[str]:
        return s.split('r4nd0m_str1ng') if s!='empty' else []