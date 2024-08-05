import Button from '../../components/UI/Button/Button';
import ButtonIcon from '../../components/UI/ButtonIcon/ButtonIcon';
import Input from '../../components/UI/Input/Input';
import classes from './Loginpage.module.css';

export default function Loginpage() {
    return (
        <div className={classes.mainWrapper}>
            <form>
                <div className={classes.wrapper}>
                    <div className={classes.top}>
                        <h1 className={classes.title}>
                            Вход
                            <br /> на сайт
                        </h1>
                        <h2 className={classes.subtitle}>
                            Войдите в аккаунт
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

                        <Input
                            classNames={classes.input}
                            placeholder={'Логин'}
                        />
                        <Input
                            classNames={classes.input}
                            placeholder={'Пароль'}
                            type={'password'}
                        />
                        <Button classNames={classes.authBtn}>Войти</Button>
                        <div className={classes.hasAccount}>
                            Уже есть аккаунт?{' '}
                            <a className={classes.link}>Сделать</a>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    );
}
