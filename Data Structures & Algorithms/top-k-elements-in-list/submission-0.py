class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create dic to store each number and its frequency
        freq={}

        # travese the array and coyunt occcurrence of each number

        for num in nums:

            # if num exists increase its count by 1

            #if num doesnt exist strat its count from 0 and add 1

            freq[num]=freq.get(num,0)+1

    #    sort dictionary ketys based on their frequencise
    #    key=freq.get use frequency as teh sroting criteria

    # reverse = True arrange from highest frquency to lowerst

        sorted_nums= sorted(freq, key=freq.get, reverse=True)

        #return only the first k elements
        # [:k] extracts the k most freqent numbers

        return sorted_nums[:k]

