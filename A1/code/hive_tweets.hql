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

SELECT count(text) FROM tweets
WHERE retweeted.status.id_str is not NULL and text RLIKE '[\ ".,;]hon[\ ".,;]|^hon[\ ".,;]'






CREATE TABLE tweets_count
AS SELECT temptable.word, temptable.count(*)
FROM tweets AS t
WHERE t.retweeted_status.id_str AND LOWER(temptable.word) RLIKE '(hon)|(han|den|det|denna|denne)'
LATERAL VIEW explode (split(text, '')) temptable AS word
GROUP BY word ORDER BY count DESC;
