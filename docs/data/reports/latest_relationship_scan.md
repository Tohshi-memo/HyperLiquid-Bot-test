# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T13:37:33.740084+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8560`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `news_risk_high->crypto_major_24h` score `52.9161` n `72` status `ready` deltaP `31.9444` edge `4.2859` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `46.4466` n `72` status `ready` deltaP `36.4584` edge `3.7654` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `38.014` n `142` status `ready` deltaP `-2.3317` edge `3.2067` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `10.4026` n `72` status `ready` deltaP `41.493` edge `0.5945` maxDD `-0.0053`
- `risk_on_high->unknown_4h` score `8.3791` n `52` status `ready` deltaP `-9.076` edge `0.7813` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.3791` n `52` status `ready` deltaP `-9.076` edge `0.7813` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.2997` n `52` status `ready` deltaP `45.4861` edge `0.3884` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2997` n `52` status `ready` deltaP `45.4861` edge `0.3884` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.0989` n `142` status `ready` deltaP `38.4438` edge `0.3878` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.6391` n `87` status `ready` deltaP `24.3745` edge `0.5117` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5327` n `87` status `ready` deltaP `21.3011` edge `0.3615` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2999` n `98` status `ready` deltaP `19.2228` edge `0.1934` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.6355` n `52` status `ready` deltaP `31.3203` edge `0.0458` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6355` n `52` status `ready` deltaP `31.3203` edge `0.0458` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5299` n `142` status `ready` deltaP `27.5012` edge `0.0693` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.4941` n `98` status `ready` deltaP `21.0192` edge `0.12` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.8998` n `72` status `ready` deltaP `24.3056` edge `0.0807` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.044` n `142` status `ready` deltaP `15.3601` edge `0.0223` maxDD `-0.3491`
- `news_risk_high->fx_4h` score `0.9247` n `87` status `ready` deltaP `10.8161` edge `0.0279` maxDD `-0.1693`
- `news_risk_high->metal_1h` score `0.7075` n `98` status `ready` deltaP `15.4558` edge `0.0161` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
