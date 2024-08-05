import classes from './Input.module.css';

export default function Input({ type, placeholder, classNames }) {
    return (
        <input
            className={
                !classNames ? classes.input : `${classes.input} ${classNames}`
            }
            type={type || 'text'}
            placeholder={placeholder || ''}
        />
    );
}
