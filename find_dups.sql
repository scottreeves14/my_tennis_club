select firstname,lastname,joined_date,phone,count(*) 
    as cnt from members_member 
    group by firstname,lastname,joined_date,phone 
    having count(*) > 1;
