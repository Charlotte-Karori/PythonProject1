import sys
import numpy as np

def main():
    #creating two 2*2 arrays
    a = np.array([[4,2],
                  [6,4]])
    b=np.array([[5,3],
                [7,1]])
    #computing elementwise addition
    result_1=np.add(a,b)
    print(f"a+b={result_1}")
    #computing elementwise multiplication
    result_2=np.multiply(a,b)
    print(f"a*b={result_2}")
    #computing the matrix product A@B
    result_3=a@b
    print(f"a@b={result_3}")
    return 0
if __name__ == '__main__':
    sys.exit(main())
