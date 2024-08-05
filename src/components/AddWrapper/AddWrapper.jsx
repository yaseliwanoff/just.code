import { useState } from 'react';
import Container from '../Container/Container';
import Input from '../UI/Input/Input';
import Tag from '../UI/Tag/Tag';
import { tags as tagsArr } from '../../data/tags';
import Textarea from '../UI/Textarea/Textarea';
import Button from '../UI/Button/Button';
import classes from './AddWrapper.module.css';
import Title from '../Title/Title';

export default function AddWrapper({ title, isShortDescr, isFullDescr }) {
    const [tags, setTags] = useState([]);
    function onClickTagHandler(tag) {
        if (tags.includes(tag)) {
            setTags((prev) => prev.filter((item) => item !== tag));
        } else setTags((prev) => [...prev, tag]);
    }
    console.log(tags);
    return (
        <div className={classes.wrapper}>
            <Container>
                <Title>{title}</Title>
                <h2 className={classes.subtitle}>Добавить теги статьи</h2>
                <div className={classes.tags}>
                    {tagsArr.map((tag, i) => (
                        <Tag
                            key={i}
                            onClick={onClickTagHandler}
                            isActive={tags.includes(tag)}
                        >
                            {tag}
                        </Tag>
                    ))}
                </div>
                <Input
                    classNames={classes.input}
                    placeholder={'Заголовок статьи'}
                />
                {isShortDescr && (
                    <Input
                        classNames={classes.input}
                        placeholder={'Краткое описание статьи'}
                    />
                )}
                {isFullDescr && (
                    <Textarea
                        classNames={`${classes.input} ${classes.descr}`}
                        placeholder={'Полное описание статьи'}
                    ></Textarea>
                )}
                <Button classNames={classes.btn}>Опубликовать</Button>
                <Button classNames={classes.btn}>Сохранить как черновик</Button>
            </Container>
        </div>
    );
}
