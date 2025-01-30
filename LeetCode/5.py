def longestPalindrome(s):
  if not s or len(s) == 1:
    return s

  def expandAroundCenter(left: int, right: int) -> str:
    while left >= 0 and right < len(s) and s[left] == s[right]:
      left -= 1
      right += 1
    return s[left + 1:right]

  max_palindrome = ""
  for i in range(len(s)):
    odd_palindrome = expandAroundCenter(i, i)
    even_palindrome = expandAroundCenter(i, i + 1)
    max_palindrome = max(max_palindrome, odd_palindrome, even_palindrome, key=len)

  return max_palindrome

print(longestPalindrome("abccbaedhe"))