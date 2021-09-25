import asyncio
import time
from random import randint

@asyncio.coroutine

def StartState():
    print("Explorand lumea dupa comori, gasesti un castel. \n")
    input_value = randint(0,1)
    time.sleep(1)
    if (input_value == 0):
        result = yield from State1(input_value)
    else :
        result = yield from State2(input_value)
    if (input_value == 0):
        result = "Inconjori castelul " + result
    else:
        result = "Intri pe poarta " + result
    print("Resume of the Transition : \nStart State calling " \
          + result)

@asyncio.coroutine

def State1(transition_value):
    outputValue = str((". Gasesti o intrare secreta dar este incuiata. = %s \n"\
                       %(transition_value)))
    input_value_camera = 0
    time. sleep(1)
    print("...Evaluating...")
    if (input_value_camera == 0):
        result = yield from State2(input_value_camera)
    result = "Intri in curte " + result
    return (outputValue + str(result))

@asyncio.coroutine

def State2(transition_value):
    outputValue = str((". Ajungi in curtea castelului = %s \n" \
                       %(transition_value)))
    input_value = randint(0,2)
    time.sleep(1)
    print("...Evaluating...")
    if (input_value == 0):
        result = yield from State1(input_value)
    elif input_value == 1 :
        result = yield from State9(input_value)
    elif input_value == 2 :
        result = yield from State3(input_value)
    if (input_value == 0):
        result = "Te duci la intrarea secreta " + result
    elif input_value == 1:
        result = "Explorezi curtea " + result
    elif input_value == 2:
        result = "Intri in castel " + result
    return (outputValue + str(result))


@asyncio.coroutine

def State3(transition_value):
    outputValue = str((". Gasesti o camera cu trepte in fata, o usa in stanga si una in dreapta. = %s \n" \
                       %(transition_value)))
    input_value = randint(0,2)
    time.sleep(1)
    print("...Evaluating...")
    if (input_value == 0):
        result = yield from State6(input_value)
    elif input_value == 1 :
        result = yield from State4(input_value)
    elif input_value == 2 :
        result = yield from State5(input_value)
    if (input_value == 0):
        result = "Urci treptele " + result
    elif input_value == 1:
        result = "Deschizi usa din stanga " + result
    elif input_value == 2:
        result = "Deschizi usa din dreapta " + result

    return (outputValue + str(result))


@asyncio.coroutine

def State4(transition_value):
    outputValue = str((". Gasesti o camera cu un birou = %s \n" \
                       %(transition_value)))
    input_value = randint(0,1)
    time.sleep(1)
    print("...Evaluating...")
    if (input_value == 0):
        result = yield from State3(input_value)
    else :
        result = yield from State11(input_value)
    if (input_value == 0):
        result = "Pleci din camera " + result
    else:
        result = "Te odihnesti pe scaun " + result
    return (outputValue + str(result))

@asyncio.coroutine

def State5(transition_value):
    outputValue = str((". Gasesti o bucatarie cu doua usi = %s \n" \
                       %(transition_value)))
    input_value = randint(0,1)
    time.sleep(1)
    print("...Evaluating...")
    if (input_value == 0):
        result = yield from State3(input_value)
    else :
        result = yield from State6(input_value)
    if (input_value == 0):
        result = "Te intorci " + result
    else:
        result = "Mergi prin usa din stanga " + result
    return (outputValue + str(result))


@asyncio.coroutine

def State6(transition_value):
    outputValue = str((". Ajungi in camera tronului unde se afla doua usi in capat = %s \n" \
                       %(transition_value)))
    input_value = randint(0,1)
    time.sleep(1)
    print("...Evaluating...")
    if (input_value == 0):
        result = yield from State5(input_value)
    else:
        result = yield from State7(input_value)
    if (input_value == 0):
        result = "Mergi prin usa din dreapta " + result
    else:
        result = "Mergi prin usa din stanga " + result
    return (outputValue + str(result))

@asyncio.coroutine

def State7(transition_value):
    outputValue = str((". Intri intr-un hol cu o usa in capat = %s \n" \
                       %(transition_value)))
    input_value = randint(0,2)
    time.sleep(1)
    print("...Evaluating...")
    if (input_value == 0):
        result = yield from State8(input_value)
    elif input_value == 1:
        result = yield from EndState(input_value)
    elif input_value == 2:
        result = yield from State6(input_value)
    if (input_value == 0):
        result = "Mergi prin usa din capat " + result
    elif input_value == 1:
        result = "Mergand prin hol, te sprijini de perete si se apasa o piatra, deschizandu-se o usa secreta. " + result
    elif input_value == 2:
        result = "Mergi prin usa spre camera tronului " + result
    return (outputValue + str(result))

@asyncio.coroutine

def State8(transition_value):
    outputValue = str((". Ai ajuns in camera regelui. = %s \n" \
                       %(transition_value)))
    input_value = randint(0,1)
    time.sleep(1)
    print("...Evaluating...")
    if (input_value == 0):
        result = yield from State7(input_value)
    else:
        result = yield from State10(input_value)
    if (input_value == 0):
        result = "Te intorci pe hol " + result
    else:
        result = "Te arunci in patul regelui " + result
    return (outputValue + str(result))

@asyncio.coroutine

def State9(transition_value):
    outputValue = str((". N-ai gasit nimic! = %s \n" \
                       %(transition_value)))
    input_value = randint(0,1)
    time.sleep(1)
    print("...Evaluating...")
    if (input_value == 0):
        result = yield from State3(input_value)
    else:
        result = yield from State3(input_value)
    result = "Intri in castel " + result
    return (outputValue + str(result))

@asyncio.coroutine

def State10(transition_value):
    outputValue = str((". Patul este comfortabil = %s \n" \
                       %(transition_value)))
    input_value = randint(0,1)
    time.sleep(1)
    print("...Evaluating...")
    if (input_value == 0):
        result = yield from State8(input_value)
    else:
        result = yield from State8(input_value)
    result = "Realizezi ca n-ai timp de pierdut si pleci " + result
    return (outputValue + str(result))

@asyncio.coroutine

def State11(transition_value):
    outputValue = str((". Scaunul este comfortabil.  = %s \n" \
                       %(transition_value)))
    input_value = randint(0,1)
    time.sleep(1)
    print("...Evaluating...")
    if (input_value == 0):
        result = yield from State4(input_value)
    else:
        result = yield from State4(input_value)
    result = " Realizezi ca n-ai timp de pierdut si pleci " + result

    return (outputValue + str(result))


@asyncio.coroutine

def EndState(transition_value):
    outputValue = str(("Gasesti camera comorilor! Ai castigat! = %s \n"\
                       %(transition_value)))
    print("...Stop Computation...")
    return (outputValue )

if __name__ == "__main__":
    print("Finite State Machine simulation with Asyncio Coroutine")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(StartState())

