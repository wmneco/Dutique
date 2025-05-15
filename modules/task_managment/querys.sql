-- Insert or ignore room into database
INSERT OR IGNORE INTO rooms (name, room_type) VALUES ('room1', 'living_room');

-- Insert or ignore room furnishing into database
INSERT OR IGNORE INTO room_furnishings (name, room_name) VALUES ('bed', 'living_room');

-- Insert or ignore task into database
INSERT OR IGNORE INTO action ()