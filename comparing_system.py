from link import token_segment
from setup_token import token


First_token = token
Second_token = token_segment

print(First_token)
print(Second_token)


if First_token == Second_token:
    print("Token is correct")

else:
    print("Token is incorrect")