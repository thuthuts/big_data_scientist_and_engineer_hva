-- a) Return all records with state 'MA'
select * from population where state = 'MA';

-- b) Count the number of records(=cities) for the state ‘MA’
Select count(*) from population where state = 'MA' group by state;

-- c) Count the number of records(=cities) for each state
Select city, count(*) from population group by city;
select * from population where city ='Chester';

-- d) Sum the number of inhabitants ( population) for each state
Select state, sum(pop) from population group by state;

-- e) alias numberOfInhabitants for the result column of question d.
Select state, sum(pop) as numberOfInhabitants from population group by state;

-- f) Order the result of e. by numberOfInhabitants
Select state, sum(pop) as numberOfInhabitants from population group by state order by numberOfInhabitants;

-- g) Return only those states with a total population > 1.000.000
Select state, sum(pop) as numberOfInhabitants from population group by state Having numberOfInhabitants > 10000000 order by numberOfInhabitants;

