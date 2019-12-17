print("WELCOME TO HD MOTORS")
n=str(input("My name's James \nWhat is your good name Sir:"))
print("Good Morning Mr."+'%s' %(n)+'!!')
w=str(input("What car type you are prefering to buy [Hatchback(H)/Sedan(S)/(SUV)] :"))
print("Great Choice Mr."+'%s'%(n))
b=int(input("May i get to know the budget you thought for your car :"))
print('''"Perfect !!" \nWe have got the newly launched and one of the best car in our showroom at your budget for you Mr.'''+"%s" %(n))
if(w=='H'):
    print("HD825:\nThe HD825 has 1 Diesel Engine and 1 Petrol Engine on offer. \nThe Diesel engine is 1248 cc while the Petrol engine is 1197 cc. \nIt is available with the Manual and Automatic transmission. \nDepending upon the variant and fuel type has the HD825 has a mileage of 21.4 to 27.39 kmpl. \nThe HD825 is a 5 seater Hatchback and has a length of 3995mm, width of 1745mm and a wheelbase of 2520mm.")
    print("Dzire:\nThe Maruti Dzire has 1 Diesel Engine and 1 Petrol Engine on offer.\nThe Diesel engine is 1248 cc while the Petrol engine is 1197 cc. \nIt is available with the Manual and Automatic transmission. \nDepending upon the variant and fuel type the Dzire has a mileage of 22.0 to 28.4 kmpl. \nThe Dzire is a 5 seater HAtchback and has a length of 3995mm, width of 1735mm and a wheelbase of 2450mm.")
    p = str(input("what is your first preference of car [Efficiency(E)/Power(P)]:"))
    if(p=='E'):
        print("The average mileage of HD825 is 20 KMPL \nThe average mileage of Dzire is 25 KMPL")
        k=int(input("What is the average distance your travel in a year (in number):"))
        t=int(input("What is the Apporaximate period you will be using this Car(years in number)?"))
        print("Okey!!"+'\nMr.%s'%(n))
        print("Lets See which car will be best suitable for you !!")
        print("The price of HD825 is 5 lakhs & The price of Dzire is 7 lakhs")
        print("Lets assume the average petrol price to be 90 Rupees")
        print("So, if you travel %d KMs and want to keep the car for %d Years \nThen to travel 100km in HD825 u will have to spend 450 rupees and 350 rupees in  Dzire" %(k,t))
        k1=k*4.5
        k2=k*3.5
        t1=k1*t
        t2=k2*t
        print("If u travel %d  in HD825 for %d years you will be spending %d \n&\nIf u travel %d in Dzire for %d Years you will be spending %d"%(k,t,t1,k,t,t2))
        ta1=5+t1
        ta2=7+t2
        print("Total Spendings after %d years on Hd825 will be %d and on Dzire will be %d"  %(t,ta1,ta2))
        if(ta1<ta2):
            print("I suggest you to buy HD825")
        else:
            print("I suggest you to buy Dzire")
    elif(p=='P'):
        print("I suggest u to buy a Diesel Engine car \nBoth car comes with a great power of 1248cc Engine")
        print("The HD825 will cost you 900000 Rupees and The Dzire will Cost you 950000 Rupees")
    else:
        print("Please enter a valid input")
elif(w=='S'):
    print("Ciaz S: \nThe Maruti Ciaz S is based on the top-spec Alpha variant and is offered with both the engine options – petrol and diesel. \nThe petrol Ciaz S is priced at Rs 9.65 lakh whereas the diesel version costs Rs 11.68 lakh (both the prices are ex-showroom Delhi). \nThe mechanicals continue to remain the same in this variant – a 1.4-litre petrol (92PS/130Nm) and a 1.3-litre diesel (90PS/200Nm) engine. \nIt’s only offered with a 5-speed manual transmission, though a 4-speed automatic is available on other variants of the Ciaz. \nWith same engines, it returns company claimed mileage of 20.73kmpl and 28.09kmpl with its petrol and diesel engines, respectively.")
    print("Verna : \nThe base E variant with a petrol engine is priced at Rs 8.08 lakh whereas the corresponding diesel variant costs Rs 9.33 lakh for diesel.\nThe Hyundai Verna is available with four engine options: 1.4-litre petrol,1.4-litre diesel, 1.6-litre petrol and 1.6-litre diesel. \nThe 1.4-litre petrol engine produces 100PS/132Nm, while the 1.6-litre petrol engine churns out 123PS/151Nm.\nAs far as features are concerned, the Verna gets automatic projector headlamps with LED daytime running lights (DRLs), electric sunroof, \nautomatic climate control, 7-inch touchscreen infotainment system with Apple CarPlay, Android Auto and Mirrorlink, ventilated front seats, rear parking camera with sensors and dynamic guidelines and cruise control, among others.")
    p = str(input("what is your first preference of car [Efficiency(E)/Power(P)]:"))
    if(p=='E'):
        print("The average mileage of Ciaz is 22 KMPL \nThe average mileage of Dzire is 27 KMPL")
        k21=int(input("What is the average distance your travel in a year (in number):"))
        t21=int(input("What is the Apporaximate period you will be using this Car(years in number?)"))
        print("Okey!!"+'\nMr.%s'%(n))
        print("Lets See which car will be best suitable for you !!")
        print("The price of Ciaz S is 11 lakhs & The price of Verna is 14 lakhs")
        print("Lets assume the average petrol price to be 90 Rupees")
        print("So, if you travel %d KMs and want to keep the car for %d Years \nThen to travel 100km in Ciaz S u will have to spend 409 rupees and 333 rupees in  Verna" %(k21,t21))
        k22=k21*4.095
        k23=k21*3.33
        t22=k22*t21
        t23=k23*t21
        print("If u travel %d  in Ciaz S for %d years you will be spending %d \n&\nIf u travel %d in Verna for %d Years you will be spending %d"%(k21,t21,t22,k21,t21,t23))
        ta3=11+t22
        ta4=14+t23
        print("Total Spendings after %d years on Ciaz S will be %d and on Verna will be %d" % (t21, ta3, ta4))
        if(ta3<ta4):
            print("I suggest you to buy Ciaz S")
        else:
            print("I suggest you to buy Verna")
    elif(p=='P'):
        print("I suggest u to buy a Diesel Engine car \nBoth car comes with a great power of 1248cc Engine")
        print("The Ciaz S will cost you 11 Lakhs and The Verna will Cost you 14 Lakhs")
    else:
        print("Please enter a valid input")
