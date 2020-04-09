"""Data anylisis of a restaurant order data"""

data = [
    {'order_id': '355c96f5-944e-4ef6-977b-6972df7b8f93', 'price': 3000,
        'customer': 'Gerrie Killshaw', 'type': 'takeaway', 'district': None, 'note': None, 'review': 5},
    {'order_id': 'ebc2b077-d18a-492d-86b7-81756205fe29', 'price': 2100, 'customer': 'Kristan Northway',
        'type': 'dine-in', 'district': None, 'note': None, 'review': None},
    {'order_id': '68a74baf-03fe-46ca-a3c4-88972a43efbc', 'price': 3400, 'customer': 'Jodee Spinas',
        'type': 'takeaway', 'district': None, 'note': None, 'review': None},
    {'order_id': 'e53b4a58-c189-4bbb-b549-99bdbe0370f9', 'price': 3400,
        'customer': 'Rozalie Henrique', 'type': 'dine-in', 'district': None, 'note': None, 'review': 5},
    {'order_id': '47afe099-8744-42e9-971b-0a9e3c3f11c6', 'price': 3500, 'customer': 'Ignacius Broadis',
        'type': 'delivery', 'district': 'VIII', 'note': None, 'review': 4},
    {'order_id': '187b9e0c-4f36-458b-8fe9-d206a6844b11', 'price': 2000,
        'customer': 'Bearnard Allchin', 'type': 'takeaway', 'district': None, 'note': None, 'review': 1},
    {'order_id': '98ce7a47-6405-4b90-a71e-34b4272774bc', 'price': 2600,
        'customer': 'Denis Mc Caughan', 'type': 'dine-in', 'district': None, 'note': None, 'review': 3},
    {'order_id': 'f1d937d3-c1e2-4569-8a99-187fe3f65c6e', 'price': 1400, 'customer': 'Batsheva Emanuelov',
        'type': 'takeaway', 'district': None, 'note': None, 'review': None},
    {'order_id': 'e875317e-94f2-417a-bff7-5ae783087ab0', 'price': 2400,
        'customer': 'Yevette Lewisham', 'type': 'takeaway', 'district': None, 'note': None, 'review': 3},
    {'order_id': '89901429-1ebf-490e-a9e0-75c3f9c4ce0d', 'price': 11000,
        'customer': 'Ramona Norvell', 'type': 'dine-in', 'district': None, 'note': None, 'review': 2},
    {'order_id': '272af23c-bfe9-4228-ac7c-ace5c4d6271a', 'price': 1400, 'customer': 'Blondell Klimko',
        'type': 'dine-in', 'district': None, 'note': 'ketchup', 'review': 3},
    {'order_id': 'd686e01d-2ca9-45f4-ba11-1a3556a5981e', 'price': 3100,
        'customer': 'Becki Mettericke', 'type': 'dine-in', 'district': None, 'note': None, 'review': 2},
    {'order_id': '855efeac-c6f0-4a4b-a5ae-b492db5354e0', 'price': 2000, 'customer': 'Maura Aspey',
        'type': 'delivery', 'district': 'VIII', 'note': None, 'review': None},
    {'order_id': '2fa0a6ca-172f-47ff-b8c8-67e6e99d0d74', 'price': 1300,
        'customer': 'Babara Bolitho', 'type': 'takeaway', 'district': None, 'note': None, 'review': 3},
    {'order_id': '8ffa92ba-e5b7-419b-9d73-c57cb13d74a7', 'price': 2600, 'customer': 'Kenneth Southby',
        'type': 'delivery', 'district': 'VII', 'note': None, 'review': 4},
    {'order_id': 'b55ddbc1-e841-46c0-9ff4-395fdd2b4935', 'price': 1300,
        'customer': 'Grantham Bolley', 'type': 'takeaway', 'district': None, 'note': None, 'review': 1},
    {'order_id': '762505e8-5704-411e-8000-5b029d4d9103', 'price': 12000,
        'customer': 'Lauraine Boss', 'type': 'delivery', 'district': 'VI', 'note': None, 'review': 3},
    {'order_id': 'e9f475fa-f04c-4ef9-a75f-f28bc128b44a', 'price': 2700, 'customer': 'Ivette McElmurray',
        'type': 'dine-in', 'district': None, 'note': None, 'review': None},
    {'order_id': '192004d5-5708-489a-9697-3a43537a2ec9', 'price': 11100,
        'customer': 'Cecilius Downage', 'type': 'dine-in', 'district': None, 'note': None, 'review': 3},
    {'order_id': '007e649f-99ef-4cda-942a-ba7e636c95d6', 'price': 2200, 'customer': 'Winne Spurgin',
        'type': 'dine-in', 'district': None, 'note': 'ketchup', 'review': 2},
    {'order_id': '516d6688-182d-45a9-bab6-e6e8a972def9', 'price': 3400, 'customer': 'Marlie Towlson',
        'type': 'takeaway', 'district': None, 'note': 'több saláta', 'review': None},
    {'order_id': 'd2e0854e-fe17-4bfa-88d3-aced4e249c71', 'price': 2100,
        'customer': 'Shea Fance', 'type': 'dine-in', 'district': None, 'note': None, 'review': 1},
    {'order_id': 'f5f05bfd-c04e-49fa-ae76-1e0dbe3756ad', 'price': 3200,
        'customer': 'Ivan Walrond', 'type': 'delivery', 'district': 'VI', 'note': None, 'review': 3},
    {'order_id': '316984c0-8340-469d-9a7f-44e103bd9feb', 'price': 1800,
        'customer': 'Lauraine Boss', 'type': 'dine-in', 'district': None, 'note': None, 'review': 1},
    {'order_id': '112fddf6-a32a-4f06-9e16-a18282a3ed45', 'price': 9600, 'customer': 'Cathe Triner',
        'type': 'delivery', 'district': 'XIV', 'note': None, 'review': None},
    {'order_id': 'a08d59be-1a36-4f26-a831-4b5c65a8f304', 'price': 6200, 'customer': 'Quintina Belderfield',
        'type': 'takeaway', 'district': None, 'note': None, 'review': None},
    {'order_id': 'dde29033-eb2d-4de9-a8ac-80d177729531', 'price': 1400,
        'customer': 'Lexine Padbery', 'type': 'delivery', 'district': 'VI', 'note': None, 'review': 4},
    {'order_id': '3cc7d813-49a2-46bb-8e75-e2304cdb3a3f', 'price': 9900, 'customer': 'Hillie Tanton',
        'type': 'dine-in', 'district': None, 'note': None, 'review': None},
    {'order_id': 'b58f63f4-7d72-4a45-9309-83702ba4163d', 'price': 2800, 'customer': 'Ag Sabathe',
        'type': 'delivery', 'district': 'VII', 'note': 'hagyma nélkül', 'review': None},
    {'order_id': '03e3ac5f-2795-4147-9732-a6ff11066c44', 'price': 6800, 'customer': 'Sybilla Albin',
        'type': 'delivery', 'district': 'VI', 'note': None, 'review': None},
    {'order_id': 'e512e8b3-849c-4c09-8b78-1009e3eeb407', 'price': 1700, 'customer': 'Hubert Vereker',
        'type': 'takeaway', 'district': None, 'note': 'több saláta', 'review': 2},
    {'order_id': '73a0ddbb-134d-4bb3-aa29-482018ba8471', 'price': 1600, 'customer': 'Courtnay Sillick',
        'type': 'takeaway', 'district': None, 'note': None, 'review': None},
    {'order_id': '097b5fd8-b2fe-4b5b-a486-4cb2abb105a8', 'price': 9400,
        'customer': 'Sibel Fanthom', 'type': 'dine-in', 'district': None, 'note': None, 'review': 5},
    {'order_id': '8b638f8b-b587-4c73-9d4d-328dcc14fe1f', 'price': 3100, 'customer': 'Kiersten McPeeters',
        'type': 'takeaway', 'district': None, 'note': None, 'review': None},
    {'order_id': '247b6998-e66d-4843-9288-e0face7319a0', 'price': 1900, 'customer': 'Emory Meader',
        'type': 'delivery', 'district': 'VIII', 'note': None, 'review': None},
    {'order_id': 'b2ca2f74-7137-47af-80d2-b6e8ebc21bcd', 'price': 6800, 'customer': 'Upton Scroxton',
        'type': 'dine-in', 'district': None, 'note': None, 'review': None},
    {'order_id': '56b91e64-4692-4aeb-b54f-6e6c206b6ad8', 'price': 2400,
        'customer': 'Phaidra Etoile', 'type': 'dine-in', 'district': None, 'note': None, 'review': 3},
    {'order_id': 'c9d3af1a-ae22-46a5-b583-b0c22bd42d60', 'price': 6900,
        'customer': 'Gloriane Dumbarton', 'type': 'dine-in', 'district': None, 'note': None, 'review': 1},
    {'order_id': '47474c8a-58c1-4710-8e92-0f19ebb17b77', 'price': 11200,
        'customer': 'Dusty Curton', 'type': 'delivery', 'district': 'VI', 'note': None, 'review': 1},
    {'order_id': '6d76cbaf-dd9e-4953-a2ff-3d2719977367', 'price': 9600,
        'customer': 'Raven McKeaney', 'type': 'takeaway', 'district': None, 'note': None, 'review': 3},
    {'order_id': 'c2ca011a-0606-45dd-90f1-cfd5895cab8b', 'price': 8100,
        'customer': 'Caril Olsen', 'type': 'dine-in', 'district': None, 'note': None, 'review': 2},
    {'order_id': 'ca055d4f-f2b5-45cf-8155-a36b1a518c25', 'price': 3300,
        'customer': 'Yvonne Ricci', 'type': 'delivery', 'district': 'VI', 'note': None, 'review': 4},
    {'order_id': '569b7e04-5aee-4b44-905f-94adbb2ee2aa', 'price': 2400, 'customer': 'Donielle Teather',
        'type': 'takeaway', 'district': None, 'note': 'hagyma nélkül', 'review': 1},
    {'order_id': 'e6424af3-4f47-407a-a31a-2f3c4d466e30', 'price': 2100,
        'customer': 'Shellysheldon Cristofori', 'type': 'dine-in', 'district': None, 'note': None, 'review': 2},
    {'order_id': '464929c1-462b-4a20-910f-3b8d2232e806', 'price': 4100,
        'customer': 'Alonso Butter', 'type': 'delivery', 'district': 'VI', 'note': None, 'review': 4},
    {'order_id': '6a6f6ee5-9188-47f4-a7d8-59d72f176981', 'price': 3400,
        'customer': 'Olivette Aronsohn', 'type': 'takeaway', 'district': None, 'note': None, 'review': 3},
    {'order_id': '96d674fc-9bd1-40c2-8d15-3983389e8e4b', 'price': 8400,
        'customer': 'Tommie Jendrich', 'type': 'dine-in', 'district': None, 'note': None, 'review': 4},
    {'order_id': 'be27358d-389a-4f59-9eb6-2b35a0c45de1', 'price': 1800,
        'customer': 'Astrid Robens', 'type': 'takeaway', 'district': None, 'note': None, 'review': 4},
    {'order_id': 'fef27b8f-ca1e-4dfe-9bc3-5fb20974bed2', 'price': 7900, 'customer': 'Gaby McChruiter',
        'type': 'dine-in', 'district': None, 'note': None, 'review': None},
    {'order_id': '1844074a-7082-4c36-85c9-ea0817a10678', 'price': 1800, 'customer': 'Carey Labroue',
        'type': 'delivery', 'district': 'VII', 'note': None, 'review': 2},
    {'order_id': '121aa53d-365b-42d4-9b99-cc2f5b22a412', 'price': 6200, 'customer': 'Adina Chalice',
        'type': 'takeaway', 'district': None, 'note': 'több saláta', 'review': 4},
    {'order_id': 'dd30091d-4d28-473d-b915-adfea304d4d3', 'price': 2700, 'customer': 'Bennett Prando',
        'type': 'takeaway', 'district': None, 'note': 'hagyma nélkül', 'review': 4},
    {'order_id': 'c435ab18-22ee-4d4e-87b6-865a4a5bca11', 'price': 1700,
        'customer': 'Gaylor Scafe', 'type': 'dine-in', 'district': None, 'note': None, 'review': 3},
    {'order_id': '9426ed24-0c2f-4b49-a23e-1c091247bd89', 'price': 1900,
        'customer': 'Cristobal Tremmil', 'type': 'takeaway', 'district': None, 'note': None, 'review': 4},
    {'order_id': 'c9ffbf30-0835-4420-aeca-8f89ebf24285', 'price': 3200, 'customer': 'Serena Woolaghan',
        'type': 'dine-in', 'district': None, 'note': 'hagyma nélkül', 'review': None},
    {'order_id': '0938b4df-ce2e-4b54-a971-165d9f426e2a', 'price': 11600, 'customer': 'Demetris Herrema',
        'type': 'delivery', 'district': 'VIII', 'note': None, 'review': 4},
    {'order_id': '3dcfe363-41d8-4442-a644-aa26c027a6d1', 'price': 4400, 'customer': 'Amalle Briscam',
        'type': 'takeaway', 'district': None, 'note': 'több saláta', 'review': None},
    {'order_id': '54c42050-68b9-4ade-b8bc-8fe2e72750bd', 'price': 2400,
        'customer': 'Bax Lovegrove', 'type': 'dine-in', 'district': None, 'note': None, 'review': 4},
    {'order_id': 'd430e521-a26f-4dbe-bc61-4b24c716653d', 'price': 12100,
        'customer': 'Noe Ruggen', 'type': 'takeaway', 'district': None, 'note': None, 'review': 1},
    {'order_id': '55277530-5de3-4910-a835-7cf54345fd03', 'price': 2100, 'customer': 'Mara Hasslocher',
        'type': 'delivery', 'district': 'VIII', 'note': None, 'review': None},
    {'order_id': '118ec29e-ed50-406b-8d19-ed3eba2467e2', 'price': 3500, 'customer': 'Jareb Allsup',
        'type': 'dine-in', 'district': None, 'note': 'több saláta', 'review': 5},
    {'order_id': 'b090cb47-f597-400e-b92b-776b7bc2f25e', 'price': 3200, 'customer': 'Mathilde Dudeney',
        'type': 'delivery', 'district': 'VI', 'note': 'több hús', 'review': None},
    {'order_id': '5901e0c5-6853-4e97-9306-9727b8966fe3', 'price': 2900,
        'customer': 'Sibel Fanthom', 'type': 'delivery', 'district': 'VI', 'note': None, 'review': 5},
    {'order_id': '1d7aaa77-1320-42b8-b20a-a675992c5abe', 'price': 6600, 'customer': 'Remus Wynn',
        'type': 'delivery', 'district': 'VI', 'note': 'hagyma nélkül', 'review': 1},
    {'order_id': '589d21d2-9078-47ba-b5d9-180b40d9a71a', 'price': 3100, 'customer': 'Charlean Lamburne',
        'type': 'dine-in', 'district': None, 'note': None, 'review': None},
    {'order_id': '669a2604-202c-4349-b713-9e4a60588268', 'price': 4900,
        'customer': 'Johny Adenot', 'type': 'dine-in', 'district': None, 'note': None, 'review': 1},
    {'order_id': '7b972af5-c5bd-4d27-9daf-66d505e303b5', 'price': 1600, 'customer': 'Meier Englefield',
        'type': 'delivery', 'district': 'VII', 'note': 'hagyma nélkül', 'review': 4},
    {'order_id': 'bd70b570-33f8-4141-9aa9-2a96e22c3734', 'price': 5500, 'customer': 'Dicky Verrell',
        'type': 'dine-in', 'district': None, 'note': 'több saláta', 'review': None},
    {'order_id': '00894631-52e9-486e-8e4d-a0fd9ee7af7a', 'price': 2800,
        'customer': 'Pippa Yare', 'type': 'dine-in', 'district': None, 'note': None, 'review': 2},
    {'order_id': 'ca121a8f-5304-4ebd-b8ad-11d417c37f83', 'price': 5500, 'customer': 'Bennett Goosnell',
        'type': 'delivery', 'district': 'VII', 'note': None, 'review': None},
    {'order_id': 'a3403920-0a88-4c2c-9c75-5e17ad8611c1', 'price': 12000,
        'customer': 'Stanislas Gercken', 'type': 'takeaway', 'district': None, 'note': None, 'review': 4},
    {'order_id': '7aba235b-2554-4c0a-bef6-da81f2e1f6c2', 'price': 2000, 'customer': 'Arlina Frigout',
        'type': 'dine-in', 'district': None, 'note': None, 'review': None},
    {'order_id': '572ee99b-a690-44f4-9878-7fd50de815c4', 'price': 7300,
        'customer': 'Joe Bendix', 'type': 'dine-in', 'district': None, 'note': None, 'review': 2},
    {'order_id': '4a9146cd-ab82-46d0-b331-febada5f77e6', 'price': 4100, 'customer': 'Early Teacy',
        'type': 'dine-in', 'district': None, 'note': 'több saláta', 'review': 5},
    {'order_id': '6764ad73-75ad-43f9-82bf-8e2d98519977', 'price': 1300, 'customer': 'Kalvin Benjamin',
        'type': 'takeaway', 'district': None, 'note': 'több saláta', 'review': 4},
    {'order_id': '3fe615c2-caf0-4e06-adb3-c9634baab332', 'price': 4000,
        'customer': 'Mallory Oris', 'type': 'dine-in', 'district': None, 'note': None, 'review': 5},
    {'order_id': '0b193c82-fc3d-4cb2-8b6b-aa22be6ebe69', 'price': 2200, 'customer': 'Rob Searby',
        'type': 'delivery', 'district': 'VIII', 'note': None, 'review': None},
    {'order_id': '6ae03738-5cf4-423f-a024-a67dae3ff067', 'price': 6900,
        'customer': 'Carmen Garfirth', 'type': 'dine-in', 'district': None, 'note': None, 'review': 5},
    {'order_id': '77e70aa3-848c-4347-ad1d-8e6247348870', 'price': 12100,
        'customer': 'Sela Gannicott', 'type': 'takeaway', 'district': None, 'note': None, 'review': 1},
    {'order_id': '389afe2c-9f8b-4d50-8e18-79a9ad5f3ea4', 'price': 2300, 'customer': 'Heinrick Zanioletti',
        'type': 'delivery', 'district': 'VI', 'note': 'ketchup', 'review': None},
    {'order_id': '946031fd-c648-41e6-aeaf-517de87b7c9b', 'price': 4900, 'customer': 'Ewan Jehan',
        'type': 'delivery', 'district': 'VII', 'note': None, 'review': 4},
    {'order_id': 'e5113f07-1606-4eab-9914-4775b23a0efb', 'price': 1900,
        'customer': 'Kevin Bartrap', 'type': 'dine-in', 'district': None, 'note': None, 'review': 4},
    {'order_id': '44c6079e-7d1d-4d52-964d-a81def49f1de', 'price': 3100, 'customer': 'Delmor Trett',
        'type': 'delivery', 'district': 'VI', 'note': 'hagyma nélkül', 'review': 4},
    {'order_id': '687caf8b-51fe-47f8-bdf5-c4cd5599b7ef', 'price': 11900,
        'customer': 'Bradly Dillinger', 'type': 'takeaway', 'district': None, 'note': None, 'review': 3},
    {'order_id': '67936966-32d5-4e60-a355-05cf347e9910', 'price': 2400,
        'customer': 'Mallory Oris', 'type': 'takeaway', 'district': None, 'note': None, 'review': 3},
    {'order_id': 'df545257-c4e6-4a90-b784-c94596d6c1aa', 'price': 4200, 'customer': 'Elianore Pittoli',
        'type': 'takeaway', 'district': None, 'note': None, 'review': None},
    {'order_id': '0759e5c0-44c9-46e4-8f18-3609039a3985', 'price': 7700, 'customer': 'Mavra Sherington',
        'type': 'delivery', 'district': 'XIV', 'note': None, 'review': 3},
    {'order_id': '77182682-0da0-4d5f-9d9c-3d1375adcf85', 'price': 1700,
        'customer': 'Roman Terzi', 'type': 'delivery', 'district': 'VI', 'note': None, 'review': 3},
    {'order_id': 'a470f976-15a4-436f-9c5a-d3525e3a86e5', 'price': 2300,
        'customer': 'Stephen Pratten', 'type': 'takeaway', 'district': None, 'note': None, 'review': 4},
    {'order_id': 'e3ab88e3-fd6c-44c8-8d34-e25ed7989396', 'price': 2600, 'customer': 'Sarajane Armall',
        'type': 'delivery', 'district': 'VII', 'note': None, 'review': 3},
    {'order_id': 'a24dc7a5-851d-44ea-a50b-4856a4007fdc', 'price': 3300,
        'customer': 'Carmen Garfirth', 'type': 'takeaway', 'district': None, 'note': None, 'review': 4},
    {'order_id': '2f720703-3748-49a3-8f2e-393d43eec633', 'price': 3000, 'customer': 'Edin Truckell',
        'type': 'delivery', 'district': 'VI', 'note': 'több saláta', 'review': 3},
    {'order_id': '42231dab-595c-4b24-a9dc-842d7de8a9c4', 'price': 2400,
        'customer': 'Linoel Gorgler', 'type': 'takeaway', 'district': None, 'note': None, 'review': 1},
    {'order_id': 'e671173d-f238-4ac6-bfaf-22c7b223072f', 'price': 2400, 'customer': 'Alicea Catlette',
        'type': 'dine-in', 'district': None, 'note': None, 'review': None},
    {'order_id': '3c802dbe-9f56-44ba-9fc3-51d85f3b65e8', 'price': 1500, 'customer': 'Garreth Gepson',
        'type': 'delivery', 'district': 'VI', 'note': None, 'review': None},
    {'order_id': '5106156e-e53b-44cb-af71-86ebb176fe34', 'price': 3300,
        'customer': 'Yance Chate', 'type': 'dine-in', 'district': None, 'note': None, 'review': 3},
    {'order_id': 'b21ac870-e53e-42b8-b1e0-b591e3a77f96', 'price': 5900, 'customer': 'Jeanna Deyenhardt',
        'type': 'delivery', 'district': 'VII', 'note': 'ketchup', 'review': 4},
    {'order_id': 'd8c90b04-ad6a-4884-9160-1196e81ea311', 'price': 3200, 'customer': 'Connor Applewhaite',
        'type': 'delivery', 'district': 'VI', 'note': None, 'review': None},
    {'order_id': '6bd4ed52-0abb-4df7-98fa-83662487ad1a', 'price': 11300, 'customer': 'Renado Bausor',
        'type': 'delivery', 'district': 'VIII', 'note': None, 'review': None},
    {'order_id': '0553bfc6-c053-480b-a754-8352c88783da', 'price': 2300, 'customer': 'Jeanna Deyenhardt',
        'type': 'takeaway', 'district': None, 'note': None, 'review': 4}
]