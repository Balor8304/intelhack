import './App.css';
import { useRef, useState, useEffect } from 'react';
import Image1 from "./images/new1.png";
import Image2 from "./images/new2.png";
import Image3 from "./images/new3.png";

function App() {
  const [showImage, setShowImage] = useState(false);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  // New state variables for productName, category, and description
  const [productName, setProductName] = useState('');
  const [category, setCategory] = useState('');
  const [description, setDescription] = useState('');
  const [resp, setResp] = useState('');

  const handleSend = (e) => {
    e.preventDefault();
    if (input.trim()) {
      setMessages([...messages, { text: input, sender: 'user' }]);
      setInput('');

             // Send user input to Django text generation endpoint
             fetch('http://127.0.0.1:8000/ai/airesp/', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                  input: input,
                  pro: productName,
                  desc: description,
              }),
          })
          .then((response) => response.json())
          .then((data) => {
              setMessages((prevMessages) => [
                  ...prevMessages,
                  { text: data.inp, sender: 'ai' },
              ]);
              console.log(data.inp)
          })
          .catch((error) => {
              console.error('Error:', error);
          });
      }
  };
  const [control, setControl] = useState(0);
  const descInputRef = useRef(null); // Create a ref to store the input element
  const [mHeight, setHeight] = useState(10);

  const handleKeyDown = (event) => {
    if (event.key === 'Enter' && event.shiftKey) {
      // Handle Shift+Enter
      if (mHeight < 500) setHeight(mHeight + 10);
      descInputRef.current.value += '\n'; // Add a newline character
      event.preventDefault(); // Prevent the default behavior of submitting the form
    }
  };

  const clicked = () => {
    if (!description || !productName) {
      // You should likely alert or show a message to the user instead of returning quietly.
      return;
    }

    fetch('http://127.0.0.1:8000/ai/airesponse/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        product: productName,
        category: category,
        desc: description,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          setMessages((prevMessages) => [
            ...prevMessages,
            { text: data.error, sender: 'ai' },
          ]);
        } else {
          // Format the response into a string to display
          setResp(data.desc);
          console.log(resp);
          

          // Update the image URL if provided in the response
          
            setShowImage(true); // Hide if no image URL is provided
          
        }
      })
      .catch((error) => {
        console.error('Error:', error);
      });

    // Clear messages and inputs when switching to chat mode
    setControl(1);
    setMessages([]);
    setInput('');
    setProductName('');
    setCategory('');
    setDescription('');
  };

  useEffect(() => {
    // Optional: Fetch initial data or images if needed
  }, []);

  if (control === 0) {
    return (
      <div className="container">
        <div className="inner">
          <h1>Hello User1</h1>
          <form className="form">
            <input
              className="productid"
              placeholder="Enter product name"
              value={productName}
              onChange={(e) => setProductName(e.target.value)} // Update productName state
            />
            <select
              className="drop"
              value={category}
              onChange={(e) => setCategory(e.target.value)} // Update category state
            >
              <option value="business">business</option>
              <option value="personal">personal</option>
            </select>
            <textarea
              style={{
                minHeight: mHeight,
                resize: 'none',
              }}
              className="desc"
              type="text"
              placeholder="Enter Your product description"
              ref={descInputRef} // Assign the ref to the input element
              onKeyDown={handleKeyDown} // Attach the event listener
              value={description}
              onChange={(e) => setDescription(e.target.value)} // Update description state
            />
            <button className="sub" onClick={clicked}>
              submit
            </button>
          </form>
        </div>
      </div>
    );
  } else {
    
    return (
      <div className="chat-container">
        
        <div className="messages">
        <div className={resp==="" ? "h" : "hi"} dangerouslySetInnerHTML={{ __html: resp }}/>
        {showImage && <img src={Image1} alt="Response Image" />}
        {showImage && <img src={Image2} alt="Response Image" />}
        {showImage && <img src={Image3} alt="Response Image" />}
          {!showImage && <>Generating idea...</>} {/* Conditionally render the image */}
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`message ${msg.sender}`}
              dangerouslySetInnerHTML={{ __html: msg.text }}
            />
          ))}
          <div style={{ paddingLeft: 0 }}>
          
        </div>
        </div>
        <form className="input-container" onSubmit={handleSend}>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type a message..."
            className="message-input"
          />
          <button type="submit" className="send-button">
            Send
          </button>
        </form>
      </div>
    );
  }
}

const TypingIndicator = () => {
  return (
    <div className="typing-indicator">
      <span className="dot"></span>
      <span className="dot"></span>
      <span className="dot"></span>
    </div>
  );
};

export default App;
