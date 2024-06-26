

function main() {
    try {
        fetch('http://localhost:8000/')
        .then(response => response.json())
        .then(data => console.log(data));   
    } catch (error) {
        console.log({error})
    }
}

 main()