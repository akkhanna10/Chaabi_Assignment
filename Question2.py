# ====================PROBLEM========================
'''
Write a program that returns the file type from a file name. The type of the
file is determined from the extension. Initially, a list of values of the
form "extension,type"(e.g. xls,spreadsheet;png,image) will be input.
The program takes input in the following form:1. Input
extension and type values in the form of a string having the following
format: a. "extension1,type1;extension2,type2;extension3,type3" b. E.g.
If we needed to input xls → spreadsheet, xlsx → spreadsheet, jpg → image
our string would be something like: "xls,spreadsheet;xlsx,spreadsheet;jpg,
image" 2. Input a list of filename.extension. E.g. an input list could be
something like ["abc.html","xyz.xls", "text.csv", "123"]
The program should return a dict of filename: type pairs.

'''


# ===================SOLUTION=========================


def fileType(extension_type_list, names):
    # Creating a empty dictionary
    extension_dict = {}
    # Iterating extension_type_list
    for pair in extension_type_list.split(';'):
        # Storing extension and filetype based on delimiter ','
        extension, file_type = pair.split(',')
        # Mapping Key-Value pair
        extension_dict[extension] = file_type

    # To store the result
    file_type_dict = {}
    # Iterating over names
    for filename in names:
        # to access the part before and after '.'
        filename_parts = filename.split('.')
        # If filename_parts has one or more parts means it has extension
        if len(filename_parts) > 1:
            # Accessing the last(extension part)
            extension = filename_parts[-1]
            # If not in exatension_dict then "unknown"
            file_type = extension_dict.get(extension, 'unknown')
            # Assingning key-value pair
            file_type_dict[filename] = file_type
        else:
            # It means no extension is there. So, 'unknown'
            file_type_dict[filename] = 'unknown'

    return file_type_dict


# Driver Code
extension_type_list = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
names = ["abc.jpg", "xyz.xls", "text.csv", "123"]
result = fileType(extension_type_list, names)
print(result)
