'''
name - chitra pandey
enrollment no - 0176AL221048
QUIZ APPLICATION
'''


import random
import re


#load quiz in file
def load_questions(quizfile):
    questions = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(';')
            if len(parts) == 6:  
                question = {
                    "question": parts[0],
                    "options": parts[1:5],
                    "answer": parts[5]
                }
                questions.append(question)
    return questions


#usename generator
user_name = input("Enter your user name: ")

special_characters = "!@#$%&*_"
random_characters = ''.join(random.choice(special_characters))

numbers = random.randint(10, 100)

def generate_username():
    return f"{random.choice (user_name)}{random_characters}{numbers}"
print(f"your username is: ",generate_username())



#check password
while True:
    password = input("enter your password: ")

    length_criteria = len(password) >= 8
    upper_case_criteria = re.search(r'[A-Z]', password) is not None
    lower_case_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[1-99]', password) is not None
    special_char_criteria = re.search(r'[!@#$%&_]', password) is not None

    
    if length_criteria and upper_case_criteria and lower_case_criteria and digit_criteria and special_char_criteria:
        break
    
    elif length_criteria and (upper_case_criteria or lower_case_criteria) and digit_criteria:
        print("enter strong password")


#dbms questions
def dbms_questions():
    questions = [
        {
        "question": " What is a DBMS?",
        "options": ["A) Database Management System", "B) Data Management System", "C) Database Model System", "D) Data Base Management Service"],
        "answer": "A"
        },
        {
        "question": " What are the types of DBMS?",
        "options": ["A) Hierarchical, Network, Relational", "B) Flat, Relational, Object-oriented", "C) Network, Relational, Document", "D) All of the above"],
        "answer": "D"
        },
        {
        "question": " Explain the difference between a primary key and a foreign key.",
        "options": ["A) Primary key uniquely identifies a record; foreign key links two tables", "B) Both are the same", "C) Primary key can be null; foreign key cannot", "D) Foreign key is always unique"],
        "answer": "A"
        },
        {
        "question": " What is normalization?",
        "options": ["A) Process of organizing data", "B) Process of duplicating data", "C) Process of storing data", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is a relational database?",
        "options": ["A) A database that stores data in tables", "B) A database that stores data as files", "C) A database that uses XML", "D) A database that uses JSON"],
        "answer": "A"
        },
        {
        "question": " Describe ACID properties.",
        "options": ["A) Atomicity, Consistency, Isolation, Durability", "B) Accuracy, Consistency, Isolation, Durability", "C) Atomicity, Consistency, Integrity, Durability", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is SQL?",
        "options": ["A) Structured Query Language", "B) Simple Query Language", "C) Sequential Query Language", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is a database schema?",
        "options": ["A) The structure of a database", "B) The data in a database", "C) The relationship between tables", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " Explain the concept of indexing in databases.",
        "options": ["A) Speeding up data retrieval", "B) Reducing data redundancy", "C) Storing data securely", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is a join?",
        "options": ["A) Combining rows from two or more tables", "B) A type of index", "C) A data model", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is a stored procedure?",
        "options": ["A) A set of SQL statements", "B) A database trigger", "C) A type of index", "D) A data model"],
        "answer": "A"
        },
        {
        "question": " What is a trigger in a database?",
        "options": ["A) A set of SQL statements", "B) A stored procedure", "C) A type of index", "D) A database event handler"],
        "answer": "D"
        },
        {
        "question": " Explain the difference between clustered and non-clustered indexes.",
        "options": ["A) Clustered indexes are faster; non-clustered indexes are slower", "B) Clustered indexes are slower; non-clustered indexes are faster", "C) Clustered indexes are used for primary keys; non-clustered indexes are used for foreign keys", "D) Clustered indexes are used for foreign keys; non-clustered indexes are used for primary keys"],
        "answer": "A"
        },
        {
        "question": " What is a transaction?",
        "options": ["A) A single SQL statement", "B) A set of SQL statements", "C) A database connection", "D) A database session"],
        "answer": "B"
        },
        {
        "question": " What is data redundancy?",
        "options": ["A) Data duplication", "B) Data inconsistency", "C) Data loss ", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is a data warehouse?",
        "options": ["A) A system for reporting and data analysis", "B) A type of database", "C) A data storage solution", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is a data mart?",
        "options": ["A) A subset of a data warehouse", "B) A type of database", "C) A data storage solution", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is denormalization?",
        "options": ["A) The process of reducing data redundancy", "B) The process of increasing data redundancy", "C) The process of organizing data", "D) None of the above"],
        "answer": "B"
        },
        {
        "question": " What is a NoSQL database?",
        "options": ["A) A database that does not use SQL", "B) A database that uses SQL", "C) A type of relational database", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is a database management system (DBMS) used for?",
        "options": ["A) To create and manage databases", "B) To store data", "C) To retrieve data", "D) All of the above"],
        "answer": "D"
        }
        ]

    random_questions = random.sample(questions, 5)
    correct_answers = 0

    for i in random_questions:
        print(i["question"])
        for options in i:
            print(i["options"])
        user_answer = input(f"{i['question']} (Choose A, B, C, or D): ")
        if user_answer.upper() == i["answer"]:
            correct_answers += 1
            print(f"You got {correct_answers} out of 5 questions correct.")
        print()


#ds questions
def ds_questions():
    questions = [
        {
        "question": " What is a data structure?",
        "options": ["A) A way to store and organize data", "B) A type of algorithm", "C) A programming language", "D) A data type"],
        "answer": "A"
        },
        {
        "question": " Which of the following is a linear data structure?",
        "options": ["A) Array", "B) Linked List", "C) Stack", "D) All of the above"],
        "answer": "D"
        },
        {
        "question": " What is the time complexity of accessing an element in an array?",
        "options": ["A) O(1)", "B) O(n)", "C) O(log n)", "D) O(n^2)"],
        "answer": "A"
        },
        {
        "question": " Which data structure uses LIFO (Last In First Out) order?",
        "options": ["A) Queue", "B) Stack", "C) Array", "D) Linked List"],
        "answer": "B"
        },
        {
        "question": " What is a binary tree?",
        "options": ["A) A tree where each node has at most two children", "B) A tree where each node can have any number of children", "C) A tree with only one node", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is the main advantage of a linked list over an array?",
        "options": ["A) Faster access time", "B) Dynamic size", "C) Easier to sort", "D) None of the above"],
        "answer": "B"
        },
        {
        "question": " Which of the following is not a type of tree?",
        "options": ["A) Binary Tree", "B) AVL Tree", "C) Linear Tree", "D) Red-Black Tree"],
        "answer": "C"
        },
        {
        "question": " What is a hash table?",
        "options": ["A) A data structure that maps keys to values", "B) A type of tree", "C) A linear data structure", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " Which data structure is used for breadth-first search?",
        "options": ["A) Stack", "B) Queue", "C) Array", "D) Linked List"],
        "answer": "B"
        },
        {
        "question": " What is the worst-case time complexity of quicksort?",
        "options": ["A) O(n log n)", "B) O(n^2)", "C) O(n)", "D) O(log n)"],
        "answer": "B"
        },
        {
        "question": " Which of the following is a non-linear data structure?",
        "options": ["A) Array", "B) Stack", "C) Tree", "D) Queue"],
        "answer": "C"
        },
        {
        "question": " What is the purpose of a stack?",
        "options": ["A) To store data in a linear order", "B) To store data in a hierarchical manner", "C) To manage function calls", "D) To sort data"],
        "answer": "C"
        },
        {
        "question": " Which traversal method is used for binary trees?",
        "options": ["A) In-order", "B) Pre-order", "C) Post-order", "D) All of the above"],
        "answer": "D"
        },
        {
        "question": " What is a priority queue?",
        "options": ["A) A queue where each element has a priority", "B) A queue that processes elements in FIFO order", "C) A queue that processes elements in LIFO order", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is the space complexity of an array of size n?",
        "options": ["A) O(1)", "B) O(n)", "C) O(n^2)", "D) O(log n)"],
        "answer": "B"
        },
        {
        "question": " Which of the following is a characteristic of a queue?",
        "options": ["A) It follows FIFO order", "B) It follows LIFO order", "C) It allows random access", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is a circular linked list?",
        "options": ["A) A linked list where the last node points to the first node", "B) A linked list with no nodes", "C) A linked list that is sorted", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is the main disadvantage of a linked list?",
        "options": ["A) Dynamic size", "B) Memory overhead for pointers", "C) Faster access time", "D) None of the above"],
        "answer": "B"
        },
        {
        "question": " What is a graph?",
        "options": ["A) A collection of nodes and edges", "B) A type of tree", "C) A linear data structure", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is the time complexity of searching in a balanced binary search tree?",
        "options": ["A) O(n)", "B) O(log n)", "C) O(n log n)", "D) O(1)"],
        "answer": "B"
        }
        ]

    random_questions = random.sample(questions, 5)
    correct_answers = 0

    for i in random_questions:
        print(i["question"])
        for options in i:
            print(i["options"])
        user_answer = input(f"{i['question']} (Choose A, B, C, or D): ")
        if user_answer.upper() == i["answer"]:
            correct_answers += 1
            print(f"You got {correct_answers} out of 5 questions correct.")
        print()


#os questions
def os_questions():
    questions = [
        {
        "question": " What is an operating system?",
        "options": ["A) A software that manages computer hardware", "B) A type of application software", "C) A programming language", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " Which of the following is not an operating system?",
        "options": ["A) Windows", "B) Linux", "C) Python", "D) macOS"],
        "answer": "C"
        },
        {
        "question": " What is the main function of an operating system?",
        "options": ["A) To manage hardware resources", "B) To provide a user interface", "C) To execute applications", "D) All of the above"],
        "answer": "D"
        },
        {
        "question": " What is multitasking?",
        "options": ["A) Running multiple applications simultaneously", "B) Running one application at a time", "C) A type of operating system", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " Which of the following is a type of operating system?",
        "options": ["A) Batch Operating System", "B) Time-Sharing Operating System", "C) Real-Time Operating System", "D) All of the above"],
        "answer": "D"
        },
        {
        "question": " What is a kernel?",
        "options": ["A) The core component of an operating system", "B) A type of application", "C) A programming language", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is a process?",
        "options": ["A) A program in execution", "B) A type of memory", "C) A hardware component", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What does the term 'deadlock' mean?",
        "options": ["A) A situation where two or more processes cannot proceed", "B) A situation where a process is terminated", "C) A type of memory allocation", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is virtual memory?",
        "options": ["A) A memory management technique", "B) A type of hardware", "C) A programming language", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is a file system?",
        "options": ["A) A method of storing and organizing files", "B) A type of application", "C) A programming language", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": "What is the purpose of device drivers?",
        "options": ["A) To communicate with hardware devices", "B) To manage files", "C) To execute applications", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is a thread?",
        "options": ["A) The smallest unit of processing", "B) A type of memory", "C) A hardware component", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is the difference between a process and a thread?",
        "options": ["A) A process is a program in execution; a thread is a lightweight process", "B) A process uses more resources than a thread", "C) A thread can exist independently of a process", "D) All of the above"],
        "answer": "A"
        },
        {
        "question": " What is a system call?",
        "options": ["A) A request to the operating system to perform a task", "B) A type of application", "C) A programming language", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " Which of the following is a memory management technique?",
        "options": ["A) Paging", "B) Segmentation", "C) Both A and B", "D) None of the above"],
        "answer": "C"
        },
        {
        "question": " What is a shell?",
        "options": ["A) A command-line interface", "B) A type of application", "C) A programming language", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is the purpose of an operating system's scheduler?",
        "options": ["A) To manage the execution of processes", "B) To allocate memory", "C) To handle input/output operations", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is a real-time operating system?",
        "options": ["A) An OS that processes data as it comes in", "B) An OS that runs applications in batch mode", "C) An OS that does not support multitasking", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is the role of the file manager in an operating system?",
        "options": ["A) To manage files and directories", "B) To execute applications", "C) To manage hardware resources", "D) None of the above"],
        "answer": "A"
        },
        {
        "question": " What is the purpose of memory allocation?",
        "options": ["A) To assign memory to processes", "B) To free up memory", "C) To manage file storage", "D) None of the above"],
        "answer": "A"
        }
        ]

    random_questions = random.sample(questions, 5)
    correct_answers = 0

    for i in random_questions:
        print(i["question"])
        for options in i:
            print(i["options"])
        user_answer = input(f"{i['question']} (Choose A, B, C, or D): ")
        if user_answer.upper() == i["answer"]:
            correct_answers += 1
            print(f"You got {correct_answers} out of 5 questions correct.")
        print()


#take user choice
while True:
    print("Select the domain in which you need to play the quiz")
    input_user = input('''1.DataBase Management System (DBMS).
2.Data Structures (DS).
3.Operating System (OS).
''')
    if input_user == "1":
        dbms_questions()
    elif input_user == "2":
        ds_questions()
    elif input_user == "3":
        os_questions()
    else:
        print("invalid choice")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    
    if play_again != "yes":
        break
    
            


    



        

        
            
            
            
