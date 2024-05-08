INSERT INTO staff (name_staff, id_team, encharge, picture)
VALUES 
('GHOST', (SELECT id_team FROM team WHERE name_team = 'Black Dragons'), 'coach', 'https://static-esports.ubisoft.com/esports-platform/common/members/4a6b523b-0fc0-4a53-838a-2d063117405b.png'),
('KIZI', (SELECT id_team FROM team WHERE name_team = 'E1 Sports'), 'coach', 'https://static-esports.ubisoft.com/esports-platform/common/members/873f62cf-034e-413a-870f-5b59a370e3a1.png'),
('RAFADELL', (SELECT id_team FROM team WHERE name_team = 'Faze Clan'), 'coach', 'https://static-esports.ubisoft.com/esports-platform/common/members/d363c253-e60d-44ae-98a6-b7489187b94c.png'),
('PANDEX', (SELECT id_team FROM team WHERE name_team = 'Fluxo'), 'coach', 'https://static-esports.ubisoft.com/esports-platform/common/members/255a53f4-f2d3-4df0-be1c-12c56ed90a44.png'),
('IGOORCTG', (SELECT id_team FROM team WHERE name_team = 'Furia Esports'), 'coach', 'https://static-esports.ubisoft.com/esports-platform/common/members/00b18da2-d8d9-4f56-b7fa-7b80319e729d.png'),
('ABREU', (SELECT id_team FROM team WHERE name_team = 'Furia Esports'), 'analist', 'https://static-esports.ubisoft.com/esports-platform/common/members/9f3c283b-5d42-42c7-b381-ffd00334ba45.png'),
('DUDDS', (SELECT id_team FROM team WHERE name_team = 'MIBR'), 'coach', 'https://static-esports.ubisoft.com/esports-platform/common/members/abbdadf7-60b1-463c-91c3-72f9e4766cbb.png'),
('GUILLE', (SELECT id_team FROM team WHERE name_team = 'MIBR'), 'manager', 'https://static-esports.ubisoft.com/esports-platform/common/members/ab5a7b2b-228b-4a58-be0a-dece6177c5c4.png'),
('TCHUBZ', (SELECT id_team FROM team WHERE name_team = 'Ninja in Pyjamas'), 'coach', 'https://static-esports.ubisoft.com/esports-platform/common/members/8bad3211-ba41-420a-9f39-4f68e4f22a33.png'),
('HUGZORD', (SELECT id_team FROM team WHERE name_team = 'Team Liquid'), 'coach', 'https://static-esports.ubisoft.com/esports-platform/common/members/0bcd14be-0f7f-4e79-ac0f-e4f6b35613c5.png'),
('NORRIS', (SELECT id_team FROM team WHERE name_team = 'W7M'), 'coach', 'https://static-esports.ubisoft.com/esports-platform/common/members/63573367-769f-429d-9285-01a76185b39b.png'),
('THUG', (SELECT id_team FROM team WHERE name_team = 'W7M'), 'analist', 'https://static-esports.ubisoft.com/esports-platform/common/members/02b870ac-4a0e-4b9f-b329-b5f1c8e76f9e.png'),
('RICKZZ', (SELECT id_team FROM team WHERE name_team = 'Vivo Keyd Stars'), 'coach', 'https://static-esports.ubisoft.com/esports-platform/common/members/2c7be9ca-7105-4d9e-bd15-b4a7a1c7c9d6.png');
