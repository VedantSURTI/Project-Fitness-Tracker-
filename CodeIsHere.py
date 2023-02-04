import numpy as np
import pandas as pd
fats = 0
carbohydrates = 0
protein = 0
vitaminA = 0
vitaminC = 0
calcium = 0
cholestrol = 0
n = 0
"""
Item = {fats,carbohydrates,protein,vitaminA,vitaminC,calcium,cholestrol}
"""
def menu():
  print("******************************************")
  print("                   Menu                   ")
  print("(1.) Vegeterian Main Course               ")
  print("(2.) Non Vegeterian Main Course           ")
  print("(3.) Pizza                                ")
  print("(4.) Snacks                               ")
  print("(5.) Beverages                            ")
  print("(6.) Fruits                               ")
  print("(7.) Ice Cream                            ")
  print("******************************************")
def response_menu():
  print("******************************************")
  print("TO ADD SOME MORE FOOD ITEMS PRESS C")
  print("TO VIEW THE ITEMS YOU HAVE ADDED PRESS V")
  print("TO VIEW YOUR REPORTS PRESS R")
  print("TO DELETE A FOOD ITEM PRESS D")
  print("TO KNOW ABOUT THE FACTS OF THE NUTRIENTS OF YOUR FOOD PRESS I")
  print("******************************************")
