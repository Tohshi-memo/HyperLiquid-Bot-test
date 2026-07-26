# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T09:07:31.499545+00:00`
- Price records: `672`
- Market context records: `7970`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11769`

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

- `market_context_high->equity_24h` score `16.2971` n `82` status `ready` deltaP `24.386` edge `1.3297` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.0816` n `82` status `ready` deltaP `35.8752` edge `0.4343` maxDD `0.0`
- `market_context_high->equity_4h` score `6.8239` n `91` status `ready` deltaP `25.716` edge `0.4865` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.9152` n `82` status `ready` deltaP `28.4002` edge `0.2902` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.7399` n `91` status `ready` deltaP `28.157` edge `0.0766` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.6005` n `91` status `ready` deltaP `22.8072` edge `0.1269` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.6832` n `98` status `ready` deltaP `13.6238` edge `0.1312` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.1569` n `82` status `ready` deltaP `25.4954` edge `0.0352` maxDD `-3.0343`
- `market_context_high->index_24h` score `1.1317` n `82` status `ready` deltaP `8.7018` edge `0.1541` maxDD `-1.3621`
- `market_context_high->crypto_alt_4h` score `1.0408` n `91` status `ready` deltaP `8.153` edge `0.1441` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.0144` n `91` status `ready` deltaP `10.6557` edge `0.1853` maxDD `-6.7444`
- `market_context_high->index_1h` score `0.9903` n `98` status `ready` deltaP `15.5451` edge `0.0219` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6682` n `98` status `ready` deltaP `9.6328` edge `0.0293` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5154` n `98` status `ready` deltaP `10.0544` edge `0.0401` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `0.051` n `98` status `ready` deltaP `1.7689` edge `0.038` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.174` n `98` status `ready` deltaP `1.9826` edge `0.0012` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.3359` n `98` status `ready` deltaP `2.1296` edge `-0.0004` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.339` n `91` status `ready` deltaP `4.5013` edge `0.0182` maxDD `-2.4502`
- `market_context_high->fx_4h` score `-0.4682` n `91` status `ready` deltaP `4.5969` edge `0.0051` maxDD `-0.9813`
- `market_context_high->unknown_1h` score `-1.7538` n `98` status `ready` deltaP `8.2182` edge `-0.1586` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
