def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Prototype: def matrix_divided(matrix, div):
    matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception
    Each row of the matrix must be of the same size, otherwise raise a TypeError exception
    div must be a number (integer or float), otherwise raise a TypeError exception
    div can’t be equal to 0, otherwise raise a ZeroDivisionError exception
    All elements of the matrix should be divided by div, rounded to 2 decimal places
    Returns a new matrix
    You are not allowed to import any module
    """

    # Validate matrix input
    if not all(isinstance(row, list) for row in matrix) or not all(all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate matrix size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div input
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div, rounded to 2 decimal places
    result_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return result_matrix
