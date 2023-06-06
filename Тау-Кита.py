for n in range(1, 10):
    r_in = open(f'Тау-Кита/input_s1_0{n}.txt', 'r')
    r_out = open(f'Тау-Кита/output_s1_0{n}.txt', 'r')

    str = r_in.readlines()
    otv = r_out.readlines()

    words = str[0].split(" ")
    
    for t in range(len(words)):
        new_word = words[t][len(words[t]) // 2]
        for i in range(1, len(words[t]) // 2 + 1):
            new_word += words[t][len(words[t]) // 2 - i]
            if (len(words[t]) // 2 + i) < len(words[t]):
                new_word += words[t][len(words[t]) // 2 + i]
        words[t] = new_word
        
    new_words = [words[len(words) // 2]]

    for i in range(1, len(words) // 2 + 1):
        new_words.append(words[len(words) // 2 - i])
        if (len(words) // 2 + i) < len(words):
            new_words.append(words[len(words) // 2 + i])
            
    if (' '.join(new_words)) == otv[0]:
        print("Совпало")
        print("Было: ",str)
        print("Cтало: ",otv,"\n")
    else:
        print("Несовпало")
