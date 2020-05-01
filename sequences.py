
def longest_common_subsequence(str1, str2):
        L1 = len(str1)
        L2 = len(str2)
        
        dp = [[0] * (L2 + 1) for _ in range(L1 + 1)]
        
        for i in range(1,L1+1):
            for j in range(1,L2+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])
              
        i = L1            
        j = L2
   
        res = ''
        
        while i > 0 or j > 0:
            if j > 0 and dp[i][j] == dp[i][j-1]:
                j -= 1
            elif i > 0 and dp[i][j] == dp[i-1][j]:
                i -= 1
            else:
                res += str1[i-1]
                i -= 1
                j -= 1
				
		return res
		
def longest_increasing_subsequence(seq):

	# To understand this algorithm, let's consider the following sequence
	# [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15].
	
	# Assume we are at position 5 in the sequence, and we ask ourselves
	# what the longest increasing subsequence in the sequence from 0-5 is.
	#
	#                   5
	#                   |
	#                   v
	# [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
	#
	#
	# Let's list all possible incr. subsequence before 10.
	# 
	# 0
	# 0,2
	# 0,4
	# 0,8
	# 0,12
	# 0,8,12
	# 0,4,12
	# 8
	# 8,12
	# 4
	# 4,12
	# 12
	# 2
	#
	# What are the most promising subsequences here?
	# 
	# For example 0,2 vs. 0,4. Which one is more promising?
	# 0,2 is better because we could append a 3 + all numbers we could append to 0,4
	# So we can forget about 0,4.
	# 
	# Let's do this for all subsequence of the same length.
	#
	# 0
	# 2        delete
	# 4        delete
	# 8        delete
	# 12       delete
	# 0,2
	# 0,4      delete
	# 0,8      delete
	# 4,12     delete
	# 8,12     delete
	# 0,12     delete
	# 0,8,12
	# 0,4,12
	#
	# Now we are left with only these subsequences.
	#
	# 0
	# 0,2
	# 0,8,12
	# 0,4,12   delete
	#
	# We further can also just keep one sequence of the 0,8,12 and 0,4,12 because they
	# are equally promising.
	#
	# 0
	# 0,2
	# 0,8,12
	#
	# Now let's append the 10 wherever it is possible. We end up with these sequences.
	#
	# 0,
	# 10,     delete
	# 0,2     
	# 0,10    delete
	# 0,2,10
	# 0,8,12  delete
	#
	# And again we delete.
	#
	# 0,
	# 0,2     
	# 0,2,10
	#
	# Let's continue to the next number 6.
	#
	# 6,       delete
	# 0,
	# 0,6      delete
	# 0,2 
	# 0,2,6     
	# 0,2,10   delete
	#
	# And we get:
	#
	# 0
	# 0,2 
	# 0,2,6
	#
	# Let's continue to the next number 14.
	#
	# 0
	# 0,2 
	# 0,2,6
	# 0,2,6,14
	#
	# We notice that instead of adding and then deleting, we could just 
	# replace the last value of the currently longest sequence with the last 
	# value greater or equal to the new value we want to add.
	#
	# If the new value larger than any last value, then we create a new sequence
	# by appending the new value to the longest sequence.
	#
	# Notice also that we do not actually care about the complete sequences in then
	# above procedure. All we need is the length and the last value of the current sequences.
	#
	# The algorithm below follows from above.
	# 
	#
	# t[i] stores the last value of the sequence of length i+1.
	# L tells us, how many sequences we are currently tracking.
	# p is used for restoring the final longest increasing subsequence.
	#

	N = len(seq)

	L = 0
	t = [0] * N
	p = [0] * N
	
	for i in range(N):
		
		j = bisect.bisect_left(t, seq[i], lo=0, hi=L)
		
		t[j] = seq[i]

		if j == 0:
			p[i] = -1
		else:
			p[i] = t[j-1]
		
		if j == L:
			L += 1
			
	res = []
	i = t[L-1]

	while i >= 0:    
		res.append(seq[i])
		i = p[i]
		
	return res[::-1]