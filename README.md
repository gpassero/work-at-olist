# Work at Olist

## Introduction
This Django project provides a set of REST web services to expose sellers' categories of products. The main provided services are:

- List existing channels.
- List all categories and subcategories of a channel.
- Return a single category with their parent categorys and subcategories.

A copy of this project is currently running at Heroku with example data: [https://work-at-olist-gpassero.herokuapp.com](https://work-at-olist-gpassero.herokuapp.com).

This project was developed regarding the requirements specified at the [Work at Olist repo](https://github.com/olist/work-at-olist).

The following sections present the API documentation.

### List channels
----

* **URL**

  _/channels_

* **Method:**  

  `GET` | `POST`
  
*  **URL Params**

No param needed.

* **Response:**

  * **Code:** 200 <br />
    **Content:** `[{"uuid":"a816bf61-2945-464b-af0c-4003dfd9e099","name":"walmart"},{"uuid":"1605b908-61b3-4131-a34d-df9ad29f53c8","name":"google"}]`
    
### List channels' categories and subcategories
----

* **URL**

  _/channels/\<uuid\>_

* **Method:**  

  `GET` | `POST`
  
*  **URL Params**

- _uuid:_ The uuid of the channel to be listed (all channels uuid and name can be seen at [*List channels*](#list-channels) service).

* **Response:**

  * **Code:** 200 <br />
    **Content:** `{"uuid":"a816bf61-2945-464b-af0c-4003dfd9e099","name":"walmart","categories":[{"uuid":"7c159432-b3d9-454c-9ad9-ca22dd0b8b2e","name":"Desktop","parent":"074c7002-a80d-4a31-b2a3-4da5b47447f0"},{"uuid":"81c503e6-aa77-4d45-934e-690fd7cb01b6","name":"Tablets","parent":"074c7002-a80d-4a31-b2a3-4da5b47447f0"},{"uuid":"34fe95d5-7e9b-4e71-a0f5-bfe30bfb6de1","name":"Notebooks","parent":"074c7002-a80d-4a31-b2a3-4da5b47447f0"},...]}`    
 
 ### List category's related categories
----

* **URL**

  _/categories/<uuid>_

* **Method:**  

  `GET` | `POST`
  
*  **URL Params**

- _uuid:_ The uuid of the category to be listed (a channel's categories can be listed at [*List channels' categories and subcategories*](#list-channels-categories-and-subcategories) service).

* **Response:**

  * **Code:** 200 <br />
    **Content:** `{"uuid":"0d8e61b7-f6b4-4457-a120-f8dd33539f06","name":"Books","channel":{"uuid":"a816bf61-2945-464b-af0c-4003dfd9e099","name":"walmart"},"parent":null,"subcategories":[{"uuid":"fb76950e-e6e3-4420-96b6-b1135b9a9459","name":"Computers"},{"uuid":"2a444f90-58ba-49ed-b376-da878bad9d98","name":"Foreign Literature"},{"uuid":"a12eed22-3bb9-4712-a9d5-f58aa2dd0c32","name":"National Literature"}]}`    
 
