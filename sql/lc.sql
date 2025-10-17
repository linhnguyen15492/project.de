


select p.product_id,
    case
            when sum(u.units) is null then 0 
            else round(sum(p.price * u.units)*1.0 / sum(u.units), 2)
    end as "average_price"
from Prices p left join UnitsSold u
    on p.product_id = u.product_id and u.purchase_date between p.start_date and p.end_date
group by p.product_id;


select p.product_id, round(coalesce(sum(p.price * u.units)*1.0 / sum(u.units), 0), 2) "average_price"
from Prices p left join UnitsSold u
    on p.product_id = u.product_id and u.purchase_date between p.start_date and p.end_date
group by p.product_id;




with
    cte
    as
    (
        select t.*, concat(EXTRACT(year from t.trans_date), '-', TO_CHAR(t.trans_date, 'MM')) as "month"
        from Transactions t
    )
select cte.month,
    cte.country,
    count(cte.id) "trans_count",
    sum(case when cte.state = 'approved' then 1 else 0 end) as "approved_count",
    sum(cte.amount) "trans_total_amount",
    sum(case when cte.state = 'approved' then cte.amount else 0 end) as "approved_total_amount"
from cte
group by cte.month, cte.country;

/*

| month   | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
| ------- | ------- | ----------- | -------------- | ------------------ | --------------------- |
| 2018-12 | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01 | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01 | DE      | 1           | 1              | 2000               | 2000                  |

*/



select TO_CHAR(t.trans_date, 'YYYY-MM') as "month",
    t.country,
    count(t.id) "trans_count",
    sum(case when t.state = 'approved' then 1 else 0 end) as "approved_count",
    sum(t.amount) "trans_total_amount",
    sum(case when t.state = 'approved' then t.amount else 0 end) as "approved_total_amount"
from Transactions t
group by month, t.country;


with
    cte
    as
    (
        select d.*, rank() over (partition by d.customer_id order by d.order_date)
        from Delivery d
    )
select round(sum(
    case 
        when cte.rank = 1 and cte.order_date = cte.customer_pref_delivery_date then 1 else 0
    end)*100.0 / count(distinct cte.customer_id), 2) "immediate_percentage"
from cte;



with
    first_login
    as
    (
        select a.player_id, min(a.event_date) first_login
        from Activity a
        group by a.player_id
        order by a.player_id
    )
select round(count(distinct a.player_id)*1.0 / (select count(distinct a.player_id)
    from Activity a), 2) "fraction"
from Activity a
    inner join first_login f
    on a.player_id = f.player_id
where (a.event_date - f.first_login) = 1;


