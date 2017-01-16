CREATE TABLE campaigns
(
  uuid          uuid PRIMARY KEY,
  name          varchar(120) NOT NULL,
  description   text,
  age           integer
);
