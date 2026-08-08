# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T23:25:22.523231+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8733`

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

- `market_context_high->equity_24h` score `3.0468` n `103` status `ready` deltaP `4.5729` edge `0.5294` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.4674` n `103` status `ready` deltaP `12.2118` edge `0.1818` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.6868` n `113` status `ready` deltaP `16.4944` edge `0.0979` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.0106` n `123` status `ready` deltaP `12.1525` edge `0.0375` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8713` n `103` status `ready` deltaP `22.2694` edge `0.0499` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4518` n `103` status `ready` deltaP `9.1002` edge `0.1504` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4221` n `123` status `ready` deltaP `2.8455` edge `-0.0046` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5279` n `123` status `ready` deltaP `-3.2922` edge `-0.0068` maxDD `-0.7809`
- `market_context_high->equity_1h` score `-0.6347` n `123` status `ready` deltaP `2.8297` edge `0.0111` maxDD `-4.6286`
- `market_context_high->metal_1h` score `-0.6395` n `123` status `ready` deltaP `-3.8265` edge `-0.0069` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6476` n `113` status `ready` deltaP `-1.5014` edge `-0.0125` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.6884` n `113` status `ready` deltaP `3.3685` edge `-0.0045` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.1657` n `113` status `ready` deltaP `-4.8551` edge `-0.0162` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.2536` n `123` status `ready` deltaP `-13.4974` edge `-0.0341` maxDD `-2.4308`
- `market_context_high->equity_4h` score `-2.2901` n `113` status `ready` deltaP `0.8229` edge `-0.0626` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.0887` n `123` status `ready` deltaP `-10.7176` edge `-0.0657` maxDD `-6.2862`
- `market_context_high->crypto_major_24h` score `-3.8011` n `103` status `ready` deltaP `6.2197` edge `-0.1088` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.3894` n `103` status `ready` deltaP `-12.4461` edge `-0.1385` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.7936` n `113` status `ready` deltaP `-13.5266` edge `-0.1441` maxDD `-6.5487`
- `market_context_high->unknown_1h` score `-8.353` n `123` status `ready` deltaP `-5.1555` edge `-0.617` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
