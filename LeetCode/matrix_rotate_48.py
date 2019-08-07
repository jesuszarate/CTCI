class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        layer_start = 0
        layer = len(matrix) - 1

        for i in range(layer_start, layer):
            tmp = [matrix[i][k] for k in range(layer_start, layer+1)]
            tmp2 = []
            for j in range(layer_start, layer):
                tmp2.append(matrix[j][layer])
                matrix[j][layer] = tmp[j - layer_start]

            tmp = []
            for j in range(layer, layer_start, -1):
                tmp.append(matrix[layer][j])
                matrix[layer][j] = tmp2[layer - j]

            tmp2 = []
            for j in range(layer, layer_start, -1):
                tmp2.append(matrix[j][i])
                matrix[j][i] = tmp[layer - j]

            tmp = []
            for j in range(layer_start, layer):
                tmp.append(matrix[i][j])
                matrix[i][j] = tmp2[j - layer_start]

            layer -= 1
            layer_start += 1

        print('')

s = Solution()

m = [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ]

m1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

m3 = [[1,2],[3,4]]


s.rotate(m3)

print(m1)