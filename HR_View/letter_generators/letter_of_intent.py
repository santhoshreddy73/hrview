from fpdf import FPDF
class PDF(FPDF):
    def header(self):
        self.image('static/images/fnc logo.png',20,8,75)
        self.set_font('Arial','B',20)
        self.cell(10,8,'',ln=1)
        self.cell(10,8,'',ln=1)
        self.ln(7)

    def bold_text_generator(self,text):
        #self.set_x(20)
        #self.new_x=XPos.LMARGIN
        #self.new_y=YPos.NEXT
        x=self.get_x()
        y=self.get_y()
        #self.set_x(x)
        #print(x,y)
        self.set_font('Arial','B',11)
        #print('bold text line executed')
        self.multi_cell(0,11,text,ln=1)
        self.set_font('Arial','',11)
        #print('test font resetted')
        #self.set_x(20)
        return ' '

    def footer(self):
        self.set_y(-40)
        self.set_font('times','B',12)
        self.cell(0,6,'____________________________________________________________________',ln=1,align='C')
        self.ln(2)
        self.line(10,-40,280,-40)
        self.cell(0,6,'Fournine Cloud Solutions Pvt Ltd',ln=1,align='c')
        self.set_font('times','',10)
        self.cell(0,6,' CIN: U74999TG2016PTC112409',ln=1,align='C')
        self.cell(0,6,'#203, Inspire Infra Horizon, Nanakramguda, Hyderabad - 500089',ln=1,align='C')
        self.cell(0,6,'www.fourninecloud.com | contactus@fourninecloud.com | +91-80 4826 0856',ln=1,align='C')
        self.ln(20)

