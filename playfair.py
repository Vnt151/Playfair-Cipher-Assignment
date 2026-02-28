import re

class PlayfairCipher:
    def __init__(self, key):
        self.matrix = self._generate_matrix(key)

    def _generate_matrix(self, key):
        key = re.sub(r'[^A-Z]', '', key.upper().replace('J', 'I'))
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        matrix_chars = []
        for char in key + alphabet:
            if char not in matrix_chars and char in alphabet:
                matrix_chars.append(char)
        return [matrix_chars[i:i+5] for i in range(0, 25, 5)]

    def _find_position(self, char):
        for r, row in enumerate(self.matrix):
            if char in row: return r, row.index(char)
        return None

    def _prepare_text(self, text):
        text = re.sub(r'[^A-Z]', '', text.upper().replace('J', 'I'))
        prepared = ""
        i = 0
        while i < len(text):
            a = text[i]
            if i + 1 < len(text):
                b = text[i+1]
                if a == b:
                    prepared += a + 'X'
                    i += 1
                else:
                    prepared += a + b
                    i += 2
            else:
                prepared += a + 'X'
                i += 1
        return prepared

    def encrypt(self, plaintext):
        prepared = self._prepare_text(plaintext)
        ciphertext = ""
        for i in range(0, len(prepared), 2):
            r1, c1 = self._find_position(prepared[i])
            r2, c2 = self._find_position(prepared[i+1])
            if r1 == r2:
                ciphertext += self.matrix[r1][(c1+1)%5] + self.matrix[r2][(c2+1)%5]
            elif c1 == c2:
                ciphertext += self.matrix[(r1+1)%5][c1] + self.matrix[(r2+1)%5][c2]
            else:
                ciphertext += self.matrix[r1][c2] + self.matrix[r2][c1]
        return ciphertext

if __name__ == "__main__":
    # Dữ liệu kiểm thử từ ví dụ buổi học
    # Gốc: "Gr bx olnh wr vwxgb d fubswrjudskb frxuvh" (Caesar shift 3)
    # Giải mã ra Plaintext:
    plaintext_example = "DO YOU LIKE TO STUDY A CRYPTOGRAPHY COURSE"
    key = "PLAYFAIR"
    
    cipher = PlayfairCipher(key)
    result = cipher.encrypt(plaintext_example)
    
    print(f"--- Playfair Encryption ---")
    print(f"Key: {key}")
    print(f"Plaintext: {plaintext_example}")
    print(f"Ciphertext: {result}")