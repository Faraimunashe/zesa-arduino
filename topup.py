from paynow import Paynow
import time

class Topup:
    def pay_now(amount, phone, email):
        try:
            paynow = Paynow(
                "11336",
                "1f4b3900-70ee-4e4c-9df9-4a44490833b6",
                '127.0.0.1:5000/topup',
                '127.0.0.1:5000/topup'
            )

            payment = paynow.create_payment('Zesa', email)

            payment.add('zesa topup', amount)

            response = paynow.send_mobile(payment, phone, 'ecocash')

            timeout = 9
            count = 0

            if(response.success):

                while (True):
                    time.sleep(2)
                    pollUrl = response.poll_url
                    status = paynow.check_transaction_status(pollUrl)

                    if(status.paid):
                        return True
                    
                    count = count + 1
                    if (count > timeout):
                        return False
        except:
            return False

