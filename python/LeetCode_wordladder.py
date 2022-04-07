"""
This is a problem on LeetCode (Hard difficulty).

The idea is to start with a word and see how many steps it takes to get to the ending word, while using a wordlist to 'traverse' between the two. With each step, the start word will turn into the closest word to it in the wordlist (only one letter diviation is allowed) until the path to the end word becomes clear. If there is no path to the end word (i.e. the end word isn't in the wordlist, or there's no way to traverse the wordlist due to no appropriate path) then the ladder ends with zero steps.

Example1:
Input: start_word = "hit", end_word = "cog", wordlist = ["hot","dot","dog","lot","log","cog"]
Output: 5 steps
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.

Example2:
Input: start_word = "hit", end_word = "cog", wordlist = ["hot","dot","dog","lot","log"]
Output: 0 steps
Explanation: The end_word "cog" is not in wordlist, therefore there is no valid transformation sequence.

Note: the start word doesn't need to be in the wordlist, but the end word does for a successful word ladder traversal. Also, setting show_steps to true will show the path the traversal took instead of only the number of steps.
"""

def wordladder(start_word:str,end_word:str,wordlist:list,show_steps:bool=False):
    word_steps = 1
    path_string = start_word
    current_word = start_word
    used_words = []
    while True:
        word_paths = []
        for w in wordlist:
            if w in used_words: continue
            if len(w) != len(current_word): continue
            absent_chars = 0
            for c in w:
                if c in current_word: continue
                absent_chars += 1
            if absent_chars == 1: word_paths.append(w)
        used_words.extend(word_paths)
        if word_paths:
            current_word = word_paths[0]
            word_steps += 1
            if end_word in word_paths:
                path_string += " -> "+end_word
                break
            path_string += " -> "+current_word
        else:
            word_steps = 0
            return word_steps
    return path_string if show_steps else word_steps

fw = "barf"
lw = "food"
wl = ["barn","feed","fool","born","boon","bool","poop","food"]
print(wordladder(fw,lw,wl,True))