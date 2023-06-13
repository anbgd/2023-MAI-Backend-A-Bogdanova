INSERT INTO
  public.film (uuid, title, year)
VALUES
  (
    'b1e594b5-11e5-4ee5-bffd-fe2cc5fbebff',
    'Мой сосед Тоторо',
    1988
  ),
  (
    'fed9d3a5-62a0-44a3-a8e0-b984c443b5d6',
    'Триплексоголик',
    2006
  ),
  (
    'f4d4e7c3-3b9a-4f3b-9f6d-4b4a4c7c4d50',
    'Под мостом над Аракавой',
    2010
  );

INSERT INTO
  public.director (uuid, name)
VALUES
  (
    '3de91d1d-ee90-4ef6-99fc-242b8522674b',
    'Хаяо Миядзаки'
  ),
  (
    '20b81375-9e57-46f0-9210-ebd7dcbe37a0',
    'Макото Баба'
  ),
  (
    '65529651-3ecb-453a-af4a-756ae73e80c7',
    'Акиюки Синбо'
  );

INSERT INTO
  public.film_director (film_uuid, director_uuid)
VALUES
  (
    'b1e594b5-11e5-4ee5-bffd-fe2cc5fbebff',
    '3de91d1d-ee90-4ef6-99fc-242b8522674b'
  ),
  (
    'fed9d3a5-62a0-44a3-a8e0-b984c443b5d6',
    '20b81375-9e57-46f0-9210-ebd7dcbe37a0'
  ),
  (
    'f4d4e7c3-3b9a-4f3b-9f6d-4b4a4c7c4d50',
    '65529651-3ecb-453a-af4a-756ae73e80c7'
  );



--         {
--             "id": "ba8c7002-5052-43ff-abb2-0275f93bec06",
--             "title": "Парад смерти",
--             "year": 2015
--         },
--         {
--             "id": "a736edbd-c912-40e4-be05-d5c0727e507b",
--             "title": "Твое имя",
--             "year": 2016
--         },
--         {
--             "id": "50126840-d264-4bf1-abb9-652daa4bbbe2",
--             "title": "Девушки и танки",
--             "year": 2017
--         }
--     ]
-- }