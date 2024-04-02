#1
# def check_even_odd(number):
#     if number % 2 == 0:
#         print("It is an even number")
#     else:
#         print("It is odd")
# num = int(input("Enter a number: "))
# check_even_odd(num)

#2
# def print_square_dictionary():
#     square_dict = {}
#     for i in range(1, 21):
#         square_dict[i] = i ** 2
#     print(square_dict)
# print_square_dictionary()

#3
# def remove_vowels(input_string):
#     vowels = "aeiouAEIOU"
#     return ''.join([char for char in input_string if char not in vowels])
# input_string = input("Enter a string: ")
# result = remove_vowels(input_string)
# print("String with vowels removed:", result)

#4
# num_powers = 10
# powers_of_2 = map(lambda x: 2 ** x, range(num_powers))
# print("Powers of 2:")
# for power in powers_of_2:
#     print(power)

#6
# def create_dict(keys, values):
#     return dict(zip(keys, values))
# keys = input("Enter the keys separated by spaces: ").split()
# values = input("Enter the values separated by spaces: ").split()
# if len(keys) == len(values):
#     result_dict = create_dict(keys, values)
#     print("Resulting Dictionary:", result_dict)
# else:
#     print("Error: The two lists must be of the same length.")

#7
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# def print_fibonacci_series(num_terms):
#     if num_terms <= 0:
#         print("Please enter a positive integer.")
#     else:
#         print("Fibonacci Series:")
#         for i in range(num_terms):
#             print(fibonacci(i), end=" ")
# num_terms = int(input("Enter the number of terms for Fibonacci series: "))
# print_fibonacci_series(num_terms)

#8
# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return(n *factorial(n-1))
# num =int(input("enter a number",))
# print("number:",num)
# print("factorial:",factorial(num))

#12
# l=[]
# n =int(input("enter the number of elements:"))
# for i in range(1,n+1):
#     elem =int(input("enter the elements:"))
#     l.append(elem)
# l.sort()
# print("the sorted list:",l)
# print("the second smallest value of this list:",l[1])

#18
# def square_values(input_list):
#     squared_values = [num ** 2 for num in input_list]
#     return squared_values
# def main():
#     input_string = input("Enter a list of integers separated by space: ")
#     input_list = list(map(int, input_string.split()))
#     squared_values = square_values(input_list)
#     print("Squared values of the input list:", squared_values)
# if __name__ == "__main__":
#     main()

#9
# import time
# def calculate_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Time taken to execute {func.__name__}: {end_time - start_time} seconds")
#         return result
#     return wrapper
# @calculate_time
# def example_function_1():
#     time.sleep(2)  
#     print("Function 1 executed")
# @calculate_time
# def example_function_2():
#     time.sleep(1)  
#     print("Function 2 executed")
# example_function_1()
# example_function_2()

#10
# def divisible_by_5_and_7_generator(n):
#     for num in range(n + 1):
#         if num % 5 == 0 and num % 7 == 0:
#             yield num
# def main():
#     try:
#         n = int(input("Enter the value of n: "))
#         if n < 0:
#             raise ValueError("Input should be a non-negative integer.")
#         divisible_numbers = divisible_by_5_and_7_generator(n)
#         result = ', '.join(map(str, divisible_numbers))
#         print("Numbers divisible by both 5 and 7 between 0 and", n, ":", result)
#     except ValueError as ve:
#         print("Error:", ve)
# if __name__ == "__main__":
#     main()

#11
# def even_numbers_generator(n):
#     for num in range(n + 1):
#         if num % 2 == 0:
#             yield num
# def main():
#     try:
#         n = int(input("Enter the value of n: "))
#         if n < 0:
#             raise ValueError("Input should be a non-negative integer.")
#         even_numbers = even_numbers_generator(n)
#         result = ', '.join(map(str, even_numbers))
#         print("Even numbers between 0 and", n, ":", result)
#     except ValueError as ve:
#         print("Error:", ve)
# if __name__ == "__main__":
#     main()

#17
# def power_of_number(number, exponent=2):
#     return number ** exponent
# print("2 raised to the power of 3:", power_of_number(2, 3))
# print("3 raised to the power of 4:", power_of_number(3, 4))
# print("5 raised to the power of 2 (default exponent):", power_of_number(5))

#19
# def sum_of_numbers_up_to_n(n):
#     return (n * (n + 1)) // 2
# def main():
#     try:
#         n = int(input("Enter a number: "))
#         if n < 1:
#             raise ValueError("Input should be a positive integer.")
#         total_sum = sum_of_numbers_up_to_n(n)
#         print("Sum of all numbers from 1 to", n, ":", total_sum)
#     except ValueError as ve:
#         print("Error:", ve)
# if __name__ == "__main__":
#     main()


