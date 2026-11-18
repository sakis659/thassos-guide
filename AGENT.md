# Οδηγίες για τον agent του Thassos Guide

Ο agent τρέχει **μία φορά την εβδομάδα**. Μεγαλώνει το site με έναν νέο οδηγό κάθε φορά και ελέγχει
ότι τα υπάρχοντα στοιχεία ισχύουν ακόμα. **Δεν δημοσιεύει ποτέ τίποτα χωρίς την έγκριση του χρήστη (Θανάσης).**

## Πώς είναι φτιαγμένο το site
- `content.json`: όλο το περιεχόμενο σε 6 γλώσσες (`en`, `el`, `ro`, `bg`, `de`, `tr`)
  - `i18n.<lang>`: τα κείμενα της αρχικής σελίδας
  - `guides`: οι αναλυτικοί οδηγοί (ένας για κάθε παραλία, χωριό ή θέμα)
  - `photos`: οι φωτογραφίες, με **φωτογράφο και άδεια**
- `build.py`: φτιάχνει όλες τις σελίδες, το `sitemap.xml` και το `robots.txt`. Τρέχει με `python3 build.py`.
- Μην αλλάζεις τα αρχεία HTML με το χέρι. Αλλάζεις μόνο το `content.json` (και το `build.py` αν χρειάζεται).

## 1. Ένας νέος οδηγός την εβδομάδα
Διάλεξε το **πρώτο θέμα της λίστας** που δεν υπάρχει ακόμα στο `guides`:
1. Marble Beach (Saliara) · `marble-beach`
2. Golden Beach (Chrysi Ammoudia) · `golden-beach`
3. Aliki: beach and ancient marble quarry · `aliki`
4. Ferries to Thassos: Keramoti and Kavala, a complete guide · `ferries`
5. Panagia village · `panagia`
6. Monastery of Archangel Michael · `archangel-michael-monastery`
7. Limenas: ancient sites and the archaeological museum · `limenas`
8. Paradise Beach · `paradise-beach`
9. Theologos village · `theologos`
10. Kazaviti (Prinos) villages · `kazaviti`
11. Getting around Thassos: car, scooter, buses · `getting-around`
12. Thassos in 3 days: itinerary · `3-day-itinerary`
13. Thassos with kids · `thassos-with-kids`
14. Potos and Limenaria · `potos-limenaria`
15. Thassos honey and local products · `honey-local-products`
16. Hiking on Thassos (Ypsario, old paths) · `hiking`

Όταν τελειώσει η λίστα, πρότεινε στον χρήστη νέα θέματα που ψάχνει ο κόσμος.

**Κανόνες για κάθε οδηγό:**
- Ψάξε **τουλάχιστον 3 πηγές** και κράτα μόνο ό,τι επιβεβαιώνουν. Ό,τι αλλάζει συχνά (τιμές,
  ακριβή ωράρια) το γράφεις γενικά και παραπέμπεις στην πηγή.
- Γράψε **με δικά σου λόγια**, στο ίδιο ύφος με τον οδηγό `giola`: `title` έως ~65 χαρακτήρες με τη
  βασική αναζήτηση (π.χ. «Marble Beach Thassos: …»), `description` έως ~160 χαρακτήρες, `h1`,
  `intro`, 3–5 `sections`, 3 `tips`.
- **Και οι 6 γλώσσες**, με φυσικές μεταφράσεις, όχι κατά λέξη. Τοπωνύμια όπως τα γράφει ο ντόπιος
  κάθε γλώσσας (π.χ. TR: Taşoz, BG: Тасос).
- `sources`: οι πηγές με link. `updated`: η σημερινή ημερομηνία.
- **Φωτογραφία:** χρησιμοποίησε μόνο φωτογραφίες με **επιβεβαιωμένη ελεύθερη άδεια**
  (Wikimedia Commons κλπ.), όπου βλέπεις καθαρά τον φωτογράφο και την άδεια (CC BY, CC BY-SA,
  Public domain). Πρόσθεσέ την στο `photos`, με `file`, `author`, `license`, `license_url`.
  Αν δεν βρεις, χρησιμοποίησε μια υπάρχουσα (π.χ. `olives`, `limenas`). **Ποτέ εικόνες από AI.**

## 2. Έλεγχος στοιχείων
- Έλεγξε αν άλλαξαν τα βασικά στοιχεία της αρχικής σελίδας: διάρκεια και συχνότητα πλοίων,
  αεροδρόμιο κλπ. Αν άλλαξαν, διόρθωσέ τα **και στις 6 γλώσσες**.
- Σημείωσε στο μήνυμα προς τον χρήστη σημαντικές εκδηλώσεις των επόμενων 2 μηνών
  (π.χ. πανηγύρια, φεστιβάλ). Δεν μπαίνουν στο site χωρίς έγκριση.
- Ενημέρωσε το `updated` στο `content.json`.

## 3. Build και έλεγχος
1. `python3 -m json.tool content.json > /dev/null` (έγκυρο JSON)
2. `python3 build.py`
3. Άνοιξε με Playwright τουλάχιστον μία σελίδα του νέου οδηγού και έλεγξε ότι δεν είναι σπασμένη.

## 4. Έγκριση: ΠΟΤΕ push στο main
1. Branch `guides/ΕΕΕΕ-ΜΜ-ΗΗ` → commit (`content.json` και ό,τι έφτιαξε το build) → push.
2. Pull Request προς `main`, με περίληψη στα ελληνικά: ποιος οδηγός, πηγές, φωτογραφία με άδεια,
   διορθώσεις στοιχείων.
3. Στείλε μήνυμα και ειδοποίηση στον χρήστη, στα ελληνικά: τι έγινε, link του PR, link προεπισκόπησης
   αν το Cloudflare δίνει, και ερώτηση αν θέλει να δημοσιευτεί.
   - Για δημοσίευση πατάει **Merge** στο GitHub ή απαντάει «ναι». Τότε κάνεις εσύ merge.
   - Αν ζητήσει αλλαγές, διορθώνεις το branch και ξαναρωτάς.
