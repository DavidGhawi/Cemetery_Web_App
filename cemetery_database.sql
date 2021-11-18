DROP TABLE IF EXISTS Login;

CREATE TABLE IF NOT EXISTS `Login` (
  `ID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `Username`	TEXT NOT NULL,
  `Password`	TEXT NOT NULL
);

INSERT INTO 'Login'('Username','Password') VALUES ('admin','admin');
