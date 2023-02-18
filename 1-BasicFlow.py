"""
Flow : Flow is the basis of all prefect workflows. The flow is decorated using @flow decorator
"""

from prefect import flow

@flow
def my_favourite_number() :
    print("What is your favourite number")
    return 19

if __name__ == "__main__" :
    print(my_favourite_number())

