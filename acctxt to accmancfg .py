# Read acc_manager
with open("acc_manager.cfg", "r") as file:
    main_text = file.readlines()

# Read acctxt
with open("accounts.txt", "r") as accounts_file:
    accounts_text = accounts_file.readlines()

# Iterate till15
for i in range(1, 16):
    # Extract login and pass from the acc.txt
    account_info = accounts_text[i - 1].strip().split(":")
    login = account_info[0]
    password = account_info[1]

    # replacement start
    login_line = f"bot_{i}_login={login}\n"
    pass_line = f"bot_{i}_pass={password}\n"

    # Replacement end
    for j in range(len(main_text)):
        if main_text[j].startswith(f"bot_{i}_login="):
            main_text[j] = login_line
        elif main_text[j].startswith(f"bot_{i}_pass="):
            main_text[j] = pass_line

# Write 
with open("acc_manager.cfg", "w") as file:
    file.writelines(main_text)
