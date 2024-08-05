import classes from './Title.module.css';

export default function Title({ children, classNames }) {
    return (
        <h1
            className={
                classNames ? `${classes.title} ${classNames}` : classes.title
            }
        >
            {children}{' '}
        </h1>
    );
}
