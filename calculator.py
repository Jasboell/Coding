for i in range(0,10):
    print("Skriv inn første tall")
    tall1=int(input())
    print("skriv in andretall")
    tall2=int(input())
    if tall2 == 0:
        print("you can´t use zero in the denominator")
    else:
        svar=tall1/tall2
        print("svar", svar)
