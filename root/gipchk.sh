#!/bin/bash

ssmtpPath="/usr/bin/"
gIP_file="/root/gipaddress.txt"
mailtxtPath="/root/mail.txt"
dstMail="tuno1000@gmail.com"

gIP=`${ssmtpPath}curl inet-ip.info`

function mailsend
{
	echo `date +%Y-%m-%d_%H:%M:%S` ${gIP} >> $mailtxtPath
	${ssmtpPath}mail -s "VPN-IPアドレス変更通知" $dstMail < $mailtxtPath
	echo $gIP > $gIP_file
}

if [ -f $gIP_file ]; then

	bsIP=`cat $gIP_file`
	
	echo $gIP
	echo $bsIP

	if [ ${gIP} != ${bsIP} ]; then
		echo "gIP:"${gIP} "bsIP:"${bsIP} >> $mailtxtPath
		mailsend
	fi
else
	echo $gIP > $gIP_file
	mailsend
fi
