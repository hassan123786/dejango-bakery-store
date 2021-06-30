from django.db import models
from .models import *
# Create your models here.
class Register(models.Model):
    user_name= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    email= models.EmailField()
    phone= models.IntegerField()

    def _str_(self):
        return self.user_name

class login(models.Model):
    user_id = models.ForeignKey(Register, on_delete=models.CASCADE)
    login_date_time= models.DateField()
    
class  Bakery_Equipments(models.Model): 
  Equipment_name= models.CharField(max_length=100)
  Equipment_type= models.CharField(max_length=100)
  Equipment_Quanity= models.CharField(max_length=100)
  entry_date_time= models.DateField()
  
def _str_(self):
        return self.Equipment_name
class Customer(models.Model):
    Customer_first_name=models.CharField(max_length=50)
Customer_Last_Name=models.CharField(max_length=50)
Customer_Email=models.EmailField()

def _str_(self):
		return self.distributor_Company_Product_Name

class Customer_personal(models.Model):
	Customer_CNIC=models.IntegerField()
	Customer_DOB=models.DateField()
	Customer_age=models.IntegerField()
	Customer_House_Number=models.IntegerField()
	Customer_Street=models.CharField(max_length=50)
	Customer_Town=models.CharField(max_length=50)
	Customer_City=models.IntegerField()
	Customer_Country=models.CharField(max_length=50)
	Customer_id=models.ForeignKey(Customer, on_delete=models.CASCADE)

class Customer_Contact(models.Model):
	Customer_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
	Customer_Contact_Number=models.CharField(max_length=50)

class Customer_payment(models.Model):
	Customer_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
	total_payment=models.IntegerField()



class payment_installment(models.Model):
	payment_id=models.ForeignKey(Customer_payment, on_delete=models.CASCADE)
	recieve_amount=models.IntegerField()
	remaining_amount=models.IntegerField()

	def str(self):
		return self.recieve_amount
class Employee(models.Model):
	Employee_First_Name=models.CharField(max_length=50)
	Employee_Last_Name=models.CharField(max_length=50)
	Employee_Email=models.EmailField()
	Employee_Type=models.CharField(max_length=50)

	def str(self):
		return self.Employee_First_Name

class Employee_Personal(models.Model):
	Employee_CNIC=models.CharField(max_length=50)
	Employee_DOB=models.DateField()
	Employee_Age=models.CharField(max_length=50)
	Employee_Education=models.CharField(max_length=100)
	Employee_Can_Drive=models.CharField(max_length=20)
	Employee_House_Number=models.CharField(max_length=50)
	Employee_Street=models.CharField(max_length=50)
	Employee_Town=models.CharField(max_length=50)
	Employee_City=models.CharField(max_length=50)
	Employee_Country=models.CharField(max_length=60)
	Employee_id=models.ForeignKey(Employee, on_delete=models.CASCADE)

	def str(self):
		return self.Employee_CNIC

class Employee_Contact(models.Model):
	Employee_id=models.ForeignKey(Employee_Personal, on_delete=models.CASCADE)
	Employee_Contact_Numeber=models.CharField(max_length=50)

	def str(self):
		return self.Employee_Contact_Numeber
#---------Employee_Previous_Details-----------
class Employee_Previous_Details(models.Model):
     Employee_ID=models.ForeignKey(Employee,on_delete=models.CASCADE)
     Previous_job=models.CharField(max_length=50)
     Previous_job_duration=models.CharField(max_length=50)
     Previous_job_Company=models.CharField(max_length=50)
     Reason_to_left_old_job=models.CharField(max_length=50)

     def str(self):
         return self.Previous_job

#---------Employee_Salary----------
class Employee_Salary(models.Model):
    Employee_ID=models.ForeignKey(Employee,on_delete=models.CASCADE)
    Salary_Ammount=models.IntegerField()
    Advance_Salary=models.IntegerField()
    Paid=models.IntegerField()
    Remaining=models.IntegerField()
    Salary_Date=models.DateField()

    def str(self):
        return self.Salary_Ammount


#---------Employee_Professional_Details--------

class Employee_Professional_Details(models.Model):

     Employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
     Employee_Experince=models.CharField(max_length=50)
     Job_description=models.CharField(max_length=50)


     def str(self):
         return self.Employee_Experince

#-------Employee_skills----------
class Employee_skills(models.Model):
	Employee_ID=models.ForeignKey(Employee_Professional_Details,on_delete=models.CASCADE)
	Skill_Name=models.CharField(max_length=50)
	def str(self):
		return self.Skill_Name

class Employee_attandance(models.Model):
	Employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)


#------------ Employee_Login -------------
class Employee_Login(models.Model):
    Employee_Id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    Password=models.CharField(max_length=50)

    def str(self):
        return self.Password


#-------------EmployEmployee_Lee Login History--------
class Employee_login_History(models.Model):
    Employee_Id=models.ForeignKey(Employee,on_delete=models.CASCADE)

