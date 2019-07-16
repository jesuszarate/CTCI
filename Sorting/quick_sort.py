
class QuickSort:

    '''
    [2, 1, 3, 3, 4, 5]

    [2, 1, 3],3,[4, 5]
    '''

    def sort(self, arr):
        self.q_sort(arr, 0, len(arr) - 1)

    def q_sort(self, arr, low, high):

        if low <= high:
            index = self.partition(arr, low, high) # This is the only item that we know is in the correct spot so we leave it where it is

            self.q_sort(arr, low, index - 1)
            self.q_sort(arr, index + 1, high)



    def partition(self, arr, low, high):

        p = self.pivot(arr, low, high)
        pivot = arr[p]

        left = low
        right = high  # Subtract one because now we have put the pivot at the last spot

        print("pivot: ", pivot)

        print("left: ", left)
        print("right: ", right)
        while left < right:

            if arr[left] < pivot: left += 1
            if arr[right] >= pivot: right -= 1


            print("left: ", left)
            print("right: ", right)

            print("l: ", arr[left])
            print("r: ", arr[right])
            if arr[left] > arr[right]:
                self.swap(arr, left, right)

                left += 1
                right -= 1

        return left


    def pivot(self, arr, low, high):
        return (low + high) // 2

    def swap(self, arr, one, two):
        arr[one], arr[two] = arr[two], arr[one]


if __name__ == "__main__":

    qs = QuickSort()

    arr = [2, 1, 3, 5, 3, 4]
    arr = [2, 1, 3, 5, 4, 3]


    qs.sort(arr)
    #qs.q_sort(arr, 4, 5)

    print(arr)

