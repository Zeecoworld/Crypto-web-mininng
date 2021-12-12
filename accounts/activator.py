from django.core.exceptions import ValidationError
import re
from verify_email import verify_email




def validate_email(mail):  #work on this!!!!
   verified = verify_email(mail)
   if verified == False:
      raise ValidationError("Invalid email...")


   return mail