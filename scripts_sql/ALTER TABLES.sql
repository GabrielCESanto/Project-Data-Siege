ALTER TABLE matchs
ADD CONSTRAINT FK_id_md1 FOREIGN KEY (id_md1)
REFERENCES map_ban_md1(id_md1);
ALTER TABLE matchs
ADD CONSTRAINT FK_id_md3 FOREIGN KEY (id_md3)
REFERENCES  map_ban_md3(id_md3);
ALTER TABLE matchs
ADD CONSTRAINT FK_id_ban1 FOREIGN KEY (id_ban1)
REFERENCES  ban_operator(id_ban);
ALTER TABLE matchs
ADD CONSTRAINT FK_id_ban2 FOREIGN KEY (id_ban2)
REFERENCES ban_operator(id_ban);
ALTER TABLE matchs
ADD CONSTRAINT FK_id_map1 FOREIGN KEY (id_map1)
REFERENCES maps(id_map);
ALTER TABLE matchs
ADD CONSTRAINT FK_id_map2 FOREIGN KEY (id_map2)
REFERENCES maps(id_map);
ALTER TABLE matchs
ADD CONSTRAINT FK_id_map3 FOREIGN KEY (id_map3)
REFERENCES maps(id_map);
ALTER TABLE matchs
ADD CONSTRAINT FK_id_team1 FOREIGN KEY (id_team1)
REFERENCES team(id_team);
ALTER TABLE matchs
ADD CONSTRAINT FK_id_team2 FOREIGN KEY (id_team2)
REFERENCES team(id_team);

ALTER TABLE team_match
ADD CONSTRAINT FK_id_team FOREIGN KEY (id_team)
REFERENCES team(id_team);
ALTER TABLE team_match
ADD CONSTRAINT FK_id_match FOREIGN KEY (id_match)
REFERENCES matchs(id_match);

ALTER TABLE team
ADD CONSTRAINT FK2_id_region FOREIGN KEY (id_region)
REFERENCES region(id_region);

ALTER TABLE staff
ADD CONSTRAINT FK2_id_team FOREIGN KEY (id_team)
REFERENCES team(id_team);

ALTER TABLE player
ADD CONSTRAINT FK3_id_team FOREIGN KEY (id_team)
REFERENCES team(id_team);


ALTER TABLE player_match
ADD CONSTRAINT FK2_id_player FOREIGN KEY (id_player)
REFERENCES player(id_player);
ALTER TABLE player_match
ADD CONSTRAINT FK2_id_match FOREIGN KEY (id_match)
REFERENCES matchs(id_match);
ALTER TABLE player_match
ADD CONSTRAINT FK4_id_team FOREIGN KEY (id_team)
REFERENCES team(id_team);
ALTER TABLE player_match
ADD CONSTRAINT FK_id_atk_operator FOREIGN KEY (id_atk_operator)
REFERENCES operator(id_operator);
ALTER TABLE player_match
ADD CONSTRAINT FK_id_def_operator FOREIGN KEY (id_def_operator)
REFERENCES operator(id_operator);

ALTER TABLE ban_operator
ADD CONSTRAINT FK4_id_match FOREIGN KEY (id_match)
REFERENCES matchs(id_match);
ALTER TABLE ban_operator
ADD CONSTRAINT FK6_id_team FOREIGN KEY (id_team)
REFERENCES team(id_team);
ALTER TABLE ban_operator
ADD CONSTRAINT FK_ban1 FOREIGN KEY (ban1)
REFERENCES operator(id_operator);
ALTER TABLE ban_operator
ADD CONSTRAINT FK_ban2 FOREIGN KEY (ban2)
REFERENCES moperator(id_operator);

ALTER TABLE map_ban_md1
ADD CONSTRAINT FK5_id_match FOREIGN KEY (id_match)
REFERENCES matchs(id_match);
ALTER TABLE map_ban_md1
ADD CONSTRAINT FK7_id_team FOREIGN KEY (id_team)
REFERENCES team(id_team);
ALTER TABLE map_ban_md1
ADD CONSTRAINT FK_ban1 FOREIGN KEY (ban1)
REFERENCES maps(id_map);
ALTER TABLE map_ban_md1
ADD CONSTRAINT FK_ban2 FOREIGN KEY (ban2)
REFERENCES maps(id_map);
ALTER TABLE map_ban_md1
ADD CONSTRAINT FK_ban3 FOREIGN KEY (ban3)
REFERENCES maps(id_map);
ALTER TABLE map_ban_md1
ADD CONSTRAINT FK_ban4 FOREIGN KEY (ban4)
REFERENCES maps(id_map);
ALTER TABLE map_ban_md1
ADD CONSTRAINT FK_pick FOREIGN KEY (pick)
REFERENCES maps(id_map);

ALTER TABLE map_ban_md3
ADD CONSTRAINT FK6_id_match FOREIGN KEY (id_match)
REFERENCES matchs(id_match);
ALTER TABLE map_ban_md3
ADD CONSTRAINT FK8_id_team FOREIGN KEY (id_team)
REFERENCES team(id_team);
ALTER TABLE map_ban_md3
ADD CONSTRAINT FK_ban1 FOREIGN KEY (ban1)
REFERENCES maps(id_map);
ALTER TABLE map_ban_md3
ADD CONSTRAINT FK_ban2 FOREIGN KEY (ban2)
REFERENCES maps(id_map);
ALTER TABLE map_ban_md3
ADD CONSTRAINT FK_pick FOREIGN KEY (pick)
REFERENCES maps(id_map);
ALTER TABLE map_ban_md3
ADD CONSTRAINT FK_ban3 FOREIGN KEY (ban3)
REFERENCES maps(id_map);
ALTER TABLE map_ban_md3
ADD CONSTRAINT FK_decider FOREIGN KEY (decider)
REFERENCES maps(id_map);