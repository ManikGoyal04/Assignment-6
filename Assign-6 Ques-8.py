class FindThreeElements:
    def __init__(self, arr):
        self.arr = arr

    def find(self):
        n = len(self.arr)
        found = False
        result = []
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if (self.arr[i] + self.arr[j] + self.arr[k] == 0):
                        result.append([self.arr[i], self.arr[j], self.arr[k]])
                        found = True

        if (found == False):
            print("No three elements sum to zero")
        else:
            print(result)

arr = [-25, -10, -7, -3, 2, 4, 8, 10]
find_three_elements = FindThreeElements(arr)
find_three_elements.find()
