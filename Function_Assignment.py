class function_assignment():
    def SubfieldsInAI_Subfields():
        for field in list:
            print(field)

    def OddEven_OddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num,'is even number')
            message = 'even number'
        else:
            print(num,'is odd number')
            message = 'odd number'
        return message

    def Elegiblity_ForMarriage_Elegible():
        Gen=input("Your Genter:")
        Age=int(input("Your Age:"))
        if(Gen=="Male"):
            if(Age<=21): 
                print('NOT ELIGIBLE.wait until your age turn 21')
                message ='NOT ELIGIBLE'    
            else:
                print('ELIGIBLE')
                message = 'ELIGIBLE'
        elif(Gen=="Female"):
            if(Age<=18):
                print('NOT ELIGIBLE.wait until your age turn 18')
                message ='NOT ELIGIBLE'               
            else:
                print('ELIGIBLE')
                message = 'ELIGIBLE'
        else:
            print('Invadid data.Enter Male or Female')
            message = 'Invadid data.Enter Male or Female'
        return message

    def Find_avg(Sub1,Sub2,Sub3,Sub4,Sub5):
        Add=(Sub1+Sub2+Sub3+Sub4+Sub5)
        print("Total:", Add)
        persentage=(Add/5)
        print('Percentage:',persentage)
        return persentage

    def Area_perimeter_of_tri():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print('Area formula:, (Height*Breadth)/2')
        Area_of_traiangle=(Height*Breadth)/2
        print('Area_of_traiangle:',Area_of_traiangle) 
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth1=int(input("Breadth1:"))
        print('Perimeter formula:, Height1+Height2+Breadth1') 
        Perimeter_of_Triangle= (Height1+Height2+Breadth1)
        print('Perimeter of Triangle:',Perimeter_of_Triangle)