Vegeterian_Main_Course = {"Bhindi Sabzi":[20.2,6.1,1.6,334.7,16.8,59.6,0],"Chana ki Daal":[9.7,25.4,8.3,322.3,12.1,45.5,0],"Baingan Bharta":[9.2,6.1,1.1,237.7,17.4,39,0],"Rajma Curry":[11.7,19,6.4,375.7,23.1,106.9,0],"Gujarati Kadhi":[8.8,6.4,4.1,159,1.5,161.4,12],"Aloo Paratha":[8.5,22.6,3.3,111.9,4.5,17.1,0],"Panner Gravy":[25.2,9.5,8.6,522.3,15.1,307.3,41],"Dosa":[5.2,18.8,2.7,47.2,0,10.9,0],"Veg Biryani":[18.2,60.8,8.9,679,25.6,155.3,4],"Idli":[0.1,7.2,1,0.8,0,4,0],"Hakka Noodles":[13,54,11,525,42,60,0],"Fried Rice":[9.1,34.81,7.02,40,4,33,103],"Roti":[3.7,15.7,2.6,30.6,0,10.4,0],"Rice":[4,39.1,3.4,33.8,0,5,0],"Veggie Burger":[11,28,5,0,0,0,30],"Chole Masala":[9.7,26.8,7.2,145.1,3.1,90.6,0],"Cauliflower Sabzi":[12.2,9,4.6,355.5,44.5,149.2,0]}
Non_Vegeterian_Main_Course = {"Chicken Biryani":[9.2,54,28,74.48,12.3,134,48],"Egg Curry":[17,18.11,14.29,196,16.7,132,389],"Fish Curry":[11.02,4.57,29.76,75,2.2,108,77],"Chicken Gravy":[8.6,6.11,14.8,81,6.6,22,45],"Chicken Burger":[14,33,27,44,0,14,71],"Egg Biryani":[23.3,37.9,11.5,906.1,10.4,88.9,5.8]}
Pizza = {"Margherita Pizza":[10.1,26.08,10.6,68,0.3,181,21],"Vegetable Pizza":[8.95,30.93,9.33,30,10,165,10],"Chicken Pizza":[12.61,29.61,10.97,29,9.5,158,22],"Vegetable Pizza with no Cheese ":[4.98,31.66,4.35,4,2.6,13,0],"SeaFood Pizza":[9.89,27.28,12.69,42,0.2,191,32],"Hawaiian Pizza":[8.96,31.06,10.74,27,10.6,152,17]}
Snacks = {"French Fries(Small)":[10,29,3,0,3.3,13,0],"Salted Potato Chips(28g/1 Small Packet)":[10.49,13.93,1.84,0,5.2,7,0],"Upma":[5.8,30.7,4,49.9,2.9,14.5,0],"Popcorn(100g)":[28.1,57.2,9,1,0.3,10,0],"Bread Butter":[4,26,3,0,0,0,3]}
Beverages = {"Milk":[7.93,11.03,7.86,68,0,276,24],"Tea":[0.82,4.97,0.93,7,0,33,3],"Coffee":[0.14,7.14,0.31,1,0,10,0],"Orange Juice":[0.5,25.79,1.74,25,12.4,27,0],"Apple Juice":[0.27,28.97,0.15,0,27.5,17,0],"Beetroot Juice":[0.25,21.29,2.57,3,8.1,31,0],"Carrot Juice":[0.35,21.92,2.24,2256,20.1,57,0],"Pomegranate Juice":[0.68,38.94,2.15,11,13.8,7,0],"Mango Juice":[0.2,42,0.4,1030.8,14.1,8,0],"Lemonade":[0.3,27.2,0.3,0,11.7,21.2,0],"Pepsi":[0,41,0,0,0,0,0],"Fanta":[0,44,0,0,0,0,0],"Sprite":[0,38,0,0,0,0,0],"Mirinda":[0,44,0,0,0,0,0],"Mountain Dew":[0,35,0,0,0,0,0],"Coca Cola":[0,39,0,0,0,0,0],"Thumps Up":[0,41,0,0,0,0,0]}
Fruits = {"Apple":[0.23,19.06,0.36,4,6.3,8,0],"Banana":[0.39,26.95,1.29,4,10.3,6,0],"Orange":[0.16,15.39,1.23,14,69.7,52,0],"Pineapple":[0.57,59.61,2.55,14,170.9,61,0],"Grapes":[0.26,28.96,1.15,5,17.3,16,0],"Mango":[0.56,35.19,1.06,79,57.3,21,0],"Papaya":[0.2,13.73,0.85,77,86.5,34,0],"Pear":[0.2,25.66,0.63,2,7,15,0]}       #In case of grapes the amout is 1 grape. And in case of papaya the amount is 1cup of diced papaya and for all others it is considered as 1 whole fruit.
Ice_Cream = {"Cookies and Cream":[13,39.5,6.5,0,0,97.5,6.5],"Strawberry Ice Cream":[12,34,6,120,18,200,38],"Chocolate Ice Cream":[14.63,37.51,5.05,157,0.9,145,45],"Vanilla Ice Cream":[10.7,22,4.2,236,0.9,145,45],"Kulfi":[9,20.4,6.9,246,1.7,295.1,13.3],"Cone":[0.3,3.2,0.3,0,0,0,0]}
Vegeterian_Main_Course_consumed = {}
Non_Vegeterian_Main_Course_consumed = {}
Pizza_consumed = {}
Fruits_consumed = {}
Snacks_consumed = {}
Beverages_consumed = {}
Ice_Cream_consumed = {}
food_counsumed = {}
user_satisfy = 0
def Facts_menu():
    print("")
    print("Fats :- The importance of fats for humans, animals, and plants lies in their high content of energy, which permits the greatest possible storage of energy in the smallest possible amount of food substance. Fats allow humans and animals to consume fat-soluble vitamins and provide them with essential fatty acids, that is, those indispensable fatty acids that their bodies are unable to synthesize themselves. The efficiency of fat as foodstuff is very high, because the fat contained in food is almost completely reabsorbed by the body.")
    print("")
    print("Proteins :- Protein is essential to building bones,and body tissues, such as muscles, but protein does much more than that. Protein participates in practically every process of a cell. It plays a part in metabolic reactions, immune response, protein provides a source of energy, assists in cellular repair, form blood cells, and more.")
    print("")
    print("Carbohydrates : - Carbohydrates are your body's main source of energy: They help fuel your brain, kidneys, heart muscles, and central nervous system. For instance, fiber is a carbohydrate that aids in digestion, helps you feel full, and keeps blood cholesterol levels in check. A carbohydrate-deficient diet may cause headaches, fatigue, weakness, difficulty concentrating, nausea, constipation, bad breath and vitamin and mineral deficiencies.")
    print("")
    print("Vitamin A:- Vitamin A is a fat-soluble vitamin that is naturally present in many foods. Vitamin A is important for normal vision, the immune system, and reproduction. Vitamin A also helps the heart, lungs, kidneys, and other organs work properly.")
    print("")
    print("Vitamin C :- Vitamin C, also known as ascorbic acid, is necessary for the growth, development and repair of all body tissues. It's involved in many body functions, including formation of collagen, absorption of iron, the proper functioning of the immune system, wound healing, and the maintenance of cartilage, bones, and teeth.")
    print("")
    print("Calcium :- Calcium is a mineral your body needs to build and maintain strong bones and to carry out many important functions. Calcium is the most abundant mineral in the body. Your body needs calcium for muscles to move and for nerves to carry messages between your brain and every part of your body. Calcium also helps blood vessels move blood throughout your body and helps release hormones that affect many functions in your body.")
    print("")
    print("Cholesterol :- Cholesterol is a waxy substance found in your blood. Your body needs cholesterol to build healthy cells, but high levels of cholesterol can increase your risk of heart disease. With high cholesterol, you can develop fatty deposits in your blood vessels.")
    print("")
