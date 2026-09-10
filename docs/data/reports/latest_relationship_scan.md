# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T06:06:06.515699+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10918`

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

- `risk_on_high->crypto_alt_24h` score `13.8065` n `94` status `ready` deltaP `30.6184` edge `0.9694` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.8065` n `94` status `ready` deltaP `30.6184` edge `0.9694` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `9.9711` n `216` status `ready` deltaP `22.9745` edge `0.7605` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.2577` n `94` status `ready` deltaP `37.2114` edge `0.3939` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.2577` n `94` status `ready` deltaP `37.2114` edge `0.3939` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.216` n `94` status `ready` deltaP `26.2844` edge `0.3453` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.216` n `94` status `ready` deltaP `26.2844` edge `0.3453` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.3301` n `94` status `ready` deltaP `20.4492` edge `0.8256` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.3301` n `94` status `ready` deltaP `20.4492` edge `0.8256` maxDD `-24.5429`
- `risk_on_high->index_24h` score `2.8958` n `94` status `ready` deltaP `31.3571` edge `0.0365` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.8958` n `94` status `ready` deltaP `31.3571` edge `0.0365` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.6689` n `216` status `ready` deltaP `15.4514` edge `0.1194` maxDD `0.0`
- `market_context_high->index_24h` score `2.3798` n `216` status `ready` deltaP `26.2153` edge `0.0629` maxDD `-0.1483`
- `risk_on_high->commodity_24h` score `1.5598` n `94` status `ready` deltaP `15.2076` edge `0.043` maxDD `-0.1519`
- `risk_on_and_context->commodity_24h` score `1.5598` n `94` status `ready` deltaP `15.2076` edge `0.043` maxDD `-0.1519`
- `risk_on_high->equity_4h` score `1.4708` n `94` status `ready` deltaP `23.5048` edge `-0.0127` maxDD `-0.7146`
- `risk_on_and_context->equity_4h` score `1.4708` n `94` status `ready` deltaP `23.5048` edge `-0.0127` maxDD `-0.7146`
- `risk_on_high->equity_1h` score `1.1277` n `94` status `ready` deltaP `17.7634` edge `0.0034` maxDD `-0.228`
- `risk_on_and_context->equity_1h` score `1.1277` n `94` status `ready` deltaP `17.7634` edge `0.0034` maxDD `-0.228`
- `risk_on_high->crypto_alt_1h` score `1.0544` n `94` status `ready` deltaP `4.335` edge `0.0942` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
