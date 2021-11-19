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
  `Information`	TEXT NOT NULL,
  `Cemetery section`	TEXT NOT NULL,
  `Grave number`	TEXT NOT NULL,
  `Image`	TEXT NOT NULL
);

INSERT INTO 'Information'('Name', 'Date of birth', 'Date of death', 'Information', 'Cemetery section', 'Grave number', 'Image') VALUES ('Albert Watkins', 'N/A', '21 December 1916', 'Chief engineer on board the ship "Rheims", died of consumption at Spezia, Italy.', 'COND40', '191', '')
INSERT INTO 'Information'('Name', 'Date of birth', 'Date of death', 'Information', 'Cemetery section', 'Grave number', 'Image') VALUES ('Edward SCAPLEHORN', 'N/A', '7 August 1918', 'Royal Field Artillery, 740902, 463rd Batt., Mon. Regt. CROUY British Cemetery, Crouy-Sur-Somme, France. Son of Charles & Clara Ann Scaplehorn, of 94 Commercial Street, Newport.', 'FCD08', '15', '')
INSERT INTO 'Information'('Name', 'Date of birth', 'Date of death', 'Information', 'Cemetery section', 'Grave number', 'Image') VALUES ('Arthur John DORAN', 'N/A', '4 November 1918', 'Memorial on Family Headstone, killed in France ', 'FCD08', '318', '')
INSERT INTO 'Information'('Name', 'Date of birth', 'Date of death', 'Information', 'Cemetery section', 'Grave number', 'Image') VALUES ('Francis John LIMBRICK', 'N/A', '5 February 1919', '3rd Western General Hospital, Cardiff, of wounds, aged 24. 5th Brigade, Royal Field Artillery, 740824. Bombadier. Son of George & Harriet Limbrick of 15 Pugsley Street, Newport.', 'COND09', '235', '')
INSERT INTO 'Information'('Name', 'Date of birth', 'Date of death', 'Information', 'Cemetery section', 'Grave number', 'Image') VALUES ('David Smith', 'N/A', '16 May 1915', 'Private David Smith NEKREWES, Monmouthshire Regiment, A Company, 3rd Btn. Killed in action at Frenzenberg, aged 32. Son of Ellen Nekrewes, 3 Carisbrooke Road, Newport and the late David Smith Nekrewes.', 'FCD08', '289', '')


