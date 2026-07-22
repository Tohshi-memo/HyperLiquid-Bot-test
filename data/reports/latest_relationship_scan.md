# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T17:07:32.548083+00:00`
- Price records: `672`
- Market context records: `7585`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14534`

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

- `market_context_high->commodity_4h` score `0.1609` n `157` status `ready` deltaP `9.4373` edge `0.0265` maxDD `-2.4139`
- `market_context_high->index_1h` score `0.045` n `157` status `ready` deltaP `6.2422` edge `0.013` maxDD `-0.9072`
- `market_context_high->commodity_24h` score `-0.0368` n `149` status `ready` deltaP `12.747` edge `0.0703` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.1814` n `157` status `ready` deltaP `5.7458` edge `0.0038` maxDD `-1.5775`
- `market_context_high->unknown_24h` score `-0.3302` n `150` status `ready` deltaP `9.7083` edge `0.0986` maxDD `-8.1196`
- `market_context_high->crypto_alt_1h` score `-0.4426` n `157` status `ready` deltaP `0.656` edge `0.0135` maxDD `-3.6359`
- `market_context_high->crypto_major_1h` score `-0.4623` n `157` status `ready` deltaP `6.2769` edge `0.0141` maxDD `-5.5504`
- `market_context_high->equity_1h` score `-0.5418` n `157` status `ready` deltaP `6.0558` edge `0.0597` maxDD `-8.8965`
- `market_context_high->fx_24h` score `-0.5463` n `149` status `ready` deltaP `8.0584` edge `0.0154` maxDD `-3.5049`
- `market_context_high->fx_1h` score `-0.5577` n `157` status `ready` deltaP `0.6236` edge `-0.0007` maxDD `-0.6615`
- `market_context_high->index_4h` score `-0.5578` n `157` status `ready` deltaP `10.1278` edge `0.0336` maxDD `-3.4775`
- `market_context_high->metal_1h` score `-0.9067` n `157` status `ready` deltaP `1.7392` edge `0.0174` maxDD `-1.0307`
- `market_context_high->unknown_1h` score `-0.9843` n `157` status `ready` deltaP `-0.0954` edge `-0.0632` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.1651` n `157` status `ready` deltaP `1.772` edge `0.0486` maxDD `-10.1158`
- `market_context_high->equity_4h` score `-1.6077` n `157` status `ready` deltaP `2.7903` edge `0.212` maxDD `-21.9375`
- `market_context_high->metal_4h` score `-1.6115` n `157` status `ready` deltaP `-1.0369` edge `0.0485` maxDD `-4.8549`
- `market_context_high->crypto_major_4h` score `-1.6364` n `157` status `ready` deltaP `6.051` edge `0.0541` maxDD `-16.6726`
- `market_context_high->fx_4h` score `-2.2689` n `157` status `ready` deltaP `-2.762` edge `-0.0022` maxDD `-2.1439`
- `market_context_high->unknown_4h` score `-2.7393` n `157` status `ready` deltaP `9.9056` edge `-0.1827` maxDD `-6.0958`
- `market_context_high->metal_24h` score `-3.0009` n `150` status `ready` deltaP `-4.0139` edge `0.0881` maxDD `-13.3528`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
