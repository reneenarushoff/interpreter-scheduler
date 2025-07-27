<!-- PROJECT SHIELDS -->
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?logo=linkedin&style=flat)](https://www.linkedin.com/in/reneenarushoff/)

<!-- PROJECT TITLE -->
# Interpreter Scheduling and Validation System

A lightweight Python application that validates appointment data, corrects common input issues, and matches interpreters based on language and availability. Ideal for appointment coordination.

## Features
- Validates required appointment fields using Pydantic v2
- Supports both 12-hour and 24-hour (military) time formats
- Fuzzy-corrects common misspellings in language names
- Ensures dates are within two years and not in the past
- Matches interpreters by language and date availability
- Generates validation reports with error explanations

## Project Structure
```
├-- main.py                 # Main script to run the program
├-- validator.py            # Pydantic-based validator
├── scheduler.py            # Interpreter matching logic
├── report_generator.py     # Validation report writer
├── appointments.json       # Sample appointment data
├── interpreters.json       # Sample interpreter data
├── lang_map.json           # Language normalization map
├── LICENSE                 # MIT license
├── .gitignore              # Files to ignore in version control
└── README.md               # This file
```
## Getting Started

### Requirements

- Python 3.10+
- `pydantic`
- `pandas`
- `python-dateutil`

### Installation

```bash
pip install -r requirements.txt
python main.py
```
## Example

### Input (`appointments.json`)

```json
{
  "Appointment_ID": "0004",
  "Client": "IBM",
  "Language": "Rushin",
  "Date": "08/01/2026",
  "Start_Time": "18:00",
  "End_Time": "20:00"
}
```
### Output 
```json
{
  "Appointment_ID": "0004",
  "Client": "IBM",
  "Language": "Russian",
  "Date": "08/01/2026",
  "Start_Time": "06:00 PM",
  "End_Time": "08:00 PM",
  "Interpreter": "Ivan Ilyich",
  "Validation Result": "Valid"
}
```
<!-- ROADMAP -->
## Roadmap

- [ ] Support interpreters with multiple languages
- [ ] Validate time availability (not just date)
- [ ] Prevent double-booking
- [ ] Build a learning-based availability analyzer

<!-- LICENSE -->
## License

This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.

> This is a simplified, personal demo project inspired by general scheduling workflows I’ve encountered.  
> All data, code, and logic are my own original work and do not reflect any proprietary systems.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Renee Narushoff - [![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?logo=linkedin&style=flat)](https://www.linkedin.com/in/reneenarushoff/) - narushoffrenee@gmail.com

Project Link: [https://github.com/reneenarushoff/interpreter-scheduler](https://github.com/reneenarushoff/interpreter-scheduler)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
