import random
play = "yes"
while play == "yes":
    secret = random.randint(1, 100)
    attempts = 0
    while attempts < 5:
        number = input("Ye adad bein 1 ta 100 vared kon: ")
        if not number.isdigit() or not 1 <= int(number) <= 100:
            print("Voroodi namotabar ast!")
            continue
        number = int(number)
        attempts += 1
        print("Talaash:", attempts, "Forsat baghimande:", 5-attempts)
        if number == secret:
            print("Afarin! Barande shodi!")
            if attempts == 1:
                print("Rotbe: Fogholade!")
            elif attempts == 2:
                print("Rotbe: Besyar khoob!")
            elif attempts == 3:
                print("Rotbe: Khoob!")
            elif attempts == 4:
                print("Rotbe: bad nabod!")
            else:
                print("Rotbe: Ba shans bordi!")
            break
        elif number > secret:
            print("Adad koochaktari vared kon!")
        else:
            print("Adad bozorgtari vared kon!")
        difference = abs(number - secret)
        if difference <= 5:
            print("Kheyli nazdiki!")
        elif difference <= 15:
            print("Nafziki, vali hanooz fasele dari!")
        else:
            print("Kheyli doori!")
    if attempts == 5 and number != secret:
        print("Bakhhti! Adade makhfi:", secret)
    play = input("Mikhay dobare bazi koni? (yes/no): ")
print("Mamnoon az bazit!")


