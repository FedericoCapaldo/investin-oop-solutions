# DIFFICULTY LEVEL: Difficult (but you can do it! we believe in you!)
# SUMMARY: Create a GP Booking system that keeps track of
#  patients, doctors and appointments inside the practice.
# IMPORTANT: Follow the correct order of the instructions to create you program successfully!


# 1.0 create a Patient class
# 1.1 the class should be initialized with the following properties (all received at object creation)
#   first_name
#   last_name
# 1.2 create a function get_name() that returns the full name of the patient


# 4.0 create a Doctor class
# 4.1 the class should be initialized with the following properites:
#   first_name
#   last_name
#   specialization (e.g. heart surgeon, pediatrician)
# 4.2 create a function get_name() that returns the full name of the doctor
# 4.3 create a function get_specialization() that returns the specialization of this doctor


# 7.0 Create a GP_Practice class
# 7.1 the class should be initialized with the following properites (only practice_name is received during object creation)
#   practice_name
#   patient_list (just an empty list)
#   doctor_list (just an empty list)
#   appointments (just an empty list)
# 7.2 create a function get_practice_name() that returns the practice_name
# 10.0 (make sure you have completed step 8 and 9 before proceeding here)
# 10.1 create a function called add_patient_to_practice(new_patient) that adds a new_patient to the patient_list of the practice.
# 12. create a function called add_doctor_to_practice(new_doctor) that adds a doctor to the doctor of the practice.
# 15. create a function called create_appointment( patient, doctor, date, notes="") that creates a new Appointment object and adds it to the appointments_list of the practice
# 17. create a function called get_all_appointments() that returns all appointments of the practice
# 19. Extra question: only allow booking of appointment if patient and doctor are part of the practice,
#   otherwise print a message back to the user that the booking cannot be done.

# 14.0 create an Appointment class
# 14.1 the class should be initialized with the following properites (all received at object creation, notes is not compulsory)
#   patient
#   doctor
#   date
#   notes="" (please note that notes is an empty string by default, so it's an optional field)
# 14.2 the class should have a function get_appointment_info() that prints a summary of the appointment (i.e. all the information inside this obejct)


if __name__ == "__main__":
    print("hello, world!")

    # 2. create two Patient objects (patient1 and patient2)
    # and initialize these objects with first and last name of your choice

    # 3. print both patient names

    # 5. create a Doctor object doctor1 and give them a name and specialization of your choice

    # 6. print the doctor1's name and it's specialization on the same line

    # 8. create a GP_Practice object called gp_practice and give it a practice_name of your choice

    # 9. print the gp_practice pratice_name

    # 11. add patient1 and patient2 to the practice

    # 13. add doctor1 to the practice

    # 16. create a new appointment for patient1 with docto1 for date "30 July 2022" and add some notes for the GP to look at

    # 18. prints a summary for all the appointments in the gp_practice

    # 20. Extra question: create a patient3 object, do NOT add it to practice, and try to book an appointment for them
    #  (if you followed step 19 correctly this appointment booking will fail.)
