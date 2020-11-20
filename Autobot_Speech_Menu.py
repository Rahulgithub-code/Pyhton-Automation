import os
import subprocess as sb
from yattag import Doc,indent
import time
import pyttsx3 as pyt
import speech_recognition as sr
r = sr.Recognizer()
os.system('clear')

def aws():
	while True:
		pyt.speak("Welcome to A W S Console")
		print("""
		1 : Configure Amazon Web Service 
		""",end = '')
		time.sleep(0.2)
		print("""
		2 : Create key pair
		""",end = '')
		time.sleep(0.2)
		print("""
		3 : Create security group
		""",end = '') 
		time.sleep(0.2)
		print("""
		4 : Create ec2 instances
		""",end = '')
		time.sleep(0.2)
		print("""
		5 : Create ebs 
		""",end = '')
		time.sleep(0.2)
		print("""
		6 : Display Key-Pair
		""",end = '')
		time.sleep(0.2)
		print("""
		7 : Display Security-group
		""",end = '')
		time.sleep(0.2)
		print("""
		8 : Exit the program
		""",end = '')
		time.sleep(0.2)
		print("""
		9 : Back to Main Menu
		""")
		time.sleep(0.2)
		with sr.Microphone() as source:
			pyt.speak("What Can I help you ?")
			audio=r.listen(source)
			pyt.speak("Proceed.")
		aws1=r.recognize_google(audio)
		aws=aws1.lower()
		print(aws)
		if ("configure" in aws) and ("amazon" in aws):
			os.system("aws configure")
			pyt.speak("Successfully A W S Configured")
		elif ("create" in aws) and ("key" in aws):
			pyt.speak("Tell me name of key pair")
			with sr.Microphone() as source_key_pair:
				pyt.speak("What Can I help you ?")
				source_key_pair_audio=r.listen(source_key_pair)
				pyt.speak("got it.")
			k=r.recognize_google(source_key_pair_audio)
			os.system("aws ec2 create-key-pair --key-name {} ".format(k))
			pyt.speak("Successfully key pair created")
		elif ("create" in aws) and ("security" in aws):
			pyt.speak("Tell me name of security group")
			with sr.Microphone() as source_security_grp:
				source_security_grp_audio=r.listen(source_security_grp)
				pyt.speak("go it.")
			k=r.recognize_google(source_security_grp_audio)
			pyt.speak("Tell me discription of security group")
			with sr.Microphone() as source_security_dis:
				source_security_dis_audio=r.listen(source_security_dis)
				pyt.speak("go it.")
			d=r.recognize_google(source_security_dis_audio)
			os.system("aws ec2 create-security-group --group-name {} --description {} ".format(k,d))
		elif ("create" in aws) and ("instance" in aws):
			print("""
					1. Amazon Linux 2 AMI
					2.Redhat 8
					3.Ubuntu 
					""")
			pyt.speak("choose os name")
			c=input("choose os name - ")
			if int(c)==1:
				pyt.speak("Enter your count")
				count=input("Enter your count -")
				pyt.speak("Enter your key name")
				key=input("Enter your key name- ")
				pyt.speak("Enter security group name")
				sg=input("Enter your security group name - ")
				os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --count {} --key-name {} --subnet-id subnet-fc7b7294 --security-group-ids {}".format(count,key,sg))
				pyt.speak("Successfully instance created")
		
			elif int(c)==2:
			
				pyt.speak("Enter your count")
				count=input("Enter your count -")
				pyt.speak("Enter your key name")
				key=input("Enter your key name- ")
				pyt.speak("Enter security group name")
				sg=input("Enter your security group name - ")
				os.system("aws ec2 run-instances --image-id ami-052c08d70def0ac62 --instance-type t2.micro --count {} --key-name {} --subnet-id subnet-fc7b7294 --security-group-ids {}".format(count,key,sg))
				pyt.speak("Successfully instance created")
		
			elif int(c)==3:
			
				pyt.speak("Enter your count")
				count=input("Enter your count -")
				pyt.speak("Enter your key name")
				key=input("Enter your key name- ")
				pyt.speak("Enter security group name")
				sg=input("Enter your security group name - ")
				os.system("aws ec2 run-instances --image-id ami-0a4a70bd98c6d6441 --instance-type t2.micro --count {} --key-name {} --subnet-id subnet-fc7b7294 --security-group-ids {}".format(count,key,sg))
				pyt.speak("Successfully instance created")

			else:
				pyt.speak("You have entered wrong keyword")
				print("You have entered wrong keyword")


		elif ("create" in aws) and ("ebs" in aws):
			print("""
			1. ap-south-1a
			2. ap-south-1b
			3. ap-south-1c
			""")
			pyt.speak("choose Availability zone")
			a=input("Choose Availability zone - ")
			if int(a)==1:
				os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1a")
		
			elif int(a)==2:
				os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1b")
		
			elif int(a)==3:
				os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1c")
			else:
				pyt.speak("You have entered wrong keyword")
				print("You have entered wrong keyword")

		elif ("Display" in aws) and ("key" in aws):
			key_pair=os.system("aws ec2 describe-key-pairs")
			print(key_pair)

		elif ("Display" in aws) and ("security" in aws):
			sec_group=os.system("aws ec2 describe-security-groups")
			print(sec_group)
		elif ("exit" in aws) and ("program" in aws):
			pyt.speak("Thanks for using AWS Console")
			os.system("figlet Thanks for using AWS Console.")
			exit()
		elif ("main" in aws) and ("menu" in aws):
			break
		else:
			os.system("tput setaf 1")
			pyt.speak("You have entered wrong keyword")
			print("You have entered wrong keyword")
			os.system("tput sgr0")

