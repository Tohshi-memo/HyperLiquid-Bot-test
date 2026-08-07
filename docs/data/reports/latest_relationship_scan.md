# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T20:52:29.435964+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->equity_24h` score `6.1591` n `87` status `ready` deltaP `2.6919` edge `0.8013` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.6796` n `87` status `ready` deltaP `14.7043` edge `0.2662` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4605` n `108` status `ready` deltaP `15.4358` edge `0.0861` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.407` n `87` status `ready` deltaP `11.6789` edge `0.1907` maxDD `-5.7715`
- `market_context_high->fx_24h` score `1.3298` n `87` status `ready` deltaP `28.7833` edge `0.0614` maxDD `-2.291`
- `market_context_high->commodity_1h` score `0.9606` n `109` status `ready` deltaP `12.0667` edge `0.0339` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.0798` n `109` status `ready` deltaP `6.5855` edge `0.0323` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.2548` n `109` status `ready` deltaP `4.7272` edge `-0.0032` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.4662` n `108` status `ready` deltaP `5.1717` edge `0.002` maxDD `-1.6928`
- `market_context_high->index_1h` score `-0.5855` n `109` status `ready` deltaP `-1.5794` edge `-0.0035` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.6313` n `108` status `ready` deltaP `1.7559` edge `-0.0038` maxDD `-1.1743`
- `market_context_high->metal_4h` score `-0.7902` n `108` status `ready` deltaP `1.0614` edge `-0.0075` maxDD `-2.7373`
- `market_context_high->metal_1h` score `-1.0195` n `109` status `ready` deltaP `-4.3317` edge `-0.0065` maxDD `-0.9664`
- `market_context_high->equity_4h` score `-1.0577` n `108` status `ready` deltaP `7.4977` edge `-0.0044` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.3604` n `109` status `ready` deltaP `-5.4373` edge `-0.0142` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.2031` n `109` status `ready` deltaP `-6.2627` edge `-0.0422` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.2056` n `87` status `ready` deltaP `6.8489` edge `-0.079` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.3224` n `87` status `ready` deltaP `-19.2067` edge `-0.1536` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.3682` n `108` status `ready` deltaP `-5.0644` edge `-0.0821` maxDD `-6.5193`
- `market_context_high->crypto_major_4h` score `-7.2292` n `108` status `ready` deltaP `-9.5867` edge `-0.1891` maxDD `-18.954`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
