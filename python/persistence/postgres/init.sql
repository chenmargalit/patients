\c patients;

create table patients_details(id serial primary key, patient_id integer unique not null);
Create index patient_ids_idx on patients_details(patient_id);
