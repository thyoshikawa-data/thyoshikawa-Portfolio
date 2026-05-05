CREATE TABLE RAW_OTA_PURCHASES (
    nk_ota_localizer_id VARCHAR2(50),
    fk_contact VARCHAR2(50),
    date_purchase DATE,
    place_origin_departure VARCHAR2(100),
    place_destination_departure VARCHAR2(100),
    place_origin_return VARCHAR2(100),
    place_destination_return VARCHAR2(100),
    fk_departure_ota_bus_company VARCHAR2(50),
    fk_return_ota_bus_company VARCHAR2(50),
    gmv_success NUMBER,
    total_tickets_quantity_success NUMBER
);
