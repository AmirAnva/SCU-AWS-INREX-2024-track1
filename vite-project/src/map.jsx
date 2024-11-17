import React, { useState } from 'react';
import { GoogleMap, useLoadScript, Marker } from '@react-google-maps/api';

const containerStyle = {
  width: '100%',
  height: '400px',
};

const center = {
  lat: 47.6061,
  lng: -122.3328,
};

function MyMap() {
  const [markerPosition, setMarkerPosition] = useState({
    lat: 47.6061,
    lng: -122.3328,
  });

  const { isLoaded } = useLoadScript({
    googleMapsApiKey: 'AIzaSyA2UUt6zgte5HGgS3C6y-IpYNGJgqruafs'  // Use environment variable
  });

  if (!isLoaded) return <div>Loading...</div>;

  return (
    <GoogleMap
      mapContainerStyle={containerStyle}
      center={center}
      zoom={10}
    >

      <Marker position={{ lat: 47.6061, lng: -122.3328 }} />

    </GoogleMap>
  );
}

export default MyMap;
