import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from PyForSatan.Base.get_yaml_config import get_yaml
from PyForSatan.Email.respond import EmailResprond

class Email_Send:

    __Resource__ = None

    def __init__(self):
        pass

    def close(self):
        pass

    def get_config(self,file_path=""):
        """

        :param file_path:
        :return:
        """
        return get_yaml().getdata()["email"]

    def SwitchToResource(self,config_name="defalut"):
        """

        :param config_name:
        :return:
        """
        config_data = self.get_config()
        if self.__Resource__ is not None:
            self.close()
        if config_data[config_name]["SSL"] == "true":
            server = smtplib.SMTP_SSL(config_data[config_name]["Server"], int(config_data[config_name]["Port"]))
        else:
            server = smtplib.SMTP(config_data[config_name]["Server"], int(config_data[config_name]["Port"]))
        server.login(config_data[config_name]["UserName"],config_data[config_name]["Password"])
        self.__Resource__ = server
        return self

    def send(self,Body:EmailResprond):
        if self.__Resource__ is None:
            self.SwitchToResource()
        #开始发送邮件
        


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__Resource__ is not None:
            self.close()


