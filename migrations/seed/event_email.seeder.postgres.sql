--liquibase formatted sql

--changeset robert.julianto:init-data-user
INSERT INTO ${database.defaultSchemaName}.user (first_name, last_name, email, city, country) VALUES
    ('Roberto', 'Julianto', 'bertoliant@gmail.com', 'Jakarta', 'Indonesia'),
    ('Ki', 'Caustick', 'kcaustick0@csmonitor.com', 'Kawengan', 'Indonesia'),
    ('Meriel', 'Wells', 'mwells1@cbslocal.com', 'Serrinha', 'Portugal'),
    ('Alastair', 'MacKellen', 'amackellen2@vkontakte.ru', 'Vanderbijlpark', 'South Africa'),
    ('Jasmine', 'Vaines', 'jvaines3@google.cn', 'Sugihwaras', 'Indonesia'),
    ('Jordain', 'Kerbler', 'jkerbler4@domainmarket.com', 'Parizh', 'Russia'),
    ('Tait', 'Merrydew', 'tmerrydew5@springer.com', 'Linzi', 'China'),
    ('Lolly', 'Lavers', 'llavers6@bravesites.com', 'Slatyne', 'Ukraine'),
    ('Gun', 'Teml', 'gteml7@noaa.gov', 'Gujrāt', 'Pakistan'),
    ('Bale', 'McAirt', 'bmcairt8@virginia.edu', 'Banyliv', 'Ukraine'),
    ('Elysia', 'Champneys', 'echampneys9@nydailynews.com', 'Oju', 'Nigeria'),
    ('Von', 'Litherland', 'vlitherlanda@privacy.gov.au', 'Cravinhos', 'Brazil'),
    ('Kalle', 'Loude', 'kloudeb@fda.gov', 'Limushan', 'China'),
    ('Cathlene', 'Dore', 'cdorec@symantec.com', 'Taisen-ri', 'South Korea'),
    ('Pattie', 'Kamena', 'pkamenad@webmd.com', 'Pedro García', 'Dominican Republic'),
    ('Dyane', 'Warr', 'dwarre@psu.edu', 'Shīrvān', 'Iran'),
    ('Baron', 'Seal', 'bsealf@typepad.com', 'Périgueux', 'France'),
    ('Vilma', 'Wisniowski', 'vwisniowskig@dyndns.org', 'Boussé', 'Burkina Faso'),
    ('Eimile', 'Yokelman', 'eyokelmanh@mapquest.com', 'Guimba', 'Philippines'),
    ('Vale', 'Cubuzzi', 'vcubuzzii@example.com', 'Lai Lai Bisi Kopan', 'Indonesia'),
    ('Gerry', 'Langsdon', 'glangsdonj@w3.org', 'Si Sa Ket', 'Thailand'),
    ('Rhodia', 'Gothup', 'rgothupk@opensource.org', 'Romorantin-Lanthenay', 'France'),
    ('Willey', 'Worham', 'wworhaml@indiatimes.com', 'Santa Rita Aplaya', 'Philippines'),
    ('Angelica', 'Pettengell', 'apettengellm@amazonaws.com', 'Cagliari', 'Italy'),
    ('Teodora', 'Cawsey', 'tcawseyn@latimes.com', 'Abu Dhabi', 'United Arab Emirates'),
    ('Worden', 'Yabsley', 'wyabsleyo@disqus.com', 'Svetlyy', 'Russia'),
    ('Zea', 'Myhan', 'zmyhanp@amazon.de', 'Chengdong', 'China'),
    ('Aeriel', 'Hutchings', 'ahutchingsq@independent.co.uk', 'Gubo', 'China'),
    ('Dallis', 'Oran', 'doranr@webeden.co.uk', 'Manzë', 'Albania'),
    ('Stace', 'Whines', 'swhiness@reverbnation.com', 'Staraya Mayna', 'Russia'),
    ('Emlen', 'Matczak', 'ematczakt@whitehouse.gov', 'Jingang', 'China');

