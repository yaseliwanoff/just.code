import classes from './Textarea.module.css';

export default function Textarea({ children, classNames, placeholder }) {
    return (
        <textarea
            placeholder={placeholder}
            className={
                classNames
                    ? `${classNames} ${classes.textarea}`
                    : classes.textarea
            }
        >
            {children}
        </textarea>
    );
}
