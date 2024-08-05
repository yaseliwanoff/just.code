import classes from './Button.module.css';

export default function Button({ children, classNames, onClick }) {
    return (
        <button
            onClick={() => onClick(children)}
            className={
                !classNames ? classes.btn : `${classes.btn} ${classNames}`
            }
        >
            {children}
        </button>
    );
}
