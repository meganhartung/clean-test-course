import { render, screen } from '@testing-library/react';
import App from './App';
import { BrowserRouter } from 'react-router-dom';
import axios from 'axios';

jest.mock('axios');

test('renders the welcome page', async () => {
  axios.get.mockResolvedValue({ data: { status: 'success', data: [] } });
  render(<App />, { wrapper: BrowserRouter });
  expect(await screen.findByText(/Welcome/i)).toBeInTheDocument();
});