while user_satisfy==0:
    menu()
    food_type = input("ENTER THE NUMBER CORRESPONDING TO THE FOOD ITEM YOU WANT TO ADD : ")
    print("")
    if food_type=="1" or food_type=="V" or food_type=="v":
        food_items = list(Vegeterian_Main_Course.keys())
        print("")
        print("LIST OF THE VEGETERIAN MAIN COURSE : ")
        print("")
        str1 = ""
        for ele in food_items:
            str1 = str1 + ele + ", "
        print(str1[:-2])
        print("TOTAL NUMBER OF CHOICES AVALIABLE : ",len(food_items))
        print("")
        loop = int(input("ENTER THE NUMBER OF DIFFERENT ITEMS YOU CONSUME : "))
        print("")
        for i in range(loop):
            for l in range(len(food_items)):
                print(l,food_items[l])
            print("")
            a = int(input("ENTER THE NUMBER CORRESPONDING TO THE FOOD ITEM : "))
            b = float(input("ENTER NUMBER OF SERVINGS YOU TAKE : "))
            print("")
            c = Vegeterian_Main_Course[food_items[a]]
            Vegeterian_Main_Course_consumed[food_items[a]] = b
            food_counsumed[food_items[a]] = b
            fats += c[0]*b
            carbohydrates += c[1]*b
            protein += c[2]*b
            vitaminA += c[3]*b
            vitaminC += c[4]*b
            calcium += c[5]*b
            cholestrol += c[6]*b
            food_items.pop(a)
    if food_type=="2" or food_type=="N" or food_type=="n":
        food_items = list(Non_Vegeterian_Main_Course.keys())
        print("")
        print("LIST OF THE NON VEGETERIAN MAIN COURSE : ")
        print("")
        str1 = ""
        for ele in food_items:
            str1 = str1 + ele + ", "
        print(str1[:-2])
        print("TOTAL NUMBER OF CHOICES AVALIABLE : ",len(food_items))
        print("")
        loop = int(input("ENTER THE NUMBER OF DIFFERENT ITEMS YOU CONSUME : "))
        print("")
        for i in range(loop):
            for l in range(len(food_items)):
                print(l,food_items[l])
            print("")
            a = int(input("ENTER THE NUMBER CORRESPONDING TO THE FOOD ITEM : "))
            b = float(input("ENTER NUMBER OF SERVINGS YOU TAKE : "))
            print("")
            c = Non_Vegeterian_Main_Course[food_items[a]]
            Non_Vegeterian_Main_Course_consumed[food_items[a]] = b
            food_counsumed[food_items[a]] = b
            fats += c[0]*b
            carbohydrates += c[1]*b
            protein += c[2]*b
            vitaminA += c[3]*b
            vitaminC += c[4]*b
            calcium += c[5]*b
            cholestrol += c[6]*b
            food_items.pop(a)
    if food_type=="3" or food_type=="P" or food_type=="p":
        food_items = list(Pizza.keys())
        print("")
        print("LIST OF PIZZAS : ")
        print("")
        str1 = ""
        for ele in food_items:
            str1 = str1 + ele + ", "
        print(str1[:-2])
        print("TOTAL NUMBER OF CHOICES AVALIABLE : ",len(food_items))
        loop = int(input("ENTER THE NUMBER OF DIFFERENT PIZZAS YOU EAT : "))
        print("")
        for i in range(loop):
            for l in range(len(food_items)):
                print(l,food_items[l])
            print("")
            a = int(input("ENTER THE NUMBER CORRESPONDING TO THE PIZZA : "))
            b = float(input("ENTER THE NUMBER OF SLICES(1/8TH OF MEDIUM PIZZA) YOU EAT : "))
            print("")
            c = Pizza[food_items[a]]
            Pizza_consumed[food_items[a]] = b
            food_counsumed[food_items[a]] = b
            fats += c[0]*b
            carbohydrates += c[1]*b
            protein += c[2]*b
            vitaminA += c[3]*b
            vitaminC += c[4]*b
            calcium += c[5]*b
            cholestrol += c[6]*b
            food_items.pop(a)
    if food_type=="4" or food_type=="S" or food_type=="s":
        food_items = list(Snacks.keys())
        print("")
        print("LIST OF SNACKS : ")
        print("")
        str1 = ""
        for ele in food_items:
            str1 = str1 + ele + ", "
        print(str1[:-2])
        print("TOTAL NUMBER OF CHOICES AVALIABLE : ",len(food_items))
        print("")
        loop = int(input("ENTER THE NUMBER OF DIFFERENT SNACKS YOU EAT : "))
        print("")
        for i in range(loop):
            for l in range(len(food_items)):
                print(l,food_items[l])
            print("")
            a = int(input("ENTER THE NUMBER CORRESPONDING TO THE SNACK : "))
            b = float(input("ENTER THE NUMBER OF SERVINGS : "))
            print("")
            c = Snacks[food_items[a]]
            Snacks_consumed[food_items[a]] = b
            food_counsumed[food_items[a]] = b
            fats += c[0]*b
            carbohydrates += c[1]*b
            protein += c[2]*b
            vitaminA += c[3]*b
            vitaminC += c[4]*b
            calcium += c[5]*b
            cholestrol += c[6]*b
            food_items.pop(a)
    if food_type=="5" or food_type=="B" or food_type=="b":
        food_items = list(Beverages.keys())
        print("")
        print("LIST OF BEVERAGES : ")
        print("")
        str1 = ""
        for ele in food_items:
            str1 = str1 + ele + ", "
        print(str1[:-2])
        print("TOTAL NUMBER OF CHOICES AVALIABLE :",len(food_items))
        print("")
        loop = int(input("ENTER THE NUMBER OF DIFFERENT BEVERAGES YOU DRINK : "))
        print("")
        for i in range(loop):
            for l in range(len(food_items)):
                print(l,food_items[l])
            print("")
            a = int(input("ENTER THE NUMBER CORRESPONDING TO THE BEVERAGE : "))
            b = float(input("ENTER THE NUMBER OF GLASSES : "))
            print("")
            c = Beverages[food_items[a]]
            Beverages_consumed[food_items[a]] = b
            food_counsumed[food_items[a]] = b
            fats += c[0]*b
            carbohydrates += c[1]*b
            protein += c[2]*b
            vitaminA += c[3]*b
            vitaminC += c[4]*b
            calcium += c[5]*b
            cholestrol += c[6]*b
            food_items.pop(a)
    if food_type=="6" or food_type=="F" or food_type=="f":
        food_items = list(Fruits.keys())
        print("")
        print("LIST OF FRUITS : ")
        print("")
        str1 = ""
        for ele in food_items:
            str1 = str1 + ele + ", "
        print(str1[:-2])
        print("TOTAL NUMBER OF CHOICES AVALIABLE : ",len(food_items))
        print("")
        loop = int(input("ENTER THE NUMBER OF DIFFERENT FRUITS YOU EAT : "))
        print("")
        for i in range(loop):
            for l in range(len(food_items)):
                print(l,food_items[l])
            print("")
            a = int(input("ENTER THE NUMBER CORRESPONDING TO THE FRUIT : "))
            if food_items[a].upper() == "GRAPES":
                b = float(input("ENTER THE NUMBER OF GRAPES YOU EAT : "))
            elif food_items[a].upper() == "PAPAYA":
                b = float(input("ENTER THE NUMBER OF SLICES YOU EAT : "))
            else:
                b = float(input("ENTER THE NUMBER OF FRUIT YOU EAT : "))
            print("")
            c = Fruits[food_items[a]]
            Fruits_consumed[food_items[a]] = b
            food_counsumed[food_items[a]] = b
            fats += c[0]*b
            carbohydrates += c[1]*b
            protein += c[2]*b
            vitaminA += c[3]*b
            vitaminC += c[4]*b
            calcium += c[5]*b
            cholestrol += c[6]*b
            food_items.pop(a)
    if food_type=="7" or food_type=="I" or food_type=="i":
        food_items = list(Ice_Cream.keys())
        print("")
        print("LIST OF ICE-CREAMS : ")
        print("")
        str1 = ""
        for ele in food_items:
            str1 = str1 + ele + ", "
        print(str1[:-2])
        print("TOTAL NUMBER OF CHOICES AVALIABLE :",len(food_items))
        print("")
        loop = int(input("ENTER THE NUMBER OF DIFFERENT ICE-CREAMS YOU EAT :"))
        print("")
        for i in range(loop):
            for l in range(len(food_items)):
                print(l,food_items[l])
            print("")
            a = int(input("ENTER THE NUMBER CORRESPONDING TO THE ICE-CREAM : "))
            if food_items[a] == "CONE":
                b = float(input("ENTER THE NUMBER OF CONES YOU EAT : "))
            else:
                b = float(input("ENTER THE NUMBER OF CUPS YOU EAT : "))
            print("")
            c = Ice_Cream[food_items[a]]
            Ice_Cream_consumed[food_items[a]] = b
            food_counsumed[food_items[a]] = b
            fats += c[0]*b
            carbohydrates += c[1]*b
            protein += c[2]*b
            vitaminA += c[3]*b
            vitaminC += c[4]*b
            calcium += c[5]*b
            cholestrol += c[6]*b
            food_items.pop(a)
    response_menu()
    responce = input("ENTER YOUR CHOICE : ")
    print("")
    if responce == "v" or responce == "V":
        food_name = []
        food_value = []
        for ele in food_counsumed.keys():
              food_name.append(ele)
              food_value.append(food_counsumed[ele])
        food_list = pd.DataFrame(food_value,index=food_name)
        food_list.columns=[" SERVING"]
        print(food_list)
        print("")
        print("TO CONTINUE ENTERING ITEMS PRESS C")
        print("TO VIEW YOUR REPORTS PRESS R")
        print("")
        responce = input("ENTER YOUR CHOICE : ")
    if responce == "d" or responce == "D":
        n = 0
        food_item = []
        for ele in food_counsumed.keys():
            print(n,ele)
            food_item.append(ele)
            n += 1
        Remove = int(input("Enter the Number corresponding to the item you want to remove : "))
        food_counsumed.pop(food_item[Remove])
    if responce == "r" or responce == "R":
          user_satisfy += 1
    if responce=="I" or responce=="i":
        Facts_menu()
        response_menu()
        responce = input("ENTER YOUR CHOICE : ")
    if responce == "r" or responce == "R":
          user_satisfy += 1
    if responce == "v" or responce == "V":
        food_name = []
        food_value = []
        for ele in food_counsumed.keys():
              food_name.append(ele)
              food_value.append(food_counsumed[ele])
        food_list = pd.DataFrame(food_value,index=food_name)
        food_list.columns=[" SERVING"]
        print(food_list)
        print("")
        print("TO CONTINUE ENTERING ITEMS PRESS C")
        print("TO VIEW YOUR REPORTS PRESS R")
        print("")
        responce = input("ENTER YOUR CHOICE : ")
    if responce == "d" or responce == "D":
        n = 0
        food_item = []
        for ele in food_counsumed.keys():
            print(n,ele)
            food_item.append(ele)
            n += 1
        Remove = int(input("Enter the Number corresponding to the item you want to remove : "))
        food_counsumed.pop(food_item[Remove])
