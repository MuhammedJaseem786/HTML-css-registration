class Error(Exception):
    pass
class ValueTooSmall(Error):
    pass
class Valuetoolarge(Error):
    pass
while(True):
    num = int(input("Enter any value in 10 to 50 range"))
    if num < 10:
        raise ValuetoosmallError
    elif num > 50:
         raise ValuetoolargeError
      break
    except ValueTooSmallError:
        print("Value is below range... Try again")
    except Valuetoolarge:
        print("value is above range... Try again")
print("Value is in the correct range")