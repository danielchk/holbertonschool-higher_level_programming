#!/usr/bin/python3
"""
module 100-matrix_mul
"""


def matrix_mul(m_a, m_b):
    """
    multiplies m_a and m_b
    """
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    lens = len(m_a)
    len1 = len(m_a[0])
    len2 = len(m_b[0])
    if lens == 0 or len1 == 0:
        raise ValueError('m_a can\'t be empty')
    if len(m_b) == 0 or len2 == 0:
        raise ValueError('m_b can\'t be empty')
    for walk in m_a:
        if len(walk) != len1:
            raise TypeError('each row of m_a must should be of the same size')
        for i in walk:
            if type(i) is not int and type(i) is not float:
                raise TypeError('m_a should contain only integers or floats')
    for walk in m_b:
        if len(walk) != len2:
            raise TypeError('each row of m_b must should be of the same size')
        for i in walk:
            if type(i) is not int and type(i) is not float:
                raise TypeError('m_b should contain only integers or floats')
    if len1 != len2:
        raise ValueError('m_a and m_b can\'t be multiplied')
    result = []
    for a in range(lens):
        row2 = []
        for b in range(len2):
            num = 0
            for c in range(len1):
                num += m_a[a][c] * m_b[c][b]
            row2.append(num)
        result.append(row2)
    return result