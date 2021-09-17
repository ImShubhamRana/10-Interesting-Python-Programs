import pyautogui
num = int(input("Enter the number to divide 100: "))
if num == 0:
    pyautogui.alert("100 can't divide by 0 !!!")
else:
    print(f"The value is {100/num}")