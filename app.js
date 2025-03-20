import React, { useEffect, useState } from 'react';
import axios from 'axios';

const TopUsers = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/top-users')
      .then(response => {
        setUsers(response.data.top_users);
      })
      .catch(error => {
        console.error('There was an error fetching the data!', error);
      });
  }, []);

  return (
    <div>
      <h2>Top 5 Users</h2>
      <ul>
        {Object.keys(users).map(userId => (
          <li key={userId}>{users[userId]}</li>
        ))}
      </ul>
    </div>
  );
};

export default TopUsers;
