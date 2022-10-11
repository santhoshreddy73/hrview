
from fpdf import FPDF
import PyPDF2 as p
"""testing fpdf 1st crating object with argumenst P/L , length units, page format"""\


class PDF(FPDF):
    def header(self):
        self.image('static/images/fnc logo.png',20,8,75)
        self.set_font('times','B',20)
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
        self.set_font('times','B',12)
        self.multi_cell(0,10,text,ln=1)
        self.set_font('times','',13)
       
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

def termination_letter_generator(header,date,role,name,ref_date,join_date,termination_date,path):

    pdf=PDF('P','mm','Letter')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True,margin=40)

    pdf.set_left_margin(25) 
    pdf.set_right_margin(25)

    pdf.set_font('times','BU',13)
    pdf.cell(0,14,'Letter of Service',align='C',ln=1)
    ref=f'REF NO:FNC/HR/{ref_date}'
    pdf.set_font('Times','B',12)
    pdf.cell(0,8,ref)
    pdf.cell(0,8,date,ln=1,align='R')

    para=f"""
To,
{header}. {name}
Hyderabad.

Sub: Letter of service as {role}

Dear {name}

This is to certify {name} that has associated with our organization as a 
{role} from {join_date} to {termination_date}.

Fournine cloud solutions wish him success in his career ahead.

Sincerely,"""
    ender1="""
Fournine Cloud Solutions Pvt. Ltd."""
    
    pdf.set_font('times','',13)
    pdf.multi_cell(0,7,para,ln=1)
    pdf.set_font('times','B',13)
    pdf.multi_cell(0,7,ender1,ln=1)
    y=pdf.get_y()
    pdf.image('static/images/hr_signature.png',30,y,40)
    pdf.ln(15)
    pdf.bold_text_generator('Usha Rani Inturi')
    pdf.bold_text_generator('HR Manager')
    pdf.output(path)
    #print('worked')
    