def Hadoop_Cluster():
	import os
	while True:
		print("""
			Press 1 : Is Hadoop is install or not
			""",end = '')
		time.sleep(0.2)
		print("""
			Press 2 : Install Hadoop
			""",end = '')
		time.sleep(0.2)
		print("""
			Press 3 : Create DataNode
			""",end = '')
		time.sleep(0.2)
		print("""
			Press 4 : Create NameNode
			""",end = '')
		time.sleep(0.2)
		print("""
			Press 5 : Hadoop Client
			""",end = '')
		time.sleep(0.2)
		print("""
			press 6 : Exit the program
			""",end = '')
		time.sleep(0.2)
		print("""
			Press 7 : Back to Main Menu
			""")
		time.sleep(0.2)
		hadoop=input("Select your choice:-")
		if int(hadoop)==1:
			os.system("rpm -q hadoop")
		elif int(hadoop)==2:
			print("Downloading required software's . . .")
			time.sleep(2)
			os.system("wget -c https://pythonfilerahul.s3.ap-south-1.amazonaws.com/hadoop-1.2.1-1.x86_64.rpm")
			os.system("wget -c ")
			os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
			os.system("rpm -ivh jdk-8u171-linux-x64.rpm")
			os.system("tput setaf 7")
			os.system("hadoop version")
			os.system("tput sgr0")
			print("Successfully Hadoop Installed.")


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
			os.system("tput sgr0")
			print('figlet  DataNode Started')
		elif int(hadoop)==4:
			masterDir=input("Give directory name:- ")
			os.system("mkdir /{}".format(masterDir))
			os.system("rm -f /etc/hadoop/core-site.xml")
			os.system("rm -f /etc/hadoop/hdfs-site.xml")
			print("Your Hadoop directory is created.")
			master_ip_address=input("Enter Your IP Address :- ")
			os.system("cd /etc/hadoop")
			doc,tag,text=Doc().tagtext()
			with tag('configuration'):
				with tag('property'):
					with tag('name'):
						text('dfs.name.dir')
					with tag('value'):
						text('/{}'.format(masterDir))
			result=indent(doc.getvalue(),indentation =' '*4,newline='\r\n')
			f=open('/etc/hadoop/hdfs-site.xml','a')
			f.write('{}\n'.format(result))
			f.close()
			doc1,tag1,text1=Doc().tagtext()
			with tag1('configuration'):
				with tag1('property'):
					with tag1('name'):
						text1('fs.default.name')
					with tag1('value'):
						text1('hdfs://{}'.format(master_ip_address)+':9001')
			res=indent(doc1.getvalue(),indentation =' '*4,newline='\r\n')
			f=open('/etc/hadoop/core-site.xml','a')
			f.write('{}\n'.format(res))
			f.close()
			print('Setup Complete')
			os.system("hadoop namenode -format -y")
			os.system("hadoop-daemon.sh start namenode")
			os.system("figlet NameNode Started")
		elif int(hadoop)==5:
			while True:
				print("""
				Press 1 : Create Hadoop Client
				""",end = '')
				time.sleep(0.2)
				print("""
				Press 2 : Show file
				""",end = '')
				time.sleep(0.2)
				print("""
				Press 3 : Create file
				""",end = '')
				time.sleep(0.2)
				print("""
				Press 4 : Send file
				""",end = '')
				time.sleep(0.2)
				print("""
				Press 5 : Read file
				""",end = '')
				time.sleep(0.2)
				print("""
				Press 6 : Remove file
				""",end = '')
				time.sleep(0.2)
				print("""
				press 7 : Exit the program
				""",end = '')
				time.sleep(0.2)
				print("""
				Press 8 : Back to Main Menu
				""",end = '')
				time.sleep(0.2)
				Client_ch=input("Select your choice :- ")
				if int(Client_ch)==1:
					os.system("rm -f /etc/hadoop/core-site.xml")
					client_ip_address=input("Enter Master IP Address :- ")
					os.system("cd /etc/hadoop")
					doc1,tag1,text1=Doc().tagtext()
					with tag1('configuration'):
						with tag1('property'):
							with tag1('name'):
								text1('fs.default.name')
							with tag1('value'):
								text1('hdfs://{}'.format(client_ip_address)+':9001')
					res=indent(doc1.getvalue(),indentation =' '*4,newline='\r\n')
					f=open('/etc/hadoop/core-site.xml','a')
					f.write('{}\n'.format(res))
					f.close()
					os.system("figlet Hadoop Client Started")
				elif int(Client_ch)==2:
					os.system("tput setaf 7")
					os.system("hadoop fs -ls /")
					os.system("tput sgr0")

				elif int(Client_ch)==3:
					file_location=input("Enter file location: -")
					file_name=input("Enter your file name: - ")
					os.system("vi {}/{}".format(file_location,file_name))
					print("Successfully file created.")

				elif int(Client_ch)==4:
					dir_location=input("Enter your directory location :- ")
					os.system("ls {}".format(dir_location))
					var_file_name=input("Enter your file name : -")
					os.system("hadoop fs -put {} /".format(var_file_name))
					os.system("tput setaf 10")
					print("Successfully uploaded.")
					time.sleep(2)
					os.system("tput sgr0")
					os.system("tput setaf 7")
					os.system("\nhadoop fs -ls /")
					os.system("tput sgr0")
				elif int(Client_ch)==5:
					os.system("\nhadoop fs -ls /")
					read_file=input("Which file you want to read : -")
					os.system("hadoop fs -cat {}".format(read_file))
				elif int(Client_ch)==6:
					os.system("\nhadoop fs -ls /")
					del_file=input("Which file you want to delete : -")
					var2=os.system("hadoop fs -rmr /{}".format(del_file))
					if int(var2)==0:
						os.system("tput setaf 7")
						time.sleep(1)
						print("Successfully Deleted")
						os.system("tput sgr0")
						os.system("\nhadoop fs -ls /")
					else:
						os.system("tput setaf 9")
						print("Input wrong keyword.")
						os.system("tput sgr0")				
				elif int(Client_ch)==7:
					os.system("figlet Thanks for using Hadoop Client.")
					exit()
				elif int(Client_ch)==8:
					break
				else:
					print("You have entered wrong keyword")
		elif int(hadoop)==6:
			os.system("figlet Thanks for using Hadoop.")
			exit()
		elif int(hadoop)==7:
			break
		else:
			os.system("tput setaf 1")
			print("You have entered wrong keyword")
			os.system("tput sgr0")