elif(w=='SUV'):
    print("MG: \nThe MG Hector is available with two petrol and one diesel engine option to choose from. The petrol engine is a 1.5-litre turbocharged unit capable of producing 143PS of maximum power and 250Nm of torque. \nThe diesel engine is the same 2.0-litre unit that powers the Compass.\nHere are fuel economy figures of the HectorPetrol MT: 14.16kmpl Petrol DCT: 13.96kmpl\n The Hector’s standout feature is its large 10.4-inch touchscreen infotainment which gets in-built internet connectivity, iSmart mobile application-based AC control as well as door lock and unlock. \nIt is also equipped with a panoramic sunroof, a 7-inch colour MID, 360 degree camera, electronic parking brake and up to six airbags. \nThe standard set of safety features include dual front airbags, ABS with EBD, ESP, traction control, rear disc brakes, hill hold assist and ISOFIX child seat anchors.")
    print("Harry : \nThe Harrier is powered by a 2.0-litre 4-cylinder turbo-diesel engine that churns out 140PS of power and 350Nm of torque.\nCurrently, Tata offers the Harrier with a 6-speed manual transmission only. However, an automatic gearbox option with a 6-speed torque \nthe Harrier with a host of features though most of them are offered on the top-end variant only, especially safety features like 6 airbags, traction control, ISOFIX child seat anchors, rollover mitigation control and electronic stability control.\nAn 8.8-inch touchscreen infotainment system with Apple CarPlay and Android Auto takes centre stage while a 7-inch multi-info display in the instrument cluster works in tandem with the infotainment system and displays navigation info, music, tripmeter and tachometer.\nApart from these, a cooled storage compartment is also present underneath the front armrest and passengers in the rear get individual spaces to stow away their mobile phones. LED elements and projector headlamps are also on offer.")
    p = str(input("what is your first preference of car [Efficiency(E)/Power(P)]:"))
    if(p=='E'):
        print("The average mileage of MG is 18 KMPL \nThe average mileage of Harry is 15 KMPL")
        k31=int(input("What is the average distance your travel in a year (in number):"))
        t31=int(input("What is the Apporaximate period you will be using this Car(years in number)?" ))
        print("Okey!!"+'\nMr.%s'%(n))
        print("Lets See which car will be best suitable for you !!")
        print("The price of MG is 15 lakhs & The price of Harry is 16 lakhs")
        print("Lets assume the average petrol price to be 90 Rupees")
        print("So, if you travel %d KMs and want to keep the car for %d Years \nThen to travel 100km in MG u will have to spend 500 rupees and 600 rupees in  Harry" %(k31,t31))
        k32=k31*5
        k33=k31*6
        t32=k32*t31
        t33=k33*t31
        print("If u travel %d  in MG for %d years you will be spending %d \n&\nIf u travel %d in Harry for %d Years you will be spending %d"%(k31,t31,t32,k31,t31,t33))
        ta5=15+t32
        ta6=16+t33
        print("Total Spendings after %d years on MG will be %d and on Harry will be %d" % (t31, ta5, ta6))
        if(ta5<ta6):
            print("I suggest you to buy MG")
        else:
            print("I suggest you to buy Harry")
    elif(p=='P'):
        print("I suggest u to buy a Diesel Engine car \nBoth car comes with a great power of 2100cc Engine")
        print("The MG will cost you 15 Lakhs and The Harry will Cost you 16 Lakhs")
    else:
        print("Please enter a valid input")
else:
    print("Please enter a valid input")
z=str(input("Which car Would you like to buy Mr.%s"%(n)+" ? :"))
print("Ohh!! \nGreat Choice Sir")
zz=str(input("How would you like to make the payment ? [CASH(CA)/CHEQUE(CH)/EMI]:"))
if(zz=='CA' or zz=='CH'):
    print("I'll take you to the Account Department for futhur processing of car papers")
elif(zz=='EMI'):
    print("I'll take you to the Finance Department for futhur processing of Car papers")
else:
    print("Please Enter a Valid input...!!")
Print("CONGRATULATIONS /%d" %(n))
Print("Thank you for visiting HD Motors \n*****VISIT AGAIN*****")