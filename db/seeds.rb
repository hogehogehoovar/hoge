def get_alphabet(n)
  ('a'[0].ord + n).chr
end

50.times do |num|
  User.create(email: "test#{num}@gmail.com", password: '000000', name: Faker::Pokemon.name, job: get_alphabet(Faker::Number.between(1, 10)), university: get_alphabet(Faker::Number.between(1, 10)), gender: Faker::Number.between(0, 1), birthday: Faker::Date.birthday(18, 35), image: 'https://www.pakutaso.com/shared/img/thumb/TRT0607001_TP_V.jpg' )
end

person_arr = ['https://www.pakutaso.com/shared/img/thumb/00_PP45_PP_TP_V.jpg',
              'https://www.pakutaso.com/shared/img/thumb/TRT0607001_TP_V.jpg',
              'https://www.pakutaso.com/shared/img/thumb/TRTM9355_TP_V.jpg',
              'https://www.pakutaso.com/shared/img/thumb/0I9A5450ISUMI_TP_V.jpg',
              'https://www.pakutaso.com/shared/img/thumb/IMARI20160807103519_TP_V.jpg',
              'https://www.pakutaso.com/shared/img/thumb/TSURU170321-85%20mm-087_TP_V.jpg',
              ]

50.times do |num|
  User.create(email: "web#{num}@gmail.com",
              password: '000000',
              name: Faker::Name.first_name,
              job: Faker::Job.field,
              university: Faker::University.name,
              gender: Faker::Number.between(0, 1),
              birthday: Faker::Date.birthday(18, 35),
              image: person_arr.shuffle.sample )
end