class distributor(models.Model):
    distributor_FirstName=models.CharField(max_length=50)
    distributor_Last_Name=models.CharField(max_length=50)
    distributor_Email=models.EmailField()
    def _str_(self):
        return self.distributor_FirstName
class distributor_personal(models.Model):
    distributor_CNIC=models.IntegerField()
    distributor_DOB=models.DateField()
    distributor_House_Number=models.IntegerField()
    distributor_Street=models.CharField(max_length=100)
    distributor_Town=models.CharField(max_length=100)
    distributor_City=models.CharField(max_length=100)
    distributor_Country=models.CharField(max_length=100)
    distributor_id=models.ForeignKey(distributor, on_delete=models.CASCADE)

    def _str_(self):
         return self.distributor_Street
class distributor_contact(models.Model):
	distributor_Contact_Number=models.CharField(max_length=30)
	distributor_id=models.ForeignKey(distributor, on_delete=models.CASCADE)
class distributor_professional_details(models.Model):
	distributor_id=models.ForeignKey(distributor, on_delete=models.CASCADE)
	distributor_Office_Address=models.CharField(max_length=100)
	distributor_Office_Contact=models.CharField(max_length=30)

class distributor_Company(models.Model):
	distributor_id=models.ForeignKey(distributor_professional_details(distributor), on_delete=models.CASCADE)
	distributor_Company_Name=models.CharField(max_length=60)
	distributor_Company_description=models.CharField(max_length=100)
	def _str_(self):
		return self.distributor_Company_Name


class distributor_Company_Product(models.Model):
	distributor_Company_id=models.ForeignKey(distributor_Company(distributor), on_delete=models.CASCADE)
	distributor_Company_Product_Name=models.CharField(max_length=50)
	distributor_Company_Product_Min_Quantity=models.CharField(max_length=50)
	distributor_Company_Product_Expected_Deivery=models.CharField(max_length=50)

	def _str_(self):
		return self.distributor_Company_Product_Name
class Purchase(models.Model):
     Distributor_Company_Product_ID=models.ForeignKey(distributor_Company_Product,on_delete=models.CASCADE)
     Purchase_Date_Time=models.DateTimeField()
#--------------Purchase_Recieve---------------
class Purchase_Recieve(models.Model):
    Purchase_ID=models.ForeignKey(Purchase,on_delete=models.CASCADE)
    Purchase_Recieve_Date=models.DateField()
    Purchase_recieve_Bill=models.IntegerField()

    def str(self):
        return self.Purchase_Recieve


#-------Distributor_Payment-----
class Distributor_Payment(models.Model):
	Purchase_Recieve_ID=models.ForeignKey(Purchase_Recieve,on_delete=models.CASCADE)
	amount_recieve=models.IntegerField()
	remaining_amount=models.IntegerField()
	def str(self):
		return self.Purchase_Recieve_Date

#-------Purchase_Quality-------
class Purchase_Quantity(models.Model):
	Purchase_ID=models.ForeignKey(Purchase,on_delete=models.CASCADE)
	Quantity_in_number=models.IntegerField()
	Qunatit_in_litter=models.IntegerField()
	Quantity_in_kg=models.IntegerField()
	def str(self):
		return self.Quantity_in_number
class Product(models.Model):   
    Product_Name=models.CharField(max_length=50)
    Product_Price=models.IntegerField()
    Product_Discount=models.IntegerField()
    Product_Description=models.CharField(max_length=150)
    Product_img=models.ImageField(upload_to='images')
    def str(self):
        return self.Product_Name   
class Product_details(models.Model): 
    Product_ID=models.ForeignKey(Product,on_delete=models.CASCADE)  
    Product_Name=models.CharField(max_length=50)
    Product_Price=models.IntegerField()
    Product_Discount=models.IntegerField()
    Product_Description=models.CharField(max_length=150)
    Product_img=models.ImageField(upload_to='images')
    def str(self):
        return self.Product_Name        

class Stock(models.Model):
    Purchase_Recieve_ID=models.ForeignKey(Purchase_Recieve,on_delete=models.CASCADE)
    Quantity_in_stock=models.IntegerField()
    Stock_Date=models.DateField()
    def str(self):
        return self.Quantity_in_stock

#------Sales---------
class Sale(models.Model):
    Product_ID=models.ForeignKey(Product,on_delete=models.CASCADE)
    Customer_ID=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Sale_Quantity=models.IntegerField()
    Sale_Bill=models.IntegerField()
    Sale_By_Employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    Sale_Date=models.DateField()

    def str(self):
        return self.Sale_Bill
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    def str(self):
        return self.name
class term_details(models.Model):
    term_para=models.CharField(max_length=150)
class Blog_details(models.Model):
    Blog_para=models.CharField(max_length=150)
    Blog_date=models.DateTimeField()
    Blog_img=models.ImageField(upload_to='image')






		


