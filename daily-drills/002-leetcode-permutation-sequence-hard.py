def getPermutation(self, n: int, k: int) -> str:
    combinations=math.factorial(n)
    List=[str(i) for i in range(1,n+1)]
    p_seq=""
    for i in range(n,1,-1):
        combinations=combinations//i
        index,k=divmod(k,combinations)
        if(k==0): # signifies after keeping index -1 digits from the list into p_seq
            #we can just del index-1 th element from List followed by reversing List and merging it with p_seq that that is potentially the final answer
            p_seq+=List[index-1]
            del List[index-1]
            p_seq+="".join(List[::-1])
            return p_seq
            
            index-=1
        p_seq+=List[index]
        del List[index]
    return p_seq+List[0]
