    # [8,2,1,0,9,8,10,4,2,3]
    # 8, 2,1,0,9
    # 8,10,4,2,3


    # 8,2,1,0,9
    # 8,2,1
    # 0,9

    # 8,2,1
    # 8,2
    # 1

    # 8,2
    # 8
    # 2


class MergeSort():


    def sort(self, numbers):

        self.sort_rec(numbers, [], 0, len(numbers) - 1)

        return numbers


    def sort_rec(self, numbers, helper, start, end):

        print("start: ", start)
        print("end: ", end)
        if start < end:

            mid = int((start + end)/2)
            first = self.sort_rec(numbers, helper, start, mid)
            second = self.sort_rec(numbers, helper, mid+1, end)

            self.merge(numbers, helper, start, mid, end)


    def merge(self, numbers, helper, start, mid, end):


        print("current: ", start)
        print(numbers)


        print("start: ", start)
        print("end", end)
        for i in range(start, end-1):
            helper[i] = numbers[i]


        h_left = start
        h_right = mid + 1
        current = start

        while h_left < mid and h_right < end:

            if numbers[h_left] <= numbers[h_right]:
                numbers[current] = helper[h_left]
                h_left += 1

            else:
                numbers[current] = helper[h_right]
                h_right += 1

            current += 1

        remaining = mid - h_left
        for i in range(0, remaining-1):
            numbers[current + i] = helper[h_left + i]


if __name__ == "__main__":

    lst = [8,2,1,0,9,8,10,4,2,3]

    ms = MergeSort()
    print(ms.sort(lst) == lst.sort())

