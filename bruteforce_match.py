def brute_force_match(text,pattern):
    for i in range(len(text)-len(pattern)):
        j = 0
        while (j < len(text) and text[i + j] == pattern[j]):
            j = j + 1;
            if j == len(text):
                return i
        return f"There is no substring of {text}  matching {pattern}."