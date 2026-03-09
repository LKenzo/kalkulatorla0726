#please add your calculator function here

'''
Anggota Tools WAF - LA07:
- Putu Surya Wibawa Taksu - 2802421236
- Josephine Alethea Emmanuelle - 2802388522
- Maximillian Delavega Adiwinata Frenat - 2802432435
- Theodore Valentinus Bachri - 2802398170
- Gregorius Darren Chiu - 2802419641
'''

result = 0
user_input = -1
count = 0

def add(x, y) :
    return(x + y)

def subtract(x, y):
    return(x - y)

def multiply(x, y):
    return(x * y)

def divide(x, y):
    return(x / y)

while user_input != 0 :
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear")
    print("0. Exit")
    user_input = int(input("Enter your choice: "))
    if(user_input != 0) :
        if(count == 0) :

            first_num = int(input("first num: "))
            sec_num = int(input("second num: "))
        elif(user_input != 5):
            first_num = result
            print(f"first num: {result}")
            sec_num = int(input("second num:"))

        match user_input:
            case 1:
                result = add(first_num, sec_num)
                count +=1 
            case 2:
                result = subtract(first_num, sec_num)
                count += 1
            case 3:
                result = multiply(first_num, sec_num)
                count += 1
            case 4:
                result = divide(first_num, sec_num)
                count += 1
            case 5:
                result = 0
                count = 0
        
        print(f"Result: {result}")


print("Goodbye!")