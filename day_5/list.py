# Day 5 - 30 Days of Python

# Exercises Level 1
list = []
num_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
print("Number list:", num_list)
print("Length of number list:", len(num_list))
print("First item:", num_list[0])
print("Middle item:", num_list[len(num_list)//2])
print("Last item:", num_list[len(num_list)-1])

personal_info = ['Sean De Guzman', 21, 1.80, 'Single', 'NSJ, Dinalupihan, Bataan']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("\nIt Companies:", it_companies)
print("Number of IT companies:", len(it_companies))
print("First Company:", it_companies[0])
print("Middle Company:", it_companies[len(it_companies)//2])
print("Last Company:", it_companies[-1])

it_companies[2] = 'Intel'
print("Modified IT Companies:", it_companies)
it_companies.append("Nvidia")
it_companies.insert(len(it_companies)//2, "Samsung")
it_companies[0] = it_companies[0].upper()
result = " #".join(it_companies)
it_companies.sort()

print("Result of joined list:", result)
print("Is IBM in the list?", 'IBM' in it_companies)
print("Sorted IT Companies:", it_companies)
it_companies.sort(reverse=True)
print("Reversed:", it_companies)

print("First three companies:", it_companies[0:3])
print("Last three companies:", it_companies[-3:])
print("Sliced Middle company:", it_companies[len(it_companies)//2:len(it_companies)//2+1])
print("Removed the first company", it_companies.pop(0), it_companies)
it_companies.remove("IBM")
print("Removed the middle company", it_companies)
it_companies.pop(-1)
print("Removed the last company", it_companies)

it_companies.clear()
print("Cleared IT Companies:", it_companies)
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

front_end.extend(back_end)
print("\nFull Stack Development:", front_end)
full_stack = front_end.copy()
full_stack.insert(len(full_stack)//2+1, 'Python')
full_stack.insert(len(full_stack)//2+1, 'SQL')
print("Full Stack Development:", full_stack)

# Exercises Level 2
# Number 1
print("\n==============================================")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Ages:", ages)
min_age = ages[0]
max_age = ages[-1]
print("Minimum age:", min_age)
print("Maximum age:", max_age)
ages.insert(0, min_age)
ages.append(max_age)
print("Updated Ages:", ages)
middle_age = ages[len(ages)//2 - 1]
middle_age2 = ages[len(ages)//2]
median_age = (middle_age + middle_age2) / 2
print("Median Age:", median_age)

average_age = sum(ages) / len(ages)
print("Average Age:", average_age)
print("Range of ages:", max_age - min_age)
compare = abs(min_age - average_age) < abs(max_age - average_age)
print("Is the minimum age closer to the average than the maximum age?:", compare)

# Number 2
print("\n==============================================")

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

print("Middle country:", countries[len(countries)//2])
first_half = countries[:len(countries)//2]
last_half = countries[len(countries)//2:]
print("First half of the countries list:", first_half)
print("\n======================================================\n")
print("Last half of the countries list:", last_half)

print("\n======================================================\n")
needed_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, rus, usa, *scandic = needed_countries
print("China:", ch)
print("Russia:", rus) 
print("USA:", usa)
print("Scandic Countries:", scandic, '\n')



