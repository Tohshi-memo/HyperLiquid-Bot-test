# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T13:07:32.947617+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11740`

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

- `market_context_high->commodity_4h` score `1.1662` n `118` status `ready` deltaP `13.3217` edge `0.093` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.6364` n `121` status `ready` deltaP `9.5759` edge `0.0308` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.5235` n `111` status `ready` deltaP `20.5613` edge `0.0493` maxDD `-4.2077`
- `market_context_high->metal_24h` score `0.4451` n `111` status `ready` deltaP `0.5881` edge `0.1366` maxDD `-2.2743`
- `market_context_high->fx_1h` score `0.0284` n `121` status `ready` deltaP `7.1745` edge `-0.0038` maxDD `-0.9998`
- `market_context_high->fx_4h` score `-0.147` n `118` status `ready` deltaP `9.353` edge `0.0048` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5071` n `121` status `ready` deltaP `-1.5205` edge `-0.0064` maxDD `-1.5448`
- `market_context_high->index_1h` score `-0.5839` n `121` status `ready` deltaP `-1.8978` edge `-0.0088` maxDD `-1.6054`
- `market_context_high->equity_1h` score `-1.0748` n `121` status `ready` deltaP `4.9476` edge `-0.0143` maxDD `-10.5179`
- `market_context_high->crypto_alt_1h` score `-1.3316` n `121` status `ready` deltaP `-3.8563` edge `-0.0142` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.3989` n `118` status `ready` deltaP `0.4263` edge `-0.0432` maxDD `-5.7857`
- `market_context_high->index_4h` score `-1.5594` n `118` status `ready` deltaP `-6.6763` edge `-0.0304` maxDD `-4.6675`
- `market_context_high->crypto_major_1h` score `-1.6105` n `121` status `ready` deltaP `-5.3719` edge `-0.0371` maxDD `-7.3514`
- `market_context_high->index_24h` score `-1.6652` n `111` status `ready` deltaP `-1.4062` edge `0.0736` maxDD `-7.2392`
- `market_context_high->metal_4h` score `-1.6944` n `118` status `ready` deltaP `-2.6534` edge `-0.0123` maxDD `-2.8969`
- `market_context_high->crypto_alt_24h` score `-3.7927` n `111` status `ready` deltaP `-10.4934` edge `-0.1018` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-6.0776` n `118` status `ready` deltaP `-0.1654` edge `-0.2492` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.1037` n `111` status `ready` deltaP `10.7521` edge `0.0223` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.6294` n `118` status `ready` deltaP `-7.95` edge `-0.1767` maxDD `-26.1534`
- `market_context_high->unknown_1h` score `-8.137` n `121` status `ready` deltaP `1.1741` edge `-0.6412` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
