import Button from '../../components/UI/Button/Button';
import ButtonIcon from '../../components/UI/ButtonIcon/ButtonIcon';
import Input from '../../components/UI/Input/Input';
import classes from './Registerpage.module.css';

export default function Registerpage() {
    return (
        <div className={classes.mainWrapper}>
            <form>
                <div className={classes.wrapper}>
                    <div className={classes.top}>
                        <h1 className={classes.title}>
                            Регистрация
                            <br /> на сайте
                        </h1>
                        <h2 className={classes.subtitle}>
                            Зарегистрируйте аккаунт
                            <br /> что бы продолжить
                        </h2>
                    </div>

                    <div className={classes.bottom}>
                        <ButtonIcon
                            classNames={classes.gmail}
                            src={'src/images/icons/gmail.svg'}
                        >
                            Gmail
                        </ButtonIcon>
                        <div className={classes.or}>или</div>

                        <Input classNames={classes.input} placeholder={'Имя'} />
                        <Input
                            classNames={classes.input}
                            placeholder={'Фамилия'}
                        />
                        <Input
                            classNames={classes.input}
                            placeholder={'Логин'}
                        />
                        <Input
                            classNames={classes.input}
                            placeholder={'Электронная почта'}
                        />
                        <Input
                            classNames={classes.input}
                            placeholder={'Пароль'}
                            type={'password'}
                        />
                        <Input
                            classNames={classes.input}
                            placeholder={'Повторите пароль'}
                            type={'password'}
                        />
                        <Button classNames={classes.authBtn}>
                            Создать аккаунт
                        </Button>
                        <div className={classes.hasAccount}>
                            Уже есть аккаунт?{' '}
                            <a className={classes.link}>Войти</a>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    );
}