def Jenkins():
	while True:
		print("""
			Press 1 : Install Jenkins
			""",end = '')
		time.sleep(0.2)
		print("""
			Press 2 : Remove Jenkins
			""",end = '')
		time.sleep(0.2)
		print("""
			press 3 : Exit the program
			""",end = '')
		time.sleep(0.2)
		print("""
			Press 4 : Back to Main Menu
			""",end = '')
		time.sleep(0.2)
		jenkins_ch=input("Select your choice :- ")
		if int(jenkins_ch)==1:
			os.system("figlet Configuring Jenkins . . . ")
			os.system("yum install sudo -y")
			os.system("sudo yum install wget -y")
			os.system("sudo yum install net-tools -y")
			os.system("sudo yum install java-latest-openjdk.x86_64 -y")
			os.system("sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo")
			os.system("sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key")
			os.system("yum install git -y")
			os.system("yum install jenkins -y")
			varr='"jenkins ALL=(ALL)  NOPASSWD:ALL"'
			os.system("echo -e {} >> /etc/sudoers".format(varr))
			os.system("systemctl start jenkins")
			os.system("figlet Jenkins is Configured")
			print("Copy your initial jenkins password:-")
			os.system("tput bold 9")
			os.system("tput setaf 9")
			os.system("\ncat /var/lib/jenkins/secrets/initialAdminPassword")
			os.system("tput sgr0")
			print("Now ! You can login your jenkins with localIP:8080")
		elif int(jenkins_ch)==2:
			os.system("sudo yum remove jenkins -y")
			os.system("rm -rvf /etc/yum.repos.d/jenkins.repo")
			os.system("figlet Jenkins is Removed.")

		elif int(jenkins_ch)==3:
			os.system("figlet Thanks for using Jenkins.")
			exit()
		elif int(jenkins_ch)==4:
			break
		else:
			os.system("tput setaf 1")
			print("You have entered wrong keyword")
			os.system("tput sgr0")

