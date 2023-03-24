 em1=Employee.objects.create(name='Nuradil',birth_date='2003-01-12',position='python developer',salary=50000,date_experience='2020-01-10')
 .
 .
 .
 wp1=WorkProject.objects.create(project_name='Block')
 wp1=WorkProject.objects.create(project_name='Block')
 wp1.members.set([em1,em2,em3],through_defaults={'date_joined':'2023-04-23'})
 em2.delete()
(3, {'person.Password': 1, 'person.Membership': 1, 'person.Employee': 1})
em5=Employee.objects.create(name='Nura',birth_date='2003-04-05',position='java developer',salary=50000,work_experience='2023-01-02')
 cl1=Client.objects.create(name='Atai',birth_date='2004-09-08',address='isa chikaeva 125',phone_number='0999888777')
 cl2=Client.objects.create(name='Faruh',birth_date='2003-09-08',address='isa chikaeva 126',phone_number='09998000777')
 cl3=Client.objects.create(name='Amal',birth_date='2004-02-08',address='isa chikaeva 127',phone_number='07088000777')
vipcl=VIPClient.objects.create(name='barsbek',birth_date='2003-01-02',address='bishkek',phone_number='000000',vip_status_start='2022-01-01',donation_amount=500000)
Client.objects.all()
<QuerySet [<Client: Client object (1)>, <Client: Client object (2)>, <Client: Client object (3)>, <Client: Client object (4)>]>
 Employee.objects.all()
<QuerySet [<Employee: Employee object (1)>, <Employee: Employee object (3)>, <Employee: Employee object (5)>]>
 WorkProject.objects.all()
<QuerySet [<WorkProject: WorkProject object (1)>, <WorkProject: WorkProject object (2)>]>
 Password.objects.all()
<QuerySet [<Password: Password object (1)>, <Password: Password object (3)>]>
 VIPClient.objects.all()
<QuerySet [<VIPClient: VIPClient object (4)>]>
Membership.objects.all()
<QuerySet [<Membership: Membership object (1)>, <Membership: Membership object (3)>]>
 WorkProject.objects.get(members=em1)
<WorkProject: WorkProject object (2)>


