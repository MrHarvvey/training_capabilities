##zalożenia
#sleep_in(False, False) → True
#sleep_in(True, False) → False
#sleep_in(False, True) → True




def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


print(sleep_in(False, True))

def sleep_in2(weekday2, vacatioon2):
    return not weekday2 or vacatioon2

print(sleep_in2(True, False))