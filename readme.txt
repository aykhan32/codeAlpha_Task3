
🧨 Vulnerabilities Identified

#	Type	Description	Risk
1	Command Injection	os.system() used with unsanitized string.	⚠️ High
2	Unsafe Deserialization	pickle.loads() on user input can execute arbitrary code.	🔥 Critical
3	Path Traversal	File saved with unsanitized username.	⚠️ Medium
4	Debug Mode Enabled	app.run(debug=True) exposes internals in prod.	⚠️ High
5	No Input Validation	No checks on username, file, or data.	⚠️ Medium
✅ Secure Coding Recommendations

Vulnerability	Recommended Fix
os.system()	Use subprocess.run() with validated arguments.
pickle.loads()	Replace with json.loads() or restrict input source.
Path traversal	Sanitize username, use secure_filename() from Flask.
Debug mode	Disable in production (debug=False).
Input validation	Use regex or Flask-WTF for input validation.
