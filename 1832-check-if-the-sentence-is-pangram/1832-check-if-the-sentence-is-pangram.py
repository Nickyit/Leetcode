class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence = sentence.lower()
        a_z = 'abcdefghijklmnopqrstuvwxyz'
        # lower_text = a_z.lower()

        for ch in a_z:
            if ch not in sentence:
                return False
        return True