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


INSERT INTO 'Information'('Name', 'Date of birth', 'Date of death', 'Information', 'Cemetery section', 'Grave number', 'Image') VALUES ('George Gratton','N/A' , 'N/A', 'George Grattan did not join the war until much later. The month after the war began; the Rhondda Leader announced that the 26 year old from Newport had taken over the management of the Tonypandy Cinema. Prior to that he had been working in Newport’s Lyceum Theatre where his brother in law was the manager.', ' ST. WOOLOS CEMETERY', '')
INSERT INTO 'Information'('Name', 'Date of birth', 'Date of death', 'Information', 'Cemetery section', 'Grave number', 'Image') VALUES (' Charles James WATKINS', 'N/A', ' 14 June 1918', 'Charles James WATKINS, 19, killed in action 14 June 1918 in France. Cheshire Regt., Private 66867. Son of Charles & Elizabeth Ann Watkins, 32 Upton Road, Newport.', 'block 78', 'Grave 352')
INSERT INTO 'Information'('Name', 'Date of birth', 'Date of death', 'Information', 'Cemetery section', 'Grave number', 'Image') VALUES ('Abram Thomas', 'N/A', 'Died 15 September 1916', 'Soldier and Welsh language poet, winner of three Bardic Chairs. Son of Mary Thomas and the late Evan Thomas of Penddol, Llanbrynmair, Montgomeryshire, Powys.', 'Block 17', 'Grave 133')
INSERT INTO 'Information'('Name', 'Date of birth', 'Date of death', 'Information', 'Cemetery section', 'Grave number', 'Image') VALUES ('George Augustus ', 'N/A', '19 June 1916 ', 'Monmouthshire Regiment, Rifleman 3474. Killed in action 19 June 1916 at the Somme. Foncquevillers Military Cemetery, France.', 'block 8', 'Grave 174')
INSERT INTO 'Information'('Name', 'Date of birth', 'Date of death', 'Information', 'Cemetery section', 'Grave number', 'Image') VALUES ('Thomas BIGMORE', 'N/A', '17 March 1900', 'Royal Garrison Artillery. Son of Simon & Helen BIGMORE. Family were living at 12 David Street, Newport, in 1901.', 'block 78', 'Grave 224')
