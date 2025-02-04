import React, { useEffect, useState } from 'react';

const StudentList = () => {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/register')
      .then(response => response.json())
      .then(data => setStudents(data.students));
  }, []);

  return (
    <div>
      <h2>Registered Students</h2>
      <ul>
        {students.map((student, index) => (
          <li key={index}>{student.name} - {student.course}</li>
        ))}
      </ul>
    </div>
  );
};

export default StudentList;
