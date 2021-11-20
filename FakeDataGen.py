#/bin/python3
import sys, os, io
import datetime
import random
import pandas
import argparse
import pyminizip
from io import StringIO
from random import randint
from tabulate import tabulate
from termcolor import colored

# Common Names
def namegen():
    name = ["ADRIAN","ALBA","ALBERTO","ALEJANDRO","ALFONSO","ALICIA","ALVARO","ANA","ANDREA","ANDRES","ANGEL","ANGELA","ANTONIA","ANTONIO","BEATRIZ","CARLA","CARLOS","CARMEN","CAROLINA","CLAUDIA","CONCEPCION","CRISTINA","DANIEL","DAVID","DIEGO","DOLORES","EDUARDO","ELENA","ENCARNACION","ENRIQUE","EVA","FERNANDO","FRANCISCA","FRANCISCO","GABRIEL","GUILLERMO","HECTOR","HUGO","IGNACIO","IRENE","ISABEL","IVAN","JAIME","JAVIER","JESUS","JOAQUIN","JORDI","JORGE","JOSE","JOSEFA","JUAN","JUANA","JULIA","LAURA","LUCIA","LUIS","MANUEL","MANUELA","MARC","MARCOS","MARGARITA","MARIA","MARINA","MARIO","MARTA","MERCEDES","MIGUEL","MONICA","MONTSERRAT","NATALIA","NURIA","OSCAR","PABLO","PATRICIA","PAULA","PEDRO","PILAR","RAFAEL","RAMON","RAQUEL","RAUL","RICARDO","ROBERTO","ROCIO","ROSA","ROSARIO","RUBEN","SALVADOR","SANDRA","SANTIAGO","SARA","SERGIO","SILVIA","SOFIA","SONIA","SUSANA","TERESA","VICENTE","VICTOR","YOLANDA"]
    last1 = ["AGUILAR","ALONSO","ALVAREZ","ARIAS","BENITEZ","BLANCO","BRAVO","CABALLERO","CABRERA","CALVO","CAMPOS","CANO","CARMONA","CARRASCO","CASTILLO","CASTRO","CORTES","CRESPO","CRUZ","DELGADO","DIAZ","DIEZ","DOMINGUEZ","DURAN","ESTEBAN","FERNANDEZ","FERRER","FLORES","FUENTES","GALLARDO","GALLEGO","GARCIA","GARRIDO","GIL","GIMENEZ","GOMEZ","GONZALEZ","GUERRERO","GUTIERREZ","HERNANDEZ","HERRERA","HERRERO","HIDALGO","IBANEZ","IGLESIAS","JIMENEZ","LEON","LOPEZ","LORENZO","LOZANO","MARIN","MARQUEZ","MARTIN","MARTINEZ","MEDINA","MENDEZ","MOLINA","MONTERO","MORA","MORALES","MORENO","MOYA","MUNOZ","NAVARRO","NIETO","NUNEZ","ORTEGA","ORTIZ","PARRA","PASCUAL","PASTOR","PENA","PEREZ","PRIETO","RAMIREZ","RAMOS","REYES","RODRIGUEZ","ROJAS","ROMAN","ROMERO","RUBIO","RUIZ","SAEZ","SANCHEZ","SANTANA","SANTIAGO","SANTOS","SANZ","SERRANO","SOLER","SOTO","SUAREZ","TORRES","VARGAS","VAZQUEZ","VEGA","VELASCO","VICENTE","VIDAL"]
    last2 = ["AGUILAR","ALONSO","ALVAREZ","ARIAS","BENITEZ","BLANCO","BRAVO","CABALLERO","CABRERA","CALVO","CAMPOS","CANO","CARMONA","CARRASCO","CASTILLO","CASTRO","CORTES","CRESPO","CRUZ","DELGADO","DIAZ","DIEZ","DOMINGUEZ","DURAN","ESTEBAN","FERNANDEZ","FERRER","FLORES","FUENTES","GALLARDO","GALLEGO","GARCIA","GARRIDO","GIL","GIMENEZ","GOMEZ","GONZALEZ","GUERRERO","GUTIERREZ","HERNANDEZ","HERRERA","HERRERO","HIDALGO","IBANEZ","IGLESIAS","JIMENEZ","LEON","LOPEZ","LORENZO","LOZANO","MARIN","MARQUEZ","MARTIN","MARTINEZ","MEDINA","MENDEZ","MOLINA","MONTERO","MORA","MORALES","MORENO","MOYA","MUNOZ","NAVARRO","NIETO","NUNEZ","ORTEGA","ORTIZ","PARRA","PASCUAL","PASTOR","PENA","PEREZ","PRIETO","RAMIREZ","RAMOS","REYES","RODRIGUEZ","ROJAS","ROMAN","ROMERO","RUBIO","RUIZ","SAEZ","SANCHEZ","SANTANA","SANTIAGO","SANTOS","SANZ","SERRANO","SOLER","SOTO","SUAREZ","TORRES","VARGAS","VAZQUEZ","VEGA","VELASCO","VICENTE","VIDAL"]
    return name[random.randint(0, len(name)-1)],last1[random.randint(0, len(last1)-1)],last2[random.randint(0, len(last2)-1)]

