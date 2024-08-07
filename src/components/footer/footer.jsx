import "./footer.css"
import {Link} from "react-router-dom";

export const Footer = () =>{
    return (
        <footer>
            <Link className={`logo`} to={`/`}>JUST.CODE</Link>
            <p>Пет-проект выполненный несколькими разработчиками и хранящиеся на github по <a href='#'>ссылке</a></p>
        </footer>
    )
}