import re
# use codebeautify.org to beautify before
string = '''
{
  "meta": {
    "status": 200
  },
  "data": {
    "results": [
      {
        "user": {
          "_id": "f52e414b-2e53-472b-9086-a2688646cf57",
          "photos": [
            {
              "id": "78cbd330-e9df-48b1-8140-19b78ae17849",
              "crop_info": {
                "user": {
                  "width_pct": 1,
                  "x_offset_pct": 0,
                  "height_pct": 0.8,
                  "y_offset_pct": 0
                },
                "algo": {
                  "width_pct": 0.18358903677435595,
                  "x_offset_pct": 0.39212916609831155,
                  "height_pct": 0.19403841339051722,
                  "y_offset_pct": 0.21424498761072755
                },
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/f52e414b-2e53-472b-9086-a2688646cf57/original_78cbd330-e9df-48b1-8140-19b78ae17849.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/f52e414b-2e53-472b-9086-a2688646cf57/640x800_78cbd330-e9df-48b1-8140-19b78ae17849.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/f52e414b-2e53-472b-9086-a2688646cf57/320x400_78cbd330-e9df-48b1-8140-19b78ae17849.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/f52e414b-2e53-472b-9086-a2688646cf57/172x216_78cbd330-e9df-48b1-8140-19b78ae17849.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/f52e414b-2e53-472b-9086-a2688646cf57/84x106_78cbd330-e9df-48b1-8140-19b78ae17849.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "fileName": "78cbd330-e9df-48b1-8140-19b78ae17849.jpg",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "7d9b8b0d-c9db-43de-8c7a-03dcb82ab0a3",
          "photos": [
            {
              "id": "8521a0db-975f-4836-bd24-1e8d72f6a2bd",
              "crop_info": {
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/7d9b8b0d-c9db-43de-8c7a-03dcb82ab0a3/original_8521a0db-975f-4836-bd24-1e8d72f6a2bd.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/7d9b8b0d-c9db-43de-8c7a-03dcb82ab0a3/640x800_8521a0db-975f-4836-bd24-1e8d72f6a2bd.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/7d9b8b0d-c9db-43de-8c7a-03dcb82ab0a3/320x400_8521a0db-975f-4836-bd24-1e8d72f6a2bd.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/7d9b8b0d-c9db-43de-8c7a-03dcb82ab0a3/172x216_8521a0db-975f-4836-bd24-1e8d72f6a2bd.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/7d9b8b0d-c9db-43de-8c7a-03dcb82ab0a3/84x106_8521a0db-975f-4836-bd24-1e8d72f6a2bd.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "fileName": "8521a0db-975f-4836-bd24-1e8d72f6a2bd.jpg",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "42166de6-6dfc-4068-a7d1-5db6d3e76ed6",
          "photos": [
            {
              "id": "db92ecf7-c88f-4edb-90c2-33d6b72802b3",
              "crop_info": {
                "user": {
                  "width_pct": 1,
                  "x_offset_pct": 0,
                  "height_pct": 0.8,
                  "y_offset_pct": 0
                },
                "algo": {
                  "width_pct": 0.5417524888645857,
                  "x_offset_pct": 0.34152628034353255,
                  "height_pct": 0.557542936950922,
                  "y_offset_pct": 0.020776236951351165
                },
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/42166de6-6dfc-4068-a7d1-5db6d3e76ed6/original_db92ecf7-c88f-4edb-90c2-33d6b72802b3.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/42166de6-6dfc-4068-a7d1-5db6d3e76ed6/640x800_db92ecf7-c88f-4edb-90c2-33d6b72802b3.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/42166de6-6dfc-4068-a7d1-5db6d3e76ed6/320x400_db92ecf7-c88f-4edb-90c2-33d6b72802b3.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/42166de6-6dfc-4068-a7d1-5db6d3e76ed6/172x216_db92ecf7-c88f-4edb-90c2-33d6b72802b3.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/42166de6-6dfc-4068-a7d1-5db6d3e76ed6/84x106_db92ecf7-c88f-4edb-90c2-33d6b72802b3.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "fileName": "db92ecf7-c88f-4edb-90c2-33d6b72802b3.jpg",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "10e8dbf6-4e81-472d-903d-bee6ddf8273d",
          "photos": [
            {
              "id": "0605fdef-4613-4a51-86f2-77bb3f250cec",
              "crop_info": {
                "user": {
                  "width_pct": 1,
                  "x_offset_pct": 0,
                  "height_pct": 0.8,
                  "y_offset_pct": 0
                },
                "algo": {
                  "width_pct": 0.10445720620919013,
                  "x_offset_pct": 0.4853784684557468,
                  "height_pct": 0.09737109924200923,
                  "y_offset_pct": 0.13895708534866572
                },
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/10e8dbf6-4e81-472d-903d-bee6ddf8273d/original_0605fdef-4613-4a51-86f2-77bb3f250cec.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/10e8dbf6-4e81-472d-903d-bee6ddf8273d/640x800_0605fdef-4613-4a51-86f2-77bb3f250cec.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/10e8dbf6-4e81-472d-903d-bee6ddf8273d/320x400_0605fdef-4613-4a51-86f2-77bb3f250cec.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/10e8dbf6-4e81-472d-903d-bee6ddf8273d/172x216_0605fdef-4613-4a51-86f2-77bb3f250cec.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/10e8dbf6-4e81-472d-903d-bee6ddf8273d/84x106_0605fdef-4613-4a51-86f2-77bb3f250cec.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "fileName": "0605fdef-4613-4a51-86f2-77bb3f250cec.jpg",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "3e1d4b44-b04c-4b33-a989-31d2057da2eb",
          "photos": [
            {
              "id": "753a3c96-2331-43bc-a914-88e32a2a5494",
              "crop_info": {
                "user": {
                  "width_pct": 1,
                  "x_offset_pct": 0,
                  "height_pct": 0.8,
                  "y_offset_pct": 0.10133035642094909
                },
                "algo": {
                  "width_pct": 0.4158499741461128,
                  "x_offset_pct": 0.2338381815701723,
                  "height_pct": 0.4569506775774062,
                  "y_offset_pct": 0.272855017632246
                },
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/3e1d4b44-b04c-4b33-a989-31d2057da2eb/original_753a3c96-2331-43bc-a914-88e32a2a5494.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/3e1d4b44-b04c-4b33-a989-31d2057da2eb/640x800_753a3c96-2331-43bc-a914-88e32a2a5494.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/3e1d4b44-b04c-4b33-a989-31d2057da2eb/320x400_753a3c96-2331-43bc-a914-88e32a2a5494.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/3e1d4b44-b04c-4b33-a989-31d2057da2eb/172x216_753a3c96-2331-43bc-a914-88e32a2a5494.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/3e1d4b44-b04c-4b33-a989-31d2057da2eb/84x106_753a3c96-2331-43bc-a914-88e32a2a5494.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "fileName": "753a3c96-2331-43bc-a914-88e32a2a5494.jpg",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "90fdc1ee-5f88-440f-a2fb-02a1495b002d",
          "photos": [
            {
              "id": "2fed8d19-1a6f-44cc-9de9-86150f054ecb",
              "crop_info": {
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/90fdc1ee-5f88-440f-a2fb-02a1495b002d/original_2fed8d19-1a6f-44cc-9de9-86150f054ecb.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/90fdc1ee-5f88-440f-a2fb-02a1495b002d/640x800_2fed8d19-1a6f-44cc-9de9-86150f054ecb.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/90fdc1ee-5f88-440f-a2fb-02a1495b002d/320x400_2fed8d19-1a6f-44cc-9de9-86150f054ecb.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/90fdc1ee-5f88-440f-a2fb-02a1495b002d/172x216_2fed8d19-1a6f-44cc-9de9-86150f054ecb.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/90fdc1ee-5f88-440f-a2fb-02a1495b002d/84x106_2fed8d19-1a6f-44cc-9de9-86150f054ecb.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "fileName": "2fed8d19-1a6f-44cc-9de9-86150f054ecb.jpg",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "ad9d40f6-1553-48f0-9694-2a30b50d4e3b",
          "photos": [
            {
              "id": "d70a9847-fb5e-4722-9375-5beb5ef443f6",
              "crop_info": {
                "user": {
                  "width_pct": 1,
                  "x_offset_pct": 0,
                  "height_pct": 0.8,
                  "y_offset_pct": 0
                },
                "algo": {
                  "width_pct": 0.08183146109804512,
                  "x_offset_pct": 0.49586710701696574,
                  "height_pct": 0.08441945377737284,
                  "y_offset_pct": 0.24879079490900038
                },
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/ad9d40f6-1553-48f0-9694-2a30b50d4e3b/original_d70a9847-fb5e-4722-9375-5beb5ef443f6.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/ad9d40f6-1553-48f0-9694-2a30b50d4e3b/640x800_d70a9847-fb5e-4722-9375-5beb5ef443f6.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/ad9d40f6-1553-48f0-9694-2a30b50d4e3b/320x400_d70a9847-fb5e-4722-9375-5beb5ef443f6.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/ad9d40f6-1553-48f0-9694-2a30b50d4e3b/172x216_d70a9847-fb5e-4722-9375-5beb5ef443f6.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/ad9d40f6-1553-48f0-9694-2a30b50d4e3b/84x106_d70a9847-fb5e-4722-9375-5beb5ef443f6.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "last_update_time": "2020-03-23T03:46:12.767Z",
              "fileName": "d70a9847-fb5e-4722-9375-5beb5ef443f6.webp",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "55f332ca-b905-4cfd-b797-d8c74992fcca",
          "photos": [
            {
              "id": "f33e523d-ce74-4d77-97e9-ed27f7ef4b11",
              "crop_info": {
                "user": {
                  "width_pct": 1,
                  "x_offset_pct": 0,
                  "height_pct": 0.8,
                  "y_offset_pct": 0.02369506584014741
                },
                "algo": {
                  "width_pct": 0.51547180818161,
                  "x_offset_pct": 0.0841616694466211,
                  "height_pct": 0.3419929604511708,
                  "y_offset_pct": 0.25269858561456204
                },
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/55f332ca-b905-4cfd-b797-d8c74992fcca/original_f33e523d-ce74-4d77-97e9-ed27f7ef4b11.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/55f332ca-b905-4cfd-b797-d8c74992fcca/640x800_f33e523d-ce74-4d77-97e9-ed27f7ef4b11.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/55f332ca-b905-4cfd-b797-d8c74992fcca/320x400_f33e523d-ce74-4d77-97e9-ed27f7ef4b11.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/55f332ca-b905-4cfd-b797-d8c74992fcca/172x216_f33e523d-ce74-4d77-97e9-ed27f7ef4b11.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/55f332ca-b905-4cfd-b797-d8c74992fcca/84x106_f33e523d-ce74-4d77-97e9-ed27f7ef4b11.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "last_update_time": "2020-04-09T16:23:36.410Z",
              "fileName": "f33e523d-ce74-4d77-97e9-ed27f7ef4b11.webp",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "ae5cc990-e004-4725-a636-563581ecb6d3",
          "photos": [
            {
              "id": "7b92ab9d-9ab7-42a2-b433-144a1c3c8bc5",
              "crop_info": {
                "user": {
                  "width_pct": 1,
                  "x_offset_pct": 0,
                  "height_pct": 0.8,
                  "y_offset_pct": 0.14919920742511747
                },
                "algo": {
                  "width_pct": 0.6412044990807771,
                  "x_offset_pct": 0.11338557847775518,
                  "height_pct": 0.7249680459499359,
                  "y_offset_pct": 0.18671518445014954
                },
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/ae5cc990-e004-4725-a636-563581ecb6d3/original_7b92ab9d-9ab7-42a2-b433-144a1c3c8bc5.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/ae5cc990-e004-4725-a636-563581ecb6d3/640x800_7b92ab9d-9ab7-42a2-b433-144a1c3c8bc5.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/ae5cc990-e004-4725-a636-563581ecb6d3/320x400_7b92ab9d-9ab7-42a2-b433-144a1c3c8bc5.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/ae5cc990-e004-4725-a636-563581ecb6d3/172x216_7b92ab9d-9ab7-42a2-b433-144a1c3c8bc5.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/ae5cc990-e004-4725-a636-563581ecb6d3/84x106_7b92ab9d-9ab7-42a2-b433-144a1c3c8bc5.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "last_update_time": "2019-11-28T08:18:04.736Z",
              "fileName": "7b92ab9d-9ab7-42a2-b433-144a1c3c8bc5.webp",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "dfc5a465-b04c-4318-9371-3cf6cd54d886",
          "photos": [
            {
              "id": "d3411913-5597-4f24-aeb6-c4bd317a64e7",
              "crop_info": {
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/dfc5a465-b04c-4318-9371-3cf6cd54d886/original_d3411913-5597-4f24-aeb6-c4bd317a64e7.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/dfc5a465-b04c-4318-9371-3cf6cd54d886/640x800_d3411913-5597-4f24-aeb6-c4bd317a64e7.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/dfc5a465-b04c-4318-9371-3cf6cd54d886/320x400_d3411913-5597-4f24-aeb6-c4bd317a64e7.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/dfc5a465-b04c-4318-9371-3cf6cd54d886/172x216_d3411913-5597-4f24-aeb6-c4bd317a64e7.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/dfc5a465-b04c-4318-9371-3cf6cd54d886/84x106_d3411913-5597-4f24-aeb6-c4bd317a64e7.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "fileName": "d3411913-5597-4f24-aeb6-c4bd317a64e7.jpg",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      }
    ]
  }
}


{
  "meta": {
    "status": 200
  },
  "data": {
    "results": [
      {
        "user": {
          "_id": "f52e414b-2e53-472b-9086-a2688646cf57",
          "photos": [
            {
              "id": "b059d8a6-adf3-42e7-8798-0a42cfd8c159",
              "crop_info": {
                "user": {
                  "width_pct": 1,
                  "x_offset_pct": 0,
                  "height_pct": 0.8,
                  "y_offset_pct": 0.13131506395526227
                },
                "algo": {
                  "width_pct": 0.15886205701972356,
                  "x_offset_pct": 0.3376994533173274,
                  "height_pct": 0.150877695120871,
                  "y_offset_pct": 0.4558762163948268
                },
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/f52e414b-2e53-472b-9086-a2688646cf57/original_b059d8a6-adf3-42e7-8798-0a42cfd8c159.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/f52e414b-2e53-472b-9086-a2688646cf57/640x800_b059d8a6-adf3-42e7-8798-0a42cfd8c159.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/f52e414b-2e53-472b-9086-a2688646cf57/320x400_b059d8a6-adf3-42e7-8798-0a42cfd8c159.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/f52e414b-2e53-472b-9086-a2688646cf57/172x216_b059d8a6-adf3-42e7-8798-0a42cfd8c159.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/f52e414b-2e53-472b-9086-a2688646cf57/84x106_b059d8a6-adf3-42e7-8798-0a42cfd8c159.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "fileName": "b059d8a6-adf3-42e7-8798-0a42cfd8c159.jpg",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "7d9b8b0d-c9db-43de-8c7a-03dcb82ab0a3",
          "photos": [
            {
              "id": "8521a0db-975f-4836-bd24-1e8d72f6a2bd",
              "crop_info": {
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/7d9b8b0d-c9db-43de-8c7a-03dcb82ab0a3/original_8521a0db-975f-4836-bd24-1e8d72f6a2bd.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/7d9b8b0d-c9db-43de-8c7a-03dcb82ab0a3/640x800_8521a0db-975f-4836-bd24-1e8d72f6a2bd.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/7d9b8b0d-c9db-43de-8c7a-03dcb82ab0a3/320x400_8521a0db-975f-4836-bd24-1e8d72f6a2bd.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/7d9b8b0d-c9db-43de-8c7a-03dcb82ab0a3/172x216_8521a0db-975f-4836-bd24-1e8d72f6a2bd.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/7d9b8b0d-c9db-43de-8c7a-03dcb82ab0a3/84x106_8521a0db-975f-4836-bd24-1e8d72f6a2bd.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "fileName": "8521a0db-975f-4836-bd24-1e8d72f6a2bd.jpg",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "42166de6-6dfc-4068-a7d1-5db6d3e76ed6",
          "photos": [
            {
              "id": "db92ecf7-c88f-4edb-90c2-33d6b72802b3",
              "crop_info": {
                "user": {
                  "width_pct": 1,
                  "x_offset_pct": 0,
                  "height_pct": 0.8,
                  "y_offset_pct": 0
                },
                "algo": {
                  "width_pct": 0.5417524888645857,
                  "x_offset_pct": 0.34152628034353255,
                  "height_pct": 0.557542936950922,
                  "y_offset_pct": 0.020776236951351165
                },
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/42166de6-6dfc-4068-a7d1-5db6d3e76ed6/original_db92ecf7-c88f-4edb-90c2-33d6b72802b3.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/42166de6-6dfc-4068-a7d1-5db6d3e76ed6/640x800_db92ecf7-c88f-4edb-90c2-33d6b72802b3.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/42166de6-6dfc-4068-a7d1-5db6d3e76ed6/320x400_db92ecf7-c88f-4edb-90c2-33d6b72802b3.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/42166de6-6dfc-4068-a7d1-5db6d3e76ed6/172x216_db92ecf7-c88f-4edb-90c2-33d6b72802b3.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/42166de6-6dfc-4068-a7d1-5db6d3e76ed6/84x106_db92ecf7-c88f-4edb-90c2-33d6b72802b3.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "fileName": "db92ecf7-c88f-4edb-90c2-33d6b72802b3.jpg",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "10e8dbf6-4e81-472d-903d-bee6ddf8273d",
          "photos": [
            {
              "id": "ef87b115-cceb-4b60-a107-afd6a6468079",
              "crop_info": {
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/10e8dbf6-4e81-472d-903d-bee6ddf8273d/original_ef87b115-cceb-4b60-a107-afd6a6468079.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/10e8dbf6-4e81-472d-903d-bee6ddf8273d/640x800_ef87b115-cceb-4b60-a107-afd6a6468079.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/10e8dbf6-4e81-472d-903d-bee6ddf8273d/320x400_ef87b115-cceb-4b60-a107-afd6a6468079.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/10e8dbf6-4e81-472d-903d-bee6ddf8273d/172x216_ef87b115-cceb-4b60-a107-afd6a6468079.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/10e8dbf6-4e81-472d-903d-bee6ddf8273d/84x106_ef87b115-cceb-4b60-a107-afd6a6468079.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "fileName": "ef87b115-cceb-4b60-a107-afd6a6468079.jpg",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "3e1d4b44-b04c-4b33-a989-31d2057da2eb",
          "photos": [
            {
              "id": "86b20967-f64d-4f6a-b090-d49e4172eade",
              "crop_info": {
                "user": {
                  "width_pct": 1,
                  "x_offset_pct": 0,
                  "height_pct": 0.8,
                  "y_offset_pct": 0.048038986604660744
                },
                "algo": {
                  "width_pct": 0.38496950297267174,
                  "x_offset_pct": 0.2103982191241812,
                  "height_pct": 0.32406887535005807,
                  "y_offset_pct": 0.28600454892963173
                },
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/3e1d4b44-b04c-4b33-a989-31d2057da2eb/original_86b20967-f64d-4f6a-b090-d49e4172eade.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/3e1d4b44-b04c-4b33-a989-31d2057da2eb/640x800_86b20967-f64d-4f6a-b090-d49e4172eade.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/3e1d4b44-b04c-4b33-a989-31d2057da2eb/320x400_86b20967-f64d-4f6a-b090-d49e4172eade.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/3e1d4b44-b04c-4b33-a989-31d2057da2eb/172x216_86b20967-f64d-4f6a-b090-d49e4172eade.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/3e1d4b44-b04c-4b33-a989-31d2057da2eb/84x106_86b20967-f64d-4f6a-b090-d49e4172eade.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "fileName": "86b20967-f64d-4f6a-b090-d49e4172eade.jpg",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "90fdc1ee-5f88-440f-a2fb-02a1495b002d",
          "photos": [
            {
              "id": "f3e6805f-9cdd-4998-85e3-177d0e1492e5",
              "crop_info": {
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/90fdc1ee-5f88-440f-a2fb-02a1495b002d/original_f3e6805f-9cdd-4998-85e3-177d0e1492e5.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/90fdc1ee-5f88-440f-a2fb-02a1495b002d/640x800_f3e6805f-9cdd-4998-85e3-177d0e1492e5.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/90fdc1ee-5f88-440f-a2fb-02a1495b002d/320x400_f3e6805f-9cdd-4998-85e3-177d0e1492e5.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/90fdc1ee-5f88-440f-a2fb-02a1495b002d/172x216_f3e6805f-9cdd-4998-85e3-177d0e1492e5.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/90fdc1ee-5f88-440f-a2fb-02a1495b002d/84x106_f3e6805f-9cdd-4998-85e3-177d0e1492e5.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "fileName": "f3e6805f-9cdd-4998-85e3-177d0e1492e5.jpg",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "ad9d40f6-1553-48f0-9694-2a30b50d4e3b",
          "photos": [
            {
              "id": "442d9789-f24c-48b6-bb5e-d8121704d98a",
              "crop_info": {
                "user": {
                  "width_pct": 1,
                  "x_offset_pct": 0,
                  "height_pct": 0.8,
                  "y_offset_pct": 0
                },
                "algo": {
                  "width_pct": 0.4921497369883582,
                  "x_offset_pct": 0.3214254792779684,
                  "height_pct": 0.5148412148654461,
                  "y_offset_pct": 0.09917746484279633
                },
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/ad9d40f6-1553-48f0-9694-2a30b50d4e3b/original_442d9789-f24c-48b6-bb5e-d8121704d98a.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/ad9d40f6-1553-48f0-9694-2a30b50d4e3b/640x800_442d9789-f24c-48b6-bb5e-d8121704d98a.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/ad9d40f6-1553-48f0-9694-2a30b50d4e3b/320x400_442d9789-f24c-48b6-bb5e-d8121704d98a.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/ad9d40f6-1553-48f0-9694-2a30b50d4e3b/172x216_442d9789-f24c-48b6-bb5e-d8121704d98a.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/ad9d40f6-1553-48f0-9694-2a30b50d4e3b/84x106_442d9789-f24c-48b6-bb5e-d8121704d98a.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "last_update_time": "2020-03-23T03:39:30.547Z",
              "fileName": "442d9789-f24c-48b6-bb5e-d8121704d98a.webp",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "55f332ca-b905-4cfd-b797-d8c74992fcca",
          "photos": [
            {
              "id": "f33e523d-ce74-4d77-97e9-ed27f7ef4b11",
              "crop_info": {
                "user": {
                  "width_pct": 1,
                  "x_offset_pct": 0,
                  "height_pct": 0.8,
                  "y_offset_pct": 0.02369506584014741
                },
                "algo": {
                  "width_pct": 0.51547180818161,
                  "x_offset_pct": 0.0841616694466211,
                  "height_pct": 0.3419929604511708,
                  "y_offset_pct": 0.25269858561456204
                },
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/55f332ca-b905-4cfd-b797-d8c74992fcca/original_f33e523d-ce74-4d77-97e9-ed27f7ef4b11.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/55f332ca-b905-4cfd-b797-d8c74992fcca/640x800_f33e523d-ce74-4d77-97e9-ed27f7ef4b11.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/55f332ca-b905-4cfd-b797-d8c74992fcca/320x400_f33e523d-ce74-4d77-97e9-ed27f7ef4b11.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/55f332ca-b905-4cfd-b797-d8c74992fcca/172x216_f33e523d-ce74-4d77-97e9-ed27f7ef4b11.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/55f332ca-b905-4cfd-b797-d8c74992fcca/84x106_f33e523d-ce74-4d77-97e9-ed27f7ef4b11.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "last_update_time": "2020-04-09T16:23:36.410Z",
              "fileName": "f33e523d-ce74-4d77-97e9-ed27f7ef4b11.webp",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "ae5cc990-e004-4725-a636-563581ecb6d3",
          "photos": [
            {
              "id": "7b92ab9d-9ab7-42a2-b433-144a1c3c8bc5",
              "crop_info": {
                "user": {
                  "width_pct": 1,
                  "x_offset_pct": 0,
                  "height_pct": 0.8,
                  "y_offset_pct": 0.14919920742511747
                },
                "algo": {
                  "width_pct": 0.6412044990807771,
                  "x_offset_pct": 0.11338557847775518,
                  "height_pct": 0.7249680459499359,
                  "y_offset_pct": 0.18671518445014954
                },
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/ae5cc990-e004-4725-a636-563581ecb6d3/original_7b92ab9d-9ab7-42a2-b433-144a1c3c8bc5.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/ae5cc990-e004-4725-a636-563581ecb6d3/640x800_7b92ab9d-9ab7-42a2-b433-144a1c3c8bc5.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/ae5cc990-e004-4725-a636-563581ecb6d3/320x400_7b92ab9d-9ab7-42a2-b433-144a1c3c8bc5.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/ae5cc990-e004-4725-a636-563581ecb6d3/172x216_7b92ab9d-9ab7-42a2-b433-144a1c3c8bc5.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/ae5cc990-e004-4725-a636-563581ecb6d3/84x106_7b92ab9d-9ab7-42a2-b433-144a1c3c8bc5.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "last_update_time": "2019-11-28T08:18:04.736Z",
              "fileName": "7b92ab9d-9ab7-42a2-b433-144a1c3c8bc5.webp",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      },
      {
        "user": {
          "_id": "6957c462-aea7-4612-a6f2-42ee7244022f",
          "photos": [
            {
              "id": "82c893cc-d9bc-4836-98d7-c2651773af18",
              "crop_info": {
                "user": {
                  "width_pct": 1,
                  "x_offset_pct": 0,
                  "height_pct": 0.8,
                  "y_offset_pct": 0.12580430935369807
                },
                "algo": {
                  "width_pct": 0.23285167608410123,
                  "x_offset_pct": 0.4333533599972725,
                  "height_pct": 0.23478297102730722,
                  "y_offset_pct": 0.40841282384004446
                },
                "processed_by_bullseye": true,
                "user_customized": false
              },
              "url": "https://preview.gotinder.com/6957c462-aea7-4612-a6f2-42ee7244022f/original_82c893cc-d9bc-4836-98d7-c2651773af18.jpeg",
              "processedFiles": [
                {
                  "url": "https://preview.gotinder.com/6957c462-aea7-4612-a6f2-42ee7244022f/640x800_82c893cc-d9bc-4836-98d7-c2651773af18.jpg",
                  "height": 800,
                  "width": 640
                },
                {
                  "url": "https://preview.gotinder.com/6957c462-aea7-4612-a6f2-42ee7244022f/320x400_82c893cc-d9bc-4836-98d7-c2651773af18.jpg",
                  "height": 400,
                  "width": 320
                },
                {
                  "url": "https://preview.gotinder.com/6957c462-aea7-4612-a6f2-42ee7244022f/172x216_82c893cc-d9bc-4836-98d7-c2651773af18.jpg",
                  "height": 216,
                  "width": 172
                },
                {
                  "url": "https://preview.gotinder.com/6957c462-aea7-4612-a6f2-42ee7244022f/84x106_82c893cc-d9bc-4836-98d7-c2651773af18.jpg",
                  "height": 106,
                  "width": 84
                }
              ],
              "fileName": "82c893cc-d9bc-4836-98d7-c2651773af18.jpg",
              "extension": "jpg,webp",
              "webp_qf": [
                75
              ]
            }
          ]
        }
      }
    ]
  }
}

'''
url = re.findall(r'(?P<url>https?://[^\s]+)', string)
urls = []
for i in url:
	if i.endswith('.jpeg",') or i.endswith('.jpeg'):
		urls.append(i)
	else:
		next
urls2 = list(set(urls))
for i in urls2:
	print(i)
