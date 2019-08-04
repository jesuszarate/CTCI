
class SubsetsNoDuplicates:

    def subsets(self, nums):
        lst = list()
        lst.sort()
        self.backtrack(lst, list(), nums, 0) # Sorting somehow maks it faster learn why
        return lst

    def backtrack(self, lst, tmp_list, nums, ind):
        lst.append([i for i in tmp_list])
        for i in range(ind, len(nums)):

            tmp_list.append(nums[i])
            self.backtrack(lst, tmp_list, nums, i+1)

            del tmp_list[-1]


if __name__ == "__main__":
    subset_no_dups = SubsetsNoDuplicates()
    print(subset_no_dups.subsets(['a','a','b']))