# Email
def mailgen(name,last_name1):
    mail = ["gmail.com","hotmail.com","protonmail.com","outook.com", "yahoo.com"]
    return (name + "." + last_name1 + "@" + mail[random.randint(0, len(mail)-1)]).lower()

# Birth date
def bdaygen():
    number = ""
    number = number+str(random.randint(1, 31))
    if int(number) < 10:
        number = "0" + str(number)
    number = number+"/"
    number = number+str(random.randint(1, 12))
    if int(number[3:]) < 10:
        number = str(number[:3]) + "0" + str(number[3:])
    if int(number[:2]) > 28 and int(number[3:]) == "02":
        number[:2] == "28"
    number = number+"/"
    x = datetime.datetime.now()
    year = (x.strftime("%Y"))
    year1 = int(year) - 60
    year2 = int(year) - 20
    number = number+str(random.randint(year1, year2))
    return number

# Phone Number
def phonegen():
    number = "9"
    number = number+random.choice("123456789")
    for i in range(7):
        number = number+random.choice("1234567890")
    return number

# Mobile Phone
def mobilegen():
    number = "6"
    for i in range(8):
        number = number+random.choice("1234567890")
    return number

# DNI / CIF
# Check on https://www.squobble.com/util/dni.html
def dnigen():
    number = ""
    number = number+random.choice("123456789")
    for i in range(7):
        number = number+random.choice("1234567890")
    letter = "TRWAGMYFPDXBNJZSQVHLCKE"[int(number) % 23]
    number = number+letter
    return number

# Citizenship
def citgen():
    citylist = ["Albacete","Alcobendas","Algeciras","Alicante","Almeria","Aranjuez","Arganda","Asturias","Badajoz","Badalona","Baracaldo","Barcelona","Benidorm","Bilbao","Bizkaia","Burgos","Caceres","Cadiz","Cantabria","Cartagena","Castelldefels","Castellon","Ceuta","Coslada","Cuenca","Elche","Elda","Estepona","Ferrol","Fuengirola","Fuenlabrada","Gerona","Getafe","Gipuzkoa","Girona","Granada","Granollers","Guadalajara","Hospitalet","Huelva","Huesca","Ibiza","Jaen","Jerez","Leganes","Leon","Lleida","Lugo","Madrid","Malaga","Manresa","Marbella","Mataro","Melilla","Mollet","Murcia","Navarra","Oviedo","Palencia","Pamplona","Ponferrada","Pontevedra","Pozuelo","Reus","Rioja","Roquetas","Rubi","Sabadell","Salamanca","Santander","Santiago","Sevilla","Soria","Tarragona","Terrasa","Teruel","Toledo","Torremolinos","Torrente","Torrevieja","Valdemoro","Valencia","Valladolid","Vigo","Viladecans","Villanueva","Villarreal","Vitoria","Zamora","Zaragoza"]
    return citylist[random.randint(0, len(citylist)-1)]

