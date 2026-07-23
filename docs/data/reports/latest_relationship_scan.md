# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T16:22:39.464492+00:00`
- Price records: `672`
- Market context records: `7686`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `1.914` n `137` status `ready` deltaP `16.3547` edge `0.2131` maxDD `-8.3438`
- `market_context_high->crypto_major_4h` score `0.5912` n `138` status `ready` deltaP `13.1959` edge `0.1331` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `0.4853` n `138` status `ready` deltaP `10.8696` edge `0.0316` maxDD `-3.0899`
- `market_context_high->equity_1h` score `0.2629` n `138` status `ready` deltaP `6.9722` edge `0.0738` maxDD `-4.2599`
- `market_context_high->index_1h` score `0.1429` n `138` status `ready` deltaP `7.1746` edge `0.0135` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.0553` n `138` status `ready` deltaP `6.2544` edge `0.0937` maxDD `-5.4629`
- `market_context_high->equity_4h` score `0.0209` n `138` status `ready` deltaP `2.2471` edge `0.2466` maxDD `-10.7123`
- `market_context_high->fx_24h` score `-0.1102` n `137` status `ready` deltaP `11.001` edge `0.0213` maxDD `-3.0343`
- `market_context_high->index_4h` score `-0.3121` n `138` status `ready` deltaP `10.7167` edge `0.0406` maxDD `-1.831`
- `market_context_high->crypto_alt_1h` score `-0.3203` n `138` status `ready` deltaP `1.9222` edge `0.0232` maxDD `-2.6829`
- `market_context_high->commodity_1h` score `-0.381` n `138` status `ready` deltaP `1.7626` edge `0.0024` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.4362` n `138` status `ready` deltaP `1.9811` edge `0.0098` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.465` n `138` status `ready` deltaP `0.2024` edge `-0.0011` maxDD `-0.4536`
- `market_context_high->metal_1h` score `-0.6272` n `138` status `ready` deltaP `0.8439` edge `0.0167` maxDD `-0.8851`
- `market_context_high->metal_24h` score `-1.1239` n `138` status `ready` deltaP `0.2567` edge `0.1007` maxDD `-3.7196`
- `market_context_high->metal_4h` score `-1.2292` n `138` status `ready` deltaP `0.0751` edge `0.0645` maxDD `-2.8073`
- `market_context_high->unknown_1h` score `-1.3248` n `138` status `ready` deltaP `-0.4491` edge `-0.0484` maxDD `-1.054`
- `market_context_high->commodity_24h` score `-1.4966` n `137` status `ready` deltaP `6.3494` edge `-0.0087` maxDD `-7.0012`
- `market_context_high->fx_4h` score `-1.583` n `138` status `ready` deltaP `-5.3982` edge `-0.0035` maxDD `-1.7438`
- `market_context_high->index_24h` score `-2.958` n `137` status `ready` deltaP `-19.8085` edge `-0.0161` maxDD `-3.8188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
