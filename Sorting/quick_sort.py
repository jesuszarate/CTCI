
class QuickSort:

    '''
    [2, 1, 3, 3, 4, 5]

    [2, 1, 3],3,[4, 5]
    '''

    def sort(self, arr):
        self.sortRec(arr, 0, len(arr) - 1)

    def sortRec(self, arr, start, end):

        if start < end:
            pi = self.partition(arr, start, end)
            self.sortRec(arr, start, pi - 1)
            self.sortRec(arr, pi + 1, end)


    def partition(self, arr, start, end):

        piv = self.pivot(arr, start, end)
        self.swap(arr, piv, end)
        left = start
        right = end - 1

        while left < right:

            if arr[left] < arr[end]:
                left += 1
                continue

            if arr[right] > arr[end]:
                right -= 1
                continue

            if arr[left] > arr[right]:
                self.swap(arr, left, right)
                left += 1
                right -= 1

        self.swap(arr, left, end)
        return left

    def pivot(self, arr, low, high):
        return (low + high) // 2

    def swap(self, arr, one, two):
        arr[one], arr[two] = arr[two], arr[one]


if __name__ == "__main__":

    qs = QuickSort()

    arr = [2, 1, 3, 5, 3, 4]
    arr = [2, 1, 3, 5, 4, 3]
    arr = [4, 1, 5, 6, 2, 3]


    qs.sort(arr)
    #qs.partition(arr, 4, 5)

    print(arr)

