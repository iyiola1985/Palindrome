def fill_palindrome(S):
    # Convert to list for easier manipulation
    chars = list(S)
    N = len(chars)
    
    # Check for palindrome and fill in question marks
    for i in range(N // 2):
        left = chars[i]
        right = chars[N - 1 - i]
        
        # Case 1: If both are question marks
        if left == '?' and right == '?':
            chars[i] = chars[N - 1 - i] = 'a'
        # Case 2: If only left is question mark
        elif left == '?':
            chars[i] = right
        # Case 3: If only right is question mark
        elif right == '?':
            chars[N - 1 - i] = left
        # Case 4: If neither are question marks and don't match
        elif left != right:
            return "NO"
    
    # Handle middle character for odd length strings
    if N % 2 == 1 and chars[N // 2] == '?':
        chars[N // 2] = 'a'
    
    return ''.join(chars)
# Test cases
print(fill_palindrome("?ab??a"))  # Should return "aabbaa"
print(fill_palindrome("bab??a"))  # Should return "NO"
print(fill_palindrome("?a?"))      # May return "aaa" or "zaz", among others