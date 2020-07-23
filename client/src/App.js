import React, {useState} from 'react';
import axios from 'axios';
import './app.css'

function App() {
  const [texto, setTexto] = useState('')
  const [predic, setPredic] = useState('')

  const enviar = (e) => {
      e.preventDefault()
      console.log(texto)

      axios.post('https://classificador-noticias.herokuapp.com/', {
        corpo: texto,
      })
      .then(function (response) {
        setPredic(response.data)
      })
      .catch(function (error) {
        alert('Ocorreu um erro na classificação!')
        console.log(error);
      });
  }

  return (
    <div className="container">
      <div className="app">
        <h1>Classificador de Notícias</h1>
        <form onSubmit={enviar} className="form">
          <textarea 
          placeholder="Insira aqui o texto para ser classificado"
          onChange={e => setTexto(e.target.value)}
          ></textarea>
          <button type='submit'>Classificar</button>
        </form>
        { predic !== '' &&
          <h2>Nosso modelo acredita que seu texto é sobre <strong>{predic}</strong></h2>
        }
      </div>
    </div>
  );
}

export default App;
