"""import pandas as pd
import random
first_names = [
    "Ali", "Ahmed", "Ibrahim", "Eanaas", "Nishaah", "Ahumed", "Mohamed", "Aminath", "Maash", "Pradeep",
    "Ahmed", "Shamna", "Vishah", "Hasim", "Hussain", "James", "Ashraf", "Huneys", "Shaheen", "Hawwa",
    "Ismail", "Zayaan", "Aishath", "Munawwar", "Sharuqeel", "Shanun", "Asjadh", "Mariyam", "Ibrahim",
    "Afsah", "Hassan", "Abdulla", "Nadheem", "Annan", "Hussain", "Ibrahim", "Aminath", "Shaheen",
    "Fathimath", "Safooh", "Ahmed", "Ilyas", "Moyaz", "Imthiyaaz", "Shahid", "Nihaad", "Anwar", "Nashid",
    "Adnan", "Yoosuf", "Ali", "Fathimath", "Saravanan", "Yamin", "Mubin", "Husna", "Mohammed"
]

last_names = [
    "Dhanish", "Rafil", "Mohamed", "Ahmed", "Zubair", "Adheeb", "Rauf", "Saaima", "Rashaad", "Wijenayake",
    "Shihaam", "Axmy", "Shaan", "Afsan", "Ibrahim", "Adam", "Reehan", "Saeed", "Razzag", "Minsar", "Maaif",
    "Niyaz", "Shareef", "Riswan", "Aly", "Jameel", "Shafeeu", "Easa", "Saleem", "Haaif", "Fishan", "Azwar",
    "Vishal", "Abaan", "Iyaaz", "Naail", "Akhiz", "Maaish", "Faaris", "Bassam", "Hanan", "Madheeh", "Easa",
    "Musthafa", "Reza", "Raeefa", "Faisal", "Anaan", "Lirugham", "Areen", "Asad", "Sahuban", "Naaif", "Samih",
    "Yameen", "Lasan", "Rasheed", "Meeha", "Nabeel", "Shaahidhu", "Sina", "Muaaviyath", "Ashfeen", "Ashfaq",
    "Viaam", "Rifau", "Huzaam", "Faisal", "Moosa", "Rifau", "Sulaiman", "Faisal", "Areej", "Adil", "Shinaan",
    "Naish", "Yamin", "Looth", "Hameem", "Imran", "Thaaif", "Saadhin", "Fayaz", "Rahman", "Muzakkir", "Jazlaan"
]
s = ["Math", "Science", "Math", "Science"]
name = []
contact = []
class_s = []
rol = []
subject_name = []
mark = []
for i in range(20000):
    name.append(random.choice(first_names)+" "+ random.choice(last_names))
    contact.append(str(96098000000+i))
    class_s.append("10A")
    rol.append(i)
    subject_name.append(random.choice(s))
    mark.append(i)
    print(i)

# Verilerinizi bir sözlük olarak oluşturun
data = {
    "name": name,
    "contact": contact,
    "class": class_s,
    "roll no": rol,
    "subject": subject_name,
    "mark obtained": mark
}

# Veriyi DataFrame'e dönüştürün
df = pd.DataFrame(data)

# DataFrame'i bir Excel dosyasına yazın
df.to_excel("students.xlsx", index=False)

print("Excel dosyası başarıyla oluşturuldu!")
"""
import pandas as pd
import random

first_names = [
    "Ali", "Ahmed", "Ibrahim", "Eanaas", "Nishaah", "Ahumed", "Mohamed", "Aminath", "Maash", "Pradeep",
    "Ahmed", "Shamna", "Vishah", "Hasim", "Hussain", "James", "Ashraf", "Huneys", "Shaheen", "Hawwa",
    "Ismail", "Zayaan", "Aishath", "Munawwar", "Sharuqeel", "Shanun", "Asjadh", "Mariyam", "Ibrahim",
    "Afsah", "Hassan", "Abdulla", "Nadheem", "Annan", "Hussain", "Ibrahim", "Aminath", "Shaheen",
    "Fathimath", "Safooh", "Ahmed", "Ilyas", "Moyaz", "Imthiyaaz", "Shahid", "Nihaad", "Anwar", "Nashid",
    "Adnan", "Yoosuf", "Ali", "Fathimath", "Saravanan", "Yamin", "Mubin", "Husna", "Mohammed"
]

last_names = [
    "Dhanish", "Rafil", "Mohamed", "Ahmed", "Zubair", "Adheeb", "Rauf", "Saaima", "Rashaad", "Wijenayake",
    "Shihaam", "Axmy", "Shaan", "Afsan", "Ibrahim", "Adam", "Reehan", "Saeed", "Razzag", "Minsar", "Maaif",
    "Niyaz", "Shareef", "Riswan", "Aly", "Jameel", "Shafeeu", "Easa", "Saleem", "Haaif", "Fishan", "Azwar",
    "Vishal", "Abaan", "Iyaaz", "Naail", "Akhiz", "Maaish", "Faaris", "Bassam", "Hanan", "Madheeh", "Easa",
    "Musthafa", "Reza", "Raeefa", "Faisal", "Anaan", "Lirugham", "Areen", "Asad", "Sahuban", "Naaif", "Samih",
    "Yameen", "Lasan", "Rasheed", "Meeha", "Nabeel", "Shaahidhu", "Sina", "Muaaviyath", "Ashfeen", "Ashfaq",
    "Viaam", "Rifau", "Huzaam", "Faisal", "Moosa", "Rifau", "Sulaiman", "Faisal", "Areej", "Adil", "Shinaan",
    "Naish", "Yamin", "Looth", "Hameem", "Imran", "Thaaif", "Saadhin", "Fayaz", "Rahman", "Muzakkir", "Jazlaan"
]

subjects = ["Math", "Science", "History", "Geography", "English"]

# Rastgele veriler oluşturmak için bir fonksiyon
def generate_random_data(num_records):
    data = {
        "name": [],
        "contact": []
    }
    
    for i in range(num_records):
        name = random.choice(first_names) + " " + random.choice(last_names)
        contact = str(9609800000 + int(i))
        class_ = "10A"
        roll_no = i
        subject = random.choice(subjects)
        mark_obtained = i
        
        data["name"].append(name)
        data["contact"].append(contact)
     
    
    return data

# Rastgele 20000 kayıt oluştur
num_records = 20000
random_data = generate_random_data(num_records)

# Veriyi DataFrame'e dönüştür
df = pd.DataFrame(random_data)

# DataFrame'i bir CSV dosyasına yaz
df.to_csv("students.csv", index=False)

print("CSV dosyası başarıyla oluşturuldu!")
