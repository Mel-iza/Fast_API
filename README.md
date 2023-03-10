<h2> Fast API </h2>

simple <b>fast api</b> implementation with user input processing via json. <br>

The API receives a <i>json file</i> as input. It will process the file into a dictionary and return one of the dictionary values. <br>


<h2> Usage </h2>

1. Clone the repo <br>
`git clone https://github.com/Mel-iza/Fast_API.git`

2. Enter the main dir <br>
`cd Fast_API`

3. Create a new env <br>
`conda create your_env_name_here`

4. Activate env <br>
`conda activate your_env_name_here`

5. Install libs and packages <br>
`pip3 install fastapi pydantic nest-asyncio pyngrok uvicorn pandas`

6. Run fast api <br>
`uvicorn simple_api:app --reload`


<h2> Request </h2>

`POST localhost:8000/classes`

<details><summary>Input</summary>


```
{
	"classes_do_user": {
		"comprar": [
			"comprar",
			"comercializar",
			"adquirir"
		],
		"preço": [
			"preço",
			"valor"
		],
		"entrega": [
			"entrega",
			"envio",
			"correios"
		],
		"resultado": [
			"resultados"
		]
	}
}
```

</details>


Expected Result: <br>
`resultado`