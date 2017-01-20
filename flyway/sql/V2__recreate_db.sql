DROP TABLE campaigns;

CREATE TABLE organization
(
  uuid            uuid PRIMARY KEY,
  name            varchar(120) NOT NULL,
  country         varchar(100),
  state           varchar(100),
  street_address  text,                   -- free form address
  logo            text                    -- file path
);

CREATE TABLE organization_contact_infos
(
  uuid            uuid PRIMARY KEY,
  type            varchar(50) NOT NULL, -- phone, mail, email, Facebook, twitter, etc.
  contact_info    text NOT NULL,        -- contact info
  details         text                  -- additional info (time of day they can answer phone, who to talk to, etc.)
);

CREATE TABLE rescuee
(
  uuid             uuid PRIMARY KEY,
  id               varchar(120) NOT NULL UNIQUE,   -- use this to store user friendly ids (slugs)
  name             varchar(120) NOT NULL,
  kind             varchar(100) NOT NULL,          -- dog, cat, narwhal, etc.
  age              integer,
  size             integer,
  weight           numeric(2),
  sex              varchar(50),
  sterilized       boolean,                        -- spayed/neutered
  health_status    text,
  temperament      varchar(100),
  description      text,
  profile_pic      text,                           -- file path
  date_of_rescue   date,
  date_of_adoption date
);

CREATE TABLE rescuee_pictures
(
  uuid            uuid PRIMARY KEY,
  rescuee         uuid REFERENCES rescuee(uuid),
  filepath        text,
  width           integer,
  heigth          integer
);

CREATE TABLE campaign
(
 uuid               uuid PRIMARY KEY,
 rescuee            uuid REFERENCES rescuee(uuid) NOT NULL,
 type               varchar(100) NOT NULL,                  -- food, medical bills, vaccines, spaying/neutering, etc.,
 goal               numeric(2) NOT NULL,
 current_amount     numeric(2) NOT NULL
);

CREATE TABLE donor
(
 uuid        uuid PRIMARY KEY,
 name        varchar(120) NOT NULL,
 email       text,                            -- should be mandatory for users to donate/upvote, but not for donors who go to the NPO and adopted an animal
 verified    boolean NOT NULL DEFAULT false
);

CREATE TABLE pending_validation (
  uuid        uuid PRIMARY KEY,
  donor       uuid REFERENCES donor(uuid) NOT NULL,
  expiration  timestamp NOT NULL                        -- not valid after this
);

