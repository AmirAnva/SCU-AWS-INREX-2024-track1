import { Fragment, useState } from "react";
import {
  GoogleMap,
  InfoWindowF,
  MarkerF,
  useLoadScript,
} from "@react-google-maps/api";




const markers = [
    {
        id: 1,
        name: "Seattle",
        position: { lat: 47.6061, lng: -122.3328 },
    },
    {
        id: 2,
        name: "Camera:62219",
        position: { lat: 47.644, lng: -122.3064 },
    }
];

function MyMap() {


  const { isLoaded } = useLoadScript({
    googleMapsApiKey: "AIzaSyA2UUt6zgte5HGgS3C6y-IpYNGJgqruafs",
  });

  const [activeMarker, setActiveMarker] = useState(null);

  const handleActiveMarker = (marker) => {
    console.log("Marker clicked:", marker);
    if (marker === activeMarker) {
      return;
    }
    setActiveMarker(marker);
  };

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
                      {console.log("got to name!", name)}
                        <p>{name}</p>
                        
                        
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