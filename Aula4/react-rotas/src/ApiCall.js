import React, {useState ,useEffect} from "react";

export default function CallApi(){
    const [tasks, setUsers] = useState([]);

    const getApiData = async () => {

        const response = await fetch(
            `http://localhost:5000/api/tasks/`
        ).then((response) => response.json());
            console.log(response);
        setUsers(response);
    };

    useEffect(() => {
        getApiData();
    }, []);

    return(
        <div className="app">
            {tasks && tasks.map((task) => (
                <div className="item-container">
                Nome da Tarefa: {task.name} - Descrição: {task.description}
                </div>
            ))}
        </div>
    );
}