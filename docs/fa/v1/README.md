# مستندات توسعه‌دهندگان CoreLink v1 — فارسی

**وضعیت: Alpha / قرارداد عمومی `1.0.0-draft`**

قرارداد عمومی بررسی‌شده فعلی روی Device و Command متمرکز است و یک event envelope کانونی نیز وجود دارد. قابلیت‌های گسترده‌تر مانند telemetry/location، partner/webhook و ابزارهای توسعه هنوز بسته به contract و acceptance gateهای خود هستند.

## شروع

- [معماری CoreLink برای توسعه‌دهندگان](concepts/architecture.md)
- [احراز هویت و محدوده tenant](concepts/tenancy-authentication.md)
- [خطاها، retry و idempotency](operations/errors-retries-idempotency.md)
- [عیب‌یابی توسعه‌دهندگان](operations/troubleshooting.md)
- [Quickstart اجرایی انگلیسی](../../v1/quickstart.md)

## مرزهای مهم

- شناسه عمومی دستگاه `corelink_device_id` است.
- شناسه و payload خام provider بخشی از قرارداد عمومی CoreLink نیست.
- وجود implementation داخلی به معنی وجود API عمومی پشتیبانی‌شده نیست.
- Console در وضعیت Alpha است؛ demo/fallback آن جای runtime/API acceptance را نمی‌گیرد.
- TypeScript و Python SDK در وضعیت Prerelease Alpha هستند.
- Java SDK، CLI، MCP Server و Mock Server در وضعیت Scaffold/Planned هستند.

## منبع حقیقت

Schema و رفتار machine-readable در [`api-contracts`](https://github.com/CoreLinkPlatform/api-contracts) تعریف می‌شوند. این ترجمه برای توضیح استفاده و مرزهای عملیاتی است و schema مستقلی ایجاد نمی‌کند.