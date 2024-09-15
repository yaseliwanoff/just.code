import {TagsComponent} from "../../../components/Tags/Tags.jsx";
import {Contents, PopArticle} from "../../../store/index.jsx";

const ContentComponent = (props) => {
    let Contents = props.Content
    return(
        <>
        {Contents.map((content)=>
            <div key={content.id} className={`article`}>
                {content.tags.map((tag,index)=><div key={index}>{tag}</div>)}
                <h1>{content.title}</h1>
                <p>{content.low_content}</p>
            </div>)}

        </>

    )
}

const PopularArticle=(props)=>{
    const articles = props.Article
    return (
        <div className={`PopularArticle`}>
            {articles.map((article,index)=>
                <div key={index}>
                    <h1>{article.title}</h1>
                    <p>{article.des}</p>
                </div>
            )}
        </div>
    )
}

export const MainPage = () =>{
    return(
        <div>
            <TagsComponent/>
            <ContentComponent Content={Contents}/>
            <PopularArticle Article={PopArticle}/>
        </div>
    )
}