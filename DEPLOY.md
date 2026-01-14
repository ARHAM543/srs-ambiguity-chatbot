# Deploying to Vercel

## Option 1: Using Vercel CLI (Recommended for quick testing)

1.  **Install Vercel CLI:**
    ```bash
    npm install -g vercel
    ```

2.  **Login:**
    ```bash
    vercel login
    ```

3.  **Deploy:**
    Run the following command in your project folder:
    ```bash
    vercel
    ```
    - Follow the prompts (pres `Enter` to accept defaults).
    - When asked `Want to modify these settings?`, type `N`.

4.  **Production Deployment:**
    Once you are happy with the preview, deploy to production:
    ```bash
    vercel --prod
    ```

## Option 2: Using GitHub Integration

1.  Push your code to a GitHub repository.
2.  Go to [Vercel Dashboard](https://vercel.com/dashboard).
3.  Click **"Add New..."** -> **"Project"**.
4.  Import your GitHub repository.
5.  Vercel will automatically detect the settings from `vercel.json`.
6.  Click **"Deploy"**.

## Troubleshooting

-   **PDF Generation:** Note that Vercel has a read-only file system. The current PDF generation saves to a `pdfs/` folder. On Vercel (serverless), you generally cannot write files to disk and expect them to persist or be served via static URLs in the same way.
    -   *Mitigation:* The current code attempts to write to `pdfs/`. In a serverless environment, this might fail or the file won't be accessible via a subsequent HTTP request if the instance changes.
    -   *Fix:* For a production Vercel app, you would typically stream the PDF directly to the user instead of saving it to disk, or save it to cloud storage (like AWS S3).
    -   *Quick Fix for Demo:* I have verified the code, and `download_pdf` attempts to read from disk. This might be flaky on Vercel. If you encounter issues, we can refactor `pdf_generator.py` to return the bytes directly and `app.py` to stream them.

