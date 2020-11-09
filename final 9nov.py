import os

print("\t\t\t WELCOME TO MENU PROGRAM")

client = input("Where do you want to run the program?(local/remote) ")

if client == 'local':

    print("""
	Press 1 to access Hadoop services 
	Press 2 to access Docker services
	Press 3 to access Storage services
	Press 4 to access Webserver services
    Press 5 to run basic command
	""")

    service_choice = input("Enter your choice : ")
	
    if int(service_choice) == 1:

        print("""
		Press 1 to see report 
		Press 2 to see all files in the cluster
		Press 3 to upload a file in cluster
        Press 4 to start the namenode
        Press 5 to start the datanode
        Press 6 to stop namenode
        Press 7 to stop datanode
        Press 8 to conf core file
        press 9 to conf hdfs for name node file
        press 10 to conf hdfs for data node
		""")

        requirement = input("Enter your choice : ")
        
        if int(requirement) == 1:
            os.system("hadoop dfsadmin -report")

        elif int(requirement) == 2:
            os.system("hadoop fs -ls /")

        elif int(requirement) == 3:
            file = input("Enter file path : ")
            os.system("hadoop fs -put {} /".format(file))
        
        elif int(requirement) == 4:
            os.system("hadoop-daemon.sh start namenode")
        
        elif int(requirement) == 5:
            os.system("hadoop-daemon.sh start datanode")
        
        elif int(requirement) == 6:
            os.system("hadoop-daemon.sh stop namenode")
        
        elif int(requirement) == 7:
            os.system("hadoop-daemon.sh stop datanode")
        elif int(requirement) == 8:
            nnip= input("enter the ip of name node :")
            file=open("coreconf.txt","w")
            file.writelines(['<property>\n','<name>fs.default.name</name>\n','<value>hdfs://{}:9001</value>\n'.format(nnip),'</property>\n'])
            os.system("sed -i '/<configuration>/r coreconf.txt' /etc/hadoop/core-site.xml")
        elif int(requirement) == 9:
            fn=input("enter the path of file ")
            file=open("hdfsconf.txt","w")
            file.writelines(['<property>\n','<name>dfs.name.dir</name>\n','<value>{}</value>\n'.format(fn),'</property>'])
            file.close()
            os.system("sed -i '/<configuration>/r hdfsconf.txt' /etc/hadoop/hdfs-site.xml")
        elif int(requirement) == 10:
            fn=input("enter the path of file ")
            file=open("hdfsconf.txt","w")
            file.writelines(['<property>\n','<name>dfs.data.dir</name>\n','<value>{}</value>\n'.format(fn),'</property>'])
            file.close()
            os.system("sed -i '/<configuration>/r hdfsconf.txt' /etc/hadoop/hdfs-site.xml")
         
       	else:
            print("""Invalid choice entered""")          
    if int(service_choice) == 2:
    
        print("""
		Press 1 to see info about running containers
		Press 2 to see info about all containers
		Press 3 to enter into a container
		Press 4 to remove a container
		Press 5 to remove all containers
        Press 6 to install the docker
		""")
        requirement = input("Enter your choice : ")

        if int(requirement) == 1:
            os.system("docker ps")
        elif int(requirement) == 2:
            os.system("docker ps -a")
        elif int(requirement) == 3:
            name = input("Enter your container name or id")
            os.system("docker attach {}".format(name))
        elif int(requirement) == 4:
            name = input("Enter your container name or id")
            os.system("docker rm {}".format(name))
        elif int(requirement) == 5:
            os.system("docker rm `docker ps -a` ")
        elif int(requirement)==6:
            os.system("yum install docker")
        else:
            print("""Invalid choice entered""")
    if int(service_choice) == 3:

        print("""
		Press 1 to create a volume group by 2 hard disks
		Press 2 to add a hard disk to a volume group
		""")

        requirement = input("Enter your choice : ")

        if int(requirement) == 1:
            name1 = input("Enter name of hard disk 1 : ")
            name2 = input("Enter name of hard disk 2 : ")
            vgname = input("Enter volume group name : ")
            os.system("pvcreate {} {}".format(name1,name2))
            os.system("vgcreate {} {} {}".format(vgname,name1,name2))

        if int(requirement) == 2:
            hdname = input("Enter hard disk name : ")
            vgname = input("Enter volume group name : ")
            os.system("vgextend {} {}".format(vgname,hdname))
        else:
            print("""Invalid choice entered""")
    if int(service_choice) == 4:

        print("""
		Press 1 to see status of webserver
		Press 2 to start webserver
		Press 3 to stop webserver
		Press 4 to enable webserver service 
		Press 5 to disable webserver service
		""")

        requirement = input("Enter your choice : ")
        if int(requirement) == 1:
            os.system("systemctl status httpd")
        if int(requirement) == 2:
            os.system("systemctl start httpd")
        if int(requirement) == 3:
            os.system("systemctl stop httpd")
        if int(requirement) == 4:
            os.system("systemctl enable httpd")	
        if int(requirement) == 5:
            os.system("systemctl disable httpd")
        else:
            print("""Invalid choice entered""")    
    if int(service_choice) == 5:
        print("""
        Press 1 to see date
        Press 2 to see cal
        Press 3 to open firefox
        press 4 to check info about storage
        Press 5 to see the ip address 
        """)
        
        requirement = input("Enter your choice : ")
        if int(requirement) == 1:
            os.system("date")
        if int(requirement) == 2:
            os.system("cal")
        if int(requirement) == 3:
            os.system("firefox")
        if int(requirement) == 4:
            os.system("fdisk -h")
        if int(requirement) == 5:
            os.system("ifconfig")
        else:
            print("""Invalid choice entered""")
