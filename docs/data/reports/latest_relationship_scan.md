# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T14:07:28.375363+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8578`

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

- `news_risk_high->crypto_major_24h` score `52.7203` n `72` status `ready` deltaP `31.5972` edge `4.2719` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `46.264` n `72` status `ready` deltaP `36.1112` edge `3.7525` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `38.0476` n `142` status `ready` deltaP `-2.3317` edge `3.2095` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `10.2597` n `72` status `ready` deltaP `41.1458` edge `0.5849` maxDD `-0.0053`
- `risk_on_high->unknown_4h` score `8.4127` n `52` status `ready` deltaP `-9.076` edge `0.7841` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.4127` n `52` status `ready` deltaP `-9.076` edge `0.7841` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.3479` n `52` status `ready` deltaP `45.8333` edge `0.3901` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.3479` n `52` status `ready` deltaP `45.8333` edge `0.3901` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.1471` n `142` status `ready` deltaP `38.791` edge `0.3895` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.6197` n `89` status `ready` deltaP `24.762` edge `0.5075` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5344` n `89` status `ready` deltaP `21.4871` edge `0.3604` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2867` n `98` status `ready` deltaP `19.0731` edge `0.1933` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.6355` n `52` status `ready` deltaP `31.3203` edge `0.0458` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6355` n `52` status `ready` deltaP `31.3203` edge `0.0458` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5299` n `142` status `ready` deltaP `27.5012` edge `0.0693` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.4809` n `98` status `ready` deltaP `20.8695` edge `0.1199` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.8648` n `72` status `ready` deltaP `23.9583` edge `0.0801` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.044` n `142` status `ready` deltaP `15.3601` edge `0.0223` maxDD `-0.3491`
- `news_risk_high->fx_4h` score `0.7724` n `89` status `ready` deltaP `9.2405` edge `0.0264` maxDD `-0.224`
- `news_risk_high->metal_1h` score `0.7195` n `98` status `ready` deltaP `15.6055` edge `0.0161` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
