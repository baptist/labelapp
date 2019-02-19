drop table if exists recordings;
create table recordings (
  id integer primary key autoincrement,
  name varchar(250),
  description text,
  started_at datetime,
  stopped_at datetime,
  duration int,
  parameters_id integer,
  range tinyint(1),
  doppler tinyint(1),
  azimuth tinyint(1),
  has_video tinyint(1),
  fps tinyint(4),
  merged_to integer,
  status tinyint(4),
  processed tinyint(1) default(0)
);

drop table if exists labels;
create table labels (
  id integer primary key autoincrement,
  name varchar(250) not null unique,
  subclass_of integer(4) null
);

drop table if exists people;
create table people (
  id integer primary key autoincrement,
  name varchar(150) not null unique,
  role integer null
);

drop table if exists recordings_people;
create table recordings_people (
  recording_id integer not null,
  person_id integer not null,
  primary key (recording_id, person_id)
);

drop table if exists recordings_labels;
create table recordings_labels (
  recording_id integer not null,
  label_id integer not null,
  primary key (recording_id, label_id)
);

drop table if exists radar_parameters;
create table radar_parameters (
  id integer primary key autoincrement,
  label varchar(150),
  fStrt double,
  fStop double,
  TRampUp double,
  TRampDo double,
  N integer,
  Np integer,
  Tp double,
  fs double,
  kf double,
  NrChn integer,
  unique (fStrt, fStop, TRampUp, TRampDo, N, Np, Tp, fs, kf, NrChn)
);

insert into radar_parameters values (0, 'default', 76250000000, 77750000000, 0.000128, 0.000064, 256, 256, 0.000256, 2000000.0, 11718750000000, 1);