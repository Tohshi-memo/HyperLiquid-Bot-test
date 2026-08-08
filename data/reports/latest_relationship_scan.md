# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T23:52:23.795083+00:00`
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

- `market_context_high->equity_24h` score `3.078` n `103` status `ready` deltaP `4.5729` edge `0.532` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.4794` n `103` status `ready` deltaP `12.2118` edge `0.1828` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.6808` n `113` status `ready` deltaP `16.4944` edge `0.0974` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.9209` n `125` status `ready` deltaP `11.1509` edge `0.0367` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8682` n `103` status `ready` deltaP `22.2694` edge `0.0495` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4581` n `103` status `ready` deltaP `9.1002` edge `0.1512` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4126` n `125` status `ready` deltaP `2.9497` edge `-0.0045` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5034` n `125` status `ready` deltaP `-2.8371` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.6064` n `125` status `ready` deltaP `-3.2347` edge `-0.0066` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6476` n `113` status `ready` deltaP `-1.5014` edge `-0.0125` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.6762` n `113` status `ready` deltaP `3.5209` edge `-0.0045` maxDD `-1.6928`
- `market_context_high->equity_1h` score `-0.743` n `125` status `ready` deltaP `1.776` edge `0.0091` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.1642` n `113` status `ready` deltaP `-4.8551` edge `-0.016` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-2.2561` n `113` status `ready` deltaP `1.1278` edge `-0.0618` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-2.2863` n `125` status `ready` deltaP `-13.5365` edge `-0.0361` maxDD `-2.4677`
- `market_context_high->crypto_major_1h` score `-3.12` n `125` status `ready` deltaP `-10.7437` edge `-0.0673` maxDD `-6.3528`
- `market_context_high->crypto_major_24h` score `-3.8023` n `103` status `ready` deltaP `6.2197` edge `-0.1089` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.429` n `103` status `ready` deltaP `-12.4461` edge `-0.1418` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.7972` n `113` status `ready` deltaP `-13.5266` edge `-0.1444` maxDD `-6.5487`
- `market_context_high->unknown_1h` score `-8.3476` n `125` status `ready` deltaP `-5.5976` edge `-0.6136` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
