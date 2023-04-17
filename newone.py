import random
from faker import Faker
from hl7apy.core import Message

fake = Faker()

def generate_random_patient_data():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "birthdate": fake.date_of_birth().strftime("%Y%m%d"),
        "gender": random.choice(["M", "F"]),
        "address": fake.address().replace("\n", "^"),
    }

def create_adt_message(patient_data, message_type):
    msg = Message(message_type)
    msg.msh.msh_3 = "ExampleSender"
    msg.msh.msh_4 = "ExampleFacility"
    msg.msh.msh_5 = "ExampleReceiver"
    msg.msh.msh_6 = "ExampleReceiverFacility"
    msg.msh.msh_7 = fake.date_time().strftime("%Y%m%d%H%M%S")
    msg.msh.msh_9 = f"{message_type}"
    msg.msh.msh_10 = str(random.randint(100000, 999999))
    msg.msh.msh_11 = "P"
    msg.msh.msh_12 = "2.5"

    msg.evn.evn_1 = "EVN"
    msg.evn.evn_2 = message_type
    msg.evn.evn_6 = fake.date_time().strftime("%Y%m%d%H%M%S")

    msg.pid.pid_3 = str(random.randint(100000, 999999))
    msg.pid.pid_5 = f"{patient_data['last_name']}^{patient_data['first_name']}"
    msg.pid.pid_7 = patient_data["birthdate"]
    msg.pid.pid_8 = patient_data["gender"]
    msg.pid.pid_11 = patient_data["address"]

    return msg

if __name__ == "__main__":
    adt_types = {
        "1": "ADT_A01",
        "2": "ADT_A02",
        "3": "ADT_A03",
        "4": "ADT_A04",
        "5": "ADT_A05",
    }

    print("Choose ADT message type:")
    for key, value in adt_types.items():
        print(f"{key}. {value}")

    user_choice = input("Enter the number of the desired ADT message type: ")
    while user_choice not in adt_types.keys():
        user_choice = input("Invalid choice. Enter the number of the desired ADT message type: ")

    patient_data = generate_random_patient_data()
    adt_message = create_adt_message(patient_data, adt_types[user_choice])

    print("\nGenerated ADT message:")
    print("MSH segment:")
    print(adt_message.msh.to_er7())
    print("EVN segment:")
    print(adt_message.evn.to_er7())
    print("PID segment:")
    print(adt_message.pid.to_er7())
    print("\nFull ADT message:")
    print(adt_message.to_er7())
