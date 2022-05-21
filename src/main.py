from proto.mat import Matrix
from utils.mat_util import mat_mul

a = Matrix([[1, 2], [3, 4]])
b = Matrix([[5, 6], [7, 8]])

result = mat_mul(a, b).data
print(result)


a = 257
b = 257

print('a is b: {}'.format(a is b))