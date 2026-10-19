-- RoomSafe database schema (empty). Create the database with: python init_db.py

CREATE TABLE "Files" (outdoor integer, Qbh integer, Cqh integer, Event_ID integer, name text, location text, localinci integer, event_date text, stime text, recirculation integer, filtration integer, humidity integer, ceiling integer, surfarea integer, User_ID text, NEGuest INTEGER, minutes INTEGER, hours INTEGER, PassReq text, MaskReq text, ServMode text, ServTiming text, ServHours INTEGER, ServMinutes INTEGER, Description text, RScore text, LastUpdate text, ageAvg interger, RiskTolerance INTEGER, SafeGuest INTEGER, GuestsReg INTEGER NOT NULL DEFAULT '0');

CREATE TABLE 'GuestLogs' ('Qb' integer, 'pm' integer, 'Cq' integer, 'Vs' text, 'Vt' text, 'Tm' integer, 'Th' integer, 'Event_ID' integer, 'Event_Name' text, 'username' text, 'event_date' text, GuestLastUpdate text, RScoreGuest text, age interger);

CREATE TABLE 'users' ('username' text, 'hash' text, 'id'  integer PRIMARY KEY  , email text);
