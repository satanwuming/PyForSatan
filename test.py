from PyForSatan.Base.path import get_absolute_jiaoben,get_exec_path
from PyForSatan.Base.get_config import config
from PyForSatan.Base.get_yaml_config import get_yaml
from PyForSatan import logger
from PyForSatan.Email.respond import EmailResprond
from PyForSatan.Email.send import Email_Send
if __name__ == "__main__":
    # print(get_absolute_jiaoben())
    # print(get_exec_path())
    # print(config())
    # print(get_yaml().getdata())
    # logger.info("测试测试")
    # EmailResprond().addRecipient({"ceshi":"frank_yongjian@163.com","wenjian":"frank_yongjian@qq.com"})
    wenjian = EmailResprond().addRecipient(["ceshi@163.com","ceshi@163.com"]).addRecipient(" wenjian wenjian@163.com ").addRecipient({"wenjian":"ceshi@163.com"})
    Email_Send().send(wenjian)
