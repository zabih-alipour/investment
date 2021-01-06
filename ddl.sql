create table user
(
    id   INTEGER not null
        primary key autoincrement
        unique,
    name TEXT    not null
);

-- ########################### payment
create table category
(
    id   INTEGER not null
        primary key autoincrement
        unique,
    name TEXT    not null
        unique
);
insert into transaction_type (id, name)
values (1, 'بدهی');

create table payment_type
(
    id          INTEGER not null
        primary key autoincrement
        unique,
    name        TEXT    not null,
    category_id INTEGER not null
        references category
);

create table payment
(
    id              INTEGER not null
        primary key autoincrement
        unique,
    user_id         INTEGER not null
        references user,
    payment_type_id INTEGER not null
        references payment_type,
    amount          NUMERIC not null,
    shamsi_date     TEXT    not null,
    description     TEXT    not null
);

CREATE VIEW vw_payment_turnover AS
select u.id          as user_id,
       u.name        as user_name,
       c.name        as category_name,
       pt.name       as payment_type_name,
       sum(p.amount) as amount
from payment p
         INNER JOIN user u on u.id = p.user_id
         inner JOIN payment_type pt on p.payment_type_id = pt.id
         inner JOIN category c on pt.category_id = c.id
GROUP by u.id, u.name, c.name, pt.name;

CREATE VIEW vw_payment_summary AS
select vw_pt.user_id,
       vw_pt.user_name,
       sum(amount) as amount
from vw_payment_turnover vw_pt
group by vw_pt.user_id, vw_pt.user_name;

-- ############################# Investment
create table investment_type
(
    id   INTEGER not null
        primary key autoincrement
        unique,
    name TEXT    not null unique,
    code TEXT    not null unique
);
insert into investment_type (id, name, code)
values (1, 'پس انداز ریال', 'Rial');
insert into investment_type (id, name, code)
values (2, 'بیت کوین', 'BitCoin');
insert into investment_type (id, name, code)
values (3, 'لایت کوین', 'LiteCoin');
insert into investment_type (id, name, code)
values (4, 'دش', 'Dash');
insert into investment_type (id, name, code)
values (5, 'طلا', 'Gold');
insert into investment_type (id, name, code)
values (6, 'اتریوم', 'Ethereum');
insert into investment_type (id, name, code)
values (7, 'واحد صندوق سرمایه گذاری', 'Fund');
insert into investment_type (id, name, code)
values (8, 'دلار', 'Dolor');

create table Investment
(
    id                      INTEGER not null
        primary key autoincrement
        unique,
    user_id                 INTEGER not null
        references user,
    amount                  NUMERIC not null,
    shamsi_date             TEXT    not null,
    investment_type_id      INTEGER not null
        references investment_type,
    side_investment_type_id INTEGER not null
        references investment_type,
    executed_price          NUMERIC not null,
    description             TEXT    not null
);

CREATE VIEW vw_investment_summary_per_user AS
SELECT u.id                                                         as user_id,
       u.name                                                       as user_name,
       sum(CASE WHEN it.id = 1 THEN i.amount else 0 end)            as RIAL,
       sum(CASE WHEN it.id = 2 THEN i.amount else 0 end)            as BITCOIN,
       sum(CASE WHEN it.id = 3 THEN i.amount else 0 end)            as LITCOIN,
       sum(CASE WHEN it.id = 4 THEN i.amount else 0 end)            as DASH,
       sum(CASE WHEN it.id = 5 THEN i.amount else 0 end)            as GOLD,
       sum(CASE WHEN it.id = 6 THEN i.amount else 0 end)            as ETHERIUM,
       sum(CASE WHEN it.id = 7 THEN i.amount else 0 end)            as FUND,
       round(sum(CASE WHEN it.id = 8 THEN i.amount else 0 end), 10) as DOLOR
from Investment i
         JOIN investment_type it on i.investment_type_id = it.id
         JOIN user u on u.id = i.user_id
group by u.id, u.name
ORDER by u.id;

CREATE VIEW vw_investment_summery AS
SELECT *
from vw_investment_summary_per_user pu
UNION ALL
SELECT NULL             as user_id,
       'TOTAL'          as TOTAL,
       sum(pu.RIAL)     as RIAL,
       sum(pu.BITCOIN)  as BITCOIN,
       sum(pu.LITCOIN)  as LITCOIN,
       sum(pu.DASH)     as DASH,
       sum(pu.GOLD)     as GOLD,
       sum(pu.ETHERIUM) as ETHERIUM,
       sum(pu.FUND)     as FUND,
       sum(pu.DOLOR)    as DOLOR
from vw_investment_summary_per_user pu;

