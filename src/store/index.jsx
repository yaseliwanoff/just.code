// import {createStore} from "redux"

export const Userstate = {
    auth:true,
    img:"none",
    id:0,
    name: "Username"
}

export const Tags = [
    {
        id:1,
        name: "Frontend"
    },
    {
        id:2,
        name: "Backend"
    },
    {
        id:3,
        name: "Fullstack"
    },
    {
        id:4,
        name:"DevOps"
    },
    {
        id:5,
        name:"JavaScript"
    },
    {
        id:6,
        name: "Algorithms"
    },
    {
        id:7,
        name:"SQL"
    },
    {
        id:8,
        name:"React"
    },
    {
        id:9,
        name: "Vue"
    },
    {
        id:10,
        name:"Angular"
    },
    {
        id:11,
        name:"Django"
    },
    {
        id:12,
        name:"FastApi"
    },
    {
        id:13,
        name:"Flask"
    },
    {
        id:14,
        name: "C#"
    },
    {
        id:15,
        name: "C++"
    },
    {
        id:16,
        name:"Математика"
    },
    {
        id:17,
        name:"Информатика"
    }
]

export const  Contents=[
    {
    id:0,
    tags: ["Frontend", "Backend"],
    author: 0 ,//user,id
    title: "this is test title",
    low_content:"this is test low content",
    content:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    created_at:"12.12.2024"
},
    {
        id:1,
        tags: ["Frontend", "Backend"],
        author: 0 ,//user,id
        title: "this is test title",
        low_content:"this is test low content",
        content:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        created_at:"12.12.2024"
    },
]

export const PopArticle =[
    {
        title:"Это просто пример главного заголовка поста",
        des:"Повседневная практика показывает, что внедрение современных методик..."
    },
    {
        title:"Это просто пример главного заголовка поста",
        des:"Повседневная практика показывает, что внедрение современных методик..."
    },
    {
        title:"Это просто пример главного заголовка поста",
        des:"Повседневная практика показывает, что внедрение современных методик..."
    },
    {
        title:"Это просто пример главного заголовка поста",
        des:"Повседневная практика показывает, что внедрение современных методик..."
    }
]
// const reducer = (state = defaultState, action) =>{
//     switch (action.type){
//         case "GET_USERNAME":
//             return {...state, name: }
//         default:state
//     }
// }
//
// const store = createStore()