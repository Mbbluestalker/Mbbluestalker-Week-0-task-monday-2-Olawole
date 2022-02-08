def nameValidator(name):
    arr = name.split()
    if name == "" or name == " ":
        return "Name Should Not Be Empty"
    elif len(arr) > 2 or name.count(" ") > 1 or len(arr) == 1:
        return "Please Enter Only Your FirstName And LastName With A Single Space Separating Them"
    elif len(arr[0]) < 5 or len(arr[1]) < 5:
        return "Your FirstName or LastName should not be less than 5 characters"
    elif len(arr[0]) > 20 or len(arr[1]) > 20:
        return "Your FirstName or LastName should not be more than 20 characters"
    elif arr[0].isalpha() == True and arr[1].isalpha() == True:
        return "VALIDATION SUCCESSFUL"
    else:
        return "Name Should Contain Only Alphabetic Characters"


print(nameValidator("akjlo bbubkns"))