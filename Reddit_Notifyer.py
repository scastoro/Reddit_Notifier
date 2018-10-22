import praw
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(body, email_subject):
    pwd = ''
    msg = MIMEMultipart()
    msg['From'] = ''
    msg['To'] = ''
    msg['Subject'] = email_subject
    msg.attach(MIMEText(body))
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(msg['From'], pwd)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.close()
    print('Sent E-mail!')

def game_title(submission_title):
    game_list = ['god of war', 'far cry']
    for name in game_list:
        if name in submission_title:
            return True
    return False

def stream_submissions():
    try:
        reddit = praw.Reddit(client_id = ,
                            client_secret = ,
                            username = ,
                            password = ,
                            user_agent = 'test',)
        subreddit = reddit.subreddit('GameDeals')
    except Exception as e:
        print(str(e))    

    for submission in subreddit.stream.submissions():
        try:
            if game_title(submission.title.lower()):
                body = submission.url + '\n' + '\n' + 'https://www.reddit.com' + submission.permalink
                subject = submission.title
                send_email(body, subject)
            else:
                pass

        except Exception as e:
            print(str(e))

def main():
    stream_submissions()

if __name__ == "__main__":
    main()