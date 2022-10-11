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
        self.multi_cell(0,8,text,ln=1)
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




def Offer_letter_generator(header,name,ctc,role,validity_date,date,ref_date,basic,hra,variable_pay,varibale_pay_amt,special_allowance,lta,path):
    
    special_allowance_type='special allowance'

    ref=f'FNC/HR/{ref_date}'

    total=(basic+hra+varibale_pay_amt+special_allowance+lta)
    total=(total)
    pdf=PDF('P','mm','Letter')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True,margin=35)
    pdf.set_left_margin(25) 
    pdf.set_right_margin(25)

    pdf.set_font('times','',12)
    pdf.set_font("Times", size=12)
    pdf.set_font('Times','B',12)
    pdf.cell(0,8,'Letter of Offer',ln=1,align='C')
    pdf.ln(5)
    pdf.cell(0,6,ref)
    pdf.cell(0,6,date,ln=1,align='R')

    pdf.ln(5)
    pdf.set_font('Times','',12)


    body=f"""To,
{header}. {name},
Hyderabad.

Sub: Employment offer for the position of {role}

Dear {name},
We are pleased to offer you the position of {role} in Fournine Cloud Solutions Pvt. Ltd. based in Hyderabad.
We trust that your knowledge, skills, and experience will be among our most valuable assets. Asdiscussed and agreed with you, you will be eligible to receive the following beginning on your joining date:
The value of your Annualised Reference Salary will be Rs. {ctc} /- Details of the Reference Salary, Bonus, and Other Benefits are in the attached Salary breakup annexure. This offer letter is valid until {validity_date}. Please send a signed copy of this letter indicating your acceptance to join.
Your Appointment Letter will be issued on the date of joining. The joining formalities and induction will be carried out in our office.
Please submit the following documents to HR at the time of your joining: (1) Photocopies of your degree certificates, (2) Certifications, if any, (3) Experience/ relieving letters (4) two-colorpassport-size photos, (5) Latest salary slip from your previous organization and (6) Proof of address.

We look forward to welcoming you aboard.
Sincerely"""

    para=f"""Name: {name}
Position: {role}"""

    pdf.multi_cell(0,6,body,ln=1)
    pdf.bold_text_generator('For Fournine Cloud Solutions Pvt. Ltd.')
    y=pdf.get_y()
    pdf.image('static/images/hr_signature.png',30,y,40)

    pdf.ln(10)

    pdf.bold_text_generator('Usha Rani Inturi')
    pdf.bold_text_generator('HR Manager')

    #create your fpdf table ..passing also max_line_height!

    pdf.add_page()
    pdf.set_font('times','B',14)

    pdf.cell(0,10,'Salary Breakup in Indian Rupees',ln=1,align='C')

    pdf.ln(10)

    pdf.multi_cell(0,8,para,ln=1)

    pdf.ln(10)

    pdf.set_font('times','B',12)
    pdf.cell(70,8, f'Earnings', border=1,align="L")
    pdf.cell(30,8, f'Annual', border=1,align='l')
    pdf.ln(8)


    pdf.set_font('times','',10)

    pdf.cell(70,8, f'Basic', border=1,align="L")
    pdf.cell(30,8, f'{basic}', border=1,align='l')
    pdf.ln(8)

    if hra!=0:
        pdf.cell(70,8, f'HRA', border=1,align="L")
        pdf.cell(30,8, f'{hra}', border=1,align='l')
        pdf.ln(8)

    if varibale_pay_amt!=0:
        pdf.cell(70,8, f'variable pay({variable_pay})', border=1,align="L")
        pdf.cell(30,8, f'{varibale_pay_amt}', border=1,align='l')
        pdf.ln(8)

    if special_allowance!=0:
        pdf.cell(70,8, f'{special_allowance_type}', border=1,align="L")
        pdf.cell(30,8, f'{special_allowance}', border=1,align='l')
        pdf.ln(8)

    if lta!=0:
        pdf.cell(70,8, f'LTA', border=1,align="L")
        pdf.cell(30,8, f'{lta}', border=1,align='l')
        pdf.ln(8)

    pdf.set_font('times','B',12)

    pdf.cell(70,8, f'TOTAL GROSS VALUE',border=1,align="L")
    pdf.cell(30,8, f'{total}', border=1,align='l',ln=1)
    pdf.ln(8)

    pdf.set_font('times','B',10)
    pdf.cell(0,8,'Your salary is subject to Income tax as per the Income Tax act, 1961')
    pdf.ln(8)

    pdf.output(path)