def linuxcmd():
	while True:
		linuxcmd=input("Enter your Linux Command :- ")
		os.system("{}".format(linuxcmd))
		if linuxcmd=='exit':
			os.system("figlet Thanks for using Linux Command.")
			break

def yum_conf():
	while True:
		print("""
			Kindly attach your RedHat IOS file before continuing.
			""")
		user_in=input("If Attached press Y or N for not :- ")
		if user_in=='Y' or user_in=='y':
			os.system("mkdir /dvd")
			os.system("mount /dev/cdrom /dvd/")
			mount_var='mount /dev/cdrom /dvd/'
			os.system("echo -e {} >> /etc/rc.d/rc.local".format(mount_var))
			os.system("chmod +x /etc/rc.d/rc.local")
			repo_file_name=input("Enter your yum repo file name:- ")
			os.system("rm -f /etc/yum.repo.d/{}.repo".format(repo_file_name))
			os.system("touch /etc/yum.repo.d/{}.repo".format(repo_file_name))
			repo_var1="[dvd1]"
			repo_var2="baseurl=file:///dvd/AppStream"
			repo_var3="gpgcheck=0"
			repo_var4="[dvd2]"
			repo_var5="baseurl=file:///dvd/BaseOS"
			repo_var6="gpgcheck=0"
			os.system("echo -e {} > /etc/yum.repo.d/{}.repo".format(repo_var1,repo_file_name))
			os.system("echo -e {} >> /etc/yum.repo.d/{}.repo".format(repo_var2,repo_file_name))
			os.system("echo -e {} >> /etc/yum.repo.d/{}.repo".format(repo_var3,repo_file_name))
			os.system("echo -e {} >> /etc/yum.repo.d/{}.repo".format(repo_var4,repo_file_name))
			os.system("echo -e {} >> /etc/yum.repo.d/{}.repo".format(repo_var5,repo_file_name))
			os.system("echo -e {} >> /etc/yum.repo.d/{}.repo".format(repo_var6,repo_file_name))
			os.system("yum repolist")
			os.system("Successfully yum configured.")
		elif user_in=='N' or user_in=='n':
			print("Please attach your Redhat IOS file.")
		else:
			os.system("tput setaf 1")
			print("You have entered wrong keyword")
			os.system("tput sgr0")
			continue

