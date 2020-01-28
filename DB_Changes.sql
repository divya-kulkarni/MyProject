ALTER TABLE commandmaster ADD COLUMN MasterCommandID INT;
                    
INSERT INTO tokentype (TypeID, TypeName, significance) VALUES (11, 'CUSTOM', 'Custom token generated from custom command');
