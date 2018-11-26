class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_al = dict(zip(alpha,morse))

        s1 = set()
        for i in words:
            now_word = []
            for j in i:
                now_word.append(morse_al[j])
            morse_str = ''.join(now_word)
            #join 比 + 方法快

            s1.add(morse_str)
        return len(s1)