# Credit Card number
# Check on https://www.mobilefish.com/services/credit_card_number_checker/credit_card_number_checker.php
def ccgen():
    number = ""
    number = number+random.choice("3456")
    for i in range(14):
        number = number+random.choice("1234567890")
    ccnumber = [] ; double = [] ; rnumber = [] ; newnumber = "" ; y = 0

    for i in str(number):
        ccnumber.append(int(i))
    for i in ccnumber[0:16:2]:
        i *= 2
        if len(str(i)) == 2:
            for x in str(i):
                y += int(str(x))
            i = y
        double.append(i) ; y = 0
    for i in ccnumber[1:15:2]:
        rnumber.append(i)
    lastdigit = ((sum(double) + sum(rnumber)) * 9) % 10
    for i in ccnumber:
        newnumber += str(i)

    newnumber = (newnumber + str(lastdigit))
    number = str(newnumber[:4]) + " " + str(newnumber[4:8]) + " " + str(newnumber[8:12]) + " " + str(newnumber[12:16])
    return number

# Expiration Date
def cdategen():
    number = ""
    number = number+str(random.randint(1, 12))
    if int(number) < 10:
        number = "0" + str(number)
    number = number+"/"
    x = datetime.datetime.now()
    year = (x.strftime("%y"))
    year1 = int(year) + 1
    year2 = int(year) + 4
    number = number+str(random.randint(year1, year2))
    return number

# CVV
def cvvgen():
    number = ""
    for i in range(1):
        number = number+random.choice("123456789")
    for i in range(2):
        number = number+random.choice("1234567890")
    return number

# Bank Account number
# Check on https://bank.codes/iban/validate
def bankgen():
    number = ""
    while len(number) != 24:
        number = ""
        banklocation = "ES"
        countrycode = "142800"
        for i in range(8):
            number = number+random.choice("1234567890")

        account1 = number
        sum1 = int(number[0]) * 4
        sum2 = int(number[1]) * 8
        sum3 = int(number[2]) * 5
        sum4 = int(number[3]) * 10
        sum5 = int(number[4]) * 9
        sum6 = int(number[5]) * 7
        sum7 = int(number[6]) * 3
        sum8 = int(number[7]) * 6

        number = sum1 + sum2 + sum3 + sum4 + sum5 + sum6 + sum7 + sum8
        number = number % 11 ; checkdigit1 = 11 - number
        if number == 10:
            checkdigit1 = 1
        if number == 11:
            checkdigit1 = 0
        account1 = str(account1) + str(checkdigit1)

        number = ""
        for i in range(10):
            number = number+random.choice("1234567890")

        account2 = number
        sum1 = int(number[0]) * 1
        sum2 = int(number[1]) * 2
        sum3 = int(number[2]) * 4
        sum4 = int(number[3]) * 8
        sum5 = int(number[4]) * 5
        sum6 = int(number[5]) * 10
        sum7 = int(number[6]) * 9
        sum8 = int(number[7]) * 7
        sum9 = int(number[8]) * 3
        sum0 = int(number[9]) * 6    

        number = sum1 + sum2 + sum3 + sum4 + sum5 + sum6 + sum7 + sum8 + sum9 + sum0
        number = number % 11 ; checkdigit2 = 11 - number
        if number == 10:
            checkdigit2 = 1
        if number == 11:
            checkdigit2 = 0
        account2 = str(checkdigit2) + str(account2)
        
        ccc = account1 + account2
        iban = account1 + account2
        iban = str(iban) + str(countrycode)
        iban = int(iban) % 97
        iban = 98 - int(iban)
        number = banklocation + str(iban) + str(ccc)
    return number

