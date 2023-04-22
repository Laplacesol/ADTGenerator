Welcome to the ADT_A01 HL7 Message Generator!

The ADT_A01 HL7 Message Generator is a Python script that enables the automated creation of ADT_A01 HL7 messages for testing and demonstration purposes. This script generates a random patient and creates an ADT_A01 HL7 message based on that data.

        ___
       /  /\                    __       ___
      /  /:/_                  /  \     /  /\
     /  /:/ /\    ___     ___/   /    /  /:/_
    /  /:/ /:/_  /__/\   /__/\  /    /  /:/ /\
   /__/:/ /:/ /\ \  \:\  \  \:\ \__ /__/:/ /:/_
   \  \:\/:/ /:/  \  \:\  \  \:\/\  \\  \:\/:/
    \  \::/ /:/    \  \:\  \__\:\ \  \\  \::/
     \__\/ /:/      \__\:\ /  /:/  \  \\__\/
       /__/:/       /  /:/ \ /:/    \__\
       \__\/       /__/:/  /__\/

## Getting Started

To use this script, please follow these steps:

1. Clone the repository:
$ git clone https://github.com/username/repo.git

2. Navigate to the cloned repository:
$ cd repo

3. Run the script using Python 3:
$ python hl7_message_generator.py

This will generate a randomly generated ADT_A01 message that will be printed to the console.

## Customization

If you would like to customize the patient data that is used to generate the HL7 message, you can modify the `generate_random_patient_data()` function in the code. Additionally, you can modify the segments and fields of the HL7 message in the `create_adt_message()` function.

## Dependencies

This script requires the following dependencies:
- [Faker](https://pypi.org/project/Faker/)
- [hl7apy](https://pypi.org/project/hl7apy/)

You can install these dependencies using pip:
$ pip install Faker hl7apy

We hope this script helps you save time and simplifies the process of generating HL7 messages for your testing and demonstration needs.
