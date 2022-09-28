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

def hike_generator(header,daTe,increment_effective_date,name,ref_date,increment_in_words,duration,path):
    
    ref=f'REF NO:FNC/HR/{ref_date}'

    pdf=PDF('P','mm','Letter')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True,margin=35)
    pdf.set_left_margin(25) 
    pdf.set_right_margin(25)
    pdf.set_font('Times','B',14)

    pdf.cell(0,8,'Letter of Increment',ln=1,align='C')
    pdf.ln(5)
    pdf.set_font('Times','B',12)
    pdf.cell(0,6,ref)
    pdf.cell(0,6,daTe,ln=1,align='R')

    pdf.set_font('Times','',12)

    para=f"""
To,
{header}. {name}
Hyderabad

Sub: Increment Letter for FY {duration}

Dear {name} ,
We congratulate you for your hard work, enthusiasm, dedication and continuous effort in meeting the organisation objective. On reviewing your performance, we are glad to announce an increment of Rs. {increment_in_words} (Rs. In words) on your existing salary with effect from {increment_effective_date}

We expect you to keep up your performance in the years to come and grow with the organisation.
Sincerely,"""

    pdf.multi_cell(0,8,para,ln=1)
    pdf.bold_text_generator('For Fournine Cloud Solutions Pvt. Ltd.')
    y=pdf.get_y()
    pdf.image('static/images/hr_signature.png',30,y,40)
    pdf.ln(10)
    pdf.bold_text_generator('Usha Rani Inturi')
    pdf.bold_text_generator('HR Manager')

    pdf.output(path)

    #print('letter created........................>>>>>>>>>>>>>>>>>.')