--changeset robert.julianto:init-data-admin
INSERT INTO ${database.defaultSchemaName}.admin (first_name, last_name, email, password, city, country) VALUES
    ('Ilse', 'Humbles', 'ihumbles0@blogspot.com', 'PasswordAdmin1', 'Kedian',  'China'),
    ('Hugo', 'Simonel', 'hsimonel1@blogtalkradio.com', 'PasswordAdmin2', 'Nova Venécia',  'Brazil')

--changeset robert.julianto:init-data-event
INSERT INTO ${database.defaultSchemaName}.event (
        name, description, date_time, venue, venue_address, venue_latitude, venue_longitude, city, country, pic, pic_contact, created_by
    ) VALUES
    ('Aggregate Robust Supply-Chains', 'Mauris lacinia sapien quis libero.', '2022-09-27T05:19:37Z', 'Wikizz', '6 Tennyson Circle', -33.1519145, 18.6642088, 'Moorreesburg', 'South Africa', 'Sherwin Legat', '171-684-4856', 'ihumbles0@blogspot.com'),
    ('Harness Efficient E-Markets', 'Sed accumsan felis. Ut at dolor quis odio consequat varius. Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi. Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus. Nulla suscipit ligula in lacus. Curabitur at ipsum ac tellus semper interdum.', '2022-01-31T13:38:07Z', 'Babbleblab', '01 Valley Edge Drive', 39.6445351, -8.5226286, 'Alburitel', 'Portugal', 'Roger Duquesnay', '615-588-2355', 'hsimonel1@blogtalkradio.com'),
    ('Cultivate Proactive Web Services', 'Nulla tellus. In sagittis dui vel nisl.', '2021-11-13T15:48:28Z', 'Mydo', '34 Erie Lane', 52.300713, -1.6462357, 'Hatton', 'United Kingdom', 'Carree Ibel', '592-453-8956', 'ihumbles0@blogspot.com'),
    ('Leverage Robust E-commerce', 'Morbi non quam nec dui luctus rutrum. Nulla tellus. In sagittis dui vel nisl. Duis ac nibh.', '2022-08-02T02:45:15Z', 'Youspan', '94 Fuller Parkway', 54.9787385, 83.1136054, 'Novolugovoye', 'Russia', 'Pryce Moye', '634-364-7065', 'hsimonel1@blogtalkradio.com'),
    ('Big Data and IoT', 'Morbi non quam nec dui luctus rutrum. Nulla tellus. In sagittis dui vel nisl. Duis ac nibh.', '2023-08-02T02:45:15Z', 'Youspan', '94 Fuller Parkway', 54.9787385, 83.1136054, 'Novolugovoye', 'Russia', 'Pryce Moye', '634-364-7065', 'hsimonel1@blogtalkradio.com');

--changeset robert.julianto:init-data-reservation
INSERT INTO ${database.defaultSchemaName}.reservation (event_id, user_id) VALUES
    (4, 20),
    (2, 3),
    (4, 30),
    (4, 6),
    (1, 23),
    (2, 14),
    (2, 9),
    (4, 29),
    (2, 30),
    (3, 30),
    (4, 15),
    (4, 25),
    (1, 22),
    (4, 8),
    (1, 8),
    (4, 16),
    (3, 28),
    (1, 10),
    (2, 17),
    (2, 8),
    (4, 30),
    (1, 23),
    (3, 24),
    (1, 22),
    (2, 6),
    (4, 26),
    (4, 20),
    (2, 19),
    (1, 28),
    (2, 19),
    (1, 29),
    (2, 6),
    (2, 3),
    (1, 21),
    (4, 22),
    (4, 15),
    (2, 27),
    (3, 8),
    (4, 18),
    (3, 2),
    (2, 17),
    (3, 3),
    (2, 6),
    (3, 14),
    (4, 29),
    (5, 1);
