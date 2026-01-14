# Test SRS Documents for Interactive Clarification

Use these sample documents to test the interactive clarification feature. Each has different types and numbers of ambiguous terms.

---

## Test Case 1: E-Commerce Platform (Simple - 3 ambiguous terms)

```
1. The system should load pages fast.
2. Users can add products to their shopping cart.
3. The checkout process must be secure.
4. The application should have good performance during peak hours.
```

**Expected Ambiguous Terms:** "fast", "secure", "good"

**Sample Answers:**
- fast → "within 1 second"
- secure → "SSL/TLS encryption and PCI-DSS compliance"
- good → "handle 10,000 concurrent users without degradation"

---

## Test Case 2: Mobile Banking App (Medium - 5 ambiguous terms)

```
1. The user can login using biometric authentication.
2. The app should be user-friendly and intuitive.
3. All transactions must be encrypted and secure.
4. The system should respond quickly to balance inquiries.
5. The app must work reliably on both iOS and Android.
6. Push notifications should be sent as soon as possible.
```

**Expected Ambiguous Terms:** "user-friendly", "intuitive", "secure", "quickly", "reliably", "as soon as possible"

**Sample Answers:**
- user-friendly → "maximum 3 taps to complete any transaction"
- intuitive → "follows iOS HIG and Material Design guidelines"
- secure → "AES-256 encryption with OAuth 2.0"
- quickly → "within 500 milliseconds"
- reliably → "99.9% uptime"
- as soon as possible → "within 5 seconds of transaction completion"

---

## Test Case 3: Healthcare Management System (Complex - 7 ambiguous terms)

```
1. The system shall store patient records securely with appropriate encryption.
2. Doctors can access patient data easily from any device.
3. The interface should be simple and clean.
4. Search functionality must be fast and efficient.
5. The system should handle a large number of concurrent users.
6. Reports must be generated quickly with good accuracy.
7. The application must be highly available and robust.
```

**Expected Ambiguous Terms:** "appropriate", "easily", "simple", "fast", "large", "quickly", "good", "highly available", "robust"

**Sample Answers:**
- appropriate → "HIPAA-compliant with AES-256 encryption"
- easily → "single sign-on with role-based access"
- simple → "maximum 5 main navigation items"
- fast → "return results within 2 seconds"
- large → "support 5,000 concurrent users"
- quickly → "generate within 10 seconds"
- good → "99.5% accuracy"
- highly available → "99.99% uptime with failover"
- robust → "handle 2x expected load without failure"

---

## Test Case 4: Social Media Platform (Usability Focus - 6 ambiguous terms)

```
1. Users can create an account easily.
2. The news feed should load fast and smoothly.
3. Image uploads must be quick regardless of size.
4. The app should have excellent performance on mobile devices.
5. Privacy settings must be clear and accessible.
6. The interface should be modern and attractive.
```

**Expected Ambiguous Terms:** "easily", "fast", "smoothly", "quick", "excellent", "clear", "modern", "attractive"

**Sample Answers:**
- easily → "complete registration in under 2 minutes"
- fast → "initial load within 1.5 seconds"
- smoothly → "60 FPS scroll rate"
- quick → "upload complete within 3 seconds for 5MB images"
- excellent → "maintain 60 FPS on devices from last 3 years"
- clear → "privacy settings with tooltips and examples"
- modern → "follow 2024 UI trends with glassmorphism"
- attractive → "pass user satisfaction score of 4.5/5"

---

## Test Case 5: Video Streaming Service (Performance Focus - 8 ambiguous terms)

```
1. The platform should stream videos smoothly without buffering.
2. Users can search for content quickly and find relevant results.
3. Video quality should adapt automatically based on connection speed.
4. The app must be lightweight and not consume excessive resources.
5. Downloads should be fast and reliable.
6. The system should support a large user base during peak times.
7. Content recommendations must be accurate and personalized.
8. Playback controls should be responsive and easy to use.
```

**Expected Ambiguous Terms:** "smoothly", "quickly", "automatically", "lightweight", "excessive", "fast", "reliable", "large", "accurate", "responsive", "easy"

