DROP TABLE IF EXISTS Login;
DROP TABLE IF EXISTS Information;

CREATE TABLE IF NOT EXISTS `Login` (
  `ID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `Username`	TEXT NOT NULL,
  `Password`	TEXT NOT NULL
);

INSERT INTO 'Login'('Username','Password') VALUES ('admin','admin');

CREATE TABLE IF NOT EXISTS `Information` (
  `ID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `Name`	TEXT NOT NULL,
  `Date of birth`	TEXT NOT NULL,
  `Date of death`	TEXT NOT NULL,
  `Information`	TEXT NOT NULL
  `Cemetery section`	TEXT NOT NULL
  `Grave number`	TEXT NOT NULL
  `Image`	TEXT NOT NULL
);

INSERT INTO 'Inforamtion'('Name', 'Date of birth', 'Date of death', 'Information', 'Cemetery section', 'Grave number', 'Image') VALUES ('', '', '', '', '')