gram_value = []
gram_value.append(fats*1)
gram_value.append(carbohydrates*1)
gram_value.append(protein*1)
gram_value.append(vitaminA*1)
gram_value.append(vitaminC*1)
gram_value.append(calcium*1)
gram_value.append(cholestrol*1)
gram_values = np.array(gram_value)

water = int(input("ENTER THE NUMBER OF GLASSES(250ml) OF WATER YOU DRINK IN A DAY : "))
weight = float(input("ENTER YOUR WEIGHT(in KG): "))
height = float(input("ENTER YOUR HEIGHT(in m): "))
print("")
print("IF YOU ARE MALE TYPE M")
print("IF YOU ARE FEMALE TYPE F")
gender = input("ENTER YOUR GENDER : ")


req_gram_calvalue_min_m = [48.9,247.5,2*weight,900,65,1000,0]
req_gram_calvalue_min_f = [40,202.5,2*weight,700,65,1000,0]
req_gram_calvalue_max_m = [116.67,487.5,3.5*weight,3000,1000,2500,300]
req_gram_calvalue_max_f = [93.34,390,3.5*weight,3000,1000,2500,300]
result_gramvalue = []

calories = []
calories.append(fats*9)
calories.append(protein*4)
calories.append(carbohydrates*4)
calories = np.array(calories)
total_calories = np.sum(calories)
perc_cal_val = []
for c in range(len(calories)):
    perc_cal_val.append(calories[c]/total_calories*100)

