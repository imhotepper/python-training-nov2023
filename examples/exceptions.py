# import traceback


def validate_email(email_address):
    username, domain = email_address.split("@")
    if "." not in domain:
        raise LookupError("Domain contains no dot.")
    return username, domain


addresses = [
    "test@example.com",
    "admin@examplecom",
    "test@test@example.com",
    "example.com",
]

for address in addresses:
    try:
        user, dom = validate_email(address)
    except ValueError:
        print(f"Exception occurred for {address}.")
    except LookupError as ex:
        print(ex, type(ex))
        # traceback.print_exception(ex)
        # traceback.print_tb(ex.__traceback__)
    else:
        print(f"Valid address {address}; username is: {user}")
    finally:
        print("Executes every time")

print("End of script")
