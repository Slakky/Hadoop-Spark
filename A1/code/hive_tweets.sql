ADD JAR hdfs:///ubuntu/serde/json-serde-1.3.8-jar-with-dependencies.jar;

set hive.support.sql11.reserved.keywords=false;

CREATE EXTERNAL TABLE if NOT EXISTS tweets (
text STRING,
retweeted_status STRUCT<
    id_str:STRING>
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
STORED AS TEXTFILE;

LOAD DATA INPATH '/input2/t*' OVERWRITE INTO TABLE tweets;

SELECT count(text) FROM tweets WHERE retweeted.status.id_str is not NULL and text RLIKE '[\ ".,;]hon[\ ".,;]|^hon[\ ".,;]|[\ ".,;]$hon'
UNION ALL
SELECT count(text) FROM tweets WHERE retweeted.status.id_str is not NULL and text RLIKE '[\ ".,;]han[\ ".,;]|^han[\ ".,;]|[\ ".,;]$han'
UNION ALL
SELECT count(text) FROM tweets WHERE retweeted.status.id_str is not NULL and text RLIKE '[\ ".,;]den[\ ".,;]|^den[\ ".,;]|[\ ".,;]$den'
UNION ALL
SELECT count(text) FROM tweets WHERE retweeted.status.id_str is not NULL and text RLIKE '[\ ".,;]det[\ ".,;]|^det[\ ".,;]|[\ ".,;]$det'
UNION ALL
SELECT count(text) FROM tweets WHERE retweeted.status.id_str is not NULL and text RLIKE '[\ ".,;]denna[\ ".,;]|^denna[\ ".,;]|[\ ".,;]$denna'
