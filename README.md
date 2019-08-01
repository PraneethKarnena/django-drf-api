## API demonstration - Django ReST Framework

Sample data has already been inserted.
Base API URL: [https://testing-19.herokuapp.com/api/](https://testing-19.herokuapp.com/api/)

 - Get all patients info - `/get-patients/` - returns just the name, ID of the patient
 - Get all doctors info - `/get-doctors/` - returns name, ID of the doctors
 - Send a friend request to a patient - `/send-request/{patient-id}/{doctor-id}/`
 - Accept a request - `/accept-request/{patient-id}/{doctor-id}/`
 - View a patient data - `/view-patient/{patient-id}/`
 - View friends - `/get-friends/{patient-id}/`

 *Note: No authentication has been implemented for time being*
