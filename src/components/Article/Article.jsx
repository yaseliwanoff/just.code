import classes from './Article.module.css';
import Tag from '../UI/Tag/Tag';
import Title from '../Title/Title';
import { useNavigate } from 'react-router-dom';

export default function Article() {
    const navigate = useNavigate();
    return (
        <div className={classes.articleWrapper} onClick={() => navigate('/')}>
            <div className={classes.articleUserWrapper}>
                <div className={classes.articleLogo}>
                    <div className={classes.articleImg}></div>
                </div>
                <div className={classes.articleUserInfo}>
                    <div className={classes.articleUsername}>username</div>
                    <div className={classes.articleDate}>10 минут назад</div>
                </div>
            </div>
            <div className={classes.articleUserTags}>
                <Tag isActive={true} classNames={classes.articleTag}>
                    Frontend
                </Tag>
                <Tag isActive={true} classNames={classes.articleTag}>
                    Frontend
                </Tag>
                <Tag isActive={true} classNames={classes.articleTag}>
                    Frontend
                </Tag>
            </div>
            <Title classNames={classes.articleTitle}>
                Это просто пример главного заголовка поста
            </Title>
            <div className={classes.articleDescr}>
                Повседневная практика показывает, что внедрение современных
                методик напрямую зависит от инновационных методов управления
                процессами. Противоположная точка зрения подразумевает, что
                активно развивающиеся страны третьего мира представляют собой не
                что иное, как квинтэссенцию...
            </div>
            <div className={classes.articleViews}>Число просмотров: 10</div>
        </div>
    );
}
