import re

queue = []
num = 0

def push(q, item):
    q.append(item)

def pop(q):
    if q:
        return q.pop(0)    
    else:
        print("queue is empty")    
        return None
    
def print_menu():
    print("1. Insert a number in the queue")
    print("2. Get the inserted number")
    print("q/Q for Quit\n")

def get_choice():
    return input("Please provide a choice\n")

def main():
    choice = 0
    num = 0
    out_num = 0

    while True:
        print_menu()
        choice = get_choice()

        if not choice:
            continue
        if choice == 'q' or choice == 'Q':
            break

        pattern = r'^\d$'
        match = re.match(pattern, choice)

        if not match:
            print("Error in choice")
            continue

        choice = int(choice)
        match choice:
            case 1:
                num = input("Please insert a num\n")
                pattern = r'^\d+$'
                match = re.match(pattern, num)
               
                if not match:
                    print("Error in num")
                    continue

                num = int(num)
                push(queue, num)
                print("Inserted\n")
            case 2:
                out_num = pop(queue)
                if out_num is not None: 
                    print("You got: ", out_num)
                    print()
            case _:
                print("Not a valid choice")

    print('Goodbye')

if __name__ == '__main__':
    main()
