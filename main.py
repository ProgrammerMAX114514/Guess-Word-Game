class play:
    import random  
    from tkinter import messagebox,Tk
    main=Tk()
    main.withdraw()
    while True:
        difficulty=input("Choose a difficulty level/选择一个难度:\n1=easy/简单(30 lives/条命)\n2=medium/适中(20 lives/条命)\n3=hard/难(10 lives/条命)\n\nEnter difficulty below/在下方输入难度(1/2/3):\n")
        if difficulty == '1' or difficulty == '2' or difficulty == '3':
            break
        if difficulty != '1' or difficulty != '2' or difficulty != '3':
            print('You seem to have entered the wrong character.Please try again./你似乎输入了错误的字符。请重试。')
    if difficulty=='1':
        lives=30
    elif difficulty=='2':
        lives=20
    elif difficulty=='3':
        lives=10

    words = ['pizza','fairy','teeth','shirt','otter',
             'plane','death','North','South','Earth',
             'pease','pearl','apple','bread','cloud',
             'drink','fruit','ghost','happy','juice',
             'knife','lemon','music','ocean','peach',
             'quilt','river','smile','tiger','umbra',
            ]
    random.shuffle(words)
    secret_word = random.choice(words)
    clue = list('?????')
    index_text = 0
    heart_symbol = u'\u2764'
    guessed_word_correctly = False
    ul = len(secret_word)


    def update_clue(guessed_letter, secret_word, clue, ul):
        index = 0
        while index < len(secret_word):
            if guessed_letter == secret_word[index]:
                clue[index] = guessed_letter
                ul = ul - 1
            index = index + 1


        return ul


    while lives > 0:
        print(clue)
        print('Lives left: ' + heart_symbol * lives)
        guess = input('Guess a letter or the whole word/猜一个字母或整个单词：')
        
        
        if guess == secret_word:
            guessed_word_correctly = True
            break
        
        
        if guess in secret_word:
            ul = update_clue(guess, secret_word, clue, ul)
        else:
            print('Incorrect.You lose a life./错误。你失去了一条生命。')
            lives = lives - 1


        if ul == 0:
            guessed_word_correctly = True
            break

    from tkinter import Tk
    root = Tk()
    root.withdraw()
    if guessed_word_correctly:
        messagebox.showinfo('Won/胜利','You won! The correct word was \'' + secret_word + '\'\n你赢了！正确的单词是：\'' + secret_word + '\'')
    else:
        messagebox.showerror('Lost/失败','You lost! The secret word was \'' + secret_word + '\'你失败了！! 正确的单词是： \'' + secret_word + '\'')
