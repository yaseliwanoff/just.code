import Container from '../Container/Container';
import Title from '../Title/Title';
import Button from '../UI/Button/Button';
import Tag from '../UI/Tag/Tag';
import classes from './DeleteWrapper.module.css';

export default function DeleteWrapper({ problem, isDescr }) {
    return (
        <Container>
            <Title>{problem}</Title>
            <div className={classes.wrapper}>
                <div className={classes.userWrapper}>
                    <div className={classes.avatar}></div>
                    <div className={classes.userInfo}>
                        <div className={classes.username}>username</div>
                        <div className={classes.time}>10 минут назад</div>
                    </div>
                </div>
                <div className={classes.tags}>
                    <Tag classNames={classes.tag}>Frontend</Tag>
                    <Tag classNames={classes.tag}>backend</Tag>
                    <Tag classNames={classes.tag}>django</Tag>
                </div>
                <h2 className={classes.title}>
                    Это просто пример главного заголовка поста
                </h2>
                {isDescr && (
                    <div className={classes.descr}>
                        Повседневная практика показывает, что внедрение
                        современных методик напрямую зависит от инновационных
                        методов управления процессами. Противоположная точка
                        зрения подразумевает, что активно развивающиеся страны
                        третьего мира представляют собой не что иное, как
                        квинтэссенцию...
                    </div>
                )}
                <div className={classes.views}>Число просмотров: 10</div>
            </div>
            <Button classNames={classes.btn}>Удалить</Button>
            <Button classNames={classes.btn}>Отмена</Button>
        </Container>
    );
}
