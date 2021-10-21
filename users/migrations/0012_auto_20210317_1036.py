# Generated by Django 3.1.7 on 2021-03-17 10:36

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210226_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='https://dezvjosh-entry-webapp-storage.s3.eu-west-2.amazonaws.com/default.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCWV1LXdlc3QtMiJIMEYCIQCCRk2FLD%2FWkVCY5N6Wm1N5ZP2uFiKmr9x%2B9tK8fYRoSgIhAKbY%2FSJmqnkqN9hm1ywo73L4FQ%2BD0H%2BFM730H60rVQU7KvYCCCwQABoMMTcxODM5NTcyMjY0Igy5Ypgs4GsADbxJKToq0wLbRjZOBUtwiTVUOOJr0CGoV05%2Bcl8chRe4Vvf67lTqnkyW3%2F0d6K2hOEyON%2F9Fnuj225elHDf27lEL%2FDfYTDFXZsiGXJmkT9IY8cKfVVQ39rcqdLzzprUeKHPQMZNbVPzSAByrzyl%2Beg6FWbw%2FZmV30fjpht5uVWXeUQLfbi%2FjSimXlDT2W%2B2ZJHlrLmG6Ns3hm0RSa0vLtwWSqOG5kIGO4xDHq%2FEFnfDXqMtgS9wGLVOJksBqhrlqChyyxSCMIsFrld00cVjGXr0rzNMOpFcC7saOwGtrJTguqFyex%2BlM2xol9lLEPChw2IrxWd9sjR2xZVnrLBjKe%2BWPNpwCW15avIU%2Fn894Ql6%2FMUxaKKrvcGt%2B3sEPubx8jD57c3a7ekLDofNAH0y8%2F9Gb481o4Q%2BY22Ou8DgizjtlNOXg%2FeCGPx2tiAFiuS1d9F0Wx%2FooRv5Dbjcw1rDHggY6sgIr5NoJ7yoT8ZsEZ66x3LFxsl9j4tgZbQqoeD55txqKiK14BlsNX%2FB0L2xGNx%2B6sbZCfssc3Z4e%2BKnfeof%2BsnAUOcZdLH9nIaP3Bn8%2BHcpou%2BgtILVuRKrWWvERWCiUX9Ug3BdGHWiKwcMCkTxPsaFj9KYNabEAcq8xfR9zKxBekHaRftEwDNYiL2pzGHz0TDWtwsxlNJq%2BE%2Fl9OYuiY7rC4eJCfCzxEVje4pJlLSTaHMW2c6TZEv3cZm83iJI9V%2BtaVIC2C7p5x6dvKy9sPc%2BAFBi4yE9S77%2FwkBYV9%2BChsvr8XJqFq13fzsnIsYqlAHK9g9XcZjiauFHQBQNe7%2FOjD5dB%2FCxTbINxnap0YNK385DuCBpPOtV6j6dW%2F48jSLcVVRl0c8K%2FTxSaYNFmnKJLWvs%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210317T103401Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIASQATPZEUDM6OFV7F%2F20210317%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Signature=235421fd4e87c1b129d6e81463de767e5b68de169ca32c4acd2fbc14d626d61d', upload_to=users.models.uploadImg_to),
        ),
    ]