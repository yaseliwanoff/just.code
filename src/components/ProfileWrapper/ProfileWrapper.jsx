import { Link, useLocation } from 'react-router-dom';
import Container from '../Container/Container';
import Title from '../Title/Title';
import classes from './ProfileWrapper.module.css';
import Button from '../UI/Button/Button';
import { themes } from '../../data/themes';
import { useState } from 'react';
import Tag from '../UI/Tag/Tag';
import Article from '../Article/Article';
export default function ProfileWrapper() {
    const location = useLocation();
    const path = location.pathname.split('/');
    const forOtherUsers = path.length === 4;
    const [activeThemeIndex, setActiveThemeIndex] = useState(0);
    return (
        <Container>
            <div className={classes.wrapper}>
                <div className={classes.userWrapper}>
                    <div className={classes.userLogo}>
                        <div className={classes.img}></div>
                    </div>
                    <div className={classes.userInfo}>
                        <div className={classes.fullname}>
                            <div className={classes.firstname}>Максим</div>
                            <div className={classes.lastname}>Максимович</div>
                        </div>
                        <Title className={classes.username}>Username</Title>
                        <div className={classes.descr}>
                            Повседневная практика показывает, что внедрение
                            современных методик напрямую зависит от
                            инновационных методов
                        </div>
                    </div>
                </div>
            </div>
            <div className={classes.bottomSide}>
                <div className={classes.links}>
                    {forOtherUsers && (
                        <>
                            <Link
                                to={'/profile/test/added-articles'}
                                className={
                                    path.at(-1) === 'added-articles'
                                        ? classes.active
                                        : ''
                                }
                            >
                                Добавленные статьи
                            </Link>
                            <Link
                                to={'/profile/test/liked-articles'}
                                className={
                                    path.at(-1) === 'liked-articles'
                                        ? classes.active
                                        : ''
                                }
                            >
                                Лайкнутые статьи
                            </Link>
                        </>
                    )}
                    {!forOtherUsers && (
                        <>
                            <Link
                                to={'/profile/added-articles'}
                                className={
                                    path.at(-1) === 'added-articles'
                                        ? classes.active
                                        : ''
                                }
                            >
                                Добавленные статьи
                            </Link>
                            <Link
                                to={'/profile/saved-drafts'}
                                className={
                                    path.at(-1) === 'saved-drafts'
                                        ? classes.active
                                        : ''
                                }
                            >
                                Сохраненные черновики
                            </Link>
                            <Link
                                to={'/profile/liked-articles'}
                                className={
                                    path.at(-1) === 'liked-articles'
                                        ? classes.active
                                        : ''
                                }
                            >
                                Лайкнутые статьи
                            </Link>
                        </>
                    )}
                </div>
                <div className={classes.line}></div>
                {!forOtherUsers && path.at(-1) !== 'liked-articles' && (
                    <div className={classes.categories}>
                        {themes.map((theme, i) => (
                            <Button
                                key={theme}
                                classNames={
                                    activeThemeIndex === i
                                        ? `${classes.category} ${classes.activeTheme}`
                                        : classes.category
                                }
                                onClick={() => {
                                    setActiveThemeIndex(i);
                                }}
                            >
                                {theme}
                            </Button>
                        ))}
                    </div>
                )}
                <div className={classes.articles}>
                    <Article />
                    <Article />
                </div>
            </div>
        </Container>
    );
}
