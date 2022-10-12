import random

line = '---------------------------------------------------'
print('今からコンピューターとじゃんけんをします')
print(line)
print('グーなら1、チョキなら2、パーなら3を入力してください')
hand = int(input())
print(line)


hands = [' ','グー','チョキ','パー']
computer = [1,2,3]
computer2 = [2,3]
computer3 = [1,3]
computer4 = [1,2]
#ここでは1=グー、2=チョキ、3=パーとする
computer_hand = random.choices(computer)

if hand == 1:
    computer_hand = random.choice(computer)
    print(f'あなたは{hands[hand]}を出しました')
    if computer_hand == 1:
        while computer_hand == hand:
            print(line)
            print('あいこなのでもう一度')
            hand = int(input())
            print(line)
            computer = [1,2,3]
            computer_hand = random.choice(computer)
        if computer_hand != hand and 0<hand<4:
            print(f'あなたは{hands[hand]}を出しました')
            computer_hand = random.choice(computer2)
            if computer_hand == 2:
                print(f'コンピューターは{hands[computer_hand]}を出しました')
                print('あなたの勝ちです')
                print(line)
            elif computer_hand == 3:
                print(f'コンピューターは{hands[computer_hand]}を出しました')
                print('あなたの負けです')
                print(line)
        else:
            print('入力する数字が違います')
            print(line)
    elif computer_hand == 2:
        print(f'コンピューターは{hands[computer_hand]}を出しました')
        print('あなたの勝ちです')
        print(line)
    elif computer_hand == 3:
        print(f'コンピューターは{hands[computer_hand]}を出しました')
        print('あなたの負けです')
        print(line)

elif hand == 2:
    computer_hand = random.choice(computer)
    print(f'あなたは{hands[hand]}を出しました')
    if computer_hand == 1:
        print(f'コンピューターは{hands[computer_hand]}を出しました')
        print('あなたの負けです')
        print(line)
        
    elif computer_hand == 2:
       if hand == 2:   
            while computer_hand == hand and 0<hand<4:
                print(line)
                print('あいこなのでもう一度')
                hand = int(input())
                print(line)
                computer = [1,2,3]
                computer_hand = random.choice(computer)
            if computer_hand != hand and 0<hand<4: 
                print(f'あなたは{hands[hand]}を出しました')
                computer_hand = random.choice(computer3)
                if computer_hand == 1:
                    print(f'コンピューターは{hands[computer_hand]}を出しました')
                    print('あなたの負けです')
                    print(line)
                elif computer_hand == 3:
                    print(f'コンピューターは{hands[computer_hand]}を出しました')
                    print('あなたの勝ちです')
                    print(line)
            else:
                print('入力する数字が違います')
                print(line)
    elif computer_hand == 3:
            print(f'コンピューターは{hands[computer_hand]}を出しました')
            print('あなたの勝ちです')
            print(line)
        
elif hand == 3:
    computer_hand = random.choice(computer)
    print(f'あなたは{hands[hand]}を出しました')
    if computer_hand == 1:
        print(f'コンピューターは{hands[computer_hand]}を出しました')
        print('あなたの勝ちです')
        print(line)
    elif computer_hand == 2:
        print(f'コンピューターは{hands[computer_hand]}を出しました')
        print('あなたの負けです')
        print(line)
    elif computer_hand == 3:
        while computer_hand == hand:
            print(line)
            print('あいこなのでもう一度')
            hand = int(input())
            print(line)
            computer = [1,2,3]
            computer_hand = random.choice(computer)
        if computer_hand != hand and 0<hand<4:
            print(f'あなたは{hands[hand]}を出しました')
            computer_hand = random.choice(computer4)
            if computer_hand == 1:
                print(f'コンピューターは{hands[computer_hand]}を出しました')
                print('あなたの勝ちです')
                print(line)
            elif computer_hand == 2:
                print(f'コンピューターは{hands[computer_hand]}を出しました')
                print('あなたの負けです')
                print(line)
        else:
            print('入力する数字が違います')
            print(line)
            
elif hand >=4 or hand <=0:
    print('入力する数字が違います')