**Sample Answers:**
- smoothly → "maintain buffer of at least 30 seconds ahead"
- quickly → "display results within 500ms of keystroke"
- automatically → "switch quality within 2 seconds of bandwidth change"
- lightweight → "maximum 150MB app size"
- excessive → "use no more than 10% CPU on mobile"
- fast → "achieve 5MB/s download speed minimum"
- reliable → "99% successful downloads without corruption"
- large → "support 1 million concurrent streams"
- accurate → "85% user satisfaction with recommendations"
- responsive → "respond to controls within 100ms"
- easy → "all controls accessible within one tap"

---

## 🎯 Testing Instructions

### For Each Test Case:

1. **Copy the requirements** (everything between the triple backticks)
2. **Paste into chatbot** at http://127.0.0.1:5000
3. **Wait for analysis** - bot will show classifications and detected terms
4. **Answer each question** - use the sample answers above or create your own
5. **Review improvements** - see how your answers are incorporated

### What to Look For:

✅ **Correct Detection**: All expected ambiguous terms are identified
✅ **Relevant Questions**: Questions make sense for each term
✅ **Acknowledgment**: Bot confirms each answer before asking next
✅ **Sequential Flow**: Questions asked one at a time, not all at once
✅ **Personalization**: Final improvements use your exact answers
✅ **Before/After**: Can compare original vs improved requirements

---

## 💡 Tips for Testing

### Try Different Answers:
- Test with **very specific** values: "within 250 milliseconds"
- Test with **ranges**: "between 2-5 seconds"
- Test with **multiple criteria**: "AES-256 encryption with OAuth 2.0 and MFA"
- Test with **standards**: "ISO 27001 compliant"

### Edge Cases to Test:
- ✏️ Very short answer: "2 seconds"
- 📝 Very detailed answer: "The system should use AES-256 encryption for data at rest, TLS 1.3 for data in transit, implement OAuth 2.0 for authentication, enforce multi-factor authentication, and log all access attempts with audit trails"
- 🔢 Numeric answer: "99.99%"
- 📊 Multiple metrics: "handle 10,000 users with less than 100ms latency"

---

## 📊 Expected Classifications

| Test Case | Functional Requirements | Non-Functional Requirements |
|-----------|------------------------|----------------------------|
| Test 1    | 1                      | 3                          |
| Test 2    | 1                      | 5                          |
| Test 3    | 2                      | 5                          |
| Test 4    | 1                      | 5                          |
| Test 5    | 2                      | 6                          |

---

## 🚀 Quick Copy-Paste

### Test 1 (Quick Test):
```
1. The system should load pages fast.
2. Users can add products to their shopping cart.
3. The checkout process must be secure.
4. The application should have good performance during peak hours.
```

### Test 2 (Mobile Banking):
```
1. The user can login using biometric authentication.
2. The app should be user-friendly and intuitive.
3. All transactions must be encrypted and secure.
4. The system should respond quickly to balance inquiries.
5. The app must work reliably on both iOS and Android.
6. Push notifications should be sent as soon as possible.
```

### Test 3 (Healthcare):
```
1. The system shall store patient records securely with appropriate encryption.
2. Doctors can access patient data easily from any device.
3. The interface should be simple and clean.
4. Search functionality must be fast and efficient.
5. The system should handle a large number of concurrent users.
6. Reports must be generated quickly with good accuracy.
7. The application must be highly available and robust.
```

### Test 4 (Social Media):
```
1. Users can create an account easily.
2. The news feed should load fast and smoothly.
3. Image uploads must be quick regardless of size.
4. The app should have excellent performance on mobile devices.
5. Privacy settings must be clear and accessible.
6. The interface should be modern and attractive.
```

### Test 5 (Video Streaming):
```
1. The platform should stream videos smoothly without buffering.
2. Users can search for content quickly and find relevant results.
3. Video quality should adapt automatically based on connection speed.
4. The app must be lightweight and not consume excessive resources.
5. Downloads should be fast and reliable.
6. The system should support a large user base during peak times.
7. Content recommendations must be accurate and personalized.
8. Playback controls should be responsive and easy to use.
```

---

## ✅ Success Criteria

Your chatbot is working correctly if:

1. ✅ Detects **all** ambiguous terms listed
2. ✅ Asks **specific questions** with helpful examples
3. ✅ **Acknowledges** each answer with green checkmark
4. ✅ **Waits** for your response before asking next question
5. ✅ **Incorporates** your exact answers into improvements
6. ✅ Shows **before/after** comparison at the end
7. ✅ **Classifies** requirements as FR/NFR correctly
8. ✅ Provides **completion message** to analyze another document

---

Happy Testing! 🎉
