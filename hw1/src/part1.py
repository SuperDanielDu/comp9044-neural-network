#!/usr/bin/env python3
"""
part1.py

UNSW COMP9444 Neural Networks and Deep Learning

ONLY COMPLETE METHODS AND CLASSES MARKED "TODO".

DO NOT MODIFY IMPORTS. DO NOT ADD EXTRA FUNCTIONS.
DO NOT MODIFY EXISTING FUNCTION SIGNATURES.
DO NOT IMPORT ADDITIONAL LIBRARIES.
DOING SO MAY CAUSE YOUR CODE TO FAIL AUTOMATED TESTING.
"""
import torch

# Simple addition operation

def simple_addition(x, y):
    """
    TODO: Implement a simple addition function that accepts two tensors and returns the result.
    """
    return torch.add(x, y)

# Resize tensors
# Use view() to implement the following functions ( flatten() and reshape() are not allowed )

def simple_reshape(x, shape):
    """
    TODO: Implement a function that reshapes the given tensor as the given shape and returns the result.
    """
    return x.view(shape)


def simple_flat(x):
    """
    TODO: Implement a function that flattens the given tensor and returns the result.
    """
    return x.view(-1)


# Transpose and Permutation

def simple_transpose(x):
    """
    TODO: Implement a function that swaps the first dimension and
        the second dimension of the given matrix x and returns the result.
    """
    return x.transpose(0, 1)


def simple_permute(x, order):
    """
    TODO: Implement a function that permute the dimensions of the given tensor
        x according to the given order and returns the result.
    """
    return x.permute(order)

# Matrix multiplication (with broadcasting).

def simple_dot_product(x, y):
    """
    TODO: Implement a function that computes the dot product of
        two rank 1 tensors and returns the result.
    """
    return torch.dot(x, y)

def simple_matrix_mul(x, y):
    """
    TODO: Implement a function that performs a matrix multiplication
        of two given rank 2 tensors and returns the result.
    """
    return torch.mm(x, y)


def broadcastable_matrix_mul(x, y):
    """
    TODO: Implement a function that computes the matrix product of two tensors and returns the result.
        The function needs to be broadcastable.
    """
    return torch.matmul(x, y)


# Concatenate and stack.
def simple_concatenate(tensors):
    """
    TODO: Implement a function that concatenates the given sequence of tensors
        in the first dimension and returns the result
    """
    return torch.cat(tensors, 0)

def simple_stack(tensors, dim):
    """
    TODO: Implement a function that concatenates the given sequence of tensors
        along a new dimension(dim) and returns the result.
    """
    return torch.stack(tensors, dim)

#
# #注: .cat 和 .stack的区别在于 cat会增加现有维度的值,可以理解为续接，stack会新加增加一个维度，可以
# 理解为叠加
# >>> a=torch.Tensor([1,2,3])
# >>> torch.stack((a,a)).size()
# torch.size(2,3)
# >>> torch.cat((a,a)).size()
# torch.size(6)