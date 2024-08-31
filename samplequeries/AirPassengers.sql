create table Ylimits as 
select 0 as minY, 600 as maxY;

create table Xlimits as 
select 1950 as minX, 1960 as maxX;

create table values as
select time, value from read_csv('https://git.io/AirPassengers');
