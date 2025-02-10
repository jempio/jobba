"""
This file contains the main constants used in the application.
"""

from datetime import datetime, timedelta


GENERIC_ATS_DOMAINS = [
    "us.greenhouse-mail.io",
    "smartrecruiters.com",
    "linkedin.com",
    "ashbyhq.com",
    "hire.lever.co",
    "hi.wellfound.com",
    "talent.icims.com",
    "myworkday.com",
    "otta.com",
]

DEFAULT_DAYS_AGO = 365 * 2
# Get the current date
current_date = datetime.now()

# Subtract 30 days
date_days_ago = current_date - timedelta(days=DEFAULT_DAYS_AGO)

# Format the date in the required format (YYYY/MM/DD)
formatted_date = date_days_ago.strftime("%Y/%m/%d")

QUERY_APPLIED_EMAIL_FILTER = (
    '(subject:"thank" AND from:"no-reply@ashbyhq.com") OR '
    '(subject:"thank" AND from:"careers@") OR '
    '(subject:"thank" AND from:"no-reply@greenhouse.io") OR '
    '(subject:"application was sent" AND from:"jobs-noreply@linkedin.com") OR '
    'from:"notification@smartrecruiters.com" OR '
    'subject:"application received" OR '
    'subject:"received your application" OR '
    'subject:"your application to" OR '
    'subject:"applied to" OR '
    'subject:"your application was sent to" OR '
    'subject:"thank you for your submission" OR '
    'subject:"thank you for applying" OR '
    'subject:"thanks for applying to" OR '
    'subject:"confirmation of your application" OR '
    'subject:"your recent job application" OR '
    'subject:"successfully submitted" OR '
    'subject:"application received" OR '
    'subject:"application submitted" OR '
    'subject:"we received your application" OR '
    'subject:"thank you for your submission" OR '
    'subject:"thank you for your interest" OR '
    'subject:"thanks for your interest" OR '
    'subject:"thank you for your application" OR '
    'subject:"thank you from" OR '
    'subject:"application has been submitted" OR '
    '(subject:"application to" AND subject:"successfully submitted") OR '
    '(subject:"your application to" AND subject:"has been received") OR '
    '(subject:"your application for" AND -subject:"update") OR '
    'subject:"your job application has been received" OR '
    'subject:"thanks for your application" OR '
    'subject:"job application confirmation" OR '
    'subject:"ve been referred" OR '
    '(subject:"we received your" AND subject:"application") '
    '-subject:"watering"'
    f"after:{formatted_date}"
)  # label:jobs -label:query4
