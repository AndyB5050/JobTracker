
select * from jobtracker.companies;
Select * from jobtracker.jobs;
select * from jobtracker.companies c join jobtracker.jobs j on c.idCompanies = j.idCompanies;

select * from jobtracker.companies where idCompanies = 2;

delete  from jobtracker.companies where idCompanies = 2;

delete from jobtracker.jobs where idJobs = 2;

Insert into jobtracker.jobs ( Role, Description, Link, idCompanies) values ('Software Engineer', 'Would work with c', null, 1);

insert into jobtracker.companies ( Name, Description, Link ) values ( 'Spok', 'Smarter faster clinical communications', 'https://www.spok.com/');
insert into jobtracker.companies ( Name, Description, Link ) values ( 'Streetlight', 'Part of Jacob - Big Data for Transportation', null);
insert into jobtracker.companies ( Name, Description, Link ) values ( 'Canonical', 'Company behind Ubuntu', null);
insert into jobtracker.companies ( Name, Description, Link ) values ( 'United Wheels', 'They make bikes.  Huffy is one of their brands.', null);
insert into jobtracker.companies ( Name, Description, Link ) values ( 'RL Carriers', 'Frieght company in Wilmington', null);
insert into jobtracker.companies ( Name, Description, Link ) values ( 'Flock', 'Neighborhood safety. Sounds like it has amazing benefits.', null);
insert into jobtracker.companies ( Name, Description, Link ) values ( 'Vision Government Solutions, Inc.', 'Vision Government Solutions is a leading high-tech Government Technology firm providing cutting-edge software and services to the public sector.', null);
commit;

Insert into jobtracker.jobs ( Role, idCompanies) values ( 'Software Engineer', 1 ); 
Insert into jobtracker.jobs ( Role, idCompanies) values ( 'Product Support Engineer', 3 );
Insert into jobtracker.jobs ( Role, idCompanies) values ( 'Product Support Engineer L2', 4 );
Insert into jobtracker.jobs ( Role, idCompanies) values ( 'Linux Support Engineer', 5 );
Insert into jobtracker.jobs ( Role, idCompanies) values ( 'Junior Front End Developer', 6 );
Insert into jobtracker.jobs ( Role, idCompanies) values ( 'QA Test Analyst', 7 );
Insert into jobtracker.jobs ( Role, idCompanies) values ( 'Software Support Specialist', 8 );
Insert into jobtracker.jobs ( Role, idCompanies) values ( 'Technical Support Engineer', 9 );




Mathews Industrial Automation,Software Engineer,https://careers.matw.com/IndustrialAutomation/job/Cincinnati-Software-Engineer-OH-45227/1250189600/,2025-03-26,applied,"Glenn's company, in Mason OH"
Spok,Product Support Engineer,https://app.jobvite.com/js/jobseeker/applications.html?1=1&#/details/p6hnzwwk,2025-04-03,passed,Smarter faster clinical communications
Streetlight,Product Support Engineer L2,https://careers.jacobs.com/en_US/careers/MyApplications,2025-04-03,passed,Part of Jacob - Big Data for Transportation
Canonical,Linux Support Engineer,https://canonical.com/careers/5169198,2025-04-07,applied,Company behind Ubuntu
United Wheels,Junior Front End Developer,https://recruitingbypaycor.com/career/JobIntroduction.action?clientId=8a7883c68ab5129a018afbd77ef02487&id=8a7885a8958c3c6d01959044891a4bab&source=&lang=en,2025-04-07,applied,They make bikes.  Huffy is one of their brands.
RL Carriers,QA Test Analyst,https://erhk.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/27851?utm_medium=jobshare,2025-04-07,applied,Frieght company in Wilmington
Flock,Technical Support Engineer,https://www.flocksafety.com/careers?ashby_jid=be4c2f44-8245-44c0-b990-99dcc8ca115d&utm_source=53ANrgQzgE,2025-04-08,applied,Neighborhood safety. Sounds like it has amazing benefits. 
Vision Government Solutions, Inc.,Software Support Specialist,https://vgsi.applytojob.com/apply/a5r8HOQXoa?source=LinkedIn,2025-04-08,applied,Vision Government Solutions is a leading high-tech Government Technology firm providing cutting-edge software and services to the public sector.