def docker_conf():
	while True:
		print("""
			Press 1 : Configure & Install Docker
			""",end = '')
		time.sleep(0.2)
		print(""" 
			Press 2 : Check your Images
			""",end = '')
		time.sleep(0.2)
		print("""
			Press 3 : Manage your container
			""",end = '')
		time.sleep(0.2)
		print("""
			Press 4 : Back to Main menu
			""",end = '')
		time.sleep(0.2)
		print("""
			Press 5 : Exit the Program
			""")
		time.sleep(0.2)
		docker_ch=input("Select your choice :- ")
		if int(docker_ch)==1:
			os.system("rm -f /etc/yum.repo.d/docker.repo")
			os.system("touch /etc/yum.repo.d/docker.repo")
			docker_repo1="[docker]"
			docker_repo2="baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/"
			docker_repo3="gpgcheck=0"
			os.system("echo -e {} > /etc/yum.repo.d/docker.repo".format(docker_repo1))
			os.system("echo -e {} >> /etc/yum.repo.d/docker.repo".format(docker_repo2))
			os.system("echo -e {} >> /etc/yum.repo.d/docker.repo".format(docker_repo3))
			os.system("yum repolist")
			print("Successfully Docker Configured")
			time.sleep(0.5)
			print("Now installing Docker . . .")
			os.system("yum install docker-ce --nobest -y")
			os.system("systemctl enable docker")
			os.system("systemctl start docker")
			print("Successfully Docker Installed")
		elif int(docker_ch)==2:
			while True:
				print("""
					Press 1 : Show Images
					""")
				time.sleep(0.2)
				print("""
					Press 2 : Pull Images
					""")
				time.sleep(0.2)
				print("""
					Press 3 : Remove Images
					""")
				time.sleep(0.2)
				print("""
					Press 4 : Back to Docker Menu
					""")
				time.sleep(0.2)
				print("""
					Press 5 : Back to Main Menu
					""")
				time.sleep(0.2)
				print("""
					Press 6 : Exit from the program
					""")
				time.sleep(0.2)
				docker_image_ch=input("Enter your choice : -")
				if int(docker_image_ch)==1:
					os.system("tput setaf 7")
					os.system("docker images")
					os.system("tput sgr0")
				elif int(docker_image_ch)==2:
					image_name=input("Enter image name : -")
					image_tag=input("Enter tag : -")
					os.system("docker pull {}:{}".format(image_name,image_tag))
					os.system("tput setaf 7")
					os.system("docker images")
					os.system("tput sgr0")
				elif int(docker_image_ch)==3:
					image_name_rm=input("Enter image name : -")
					image_tag_rm=input("Enter tag : -")
					os.system("docker rmi {}:{}".format(image_name_rm,image_tag_rm))
					os.system("tput setaf 7")
					os.system("docker images")
					os.system("tput sgr0")
				elif int(docker_image_ch)==4:
					break
				elif int(docker_image_ch)==5:
					break
					break

				elif int(docker_image_ch)==6:
				 	exit()
				else:
					os.system("tput setaf 1")
					print("You have entered wrong keyword")
					os.system("tput sgr0")
		elif int(docker_ch)==3:
			while True:
				print("""
					Press 1 : Check status of  container
					""")
				time.sleep(0.2)
				print("""
					Press 2 : Stop existing container
					""")
				time.sleep(0.2)
				print("""
					Press 3 : Launch new container
					""")
				time.sleep(0.2)
				print("""
					Press 4 : Remove container
					""")
				time.sleep(0.2)
				print("""
					Press 5 : Remove all container
					""")
				time.sleep(0.2)
				print("""
					Press 6 : Back to Docker Menu
					""")
				time.sleep(0.2)
				print("""
					Press 7 : Back to Main Menu
					""")
				time.sleep(0.2)
				print("""
					Press 8 : Exit from the program
					""")
				time.sleep(0.2)
				docker_container_ch=input("Enter your choice : -")
				if int(docker_container_ch)==1:
					os.system("tput setaf 7")
					os.system("docker ps -a")
					os.system("tput sgr0")
				elif int(docker_container_ch)==2:
					container_name_rm=input("Enter container name:- ")
					os.system("docker stop {}".format(container_name_rm))
					os.system("tput setaf 7")
					os.system("docker ps -a")
					os.system("tput sgr0")
				elif int(docker_container_ch)==3:
					container_name=input("Enter container name:- ")
					container_image_name=input("Enter container image name:- ")
					container_image_tag=input("Enter container image tag:- ")
					os.system("docker run -itd --name {}  {}:{}".format(container_name,container_image_name,container_image_tag))
					os.system("tput setaf 7")
					os.system("docker ps -a")
					os.system("tput sgr0")
				elif int(docker_container_ch)==4:
					docker_rm_ch=input("Enter container name : -")
					os.system("docker rm {}".format(docker_rm_ch))
					os.system("tput setaf 7")
					os.system("docker ps -a")
					os.system("tput sgr0")
				elif int(docker_container_ch)==5:
					os.system("docker rm -f `docker ps -a -q`")
					os.system("tput setaf 7")
					os.system("docker ps -a")
					os.system("tput sgr0")
				elif int(docker_container_ch)==6:
					break
				elif int(docker_container_ch)==7:
					break
					break

				elif int(docker_container_ch)==8:
					os.system("figlet Thanks for using Python AutoBot.")
					exit()
				else:
					os.system("tput setaf 1")
					print("You have entered wrong keyword")
					os.system("tput sgr0")
		elif int(docker_container_ch)==4:
			break					
		elif int(docker_container_ch)==5:
			exit()
		else:
			os.system("tput setaf 1")
			print("You have entered wrong keyword")
			os.system("tput sgr0")

