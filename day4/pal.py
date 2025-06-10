
def palindrome(N):
    N = N.lower()
    for i in range(len(N) // 2):
        if N[i] != N[len(N) - 1 - i]:
            return "It is not a palindrome"
    return "It is a palindrome"

N = "madam"
print(palindrome(N))
