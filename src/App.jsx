import { Route, Routes } from 'react-router-dom';
import Loginpage from './pages/Loginpage/Loginpage';
import Registerpage from './pages/Registerpage/Registerpage';
import AddArticlepage from './pages/AddArticlepage/AddArticlepage';
import AddNewspage from './pages/AddNewspage/AddNewspage';
import AddErrorsAndBugspage from './pages/AddErrorsAndBugspage/AddErrorsAndBugspage';
import DeleteArticlepage from './pages/DeleteArticlepage/DeleteArticlepage';
import DeleteNewspage from './pages/DeleteNewspage/DeleteNewspage';
import DeleteErrorsAndBugspage from './pages/DeleteErrorsAndBugspage/DeleteErrorsAndBugspage';
import ProfileWrapper from './components/ProfileWrapper/ProfileWrapper';

function App() {
    return (
        <>
            <ProfileWrapper forOtherUsers={true} />
            <Routes>
                <Route path="/login" element={<Loginpage />} />
                <Route path="/register" element={<Registerpage />} />
                <Route path="/add/article" element={<AddArticlepage />} />
                <Route path="/add/news" element={<AddNewspage />} />
                <Route
                    path="/add/errors-and-bugs"
                    element={<AddErrorsAndBugspage />}
                />
                <Route path="/add/"></Route>
                <Route path="/delete/article" element={<DeleteArticlepage />} />
                <Route path="/delete/news" element={<DeleteNewspage />} />
                <Route
                    path="/delete/errors-and-bugs"
                    element={<DeleteErrorsAndBugspage />}
                />
                <Route path="/profile/added-articles" />
                <Route path="/profile/saved-drafts" />
                <Route path="/profile/liked-articles" />
                <Route path="/profile/:id/added-articles" />
                <Route path="/profile/:id/liked-articles" />
            </Routes>
        </>
    );
}

export default App;