def water_report(water = water*250):
    if water <= 3700 and gender.upper() == "M":
        print("")
        print("YOUR WATER CONSUMPTION IS LOW.")
        print("CONSUME MORE WATER.")
        print("")
    elif water <= 2700 and gender.upper() == "F":
        print("")
        print("YOUR WATER CONSUMPTION IS LOW.")
        print("CONSUME MORE WATER.")
        print("")
    else:
        print("")
        print("YOUR WATER CONSUMPTION IS ADEQUATE")
        print("")

for o in range(len(gram_value)):
    if gender.upper() == "M":
        req_gram_calvalue_min = req_gram_calvalue_min_m
        req_gram_calvalue_max = req_gram_calvalue_max_m
    else: 
        req_gram_calvalue_min = req_gram_calvalue_min_f
        req_gram_calvalue_max = req_gram_calvalue_max_f
    if gram_value[o] >= req_gram_calvalue_min[o] and gram_value[o] <= req_gram_calvalue_min[o]:
        result_gramvalue.append(1)
    elif gram_value[o] < req_gram_calvalue_min[o]:
        result_gramvalue.append(0)
    else:
        result_gramvalue.append(2)
        
def fat_report(a = result_gramvalue[0]):
    print("YOUR FATS REPORTS ARE HERE : ")
    if a == 0 and gender.upper() == "F":
        print("")
        print("Your fat content is low. It would be beneficial if you would increase them")
        print("")
        print("To increase your fat content, try consuming dishes which include eggs, fish and cheese")
        print("Some suggestions include avocado, butter baked salmon, egg biryani and chicken pizza") 
        print("")
    elif a == 0 and gender.upper() == "M":
        print("")
        print("Your fat content is low. It would be beneficial if you would increase them")
        print("")
        print("To increase your fat content, try consuming dishes which include eggs, fish and cheese")
        print("Some suggestions include avocado, butter baked salmon, egg biryani and chicken pizza") 
        print("")
    elif a == 1 and gender.upper() == "F":
        print("")
        print("CONGRATULATIONS!!! Your diet contains the right amount of fat. :)")
        print("")
    elif a == 1 and gender.upper() == "M":
        print("")
        print("CONGRATULATIONS!!! Your diet contains the right amount of fat. :)")
        print("")
    elif a == 2 and gender.upper() == "F":
        print("")
        print("Your diet contains an excess amount of fats. It would be beneficial if you would decrease them")
        print("")
        print("To decrease your fat content, decrease the consumption of dishes which include eggs, fish and cheese")
        print("")
    elif a == 2 and gender.upper() == "M":
        print("")
        print("Your diet contains an excess amount of fats. It would be beneficial if you would decrease them")
        print("")
        print("To decrease your fat content, decrease the consumption of dishes which include eggs, fish and cheese")
        print("")
        
