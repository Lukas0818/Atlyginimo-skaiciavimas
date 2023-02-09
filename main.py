from databse import engine, Duombaze
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = int(input("Pasirinkite veiksmą: \n1 - Pridėti įraša \n2 - Peržiūrėti įrašus  "
                             "\n3 - Atnaujinti įrašus \n4 - Ištrinti įrašus \n0 - Išeiti iš programos \n"))

    if pasirinkimas == 1:
        vardas = input("Įveskite varda: ")
        pinigai = input("Įveskite pinigus: ")
        duombaze = Duombaze(vardas, pinigai)
        session.add(duombaze)
        session.commit()

    if pasirinkimas == 2:
        duombaze = session.query(Duombaze).all()
        print("-" * 30)
        for duom in duombaze:
            print(duom)
        print("-" * 30)

    if pasirinkimas == 3:
        duombaze = session.query(Duombaze).all()
        print("-" * 30)
        for duom in duombaze:
            print(duom)
        print("-" * 30)
        keiciamo_id = int(input("Pasirinkite norimo pakeisti projekto ID: "))
        keiciamas_duom = session.query(Duombaze).get(keiciamo_id)
        pakeitimas = int(input("Ką norite pakeisti: , 1 - Pinigus \n"))
        if pakeitimas == 1:
            keiciamas_duom.pinigai = float(input("Įveskite pinigus: "))
        session.commit()

    if pasirinkimas == 4:
        duombaze = session.query(Duombaze).all()
        print("-" * 30)
        for duom in duombaze:
            print(duom)
        print("-" * 30)
        keiciamo_id = int(input("Pasirinkite norimo ištrinti įrašo ID: "))
        trinamas_duom = session.query(Duombaze).get(keiciamo_id)
        session.delete(trinamas_duom)
        session.commit()

    if pasirinkimas == 0:
        break