def ansible():
	while True:
		print("""
			Press 1 : Configure & Install Ansible
			""",end = '')
		time.sleep(0.2)
		print("""
			Press 2 : Back to Main menu
			""",end = '')
		time.sleep(0.2)
		print("""
			Press 3 : Exit the Program
			""")
		time.sleep(0.2)
		ansible_ch=input("Enter your choice : -")
		if int(ansible_ch)==1:
			print("Is your YUM configured ? [Y/N] :- ")
			yum_ch=input("")
			if yum_ch=='N' or yum_ch=='n':
				yum_conf()
			elif yum_ch=='Y' or yum_ch=='y':
				os.system("yum install python3 -y")
				os.system("pip3 install ansible")
				os.system("mkdir /etc/ansible")
				os.system("touch /etc/ansible/ansible.cfg")
				os.system("ansible --version")
				os.system("tput setaf 10")
				print("Successfully Ansible installed")
				os.system("tput sgr0")
			else:
				print("You have entered wrong keyword")
		elif int(ansible_ch)==2:
			break
		elif int(ansible_ch)==3:
			os.system("figlet Thanks for using Python AutoBot.")
			exit()
		else:
			os.system("tput setaf 1")
			print("You have entered wrong keyword")
			os.system("tput sgr0")

while True :
	print("-----------------------------------------------------------------------------")
	os.system("figlet Welcome to Python AutoBot")
	print("-----------------------------------------------------------------------------")
	pyt.speak("Welcome to Python Auto bot.")
	print(""" 
		1 : Amazon Console
		""",end = '')
	time.sleep(0.2)
	print(""" 
		2 : Configure Hadoop-Cluster
		""",end = '')
	time.sleep(0.2)
	print("""
		3 : Configure YUM
		""",end = '')
	time.sleep(0.2)
	print("""
		4 : Configure Docker
		""",end = '')
	time.sleep(0.2)
	print("""
		5 : Configure Jenkins
		""",end = '')
	time.sleep(0.2)
	print("""
		6 : Configure Ansible
		""",end = '')
	time.sleep(0.2)
	print("""
		7 : Run Linux Command
		""",end = '')
	time.sleep(0.2)
	print("""
		8 : Exit the Program
		""")
	time.sleep(0.2)
	with sr.Microphone() as source:
		pyt.speak("What Can I help you ?")
		audio=r.listen(source)
		pyt.speak("Proceed.")
	ch1=r.recognize_google(audio)
	ch=ch1.lower()
	print(ch)
	if ("amazon" in ch) or ("console" in ch):
		aws()
	elif ("configure" in ch) or ("Hadoop" in ch):
		Hadoop_Cluster()
	elif ("configure" in ch) or ("YUM" in ch):
		yum_conf()
	elif ("configure" in ch) or ("Dcoker" in ch):
		docker_conf()
	elif ("configure" in ch) or ("Jenkins" in ch):
		Jenkins()
	elif ("configure" in ch) or ("Ansible" in ch):
		ansible()
	elif ("run" in ch) or ("Linux" in ch):
		linuxcmd()
	elif ("exit" in ch) or ("program" in ch):
		pyt.speak("Thanks for using Python AutoBot.")
		os.system("figlet Thanks for using Python AutoBot.")
		exit()
	else:
		os.system("tput setaf 1")
		print("You have entered wrong keyword")
		os.system("tput sgr0")
			