elif client == 'remote':
    ip = input("Enter ip address of the system : ")

    print("""
        Press 1 to access Hadoop services 
        Press 2 to access Docker services
        Press 3 to access Storage services
        Press 4 to access Webserver services
        Press 5 to run basic commands
	Press 6 to launch ec2 instance at aws
        """)

    service_choice = input("Enter your choice : ")
    
    if int(service_choice) == 1:
        print("""
            Press 1 to see report 
            Press 2 to see all files in the cluster
            Press 3 to upload a file in cluster
            Press 4 to start the namenode
            Press 5 to start the datanode
            Press 6 to stop namenode
            Press 7 to stop datanode
		""")

        requirement = input("Enter your choice : ")

        if int(requirement) == 1:
            os.system("ssh {} hadoop dfsadmin -report".format(ip))

        if int(requirement) == 2:
            os.system("ssh hadoop fs -ls /".format(ip))

        if int(requirement) == 3:
            file = input("Enter file path : ")
            os.system("ssh {} hadoop fs -put {} /".format(ip,file))
        if int(requirement) == 4 :
            os.system("ssh {} hadoop-daemon.sh start namenode".format(ip))
        if int(requirement) == 5:
            os.system("ssh {} hadoop-daemon.sh start datanode".format(ip))
        if int(requirement) == 6:
            os.system("ssh {} hadoop-daemon.sh stop namenode".format(ip))
        if int(requirement) == 7:
            os.system("ssh {} hadoop-daemon.sh stop datanode".format(ip))
        else:
            print("""Invalid choice entered""")
    if int(service_choice) == 2:
        print("""
            Press 1 to see info about running containers
            Press 2 to see info about all containers
            Press 3 to enter into a container
            Press 4 to remove a container
            Press 5 to remove all containers
            """)

        requirement = input("Enter your choice : ")

        if int(requirement) == 1:
            os.system("ssh {} docker ps".format(ip))
        if int(requirement) == 2:
            os.system("ssh {} docker ps -a".format(ip))
        if int(requirement) == 3:
            name = input("Enter your container name or id")
            os.system("ssh {} docker attach {}".format(ip,name))
        if int(requirement) == 4:
            name = input("Enter your container name or id")
            os.system("ssh {} docker rm {}".format(ip,name))
        if int(requirement) == 5:
            os.system("ssh {} docker rm `docker ps -a` ".format(ip))
        else:
            print("""Invalid choice entered""")
    if int(service_choice) == 3:

        print("""
		Press 1 to create a volume group by 2 hard disks
		Press 2 to add a hard disk to a volume group
		""")

        requirement = input("Enter your choice : ")

        if int(requirement) == 1:
            name1 = input("Enter name of hard disk 1 : ")
            name2 = input("Enter name of hard disk 2 : ")
            vgname = input("Enter volume group name : ")
            os.system("ssh {} pvcreate {} {}".format(ip,name1,name2))
            os.system("ssh {} vgcreate {} {} {}".format(ip,vgname,name1,name2))

        if int(requirement) == 2:
            hdname = input("Enter hard disk name : ")
            vgname = input("Enter volume group name : ")
            os.system("ssh {} vgextend {} {}".format(ip,vgname,hdname))
        else:
            print("""Invalid choice entered""")
    if int(service_choice) == 4:

        print("""
            Press 1 to see status of webserver
            Press 2 to start webserver
            Press 3 to stop webserver
            Press 4 to enable webserver service 
            Press 5 to disable webserver service
            """)

        requirement = input("Enter your choice : ")

        if int(requirement) == 1:
            os.system("ssh {} systemctl status httpd".format(ip))
        if int(requirement) == 2:
            os.system("ssh {} systemctl start httpd".format(ip))
        if int(requirement) == 3:
            os.system("ssh {} systemctl stop httpd".format(ip))
        if int(requirement) == 4:
            os.system("ssh {} systemctl enable httpd".format(ip))	
        if int(requirement) == 5:
            os.system("ssh {} systemctl disable httpd".format(ip))
        else:
            print("""Invalid choice entered""")
            
    if int(service_choice) == 5:
        print("""
        Press 1 to see date
        Press 2 to see cal
        Press 3 to open firefox
        press 4 to check info about storage
        Press 5 to see the ip address 
        Press 6 to check network connectivity
        """)
        
        requirement = input("Enter your choice : ")
        if int(requirement) == 1:
            os.system("ssh {} date".format(ip))
        if int(requirement) == 2:
            os.system("ssh {} cal".format(ip))
        if int(requirement) == 3:
            os.system("ssh {} firefox".format(ip))
        if int(requirement) == 4:
            os.system("df -h")
        if int(requirement) == 5:
            os.system("ifconfig")
        if int(requirement) == 6:
            os.system("ping goo.gl -c 4")
        if int(requirement) == 7:
            i=input("write file name:")
            os.system("ssh {} gedit {}".format(ip,i))
        else:
            print("""Invalid choice entered""")
    if int(service_choice) == 6:
        print("""
        Press 1 to check AWS CLI install
        Press 2 to get AWS help
        Press 3 to AWS configure then give Access Key,Secret Key , Default region,Default output format
        Press 4 to launch amazon-linux instance on AWS Cloud
	Press 5 to stop instance
Press 6 to start instance
        """)            
        requirement = input("Enter your choice : ")
        if int(requirement) == 1:
            os.system("aws --version")
        if int(requirement) == 2:
            os.system("aws help")
        if int(requirement) == 3:
            a=input("Access Key")
            s=input("Secret Key")
            r=input("Default region")
            f=input("give default format")
            os.system("aws configure ".format(a,s,r,f))    	
        if int(requirement) == 4:
            n=input("how many instances u want to launch")
            sn=input("give submit id")
            kn=input("give key name")
            os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --count {0} --subnet-id {} --security-group-ids sg-091ded016fa6197a7 --key-name {}".format(n,sn,kn))
        if int(requirement) == 5:
            si=input("Type Instance Id:")
            os.system("aws ec2 stop-instances --instance-ids {}".format(si))
        if int(requirement) == 6:
            oi=input("Type Instance Id:")
            os.system("aws ec2 start-instances --instance-ids {}".format(oi))
            
        else:
            print("""Invalid choice entered""")
    
else:
	print("""Invalid choice entered""")
            


		

