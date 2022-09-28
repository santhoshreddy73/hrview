from fpdf import FPDF

def service_agreement_generator(employee_duration,employee_duration_in_words,penaulty_amount,penaulty_in_words,training_duration,path):
    pdf=FPDF('P','mm','A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True,margin=30)

    pdf.image('static/images/judicial_logo.png',23,30,165)
    pdf.set_left_margin(20) 
    pdf.set_right_margin(20)
    pdf.set_xy(25,150)
    pdf.set_font('Arial','',11)

    page1="""THIS AGREEMENT made at Hyderabad on _____________ Between FOURNINE CLOUD SOLUTIONS PVT LTD, and ___________________










    """
    #in all letters i given content out of identation in order to produce alignment of the content in the generator letters
    page2=f"""
a company incorporated under the companies act 1956 (hereinafter referred to as"FOURNINE") and having its corporate office at B-9, 3002, My Home Avatar, Narsingi,Rangareddy Telangana - 500089 of the first part and _________________ S/o D/o W/o ____________________ aged _____ years, Occupation _________________, an Indian nationality residing at _________________________________________________ and having permanent address at _________________________________________________(hereinafter referred to as 'Mr./Ms. _______________________________') of the second part AND ________________________(hereinafter referred to as 'The Surety') which expression shall be deemed to include his/her executor, heir and administrator of the third part

Whereas FOURNINE is involved in the business of problem-solving or consultancy and as of present and the foreseeable future specifically in the business of computer and management consultancy - offering services and products in India and abroad. 

Whereas, the possessionof the above problem-solving techniques and effective use of high technologies equipmentca be acquired mainly through special training and or specific on the job training ("Training")

Whereas the said training is of a duration of {training_duration} months and is liable to be extended by afurther duration based on performance of Mr. /Ms _________________ during the training,of which FOURNINE shall be the sole judge.

Whereas the above-mentioned training involves considerable expenditure - both direct and indirect, financial and unliquidated - related to faculty, computer time, support facilities,salary of Mr./ Ms. __________________ while under training

Whereas this training substantially improves the professional standing of Mr./Ms._______________, and it has been imparted by FOURNINE at considerableexpenditure as an investment, Fournine expects a commitment (elaborated below) from theemployee to recover its expenditure or seek a penalty for non-fulfilment of the same

Whereas the expenditure involved in imparting the said Training to Mr. /Ms. _________________ is several times in excess of the penalty demanded from him/her.

IT IS NOW HEREBY AGREED AS UNDER:
1. In consideration of the training to be imparted by FOURNINE, Mr./Ms.________________________ undertakes irrevocably to serve FOURNINE or any of itsassociated or affiliated companies to which he/she may be transferred for a minimum periodof {employee_duration}({employee_duration_in_words})  years (excluding Leave without pay period, Training Period and/or unauthorisedabsence, if any) from the date of joining FOURNINE.

    """
    page3=f"""
2. Mr. /Ms. __________________ is giving this undertaking in view of the considerable expenditure incurred by FOURNINE on him/her
3. Mr./Ms. __________________ agrees not to take employment with any other person, firm or company during the period of applicability of this agreement.
4. By way of guarantee for due performance of all terms and conditions contained in this agreement, Mr./Ms. _________________ provide herein below the name of his/her near relative/person in order of preference and who have consented by signing herein below to stand as surety on his/her behalf to ensure compliance of the aforesaid covenant, and that in the event of failure/neglect by Mr./Ms __________________ to fulfil any of the terms of this undertaking of which FOURNINE shall be the sole judge the surety shall be liable to pay FOURNINE Rs.{penaulty_amount } ({penaulty_in_words }) as compensation with interest thereon applicable and the surety hereby agree, confirm and accept that the surety shall be liable jointly and severally with Mr./Ms.__________________ to pay the same as FOURNINE
Name, Address, Occupation (Of the Surety)
_______________________________________
______________________________________________________________________
______________________________________________________________________
______________________________________________________________________

5. In the event of any dispute or disagreement over the interpretation of any of the terms hereinabove contained or any claim of liability of any part including the surety the same shall be referred to a person to be nominated by FOURNINE whose decision shall be final and binding upon the parties hereto. Such reference shall be deemed to a submission to arbitration under The Arbitration and Conciliation Act, 1996 or of any modification or re-enactment thereof. The venue of arbitration shall be Hyderabad.
6. During the period of 2(TWO) years (excluding Leave without Pay period, Training Period and/or unauthorised absence, If any) from the date of joining, if Mr./Ms.  ____________________ leaves/resigns/abandons of the services or violates the terms of agreement, Mr./Ms________________________ will have to pay liquidated damages amounting to Rs. {penaulty_amount } ({penaulty_in_words }) and give Three calendar months written notice or salary in lieu thereof. Mr./Ms. _____________________________ agrees that the said amount of Rs.{penaulty_amount }/- can be recovered/adjusted by FOURNINE from the legal dues, if any, payable to him. On being absorbed as an Employee of FOURNINE, after completion of the said Training period, FOURNINE would be entitled to terminate the
services of the Employee with Three Calendar Months' written notice during the tenure of service agreement"""
    
    page4=f"""
The provisions stated herein for breach by Mr./Ms. ________________________ of the provisions of this agreement shall be without prejudice to other remedies available to FOURNINE.

ADDRESS FOR THE PURPOSE OF SERVICE:
All communications between Mr./Ms. ____________________________ or FOURNINE and Surety shall be deemed to have effectively served if addressed to the following address:
FOURNINE (FOURNINE CLOUD SOLUTIONS PVT LTD) at:
#203, Inspire Infra Horizon, Nanakramguda, Hyderabad - 500089.
(Dr./Mr./Miss/Mrs.)_______________________________________________________

(At)._________________________________________________________________________________________________________________________________________

Surety(Dr./Mr./Miss/Mrs.)30._______________________________________________

(At)_________________________________________________________________________________________________________________________________

Any change in the above addresses of any of the concerned parties i.e. FOURNINE, Mr./Ms._________________________________ or Surety, shall be intimated to the other parties by the party whose address has changed within a period of seven days of such change. If no such change has been intimated or received, the addresses mentioned above shall be deemed to be the addresses of the concerned parties.
As a token of his/her consent, he/she has signed this agreement as surety :) Dated this:___________________
Signed and delivered by Mr./Ms:._____________________________
Accepted for and behalf Of FOURNINE CLOUD SOLUTIONS PVT LTD ( By their constituted Attorney )"""
    page5=f"""
This is to certify that I, ___________________________________________________
(Name of the Surety) am standing surety for
_______________________________________ (Name of the Employee) who is my
____________________________ (Relationship). Mr. /Ms.
______________________________________________ (Name of the Employee) has
joined FOURNINE CLOUD SOLUTIONS PVT LTD. On __________________ (Employee's
date of joining) and executed an agreement on ___________________________________
(Candidate's date of joining). In the event that Mr./Ms.
________________________________________ (Name of the Employee) does not fulfill
the terms of the agreement, I stand guarantee and will be liable to the liquidated damages of
Rs.{penaulty_amount }/-. My permanent address is as follows:
Name (of the Surety): ________________________________________________________
Address (of the Surety):
_________________________________________________________________________
_________________________________________________________________________
Phone (of the surety):
_______________________________ (With country and area code)

(Signature of the Surety)

(Signature verification by competent authority)

Name:
Designation:
Date:
Place:
"""
    pdf.multi_cell(0,6,page1,ln=1)
    pdf.cell(0,6,'Signature of the Employee')
    pdf.cell(0,6,'Signature of the Surety',ln=1,align='R')
    pdf.add_page()
    pdf.multi_cell(0,5,page2,ln=1)
    pdf.ln(20)
    pdf.cell(0,6,'Signature of the Employee')
    pdf.cell(0,6,'Signature of the Surety',ln=1,align='R')
    pdf.add_page()
    pdf.multi_cell(0,6,page3,ln=1)
    pdf.ln(20)
    pdf.cell(0,6,'Signature of the Employee')
    pdf.cell(0,6,'Signature of the Surety',ln=1,align='R')
    pdf.add_page()
    pdf.multi_cell(0,6,page4,ln=1)
    pdf.ln(20)
    pdf.cell(0,6,'Signature of the Employee')
    pdf.cell(0,6,'Signature of the Surety',ln=1,align='R')
    pdf.add_page()
    pdf.set_y(20)
    pdf.set_font('Arial','B',11)
    pdf.cell(0,6,'Surety Verification',ln=1,align='C')
    pdf.set_font('Arial','',11)
    pdf.multi_cell(0,8,page5,ln=1)

    pdf.output(path)