import sys

def calculator(operation, num1, num2):
    """define a simple calculator"""

    if operation == "+":
        return num1 + num2
    
    elif operation == "-":
        return num1 - num2
    
    elif operation == "/":
        if num2 == 0:
            return "error: divided number can not be zero!"
        else:
            return num1 / num2
        
    elif operation == "*":
        return num1 * num2
    
    else:
        return "error: unknow operator!"
    
# define calculator display 
def main():
    print(" " * 50)
    print("=" * 50)
    print("Simple Python Calculator Designed by Maxwell")
    print("=" * 50)
    print("We supported operations: +, -, *, /")
    print("'quit' or 'exit' to exit the app")
    print("=" * 50)
    print()


    while True:
        try:
            # get the user input
            user_input = input("Please enter calculation (e.g., 1 + 2): ").strip()

            # check if exit or quit
            if user_input.lower() in ['quit', 'exit']:
                print("Thanks for using the app, bye")
                break

            # if input is NULL, tell user input again
            if not user_input:
                continue

            # split user_input
            list_in = user_input.split()

            # check the list_in format should have 3 str 
            if len(list_in) != 3:
                print("input error: please user format like num1 + num2")
                print("example: 1 + 2")
                continue

            # get the value from list_in
            num1_str = list_in[0]
            num2_str = list_in[2]
            operation = list_in[1]

            if operation not in ['+', '-', '*', '/']:
                print(f"error: '{operation}' is not a valid operation")
                print("We supported operations are: +, -, *, /")
                continue

            try:
                # change str to float
                num1 = float(num1_str)
                num2 = float(num2_str)

            except ValueError:
                print("Error: Pelase enter valid number")
                continue

            # 执行计算
            try:
                result = calculator(operation, num1, num2)
                print(f"Result: {num1} {operation} {num2} = {result}")
                print("-" * 50)

            except ValueError as e:
                print("Error: {e}")
                print("-" * 50)

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print("Unexpected error")
            print("-" * 50)


if __name__ == '__main__':
    sys.exit(main()) # 运行 main() 并将退出返回值 传递给操作系统 






