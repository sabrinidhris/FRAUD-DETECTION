CREATE DATABASE fraud_analysis;
use fraud_analysis;
CREATE TABLE transactions(step INT,type VARCHAR(20),
amount DOUBLE,nameorig VARCHAR(20),
oldbalanceorg DOUBLE,newbalanceorg DOUBLE,namedest VARCHAR(20),
 oldbalancedest DOUBLE,newbalancedest DOUBLE,isfraud TINYINT);
SELECT COUNT(*) AS total_rows, SUM(isfraude) AS fraud_count
 FROM transactions; 
 SELECT sum(isfraude) as fraud_count
 FROM transactions
 GROUP BY type;