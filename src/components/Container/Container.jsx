import classes from './Container.module.css';

export default function Container({ children, classNames }) {
    return (
        <div
            className={
                classNames
                    ? `${classNames} ${classes.container}`
                    : classes.container
            }
        >
            {children}
        </div>
    );
}
