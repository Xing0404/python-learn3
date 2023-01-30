'''
DDL数据定义

SQL语言大小写不敏感；SQL可以单行或多行书写，最后以;号结束

SQL基础语法：
查看数据库：show databases;
使用数据库：use 数据库名称;
创建数据库：create database 数据库名称 [charset utf8];    # [charset utf8]代表可写charset utf8也可以不写的意思（写的话不需要加上[]），代表字符集格式
删除数据库：drop database 数据库名称;
查看当前使用的数据库：select database();

查看有哪些表（需要先选择数据库）：show tables;
删除表：drop table 表名称;     drop table if exists 表名称;
创建表：creat table 表名称(
    列名称 列类型,            # 列类型有：int 整数   float 浮点数   varchar(长度) 文本，长度为数字，长度最大可填255
    列名称 列类型,                      date 日期类型      timestamp 时间戳类型   （字符串的值出现在sql语句中必须要用单引号''包围起来）
    ......
);

SQL支持注释:
单行注释： -- 注释内容 （--后面一定要有一个空格）
单行注释： # 注释内容（#后面可以不加空格，推荐加上）
多行注释：/* 注释内容 */
'''


'''

DML数据操作

数据插入 insert:
基础语法：insert into 表[(列1, 列2, ......)]  values(值1, 值2, .......)[, (值1, 值2, .......), (值1, 值2, .......)];
# 如果不写列，那么values中的值就会按照表中创建列的先后顺序赋值

数据删除 delete:
基础语法：delete from 表名称 [where 条件判断];

数据更新 upadte 
基础语法：update 表名 set 列=值 [where 条件判断];

'''


'''

DQL数据查询

基础数据查询
基础语法：select 字段列表|* from 表：  
 例：select id from student; 查询表student中名为id的列
    select * from student;  查询表student中所有的列 
    
基础数据查询-过滤
语法：select 字段列表|* from 表 where 条件判断

分组聚合
基础语法：select 列|聚合函数 from 表 [where 条件] group by 列;       # gruop by 列   按照列分组
例：select gender, avg(age), sum(age) from student group by gender;        # 注意这里一定要gruop by后写了的列，才能在select后出现，
                                                                             但聚合函数中写的列就不需要一定要在group by后面出现。
聚合函数有：sum(列) 求和   avg(列) 求平均值   min(列) 求最小值  
         max() 求最大值  count(列|*) 求数量
         
结果排序 只需在最后加上order by
select 列|聚合函数 from 表 [where 条件] group by 列 order by 列 [asc | desc]   asc是升序排列，也是默认的排列，desc是降序排列
例：select * from student where age > 20 order by age desc;
         
结果分页限制  只需在最后加上limt n[, m]
select 列|聚合函数 from 表 [where 条件] group by 列 order by 列 [asc | desc] limit n[, m]
例：select * from student limit 5;       只输出5条结果
   select * from student limit 10, 5;   从第10条开始，向后取5条

执行顺序：from->where->group by和聚合函数->select->order by->limit

'''




















