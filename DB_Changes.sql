ALTER TABLE commandmaster ADD COLUMN MasterCommandID INT;
                    
INSERT INTO tokentype (TypeID, TypeName, significance) VALUES (11, 'CUSTOM', 'Custom token generated from custom command');

INSERT INTO tokentype (TypeID, TypeName, significance) VALUES (12, 'UNDEFINED', 'Undefined token');

UPDATE token SET TypeID = 12 WHERE TokenID = 24;