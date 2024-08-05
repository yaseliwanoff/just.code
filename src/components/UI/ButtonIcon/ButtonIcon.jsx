import Button from '../Button/Button';
import classes from './ButtonIcon.module.css';

export default function ButtonIcon({ src, children, classNames }) {
    return (
        <div
            className={
                classNames
                    ? `${classNames} ${classes.wrapper}`
                    : `${classes.wrapper}`
            }
            style={{ position: 'relative' }}
        >
            <img src={src} className={classes.inputWithIcon} />
            <Button
                classNames={
                    classNames
                        ? `${classNames} ${classes.btn}`
                        : `${classes.btn}`
                }
            >
                {children}
            </Button>
        </div>
    );
}
