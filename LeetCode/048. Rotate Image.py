class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)/2):
            first = i
            last = len(matrix)-1-i
            for j in range(i,len(matrix)-1-i):

                f = j
                l = len(matrix)-1-j
                temp = matrix[first][f]
                matrix[first][f] = matrix[l][first]
                matrix[l][first] = matrix[last][l]
                matrix[last][l] = matrix[f][last]
                matrix[f][last] = temp