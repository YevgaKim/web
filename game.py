import random

code = random.sample(list(range(1,10)),4)

count = 0
while count!=8:
    answer = input("Enter the four-digit code(without 0(zero)): ")
    if answer=="exit":
        continue
    if "0" in answer:
        print("Without 0(zero)")
        continue
    if len(answer) != 4:
        print("The code must be four characters long!")
    else:
        try:
            user_code = int(answer)  
            lst_num = [int(digit) for digit in str(user_code)]
            correct_numbers = [i for i in lst_num if i in code]
            correct_positions=0
            for i,j in zip(lst_num,code):
                if i==j:
                    correct_positions+=1
            
            count+=1
            print(f"Correct_numbers: {len(correct_numbers) if correct_numbers!=[] else 0}\nCorrect Positions: {correct_positions}")
            if correct_positions==4:
                print("You won!!!")
                break
        except ValueError:
            print("The entered value must consist of 4 digits")
else:
    print("Attempts are over. Game over")
    print(f"Right code is {''.join(map(str,code))}")