def carbohydrates_report(a = result_gramvalue[1]):
    print("YOUR CARBOHYDRATES REPORTS ARE HERE : ")
    if a == 0 and gender.upper() == "F":
        print("")
        print("Your carbohydrate content is low. It would be beneficial if you would increase them")
        print("")
        print("To increase your carbohydrate content, try consuming dishes which include corns, rice, cereals, potatoes, kidney beans and chickpeas")
        print("Some suggestions include bananas, hakka noodles, baked sweet potato, chicken/veg biryani and dates") 
        print("")
    elif a == 0 and gender.upper() == "M":
        print("")
        print("Your carbohydrate content is low")
        print("")
        print("To increase your carbohydrate content, try consuming dishes which include corns, rice, cereals, potatoes, kidney beans and chickpeas")
        print("Some suggestions include bananas, hakka noodles, baked sweet potato, chicken/veg biryani and dates")
        print("")
    elif a == 1 and gender.upper() == "F":
        print("")
        print("CONGRATULATIONS!!! Your diet contains the right amount of carbohydrates. :)")
        print("")
    elif a == 1 and gender.upper() == "M":
        print("")
        print("CONGRATULATIONS!!! Your diet contains the right amount of carbohydrates. :)")
        print("")
    elif a == 2 and gender.upper() == "F":
        print("")
        print("Your diet contains an excess amount of carbohydrates. It would be beneficial if you would reduce them")
        print("")
        print("To decrease your carbohydrate content, decrease the consumption of dishes which include corns, rice, cereals, potatoes, kidney beans and chickpeas")
        print("Also avoid soft drinks")
        print("")
    elif a == 2 and gender.upper() == "M":
        print("")
        print("Your diet contains an excess amount of carbohydrates. It would be beneficial if you would reduce them")
        print("")
        print("To decrease your carbohydrate content, decrease the consumption of dishes which include corns, rice, cereals, potatoes, kidney beans and chickpeas")
        print("Also avoid soft drinks")
        print("")
        
def protein_report(a = result_gramvalue[2]):
    print("YOUR PROTEINS REPORTS ARE HERE : ")
    if a == 0 and gender.upper() == "F":
        print("")
        print("Your protein content is low. It would be beneficial if you would increase it")
        print("")
        print("To increase your protein content, try consuming dishes which include eggs, meat, paneer and chickpeas")
        print("Some suggestions include fish curry, chicken burger, chicken fired rice and paneer gravy")
        print("")
    elif a == 0 and gender.upper() == "M":
        print("")
        print("Your protein content is low. It would be beneficial if you would increase it")
        print("")
        print("To increase your protein content, try consuming dishes which include eggs, meat, paneer and chickpeas")
        print("Some suggestions include fish curry, chicken burger, chicken fired rice and paneer gravy")
        print("")
    elif a == 1 and gender.upper() == "F":
        print("")
        print("CONGRATULATIONS!!! Your diet contains the right amount of proteins. :)")
        print("")
    elif a == 1 and gender.upper() == "M":
        print("")
        print("CONGRATULATIONS!!! Your diet contains the right amount of proteins. :)")
        print("")
    elif a == 2 and gender.upper() == "F":
        print("")
        print("Your diet contains an excess amount of proteins. It would be beneficial if you would decrease them")
        print("")
        print("To decreaese your protein content, decrease the consumption of dishes which include eggs, meat, paneer and chickpeas")
        print("")
    elif a == 2 and gender.upper() == "M":
        print("")
        print("Your diet contains an excess amount of proteins. It would be beneficial if you would decrease them")
        print("")
        print("To decreaese your protein content, decrease the consumption of dishes which include eggs, meat, paneer and chickpeas")
        print("")