# Social Security
# Check on https://www.asinom.com/calculador-numero-seguridad-social.php
def ssgen():
    number = ""
    for i in range(2):
        number = number+random.choice("123450")
    for i in range(8):
        number = number+random.choice("1234567890")
    control = int(number) % 97
    if control < 10:
        control = "0" + str(control)
    number = str(number[0:2]) + "/" + str(number[2:]) + "/" + str(control)
    return number

# Generate Data
def number(args):
    delim = ","
    print("Nombre,Apellidos,Correo Electronico,Fecha de Nacimiento,DNI,Telefono Fijo,Telefono Movil,Ciudad,Seguridad Social,Tarjeta de Credito,Caducidad,CVV,Numero de Cuenta (IBAN)")
    for i in range(args.number):
        name,last_name1,last_name2 = namegen() 
        mail = mailgen(name,last_name1)
        bday = bdaygen()
        phone = phonegen()
        mobile = mobilegen()
        dni = dnigen()
        city = citgen()
        cc = ccgen()
        cdate = cdategen()
        cvv = cvvgen()
        iban = bankgen()
        ss = ssgen()

        print(name.capitalize() + delim + last_name1.capitalize() + " " + last_name2.capitalize() + delim + mail + delim + bday + delim + dni + delim + phone + delim + mobile + delim + city + delim + ss + delim + cc + delim + cdate + delim + cvv + delim + iban)

# Main
def main():
    banner= """
  _____     _        ____        _         ____            
 |  ___|_ _| | _ ___|  _ \  __ _| |_ __ _ / ___| ___ _ __  
 | |_ / _` | |/ / _ \ | | |/ _` | __/ _` | |  _ / _ \ '_ \ 
 |  _| (_| |   <  __/ |_| | (_| | || (_| | |_| |  __/ | | |
 |_|  \__,_|_|\_\___|____/ \__,_|\__\__,_|\____|\___|_| |_|
                                                           
  -------------------- by @JoelGMSec ---------------------
    """

    print(colored(banner, "blue"))
    parser = argparse.ArgumentParser()
    parser.add_argument("-n","--number", type=int, help="The number of records should be created")
    parser.add_argument("-b","--bankdata", action="store_true", help="Show only bank data (Card, CVV, IBAN..)")
    parser.add_argument("-e","--extended", action="store_true", help="Show only extended info (City, Phone, SS..)")
    parser.add_argument("-f","--file", type=str, help="File path to save data")
    parser.add_argument("-z","--zip", action="store_false", help="Compress data to zip file")
    parser.add_argument("-p","--password", type=str, help="Password to protect zip file")
    args = parser.parse_args()

    if len(sys.argv) < 2:
        print(parser.print_help())
        exit()

    if args.number is not None:
        if args.file is None:
            file = "/tmp/FakeDataGenTemp.csv"
            print(colored("[+] Data created successfully!\n", "green")) 
            stdoutput = sys.stdout ; sys.stdout = open(file, "w")
            buffer = io.StringIO(number(args))
            sys.stdout.close() ; sys.stdout = stdoutput
            df = pandas.read_csv(file)
            if args.bankdata is not False:
                table = df.iloc[: , 9:13]
            elif args.extended is not False:
                table = df.iloc[: , 4:9]
            else:
                table = df.iloc[: , 0:4]
            print(tabulate(table, showindex="never", headers="keys"))
            print ("\n") ; os.remove(file)

    if args.file is not None:
        print(colored("[+] Data saved successfully!\n", "green"))
        stdoutput = sys.stdout ; sys.stdout = open(args.file, "w")
        number(args) ; sys.stdout.close() ; sys.stdout = stdoutput

        if args.zip is False:
            fd = os.open("/dev/null",os.O_WRONLY)
            os.dup2(fd,2)
            zipfile = args.file.split(".")[0] + ".zip"
            pwd = "/" ; password = "" ; compression = 0
            pyminizip.compress(args.file, pwd, zipfile, password, compression) 
            if args.password is not None:
                password = args.password
                pyminizip.compress(args.file, pwd, zipfile, password, compression) 
            os.remove(args.file)

    exit()

if __name__ == "__main__":
    main()
