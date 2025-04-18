# def toString(List):
#     return ''.join(List)
#
# # Function to print permutations of string
# # This function takes three parameters:
# # 1. String
# # 2. Starting index of the string
# # 3. Ending index of the string.
# def permute(a, l, r):
#     print("new call: ",l,r,a)
#     if l==r:
#         print (toString(a))
#     else:
#         for i in range(l,r):
#             print("i: ",i,l,r,a)
#             a[l], a[i] = a[i], a[l]
#             permute(a, l+1, r)
#             print("Backtracking")
#             a[l], a[i] = a[i], a[l] # backtrack
#
# # Driver program to test the above function
# string = "ABC"
# n = len(string)
# a = list(string)
# permute(a, 0, n)



# Python program to implement
# the above approach
def permute(s, answer):
    if (len(s) == 0):
        print(answer, end = "  ")
        return

    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        permute(rest, answer + ch)

# Driver Code
answer = ""
s = input("Enter the string : ")
print("All possible strings are : ")
permute(s, answer)