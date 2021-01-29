delete from "bmwsys_msysval"
 where sys_name = 'mailbk';

insert into "bmwsys_msysval" 
( sys_name
, item_name1
, item_name2
, item_name3
, item_name4
, item_name5
, char_value1
, char_value2
, char_value3
, char_value4
, char_value5
, char_value6
, char_value7
, char_value8
, char_value9
, char_value10
, int_value1
, int_value2
, int_value3
, int_value4
, int_value5
, int_value6
, int_value7
, int_value8
, int_value9
, int_value10
) values 
('mailbk'
, 'rootdir'
, ''
, ''
, ''
, ''
,'127.0.0.1'
,'Users'
,'administrator/dev/mailbk'
, 'root'
, 'system22'
, ''
, ''
, ''
, ''
, ''
, 0
, 0
, 0
, 0
, 0
, 0
, 0
, 0
, 0
, 0
);

SELECT * FROM "bmwsys_msysval" LIMIT 1000;
