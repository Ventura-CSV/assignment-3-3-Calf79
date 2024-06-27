def main():
    email = input('Enter your email: ')
    """
    ########################################
    Code Your Program here
    ########################################
    """
    alphabet = email[0].isalpha()
    length = 5 <len(email)<30
    need = '@' in email
    dotn = '.' in email [email.index('@'):]
    result = alphabet and length and need and dotn
    print(result)
    
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
