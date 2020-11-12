import os
import subprocess as sb
from yattag import Doc,indent
os.system('clear')

def aws():
	while True:
		print("""
		press 1 : to config aws
		press 2 : to create key pair
		press 3 : to create sg 
		press 4 : create ec2 instances
		press 5 : create ebs
		press 6 : Display Key-Pair
		press 7 : Display Security-group
		press 8 : Exit the program
		Press 9 : Back to Main Menu
	""")
		aws=input("Select your choice :- ")
		if int(aws)==1:
			os.system("aws configure")
		elif int(aws)==2:
			k=input("Enter key name - ")
			os.system("aws ec2 create-key-pair --key-name {} ".format(k))
		elif int(aws)==3:
			k=input("security group name - ")
			d=input("Enter discription name - ")
			os.system("aws ec2 create-security-group --group-name {} --description {} ".format(k,d))
		elif int(aws)==4:
			print("""
					1. Amazon Linux 2 AMI
					2.Redhat 8
					3.Ubuntu 
					""")
			c=input("choose os name - ")
			if int(c)==1:
				count=input("Enter your count -")
				key=input("Enter your key name- ")
				sg=input("Enter your security group name - ")
				os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --count {} --key-name {} --subnet-id subnet-fc7b7294 --security-group-ids {}".format(count,key,sg))
		
			elif int(c)==2:
			
				count=input("Enter your count -")
				key=input("Enter your key name- ")
				sg=input("Enter your security group name - ")
				os.system("aws ec2 run-instances --image-id ami-052c08d70def0ac62 --instance-type t2.micro --count {} --key-name {} --subnet-id subnet-fc7b7294 --security-group-ids {}".format(count,key,sg))
		
			elif int(c)==3:
			
				count=input("Enter your count -")
				key=input("Enter your key name- ")
				sg=input("Enter your security group name - ")
				os.system("aws ec2 run-instances --image-id ami-0a4a70bd98c6d6441 --instance-type t2.micro --count {} --key-name {} --subnet-id subnet-fc7b7294 --security-group-ids {}".format(count,key,sg))

			else:
				print("You have entered wrong keyword")

		elif int(aws)== 5:
			print("""
			1.ap-south-1a
			2.ap-south-1b
			3.ap-south-1c
			""")
			a=input("Enter Availability zone - ")
			if int(a)==1:
				os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1a")
		
			elif int(a)==2:
				os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1b")
		
			elif int(a)==3:
				os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1c")
			else:
				print("You have entered wrong keyword")

		elif int(aws)==6:
			key_pair=os.system("aws ec2 describe-key-pairs")
			print(key_pair)

		elif int(aws)==7:
			sec_group=os.system("aws ec2 describe-security-groups")
			print(sec_group)
		elif int(aws)== 8:
			exit()
		elif int(aws)== 9:
			break
		else:
			print("You have entered wrong keyword")

def Hadoop_Cluster():
	import os
	while True:
		print("""
			Press 1 : Is Hadoop is install or not
			Press 2 : Install Hadoop
			Press 3 : Create DataNode
			Press 4 : Create NameNode 
			""")
		hadoop=input("Select your choice:-")
		if int(hadoop)==1:
			os.system("rpm -q hadoop")
		elif int(hadoop)==2:
			print("Under working.....")
		elif int(hadoop)==3:
			directoryname=input("Give directory name:- ")
			os.system("mkdir /{}".format(directoryname))
			os.system("rm -f /etc/hadoop/core-site.xml")
			os.system("rm -f /etc/hadoop/hdfs-site.xml")
			print("Your Hadoop directory is created.")
			ip_address=input("Enter Master IP Address :- ")
			os.system("cd /etc/hadoop")
			doc,tag,text=Doc().tagtext()
			with tag('configuration'):
				with tag('property'):
					with tag('name'):
						text('dfs.data.dir')
					with tag('value'):
						text('/{}'.format(directoryname))
			result=indent(doc.getvalue(),indentation =' '*4,newline='\r\n')
			f=open('/etc/hadoop/hdfs-site.xml','a')
			f.write('{}\n'.format(result))
			f.close()
			print("Successfully DataNode Configured")
			doc1,tag1,text1=Doc().tagtext()
			with tag1('configuration'):
				with tag1('property'):
					with tag1('name'):
						text1('fs.default.name')
					with tag1('value'):
						text1('hdfs://{}'.format(ip_address)+':9001')
			res=indent(doc1.getvalue(),indentation =' '*4,newline='\r\n')
			f=open('/etc/hadoop/core-site.xml','a')
			f.write('{}\n'.format(res))
			f.close()
			os.system("hadoop-daemon.sh start datanode")
            os.system("jps")
			os.system('tput setaf  2')
			print('Setup Complete')


while True :
	print(""" 
		Press 1 : Configure AWS
		Press 2 : Configure Hadoop-Cluster
		Press 3 : Configure YUM
		Press 4 : Configure Docker
		Press 5 : Configure Jenkins
		Press 6 : Configure Ansible
		Press 7 : Run Linux Command
		Press 8 : Exit the Program
		""")

	configure=input("Select your choice :- ")
	if int(configure)==1:
		aws()
	if int(configure)==2:
		Hadoop_Cluster()
			