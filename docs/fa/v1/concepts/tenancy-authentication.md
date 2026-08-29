# احراز هویت و محدوده Tenant

**وضعیت: Alpha / قرارداد عمومی `1.0.0-draft`**

قرارداد عمومی فعلی درخواست‌ها را با Bearer JWT احراز هویت می‌کند. این قرارداد endpoint عمومی برای صدور self-service token تعریف نمی‌کند؛ بنابراین application باید credential را از مسیر onboarding/environment تأییدشده دریافت کند و OAuth flow خیالی نسازد.

## مرز درخواست

```http
Authorization: Bearer <access-token>
```

مسیر resourceهای tenant-scoped نیز tenant را مشخص می‌کند، اما مقدار URL جای authorization را نمی‌گیرد. actor، scope/claim، membership و policy سمت سرور همچنان تعیین‌کننده دسترسی‌اند.

## قواعد client

- access token را در source control، screenshot، issue یا log ذخیره نکنید.
- در browser application در صورت امکان از session/BFF سمت سرور استفاده کنید تا CoreLink token در browser storage قرار نگیرد.
- خطای `401` یا `403` را با حدس زدن tenant دیگر retry نکنید.
- machine credential باید least-privilege باشد.
- rotation و revocation بخشی از lifecycle عادی credential هستند.

## خطاها

- `401`: احراز هویت وجود ندارد، نامعتبر است یا دیگر پذیرفته نمی‌شود.
- `403`: actor احراز هویت شده اما برای tenant یا operation مجاز نیست.
- `404`: از آن نتیجه نگیرید که resource در tenant دیگری وجود دارد؛ API امن ممکن است عمداً وجود resource را افشا نکند.

## credentialهای partner/service

lifecycle کامل partner/service credential از Device/Command draft فعلی گسترده‌تر است. می‌توان اصول امنیتی آن را مستند کرد، اما endpoint یا support claim دقیق فقط پس از contract/runtime acceptance نسخه‌دار معتبر است.

## مرز Console

CoreLink Console از OIDC/Auth.js و BFF سمت سرور استفاده می‌کند تا bearer token در browser storage نگهداری نشود. این معماری یک reference implementation برای browser است، نه الزام استفاده از Auth.js برای همه clientها.