def vitaminA_report(a = result_gramvalue[3]):
    print("YOUR VITAMIN A REPORTS ARE HERE : ")
    if a == 0 and gender.upper() == "F":
        print("")
        print("Your Vitamin A content is low. It would be beneficial if you would increase it")
        print("")
        print("To increase your Vitamin A content, try consuming dishes which include carrot, green leafy vegetables, mango and sea food")
        print("Some suggestions include carrot juice, brocolli broth, paneer veggie wrap and tomato omelette")
        print("")
    elif a == 0 and gender.upper() == "M":
        print("")
        print("Your Vitamin A content is low. It would be beneficial if you would increase it")
        print("")
        print("To increase your Vitamin A content, try consuming dishes which include carrot, green leafy vegetables, mango and sea food")
        print("Some suggestions include carrot juice, brocolli broth, paneer veggie wrap and tomato omelette")
        print("")
    elif a == 1 and gender.upper() == "F":
        print("")
        print("CONGRATULATIONS!!! Your diet contains the right amount of Vitamin A. :)")
        print("")
    elif a == 1 and gender.upper() == "M":
        print("")
        print("CONGRATULATIONS!!! Your diet contains the right amount of Vitamin A. :)")
        print("")
    elif a == 2 and gender.upper() == "F":
        print("")
        print("Your diet contains an excess amount of Vitamin A. It would be beneficial if you would decrease them")
        print("")
        print("To decrease your Vitamin A content, decrease the consumption of dishes which include carrot, green leafy vegetables, mango and sea food")
        print("")
    elif a == 2 and gender.upper() == "M":
        print("")
        print("Your diet contains an excess amount of Vitamin A. It would be beneficial if you would decrease them")
        print("")
        print("To decrease your Vitamin A content, decrease the consumption of dishes which include carrot, green leafy vegetables, mango and sea food")
        print("")
        
def vitaminC_report(a = result_gramvalue[4]):
    print("YOUR VITAMIN C REPORTS ARE HERE : ")
    if a == 0 and gender.upper() == "F":
        print("")
        print("Your Vitamin C content is low. It would be beneficial if you would increase it")
        print("")
        print("To increase your Vitamin C content, try consuming dishes which include citrus fruits, papaya, green leafy vegetables and guava")
        print("")
    elif a == 0 and gender.upper() == "M":
        print("")
        print("Your Vitamin C content is low. It would be beneficial if you would increase it")
        print("")
        print("To increase your Vitamin C content, try consuming dishes which include citrus fruits, papaya, green leafy vegetables and guava")
        print("")
    elif a == 1 and gender.upper() == "F":
        print("")
        print("CONGRATULATIONS!!! Your diet contains the right amount of Vitamin C. :)")
        print("")
    elif a == 1 and gender.upper() == "M":
        print("")
        print("CONGRATULATIONS!!! Your diet contains the right amount of Vitamin C. :)")
        print("")
    elif a == 2 and gender.upper() == "F":
        print("")
        print("Your diet contains an excess amount of Vitamin C. It would be beneficial if you would decrease them")
        print("")
        print("To decrease your Vitamin C content, decrease the consumption of dishes which include citrus fruits, papaya, green leafy vegetables and guava")
        print("")
    elif a == 2 and gender.upper() == "M":
        print("")
        print("Your diet contains an excess amount of Vitamin C. It would be beneficial if you would decrease them")
        print("")
        print("To decrease your Vitamin C content, decrease the consumption of dishes which include citrus fruits, papaya, green leafy vegetables and guava")
        print("")
        
