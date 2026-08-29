# معماری CoreLink برای توسعه‌دهندگان

**وضعیت: مستندات Alpha**

CoreLink یک مرز محصول مستقل از provider در مقابل موتورهای اتصال دستگاه، زیرساخت هویت، datastoreها و integration providerها ایجاد می‌کند. کد application باید به قراردادهای CoreLink وابسته باشد، نه API یا شناسه‌های اختصاصی provider.

## مرز محصول

```text
Application / Console / SDK / CLI / MCP
                 |
                 v
        CoreLink public contracts
                 |
      +----------+-----------+
      |                      |
  Core runtime          Event/Webhook boundary
      |
  Integration adapters
      |
  Device/connectivity providers
```

مرز عمومی عمداً از implementation خصوصی runtime کوچک‌تر است. پیاده‌سازی یک قابلیت در داخل Platform به‌تنهایی آن قابلیت را به API عمومی پشتیبانی‌شده تبدیل نمی‌کند.

## هویت کانونی

resourceهای عمومی از شناسه‌های متعلق به CoreLink استفاده می‌کنند. در قرارداد فعلی Device، شناسه عمومی `corelink_device_id` است. شناسه provider ممکن است برای reconciliation داخلی نگهداری شود، اما شناسه resource عمومی نیست.

## مرز tenant

عملیات عمومی tenant-scoped هستند. قرار گرفتن `tenant_id` در URL مجوز دسترسی ایجاد نمی‌کند؛ actor احراز هویت‌شده باید برای همان tenant و operation مجاز باشد. `401` و `403` باید خطای auth/authorization تلقی شوند، نه سیگنالی برای امتحان tenant دیگر.

## مصرف‌کننده‌های contract-first

- `api-contracts` مرجع OpenAPI، AsyncAPI و schemaهاست.
- `developer-docs` نحوه استفاده را توضیح می‌دهد.
- SDKهای generated باید provenance قرارداد immutable داشته باشند.
- Console، CLI، Mock و MCP نباید schema عمومی موازی و خصوصی بسازند.

## استقلال از provider

رفتار اختصاصی provider پشت Integration Adapter می‌ماند. public docs، SDK typeها، error codeها، exampleها، MCP toolها و مدل دامنه Console باید از واژگان CoreLink استفاده کنند، مگر در سند operator-only که عمداً جزئیات provider را توضیح می‌دهد.

## evidence قبل از claim

CoreLink بین implementation، deployment و Product Acceptance تفاوت می‌گذارد. merge شدن PR یا سبز بودن CI فقط implementation evidence است؛ maturity پشتیبانی‌شده به contract، security، runtime/conformance، documentation و release gateهای مرتبط نیز نیاز دارد.