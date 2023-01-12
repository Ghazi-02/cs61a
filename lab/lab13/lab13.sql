.read data.sql


CREATE TABLE bluedog AS
  SELECT color,pet from students where color = "blue" and pet = "dog"; 

CREATE TABLE bluedog_songs AS
  SELECT color,pet,song from students where color = "blue" and pet = "dog";


CREATE TABLE smallest_int_having AS
  SELECT time, smallest from students group by smallest  having count(*) = 1 ;


CREATE TABLE matchmaker AS
  SELECT a.pet,a.song,a.color,b.color 
    from students as a, students as b where a.pet = b.pet and a.song = b.song and a.time < b.time;


CREATE TABLE sevens AS
  SELECT s.seven
    FROM students AS s, numbers AS n 
      where s.number = 7 and n.'7' = "True" and s.time = n.time;


CREATE TABLE average_prices AS
  SELECT p1.category as category, AVG(p1.msrp) as average_price 
    FROM products AS p1 group by category;

CREATE TABLE lowest_prices AS
  SELECT i.store as store ,i.item as item ,min(i.price) as lowest_prices
    from inventory as i group by item;
 
CREATE TABLE sl_helper AS
 SELECT l.item as item, l.store as store , p.msrp / p.rating as value, p.category as category
    from lowest_prices as l, products as p
        where l.item =p.name;

CREATE TABLE shopping_list AS
  SELECT sl.item as item, sl.store as store
    from sl_helper as sl group by sl.category having min(value);


CREATE TABLE total_bandwidth AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