def calcium_report(a = result_gramvalue[5]):
    print("YOUR CALCIUM REPORTS ARE HERE : ")
    if a == 0 and gender.upper() == "F":
        print("")
        print("Your Calcium content is low. It would be beneficial if you would increase it")
        print("")
        print("To increase your Calcium content, try consuming dishes which include milk and dairy products, green leafy vegetables, soybeans and almonds")
        print("")
    elif a == 0 and gender.upper() == "M":
        print("")
        print("Your Calcium content is low. It would be beneficial if you would increase it")
        print("")
        print("To increase your Calcium content, try consuming dishes which include milk and dairy products, green leafy vegetables, soybeans and almonds")
        print("")
    elif a == 1 and gender.upper() == "F":
        print("")
        print("CONGRATULATIONS!!! Your diet contains the right amount of Calcium. :)")
        print("")
    elif a == 1 and gender.upper() == "M":
        print("")
        print("CONGRATULATIONS!!! Your diet contains the right amount of Calcium. :)")
        print("")
    elif a == 2 and gender.upper() == "F":
        print("")
        print("Your diet contains an excess amount of Calcium. It would be beneficial if you would decrease them")
        print("")
        print("To decrease your Vitamin C content, decrease the consumption of dishes which include milk and dairy products, green leafy vegetables, soybeans and almonds")
        print("")
    elif a == 2 and gender.upper() == "M":
        print("")
        print("Your diet contains an excess amount of Calcium. It would be beneficial if you would decrease them")
        print("")
        print("To decrease your Vitamin C content, decrease the consumption of dishes which include milk and dairy products, green leafy vegetables, soybeans and almonds")
        print("")
        
def cholestrol_report(a = result_gramvalue[6]):
    print("YOUR CHOLESTEROL REPORTS ARE HERE : ")
    if a == 0 and gender.upper() == "F":
        print("")
        print("Low Contain")
        print("")
    elif a == 0 and gender.upper() == "M":
        print("")
        print("Low Contain")
        print("")
    elif a == 1 and gender.upper() == "F":
        print("")
        print("CONGRATULATIONS!!! Your diet contains a safe amount of Cholesterol. :)")
        print("")
    elif a == 1 and gender.upper() == "M":
        print("")
        print("CONGRATULATIONS!!! Your diet contains a safe amount of Cholesterol. :)")
        print("")
    elif a == 2 and gender.upper() == "F":
        print("")
        print("Your diet contains an excess amount of Cholesetrol. It would be beneficial if you would decrease them")
        print("")
        print("To decrease your Cholesterol content, decrease the consumption of dishes which include milk and dairy products, meat and eggs")
        print("")
    elif a == 2 and gender.upper() == "M":
        print("")
        print("Your diet contains an excess amount of Cholesetrol. It would be beneficial if you would decrease them")
        print("")
        print("To decrease your Cholesterol content, decrease the consumption of dishes which include milk and dairy products, meat and eggs")
        print("")




print("-------------------------------------------------------------------------------------------------------------")
print("")
bmi = (weight)/(height)**2
print("-----------------------------------------------------")
print("YOUR BMI REPORT :")
print("")
print("YOUR BMI IS : ",'%.3f' %bmi)
if bmi<18.5:
    print("YOU ARE UNDERWEIGHT.")
elif bmi>=18.5 and bmi<=24.9:
    print("CONGRATULATIONS!!! YOUR BMI IS WITHIN THE HEALTHY RANGE. :)")
elif bmi>24.9 and bmi<=29.9:
    print("YOU ARE OVERWEIGHT")
elif bmi>29.9 and bmi<=34.9:
    print("OBESE CLASS 1")
elif bmi>34.9 and bmi<=39.9:
    print("OBESE CLASS 2")
else:
    print("OBESE CLASS 3")
print("-----------------------------------------------------")
print("")
print("-----------------------------------------------------")
water_report()
print("-----------------------------------------------------")
print("")
print("")
print("CALORIES REPORT")
print("")
print("YOUR TOTAL CALORIES ARE : ",'%.4f' % total_calories)
print("")
print("YOUR PERCENTAGE OF CALORIES FROM FATS ARE : ",'%.5f' % perc_cal_val[0],"%")
print("YOUR PERCENTAGE OF CALORIES FROM PROTEINS ARE : ",'%.5f' % perc_cal_val[1],"%")
print("YOUR PERCENTAGE OF CALORIES FROM CARBOHYDRATES ARE : ",'%.5f' % perc_cal_val[2],"%")
print("")
print("-----------------------------------------------------")
print("")
print("-----------------------------------------------------")
fat_report()
print("-----------------------------------------------------")
print("")
print("-----------------------------------------------------")
carbohydrates_report()
print("-----------------------------------------------------")
print("")
print("-----------------------------------------------------")
protein_report()
print("-----------------------------------------------------")
print("")
print("-----------------------------------------------------")
vitaminA_report()
print("-----------------------------------------------------")
print("")
print("-----------------------------------------------------")
vitaminC_report()
print("-----------------------------------------------------")
print("")
print("-----------------------------------------------------")
calcium_report()
print("-----------------------------------------------------")
print("")
print("-----------------------------------------------------")
cholestrol_report()
print("-----------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------")

 














