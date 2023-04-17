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

    # MSH segment
    msg.msh.msh_3 = "ExampleSender"
    msg.msh.msh_4 = "ExampleFacility"
    msg.msh.msh_5 = "ExampleReceiver"
    msg.msh.msh_6 = "ExampleReceiverFacility"
    msg.msh.msh_7 = fake.date_time().strftime("%Y%m%d%H%M%S")
    msg.msh.msh_9 = f"{message_type}"
    msg.msh.msh_10 = str(random.randint(100000, 999999))
    msg.msh.msh_11 = "P"
    msg.msh.msh_12 = "2.5"

    # EVN segment
    msg.evn.evn_1 = "EVN"
    msg.evn.evn_2 = message_type
    msg.evn.evn_6 = fake.date_time().strftime("%Y%m%d%H%M%S")

    # PID segment
    msg.pid.pid_3 = str(random.randint(100000, 999999))
    msg.pid.pid_5 = f"{patient_data['last_name']}^{patient_data['first_name']}"
    msg.pid.pid_7 = patient_data["birthdate"]
    msg.pid.pid_8 = patient_data["gender"]
    msg.pid.pid_11 = patient_data["address"]

    # NK1 segment
    msg.nk1.nk1_1 = "1"
    msg.nk1.nk1_2 = f"{fake.last_name()}^{fake.first_name()}"
    msg.nk1.nk1_3 = "S^Spouse"

    # PV1 segment
    msg.pv1.pv1_1 = "1"
    msg.pv1.pv1_2 = "I"
    msg.pv1.pv1_3 = f"{random.randint(1, 999)}^{random.randint(1, 999)}^{random.randint(1, 999)}"
    msg.pv1.pv1_7 = f"{fake.last_name()}^{fake.first_name()}^{fake.suffix()}^"
    msg.pv1.pv1_10 = "SUR^Surgery"
    msg.pv1.pv1_18 = "PVT^Private"
    msg.pv1.pv1_19 = str(random.randint(100000, 999999))
    msg.pv1.pv1_36 = "D"

    # AL1 segment
    msg.al1.al1_1 = "1"
    msg.al1.al1_2 = "DA"
    msg.al1.al1_3 = "PENICILLIN^Penicillin"
    msg.al1.al1_4 = "SEV^Severe"

    # DG1 segment
    msg.dg1.dg1_1 = "1"
    msg.dg1.dg1_2 = "ICD9"
    msg.dg1.dg1_3 = "250.01^DIABETES MELLITUS"
    msg.dg1.dg1_5 = "A^Admitting"
    msg.dg1.dg1_6 = fake.date_time().strftime("%Y%m%d")

    return msg.to_er7()

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
    print(adt_message)

