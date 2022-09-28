
from fpdf import FPDF

"""testing fpdf 1st crating object with argumenst P/L , length units, page format"""


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
        #print('bold text line executed')
        self.multi_cell(0,8,text,ln=1)
        self.set_font('times','',12)
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

    

"""testing fpdf 1st crating object with argumenst P/L , length units, page format"""


def apt_generator(header,date,name,role,ref_date,ctc_in_words,annual_ctc,reports_to,notice_period,path,join_date=''):
    st=f'REFNO:FNC/HR/{ref_date}'
    pdf=PDF('P','mm','Letter')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True,margin=40)
    pdf.set_left_margin(25) 

    pdf.set_right_margin(25)

    
    pdf.ln(6)
    pdf.set_font('times','B',14)
    pdf.cell(0,6,'Letter of Appointment',ln=1,align='c')
    pdf.ln(10)
    pdf.set_font('Times','B',12)
    pdf.cell(0,8,st)
    pdf.cell(0,8,date,ln=1,align='R')
    pdf.set_font('times','',12)
    para=f"""
To
{header}. {name},
Hyderabad
        
Subject: Appointment for the post of  {role}

Dear {name} ,

We are pleased to offer you the position of {role} with Fournine Cloud Solutions Pvt. Ltd. (the 'Company') on the following terms and conditions:
"""


    heading1='1.	Commencement of employment'

    para1=f"""Your employment will be effective, as of   {join_date}.
    """


    heading2='2.	Job title'
        
    para2=f"""job title will be {role}, and you will report to Mr/Ms.{reports_to}. 
    """


    heading3='3.	Salary'

    para3=f"""Your annual CTC is, {annual_ctc}/- ({ctc_in_words} rupees Only)
    """
        

    heading4='4.	Place of posting'

    para4=f"""You will be posted in Hyderabad, Telangana. You may, however, be required to work at any place of business which the Company has, or may later, acquire.
    """


    heading5='5.	Hours of Work'

    para5=f"""The normal working days are Monday through Friday or Five days a week based on the shifts, if any. You will be required to work for such hours as necessary for the proper discharge of your duties to the Company. The normal working hours are from 9 AM to 6 PM and you are expected to work not less than 40 hours each week, and if necessary for additional hours depending on your responsibilities.
    """


    heading6='6.	Leave/Holidays'

    para6=f"""    6.1 You are entitled to a casual leave of 12 days.
    6.2 You are entitled to 8 working days of paid sick leave.
   6.3 The Company shall notify a list of declared holidays at the beginning of each year.
        """


    heading7='7.	Nature of duties'

    para7=f"""You will perform to the best of your ability all the duties as are inherent in your post and such additional duties as the company may call upon you to perform, from time to time.
    """

    heading8='8.	Company property'

    para8=f"""You will always maintain in good condition Company property, which may be entrusted to you for official use during the course of your employment and shall return all such property to the Company prior to a relinquishment of your charge, failing which the cost of the same will be recovered from you by the Company.
    """


    heading9='9.	Borrowing/accepting gifts'
    
    para9=f"""You will not borrow or accept any money, gifts, reward, or compensation for your personal gains from or otherwise place yourself under pecuniary obligation to any person/client with whom you may be having official dealings.
    """

    heading10='10.	Termination'
    para10=f""" Your appointment can be terminated by the Company, without any reason, by giving you not less than {notice_period} months' prior notice in writing or salary in lieu thereof. For the purpose of this clause, salary shall mean the basic salary.

        You may terminate your employment with the Company, without any cause, by giving no less than {notice_period}s months' prior notice or salary for an unsaved period, left after adjustment of pending leaves, as on date.

        The Company reserves the right to terminate your employment summarily without any notice period or termination payment if it has reasonable ground to believe you are guilty of misconduct or negligence, or have committed any fundamental breach of contract or caused any loss to the Company.

        On the termination of your employment for whatever reason, you will return to the Company all property; documents, and paper, both original and copies thereof, including any samples, literature, contracts, records, lists, drawings, blue#prints, letters, notes, data and the like; and Confidential Information, in your possession or under your control relating to your employment or to clients' business affairs.
    """


    heading11='11.	Confidential Information'
    para11=f"""     During your employment with the Company, you will devote your whole time, attention, and skill to the best of your ability for its business. You shall not, directly or indirectly, engage or associate yourself with, be connected with, concerned, employed, or engaged in any other business or activities or any other post or work part-time or pursue any course of study whatsoever, without the prior permission of the Company.

        At no time, will you remove any Confidential Information from the office without permission.

        Your duty to safeguard and not disclose Confidential Information will survive the expiration or termination of this Agreement and/or your employment with the Company.
    
        Breach of the conditions of this clause will render you liable to summary dismissal under the clause above, in addition to any other remedy the Company may have against you in law.
        """
        

    heading12='12.	Notices'

    para12=f"""Notices may be given by you to the Company at its registered office address. Notices may be given by the Company to you at the address intimated by you in the official records.
    """


    heading13='13.	Applicability of Company Policy'

    para13=f"""The Company shall be entitled to make policy declarations from time to time pertaining to makers like leave entitlement, maternity leave, employees' benefits, working hours, transfer policies, etc., and may alter the same from time to time at its sole discretion. All such policy decisions of the Company shall be binding on you and shall override this Agreement to that extent.
    """


    heading14='14.	Governing Law/Jurisdiction'

    para14=f"""Your employment with the Company is subject to Indian laws. All disputes shall be subject to the jurisdiction of Hyderabad, Telangana only.
    """


    heading15='15.	Acceptance of our offer'

    para15=f"""Please confirm your acceptance of this Contract of Employment by signing and returning the duplicate copy.

    We welcome you and look forward to receiving your acceptance and to working with you.
Yours Sincerely,"""

    ##pdf.set_x(20)
    pdf.multi_cell(0,6,para,ln=1)
    pdf.bold_text_generator(heading1)
    pdf.multi_cell(0,6,para1,ln=1)
    pdf.bold_text_generator(heading2)
    pdf.multi_cell(0,6,para2,ln=1)
    pdf.bold_text_generator(heading3)
    pdf.multi_cell(0,6,para3,ln=1)
    #
    pdf.bold_text_generator(heading4)
    pdf.multi_cell(0,6,para4,ln=1)
    pdf.bold_text_generator(heading5)
    pdf.multi_cell(0,6,para5,ln=1,align='')

    pdf.bold_text_generator(heading6)
    pdf.multi_cell(0,6,para6,ln=1)

    pdf.bold_text_generator(heading7)
    pdf.multi_cell(0,6,para7,ln=1)

    pdf.bold_text_generator(heading8)
    pdf.multi_cell(0,6,para8,ln=1)
    #
    pdf.bold_text_generator(heading9)
    pdf.multi_cell(0,6,para9,ln=1)

    pdf.bold_text_generator(heading10)
    pdf.multi_cell(0,6,para10,ln=1)

    pdf.bold_text_generator(heading11)
    pdf.multi_cell(0,6,para11,ln=1)

    pdf.bold_text_generator(heading12)
    pdf.multi_cell(0,6,para12,ln=1)

    pdf.bold_text_generator(heading13)
    pdf.multi_cell(0,6,para13,ln=1)

    pdf.bold_text_generator(heading14)
    pdf.multi_cell(0,6,para14,ln=1)

    pdf.bold_text_generator(heading15)
    pdf.multi_cell(0,6,para15,ln=1)

    y=pdf.get_y()
    pdf.image('static/images/hr_signature.png',30,y,40)
    
    pdf.ln(10)
    pdf.bold_text_generator('Usha Rani Inturi')
    pdf.bold_text_generator('HR Manager')
    pdf.output(path)
   
    return path

