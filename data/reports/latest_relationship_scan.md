# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T21:22:30.534248+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11607`

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

- `market_context_high->equity_24h` score `2.976` n `103` status `ready` deltaP `4.5729` edge `0.5235` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.4254` n `103` status `ready` deltaP `12.2118` edge `0.1783` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.6554` n `108` status `ready` deltaP `16.0569` edge `0.0982` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.0868` n `115` status `ready` deltaP `12.8795` edge `0.039` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8951` n `103` status `ready` deltaP `22.443` edge `0.0518` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4276` n `103` status `ready` deltaP `9.1002` edge `0.1473` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.4919` n `115` status `ready` deltaP `-2.6451` edge `-0.0065` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5035` n `115` status `ready` deltaP `1.9031` edge `-0.0051` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.599` n `115` status `ready` deltaP `-3.1229` edge `-0.0064` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-0.6149` n `115` status `ready` deltaP `2.3718` edge `0.0158` maxDD `-4.6286`
- `market_context_high->index_4h` score `-0.678` n `108` status `ready` deltaP `-2.2075` edge `-0.0117` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.8459` n `108` status `ready` deltaP `1.4905` edge `-0.0051` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0853` n `108` status `ready` deltaP `-3.5343` edge `-0.0147` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0654` n `115` status `ready` deltaP `-12.0893` edge `-0.0286` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.2499` n `108` status `ready` deltaP `0.4855` edge `-0.057` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.6574` n `115` status `ready` deltaP `-8.6462` edge `-0.0568` maxDD `-5.2274`
- `market_context_high->crypto_major_24h` score `-3.6643` n `103` status `ready` deltaP `6.2197` edge `-0.0974` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.1398` n `103` status `ready` deltaP `-12.4461` edge `-0.1177` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.7072` n `108` status `ready` deltaP `-13.6461` edge `-0.1361` maxDD `-6.5487`
- `market_context_high->unknown_1h` score `-8.233` n `115` status `ready` deltaP `-4.12` edge `-0.6139` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
