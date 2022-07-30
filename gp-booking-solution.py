# DIFFICULTY LEVEL: Difficult (but you can do it! we believe in you!)
# SUMMARY: Create a GP Booking system that keeps track of
#  patients, doctors and appointments inside the practice.
# IMPORTANT: Follow the correct order of the instructions to create you program successfully!


# 1.0 create a Patient class
# 1.1 the class should be initialized with the following properties (all received at object creation)
#   first_name
#   last_name
# 1.2 create a function get_name() that returns the full name of the patient
class Patient:

  def __init__(self, fn, ln):
    self.first_name = fn
    self.last_name = ln

  def get_full_name(self):
    return self.first_name + " " + self.last_name


# 4.0 create a Doctor class
# 4.1 the class should be initialized with the following properites (all received at object creation):
#   first_name
#   last_name
#   specialization (e.g. heart surgeon, pediatrician)
# 4.2 create a function get_name(self) that returns the full name of the doctor
# 4.3 create a function get_specialization(self) that returns the specialization of this doctor
class Doctor:

  def __init__(self, first_name, last_name, spec):
    self.first_name = first_name
    self.last_name = last_name
    self.specialization = spec

  def get_name(self):
    return self.first_name + " " + self.last_name

  def get_specialization(self):
    return self.specialization


# 7.0 Create a GP_Practice class
# 7.1 the class should be initialized with the following properites (only practice_name is received during object creation)
#   practice_name
#   patient_list (just an empty list)
#   doctor_list (just an empty list)
#   appointments (just an empty list)
# 7.2 create a function get_practice_name() that returns the practice_name
# 10.0 (make sure you have completed step 8 and 9 before proceeding here)
# 10.1 create a function called add_patient_to_practice(self, new_patient) that adds a new_patient to the patient_list of the practice.
# 12. create a function called add_doctor_to_practice(self, new_doctor) that adds a doctor to the doctor of the practice.
# 15. create a function called create_appointment(self, patient, doctor, date, notes="") that creates a new Appointment object and adds it to the appointments_list of the practice
# 17. create a function called get_all_appointments(self) that returns all appointments of the practice
# 19. Extra question: only allow booking of appointment if patient and doctor are part of the practice, otherwise print a message back to the user that the booking cannot be done.
class GP_Practice:
  def __init__(self, practice_name):
    self.practice_name = practice_name
    self.patient_list = []
    self.doctor_list = []
    self.appointments = []

  def get_practice_name(self):
    return self.practice_name

  def add_patient_to_practice(self, new_patient):
    self.patient_list.append(new_patient)

  def add_doctor_to_practice(self, new_doctor):
    self.doctor_list.append(new_doctor)

  def create_appointment(self, patient, doctor, date, notes=""):
    if patient not in self.patient_list or doctor not in self.doctor_list:
      print("Could not create appointment as patient or doctor is not registered in this GP Practice")
    else:
      app = Appointment(patient, doctor, date, notes)
      self.appointments.append(app)

  def get_all_appointments(self):
    return self.appointments

# 14.0 create an Appointment class
# 14.1 the class should be initialized with the following properites (all received at object creation, notes is not compulsory)
#   patient
#   doctor
#   date
#   notes="" (please note that notes is an empty string by default, so it's an optional field. Google 'python default function paramenter' for more information)
# 14.2 the class should have a function get_appointment_info(self) that prints a summary of the appointment (i.e. all the information inside this obejct)
class Appointment:

  def __init__(self, patient, doctor, date, notes=""):
    self.patient = patient
    self.doctor = doctor
    self.date = date
    self.notes = notes

  def get_appointment_info(self):
    return "Patient -> " + self.patient.get_full_name() + " Doctor -> " + self.doctor.get_name() + "(" + self.doctor.get_specialization() + ")" + "Notes (optional) -> " + self.notes


if __name__ == "__main__":
  print("hello, world!")

  # 2. create two Patient objects (patient1 and patient2)
  # and initialize these objects with first and last name of your choice
  patient1 = Patient("Katie", "Smith")
  patient2 = Patient("John", "McHello")

  # 3. print both patient names
  print(patient1.get_full_name())
  print(patient2.get_full_name())

  # 5. create a Doctor object doctor1 and give them a name and specialization of your choice
  doctor1 = Doctor("Stephanie", "Hall", "Pediatrician")

  # 6. print the doctor1's name and it's specialization on the same line
  print(doctor1.get_name(), doctor1.get_specialization())

  # 8. create a GP_Practice object called gp_practice and give it a practice_name of your choice
  gp_practice = GP_Practice("Cabot Square Practice")

  # 9. print the gp_practice pratice_name
  print(gp_practice.get_practice_name())

  # 11. add patient1 and patient2 to the practice
  gp_practice.add_patient_to_practice(patient1)
  gp_practice.add_patient_to_practice(patient2)

  # 13. add doctor1 to the practice
  gp_practice.add_doctor_to_practice(doctor1)

  # 16. create a new appointment for patient1 with doctor1 for date "30 July 2022" and add some notes for the GP to look at
  gp_practice.create_appointment(patient1, doctor1, "30 July 2022", "Just checking overall health")

  # 18. prints a summary for all the appointments in the gp_practice
  for appointment in gp_practice.get_all_appointments():
    print("APPOINTMENT SUMMARY")
    print(appointment.get_appointment_info())
    print() # just to print an empty line

  # 20. Extra question: create a patient3 object, do NOT add it to practice, and try to book an appointment for them
  #  (if you followed step 19 correctly this appointment booking will fail.)
  patient3 = Patient("Someone", "Else")
  gp_practice.create_appointment(patient3, doctor1, "30 July 2022", "Just checking overall health")
