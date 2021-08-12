from string import digits, ascii_letters
import re

chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'E', 'I', 'INT+', 'INT-', "Y'", 'abs', 'acos', 'acosh', 'acoth', 'add', 'asin', 'asinh', 'atan', 'atanh', 'cos', 'cosh', 'div', 'exp', 'ln', 'mul', 'pi', 'pow', 'sign', 'sin', 'sinh', 'sqrt', 'sub', 'tan', 'tanh', 'x']
pre_dict = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', 'E': 'a', 'I': 'b', 'INT+': 'c', 'INT-': 'd', "Y'": 'e', 'abs': 'f', 'acos': 'g', 'acosh': 'h', 'acoth': 'i', 'add': 'j', 'asin': 'k', 'asinh': 'l', 'atan': 'm', 'atanh': 'n', 'cos': 'o', 'cosh': 'p', 'div': 'q', 'exp': 'r', 'ln': 's', 'mul': 't', 'pi': 'u', 'pow': 'v', 'sign': 'w', 'sin': 'x', 'sinh': 'y', 'sqrt': 'z', 'sub': 'A', 'tan': 'B', 'tanh': 'C', 'x': 'D'}
post_dict = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', 'a': 'E', 'b': 'I', 'c': 'INT+', 'd': 'INT-', 'e': "Y'", 'f': 'abs', 'g': 'acos', 'h': 'acosh', 'i': 'acoth', 'j': 'add', 'k': 'asin', 'l': 'asinh', 'm': 'atan', 'n': 'atanh', 'o': 'cos', 'p': 'cosh', 'q': 'div', 'r': 'exp', 's': 'ln', 't': 'mul', 'u': 'pi', 'v': 'pow', 'w': 'sign', 'x': 'sin', 'y': 'sinh', 'z': 'sqrt', 'A': 'sub', 'B': 'tan', 'C': 'tanh', 'D': 'x'}

new_file = open("alpha.test", "a+")

#old_file = open("new_prim_fwd.train", "r")
count1 = 0
count2 = 5500


with open("prim_fwd.valid") as fileobject:
    for line in fileobject:
        if count1 > 0:
            count1 -= 1
            continue
        #new_file.write(line)
        if count2 > 0:
            line = line.split('|')[1]
            for key in sorted(pre_dict, key=len, reverse=True):
                line = line.replace(key, pre_dict[key])
                line = line.replace(' ', '')
            new_file.write(line)
            count2-=1
        else:
            break