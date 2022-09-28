from fpdf import FPDF
class PDF(FPDF):
    def header(self):
        self.image('static/images/fnc logo.png',20,8,75)
        self.set_font('arial','B',20)
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
        self.set_font('arial','B',11)
        self.multi_cell(0,11,text,ln=1)
        self.set_font('Arial','',11)
        #print('test font resetted')
        #self.set_x(20)
        return ' '

    def footer(self):
        self.set_y(-40)
        self.set_font('arial','B',12)
        self.cell(0,6,'____________________________________________________________________',ln=1,align='C')
        self.line(10,-40,280,-40)
        self.cell(0,6,'Fournine Cloud Solutions Pvt Ltd',ln=1,align='c')
        self.set_font('arial','',11)
        self.cell(0,6,' CIN: U74999TG2016PTC112409',ln=1,align='C')
        self.cell(0,6,'#203, Inspire Infra Horizon, Nanakramguda, Hyderabad - 500089',ln=1,align='C')
        self.cell(0,6,'www.fourninecloud.com | contactus@fourninecloud.com | +91-80 4826 0856',ln=1,align='C')

def issue_internship_certificate(name,id,role,date,end_date,start_date,ref_date,path):
    pdf=PDF('P','mm','Letter')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True,margin=35)
    pdf.set_left_margin(25) 
    pdf.set_right_margin(25)
    pdf.set_font('arial','B',14)
    pdf.cell(0,8,'CERTICATE OF INTERNSHIP',ln=1,align='C')
    ref=f'REF NO:FNC/HR/{ref_date}'
    pdf.ln(10)
    pdf.set_font('arial','B',12)
    pdf.cell(0,6,ref)
    pdf.cell(0,6,date,ln=1,align='R')
    pdf.set_font('arial','',12)

    pdf.ln(7)

    para=f"""
Name: {name}
Intern ID: {id}
Designation: {role}

This is to certify that {name}  has successfully completed Internship in {role} with us from {start_date} to {end_date} During her internship period, her contributions to the organization are highly appreciated.

We wish her all the best for her future endeavors.

Yours Sincerely"""
    pdf.multi_cell(0,8,para,ln=1)

    y=pdf.get_y()
    pdf.image('static/images/hr_signature.png',30,y,40)
    pdf.ln(7)
    pdf.bold_text_generator('Usha Rani Inturi')
    pdf.bold_text_generator('HR Manager')
    pdf.output(path)

