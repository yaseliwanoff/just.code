import {createBrowserRouter} from "react-router-dom";
import {Ziro} from "./pages/ziro/ziro.jsx";
import App from "../App.jsx";
import {MainPage} from "./pages/main/main.jsx";

const r = createBrowserRouter([
    {
        path:"/",
        element:<App/>,
        children: [
            {
                path:"/",
                element:(<Ziro/>)
            },
            {
                path:"/main",
                element:(<MainPage/>)
            }
        ]
    },
])

export default r;