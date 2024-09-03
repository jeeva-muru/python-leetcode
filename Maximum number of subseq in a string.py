def maximumSubsequenceCount(text, pattern):
    result = 0
    count0 = 0
    count1 = 0

    # for i, c in enumerate(text):
    for c in text:
      

      if c == pattern[0]:
        count0 += 1
        print("char", c + "=" + pattern[0])
        print("result", result)
        print("count0", count0)


      if c == pattern[1]:
        result += count0
        count1 += 1

        print("char", c + "=" + pattern[1])
        print("result", result)
        print("count1", count1) 

    # Adding pattern[0] in the beginning or
    # Adding pattern[1] in the end is optimal
    return result + max(count0, count1)

# count = maximumSubsequenceCount("abdacdbc", "ac")
count = maximumSubsequenceCount("abdcdbc", "ac")

print(count)
