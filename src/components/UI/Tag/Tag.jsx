import Button from '../Button/Button';
import classes from './Tag.module.css';

export default function Tag({ children, onClick, isActive, classNames }) {
    return (
        <Button
            classNames={
                isActive
                    ? classNames
                        ? `${classes.tag} ${classes.active} ${classNames}`
                        : `${classes.tag} ${classes.active}`
                    : classNames
                    ? `${classNames}`
                    : `${classes.tag}`
            }
            onClick={onClick}
        >
            {children}
        </Button>
    );
}
