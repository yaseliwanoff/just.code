import {Tags} from "../../store/index.jsx"
export const TagsComponent = () => {
    return(
        <>
            <div>
                {Tags.map((tag) => <div key={tag.id} className={`btn`}>{tag.name}</div>)}
            </div>
            <div>
                <input title={`Поиск информации по сайту`}/> <button>Найти</button>
            </div>
            <div>
                <div className={`btn`}>Статьи</div>
                <div className={`btn`}>Новости</div>
                <div className={`btn`}>Ошибки и баги</div>
            </div>
        </>
    )
}
