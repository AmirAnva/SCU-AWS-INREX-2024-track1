import { Fragment, useState, useEffect} from "react";
import {
  GoogleMap,
  InfoWindowF,
  MarkerF,
  useLoadScript,
} from "@react-google-maps/api";
import axios from 'axios';

//This function takes in latitude and longitude of two locations
// and returns the distance between them as the crow flies (in meters)
function calcCrow(coords1, coords2)
{
  var R = 6371000;
  var dLat = toRad(coords2.lat-coords1.lat);
  var dLon = toRad(coords2.lng-coords1.lng);
  var lat1 = toRad(coords1.lat);
  var lat2 = toRad(coords2.lat);

  var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
    Math.sin(dLon/2) * Math.sin(dLon/2) * Math.cos(lat1) * Math.cos(lat2); 
  var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
  var d = R * c;
  return d;
}

// Converts numeric degrees to radians
function toRad(Value)
{
    return Value * Math.PI / 180;
}

function error() {
  console.log("Unable to retrieve your location");
}


// const markers = [
//     {
//         id: 1,
//         name: "Seattle",
//         position: { lat: 47.6061, lng: -122.3328 },
//     },
//     {
//         id: 2,
//         name: "Camera:62219",
//         position: { lat: 47.644, lng: -122.3064 },
//     }
// ];

function MyMap() {

  const [markers, setMarkers] = useState([]);
  const [activeMarker, setActiveMarker] = useState(null);

  const LAT = 47.69;
  const LONG = -122.332486;
  
  const LAT1 = 47.515578;
  const LONG1 = -122.332486;
  const LAT2 = 47.734360;
  const LONG2 = -122.329642;

  useEffect(() => {
    axios({
      method: "GET",
      //http://172.31.146.192:8080/cameras?token=nx7BbllXcQ-yB6kA3*Gjr2RwxvWN5EzuIpBqRJcithI|&corner1=47.735404|-122.373787&corner2=47.501669|-122.244698
      url: `http://172.31.146.192:8080/cameras?token=ShemiXri0hwtfymsd1iiEa*hFju1FiZ*UQtwwVcZ8*k|&corner1=${LAT1}|${LONG1}&corner2=${LAT2}|${LONG2}`
    })
    .then((response) => {
      //console.log("Original Cameras:", response.data['cameras']);
      const filteredCameras = response.data['cameras'].filter(obj => 
      calcCrow({lat: LAT, lng: LONG}, {lat: obj.latitude, lng: obj.longitude}) <= 1609.34
      );
      console.log("FILTERED:",filteredCameras);
      const formattedMarkers = filteredCameras.map(camera => ({
        id: 'Current Location',
        name: `current_location`,
        position: { lat: parseFloat(camera.latitude), lng: parseFloat(camera.longitude) }
      //setMarkers({ id: parseInt(filteredCameras[0].id), name: filteredCameras[0].id, position: { lat: parseFloat(filteredCameras[0].latitude), lng: parseFloat(filteredCameras[0].longitude)} });
      // setMarkers(filteredCameras.map((camera) => ({
      //   id: parseInt(camera.id),
      //   name: camera.id,
      //   position: { lat: parseFloat(camera.latitude), lng: parseFloat(camera.longitude) },
      // })));
    }));
    setMarkers(formattedMarkers);
    setMarkers(prevMarkers => [
      ...prevMarkers,
      {
        id: prevMarkers.length, // Use the current length as the new ID
        name: `Camera:${prevMarkers.length}`,
        position: { lat: LAT, lng: LONG }
      }
    ]);
  })
    .catch((error) => {
      console.error("Error fetching camera data:", error);
    });
  }, []);
  console.log(`NEW ${markers}`);
  //markers = { id: markers[0].id, name: markers[0].id, position: { lat: markers[0].latitude, lng: markers[0].longitude } }
  // const markers = [
  //   {
  //       id: 1,
  //       name: "Seattle",
  //       position: { lat: 47.6061, lng: -122.3328 },
  //   },
  //   {
  //       id: 2,
  //       name: "Camera:62219",
  //       position: { lat: 47.644, lng: -122.3064 },
  //   }
  // ];
  const handleActiveMarker = (marker) => {
    console.log("Marker clicked:", marker);
    if (marker === activeMarker) {
      return;
    }
    setActiveMarker(marker);
  };

  const { isLoaded } = useLoadScript({
    googleMapsApiKey: "AIzaSyA2UUt6zgte5HGgS3C6y-IpYNGJgqruafs",
  });

  return (
    <Fragment>
      <div className="container">
        <h1 className="text-center">Traffic Detection</h1>
        <div className="map-container" style={{ height: "90vh", width: "100%" }}>
          {isLoaded ? (
            <GoogleMap
              center={{ lat: 47.6061, lng: -122.3328 }}
              zoom={10}
              onClick={() => setActiveMarker(null)}
              mapContainerStyle={{ width: "100%", height: "90vh" }}
            > 


              {markers.map(({ id, name, position }) => (
                <MarkerF
                  key={id}
                  position={position}
                  onClick={() => handleActiveMarker(id)}
                  // icon={{
                  //   url:"https://t4.ftcdn.net/jpg/02/85/33/21/360_F_285332150_qyJdRevcRDaqVluZrUp8ee4H2KezU9CA.jpg",
                  //   scaledSize: { width: 50, height: 50 }
                  // }}
                >
                  {activeMarker === id ? (
                    <InfoWindowF onCloseClick={() => setActiveMarker(null)}>
                      <div>
                        <p> { name === 'current_location' ? `${id}` : `Camera ID: ${id}`}</p>
                        <p>Position: {JSON.stringify(position)}</p>
                      </div>
                    </InfoWindowF>
                  ) : null}
                </MarkerF>
              ))}
            </GoogleMap>
          ) : null}
        </div>
      </div>
    </Fragment>
  );
}

export default MyMap;