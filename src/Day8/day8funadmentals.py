

import numpy as np

#one mentional
a=np.array([1,2,3])
b=np.array([10,20,30])
result = a + b
print("One dimensional")
print(result)

#2 dimensional

c=np.array([[1,2,3],
            [4,5,6]])
d=np.array([[10,11,12],
            [7,8,9]])
result1=c+d
print("two dimensional")
print(result1)

#multi dimensional
e=np.array([[1,2,3],
            [4,5,6]])
f=np.array([[10,20,30],
            [20,10,30]])
result2= e + f
print("multi dimensional")
print(result2)

# Vectorized vs Loop example
arr = np.random.rand(100)
# Vectorized
squared = arr ** 2
print(arr)
print(squared)


#reshap
arr = np.arange(27)
reshaped = arr.reshape(9, 3)
print(reshaped)

#restack
a = np.array([[1, 2,3]])
b = np.array([[4,5,6]])

vstacked = np.vstack((a, b))
print(vstacked)

hstacked = np.hstack((a, b))
print(hstacked)


#static
data = np.array([[10, 20, 30],
                 [40, 50, 60]])

print(np.mean(data))
print(np.mean(data, axis=0))
print(np.mean(data, axis=1))

#linear algibra
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(np.dot(A, B))


#linespace

arr=np.array([[1,2,3],[4,5,6]])
arr=np.linspace(0, 2 ,5)
print(arr)



######task1###########
import numpy as np

scores = np.random.randint(50, 101, size=(5, 3))

subject_mean = scores.mean(axis=0)

centered_scores = scores - subject_mean

print("Original Scores:\n", scores)
print("\nSubject-wise Mean:\n", subject_mean)
print("\nCentered (Normalized) Scores:\n", centered_scores)



###task2########
import numpy as np

data = np.arange(24)
reshaped_data = data.reshape(4, 3, 2)
final_data = reshaped_data.transpose(0, 2, 1)

print("Final Shape:", final_data.shape)
print("\nFinal Array:\n", final_data)