def intent_letter_generator(date,name,role_offered,temporary_Role,appointed_as,annual_Ctc,path):
    
    pdf=PDF('P','mm','Letter')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True,margin=35)
    pdf.set_left_margin(25) 
    pdf.set_right_margin(25)
    pdf.set_font('arial','B',12)
    pdf.cell(0,6,f'{date}',ln=1)
    pdf.cell(0,6,f'Dear {name}',ln=1)
    pdf.set_font('arial','',12)
    ##
    para=f"""
    
With reference to your application and the subsequent discussion(s) that we had, we are pleased to offer you {role_offered} with Fournine Cloud Solutions Private Limited (hereinafter referred to as "the Company or Fournine Cloud Solutions") subject to the below terms and condition. Please note that your subsequent employment with the Company is subject to your completing the training as given below.

Please note that this offer does not give you the employee status of the Company. Your appointment as Technical Graduate Trainee comes into effect only after completing the joining formalities with the Company and subject to the below Terms and Conditions. This communication does not confer you with any right against the company until you join for training.

You will be undergoing a training program anywhere in India and at the end of which, you will be evaluated. Company shall determine, as necessary, the period of training on the basis of your performance during the training period. Please note that the duration of the training period shall depend on our evaluation of your skill, project, domain, etc. during the evaluation tests conducted by the Company. The discretion with respect to determining the duration of training period shall vest solely with the Company. On your start date, please bring the documents as per Annexure A.

Please note that the offer of appointment and continuation of employment thereof is subject to successful completion of your:
a)	Background Verification
b)	Induction training on joining the Company with a minimum score of 65% in the final evaluation on completion of the training.

On successful completion of your training, you will be appointed as a {appointed_as} and will be on probation for an initial period of 6 months."""
    
    para_addon=f"""
Your total compensation inclusive of all benefits will be Rs. {annual_Ctc}/- on confirmation and the same will be subject to a deduction of tax at source in accordance with the prevailing laws. The retirement age is 62 years. This contract of employment can be terminated by either party by giving a notice period 60 days for employees who have been confirmed in your Salary Grade. Either party is not bound to give any reasons thereof. Any retention Bonus if applicable will be detailed in your letter of employment and will be subject to the terms and conditions of your letter of employment.

A formal letter communicating your location (anywhere in India and can include Company's affiliate offices across India) and date of joining will be sent to you at a later period. We will endeavour to give you adequate notice so that you can make necessary arrangements and travel plan. At the time of joining, you are requested to submit the documents as per Annexure A. You shall be on the rolls of company's establishment at Hyderabad and this offer shall be subject to jurisdiction of Hyderabad, Telangana. This is an offer of appointment. On your acceptance, a detailed formal letter of appointment will be issued to you at the time of joining."""

    heading1='Annexure A'

    para1=f"""
At the time of joining, you are requested to bring the following documents in Original, along with two copies of each. The original certificates are required for verification only and will be returned the same day.
1.	Certificates & mark sheets supporting your educational qualifications:
    a.	Xth Certificate and mark sheet
    b.	XIIth Certificate and mark sheet
  c.	Degree Certificate/Provisional Certificate and individual semester mark sheets, Consolidated     

2.	Three copies of your recent Passport size colour photograph (white background)
For any further clarification, you can mail to hr@fourninecloud.com
If any declaration given or furnished by you to the company proves to be false or if you are found to have wilfully suppressed any material information, in such a case, you will be liable to be removed from the service without any notice.
Yours sincerely,"""


    para2=f"""
We request you to please read and sign the enclosed copy of this letter and return it to indicate your acceptance of this offer. I agree & accept employment on the terms and conditions mentioned

Name:         
    """
    heading2="""DECLARATION"""

    para3=f"""
I,	________________________________________  (Name of the Candidate) S/O, D/O,W/O	,________________________________________  having permanent address at __________________________________________________________ do hereby acknowledge, represent and confirm to Fournine Cloud Solutions Private Limited, (hereinafter referred to as "the Company"), which expression shall unless it be repugnant to the context or meaning thereof, deemed to mean and include its successors, affiliates, sister concerns and assigns) that my offer will be subject to:
1.	My willingness to relocate to any of the locations of the Company. I agree that the Company reserves the right to depute / transfer my services to any other location/ centres of the Company/ client location/ Group Company in consistence with the Company's business/ project requirement and interests. In case I fail to accept such deputation or transfer, the Company at its sole discretion reserves the right to initiate appropriate actions in accordance with the Company policy.

2.	My willingness to work in any of the shifts (i.e. either day or night shifts). I agree that the Company reserves the right to depute me to work in any of the shifts in consistence with the Company's business/ project requirement and interests. In case I refuse to work in any of the shifts as required by the Company, the Company at its sole discretion reserves the right to initiate appropriate actions in accordance with the Company policy.

3.	My willingness to work in any kind of technology project. I agree that the Company reserves the right to depute me to work on any kind of technology/ projects in consistence with the Company's business/ project requirement and interests. In case I refuse to work on any kind of technology/ projects as required by the Company, the Company at its sole discretion reserves the right to initiate appropriate actions in accordance with the Company policy.

I, do hereby verify and declare that the contents of this declaration are true and correct and given with my free will and consent, no part of it is false, and nothing material has been concealed therein, and I am solely responsible for its accuracy and know of no agreements, obligations or restrictions which prevent or prohibit me from complying with them.

Name:  
    """

    pdf.multi_cell(0,6,para,ln=1)

    
    pdf.add_page()
    pdf.multi_cell(0,6,para_addon,ln=1)
    pdf.add_page()
    pdf.set_font('arial','B',12)
    pdf.cell(0,6,heading1,ln=1,align='C')
    pdf.set_font('arial','',12)

    pdf.multi_cell(0,6,para1,ln=1)
    pdf.bold_text_generator('FOR FOURNINE CLOUD SOLUTIONS PRIVATE LIMITED')
    y=pdf.get_y()

    pdf.image('static/images/hr_signature.png',30,y+2,40)
    pdf.ln(15)
   
    pdf.bold_text_generator('Usha Rani Inturi')

    pdf.bold_text_generator('Director - HR ')
    y=pdf.get_y()
    pdf.line(25,y,190,y)
    pdf.set_font('arial','',12)
    pdf.multi_cell(0,6,para2,ln=1)
    pdf.cell(0,6,'Date:')
    pdf.cell(0,6,'Sign:_____________________________',ln=1,align='R')


    pdf.add_page()

    pdf.set_font('arial','B',12)
    pdf.cell(0,8,heading2,ln=1,align='C')

    pdf.set_font('arial','',12)

    pdf.multi_cell(0,5,para3,ln=1)

    pdf.cell(0,6,'Date:   ')
    pdf.cell(0,6,'Sign:_____________________________  ',ln=1,align='R')
    pdf.output(path)
    #print('working ')