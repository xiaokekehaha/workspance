update price set assist_type_id=53 where exists(select null from rcu_news.baojia_baojia where td_id=price.old_id and met=1);
update price set assist_type_id=54 where exists(select null from rcu_news.baojia_baojia where td_id=price.old_id and met=2);
update price set assist_type_id=57 where exists(select null from rcu_news.baojia_baojia where td_id=price.old_id and met=3);
update price set assist_type_id=55 where exists(select null from rcu_news.baojia_baojia where td_id=price.old_id and met=4);
update price set assist_type_id=58 where exists(select null from rcu_news.baojia_baojia where td_id=price.old_id and met=5);
update price set assist_type_id=56 where exists(select null from rcu_news.baojia_baojia where td_id=price.old_id and met=6);
update price set assist_type_id=59 where exists(select null from rcu_news.baojia_baojia where td_id=price.old_id and met=7);
update price set assist_type_id=179 where exists(select null from rcu_news.baojia_baojia where td_id=price.old_id and met=8);
update price set assist_type_id=180 where exists(select null from rcu_news.baojia_baojia where td_id=price.old_id and met=9);
update price set assist_type_id=181 where exists(select null from rcu_news.baojia_baojia where td_id=price.old_id and met=10);
