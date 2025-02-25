from GF import GF
from polynomials import Polynomials

pi_vector = bytearray([
    252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 233,
    119, 240, 219, 147, 46, 153, 186, 23, 54, 241, 187, 20, 205, 95, 193, 249, 24, 101,
    90, 226, 92, 239, 33, 129, 28, 60, 66, 139, 1, 142, 79, 5, 132, 2, 174, 227, 106, 143,
    160, 6, 11, 237, 152, 127, 212, 211, 31, 235, 52, 44, 81, 234, 200, 72, 171, 242, 42,
    104, 162, 253, 58, 206, 204, 181, 112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156,
    183, 93, 135, 21, 161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178,
    177, 50, 117, 25, 61, 255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87, 223,
    245, 36, 169, 62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3, 224, 15, 236,
    222, 122, 148, 176, 188, 220, 232, 40, 80, 78, 51, 10, 74, 167, 151, 96, 115, 30, 0,
    98, 68, 26, 184, 56, 130, 100, 159, 38, 65, 173, 69, 70, 146, 39, 94, 85, 47, 140, 163,
    165, 125, 105, 213, 149, 59, 7, 88, 179, 64, 134, 172, 29, 247, 48, 55, 107, 228, 136,
    217, 231, 137, 225, 27, 131, 73, 76, 63, 248, 254, 141, 83, 170, 144, 202, 216, 133,
    97, 32, 113, 103, 164, 45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166,
    116, 210, 230, 244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182
])

inv_pi_vector = bytearray([
    165, 45, 50, 143, 14, 48, 56, 192, 84, 230, 158, 57, 85, 126, 82, 145,
    100, 3, 87, 90, 28, 96, 7, 24, 33, 114, 168, 209, 41, 198, 164, 63, 224,
    39, 141, 12, 130, 234, 174, 180, 154, 99, 73, 229, 66, 228, 21, 183, 200,
    6, 112, 157, 65, 117, 25, 201, 170, 252, 77, 191, 42, 115, 132, 213, 195,
    175, 43, 134, 167, 177, 178, 91, 70, 211, 159, 253, 212, 15, 156, 47, 155,
    67, 239, 217, 121, 182, 83, 127, 193, 240, 35, 231, 37, 94, 181, 30, 162,
    223, 166, 254, 172, 34, 249, 226, 74, 188, 53, 202, 238, 120, 5, 107, 81,
    225, 89, 163, 242, 113, 86, 17, 106, 137, 148, 101, 140, 187, 119, 60, 123,
    40, 171, 210, 49, 222, 196, 95, 204, 207, 118, 44, 184, 216, 46, 54, 219,
    105, 179, 20, 149, 190, 98, 161, 59, 22, 102, 233, 92, 108, 109, 173, 55, 97,
    75, 185, 227, 186, 241, 160, 133, 131, 218, 71, 197, 176, 51, 250, 150, 111, 110,
    194, 246, 80, 255, 93, 169, 142, 23, 27, 151, 125, 236, 88, 247, 31, 251, 124,
    9, 13, 122, 103, 69, 135, 220, 232, 79, 29, 78, 4, 235, 248, 243, 62, 61, 189,
    138, 136, 221, 205, 11, 19, 152, 2, 147, 128, 144, 208, 36, 52, 203, 237, 244,
    206, 153, 16, 68, 64, 146, 58, 1, 38, 18, 26, 72, 104, 245, 129, 139, 199, 214,
    32, 10, 8, 0, 76, 215, 116
])

from_char_to_poly = lambda number, modulus = 2: Polynomials(modulus,
                                                        [int(elem) for elem in bin(number)[2:][::-1]])

from_poly_to_char = lambda polynomial: int("".join(list(reversed([str(cooeff) for cooeff in polynomial.cooeffs]))), 2)

pi_transformation = lambda number, vector: vector[number]


def linear_transformation(block: bytearray):
    transformation_coeffs = bytearray([
        0x94, 0x20, 0x85, 0x10, 0xC2, 0xC0, 0x01, 0xFB, 0x01, 0xC0, 0xC2, 0x10, 0x85, 0x20, 0x94, 0x01
    ])
    primitive_poly = Polynomials(2, [1, 1, 0, 0, 0, 0, 1, 1, 1])
    galois_field = GF(2, primitive_poly)
    current_poly = None
    for i in range(16):
        summand = galois_field.multiplication_of_polynomials(from_char_to_poly(transformation_coeffs[i]),
                                                             from_char_to_poly(block[i]))
        if current_poly is None:
            current_poly = summand
        else:
            current_poly = galois_field.addition_of_polynomials(
                current_poly, summand
            )
    return from_poly_to_char(current_poly)


def big_r_transformation(block: bytearray):
    return_block = list()
    for i in range(16):
        if i == 0:
            return_block.append(linear_transformation(block))
        else:
            return_block.append(block[i - 1])
    return bytearray(return_block)


def reverse_big_r_transformation(block: bytearray):
    return_block = list()
    last_element = linear_transformation(bytearray([block[i+1] for i in range(len(block) - 1)] + [block[0]]))
    for i in range(16):
        if i == 15:
            return_block.append(last_element)
        else:
            return_block.append(block[i+1])
    return bytearray(return_block)


def X_K(key: bytearray, block: bytearray):
    result = bytearray()
    for i in range(16):
        result.append(key[i] ^ block[i])
    return result


def S(block: bytearray, inv: bool):
    result = list()
    for i in range(16):
        result.append(pi_transformation(block[i], inv_pi_vector if inv else pi_vector))
    return bytearray(result)


def L(block: bytearray, inv: bool):
    current_block = block
    for i in range(16):
        current_block = reverse_big_r_transformation(current_block) if inv else big_r_transformation(current_block)
    return current_block

def F_k(k: bytearray, a_1: bytearray, a_0: bytearray):
    return [X_K(L(S(X_K(a_1, k), False), False), a_0), a_1]


def deploying_keys(key: bytearray):
    keys = [key[:16], key[16:]]
    for i in range(1, 5):
        left_operand, right_operand = keys[2*i - 2], keys[2*i - 1]
        for j in range(1, 9):
            C = L(bytearray((8*(i-1) + j).to_bytes(16, byteorder='big')), False)
            left_operand, right_operand = F_k(C, left_operand, right_operand)
        keys.extend([left_operand, right_operand])
    return keys


def block_encryption(block: bytearray, keys: list):
    current_value = L(S(X_K(keys[0], block), False), False)
    for i in range(1, 9):
        current_value = L(S(X_K(keys[i], current_value), False), False)
    return X_K(keys[9], current_value)


def block_decryption(block: bytearray, keys: list):
    current_value = S(L(X_K(keys[-1], block), True), True)
    for i in range(2, 10):
        current_value = S(L(X_K(keys[-i], current_value), True), True)
    return X_K(keys[-10], current_value)
