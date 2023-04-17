import random
from faker import Faker
from hl7apy.core import Message

fake = Faker()

def generate_random_patient_data():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
    }

def generate_random_order_data():
    test_names = ["CBC", "CMP", "Lipid Panel", "TSH", "HbA1c"]
    return {
        "order_id": str(random.randint(100000, 999999)),
        "test_name": random.choice(test_names),
    }

def create_orm_message(patient_data, order_data):
    msg = Message("ORM_O01")
    msg.msh.msh_3 = "ExampleSender"
    msg.msh.msh_4 = "ExampleFacility"
    msg.msh.msh_5 = "ExampleReceiver"
    msg.msh.msh_6 = "ExampleReceiverFacility"
    msg.msh.msh_7 = fake.date_time().strftime("%Y%m%d%H%M%S")
    msg.msh.msh_9 = "ORM^O01"
    msg.msh.msh_10 = str(random.randint(100000, 999999))
    msg.msh.msh_11 = "P"
    msg.msh.msh_12 = "2.5"

    msg.pid.pid_3 = str(random.randint(100000, 999999))
    msg.pid.pid_5 = f"{patient_data['last_name']}^{patient_data['first_name']}"

    msg.orc.orc_1 = "NW"
    msg.orc.orc_2 = order_data["order_id"]

    msg.obr.obr_1 = "1"
    msg.obr.obr_4 = f"{order_data['test_name']}^LN"

    return msg.to_er7()

if __name__ == "__main__":
    patient_data = generate_random_patient_data()
    order_data = generate_random_order_data()
    orm_message = create_orm_message(patient_data, order_data)
    print(orm_message)
