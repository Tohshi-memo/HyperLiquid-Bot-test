# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T13:51:56.783257+00:00`
- Price records: `672`
- Market context records: `871`
- Flow alert records: `2447`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1386`

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

- `risk_on_high->crypto_major_24h` score `22.2335` n `31` status `ready` deltaP `32.6389` edge `1.6352` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `22.2335` n `31` status `ready` deltaP `32.6389` edge `1.6352` maxDD `0.0`
- `risk_on_high->equity_24h` score `13.705` n `31` status `ready` deltaP `25.3472` edge `0.9731` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `13.705` n `31` status `ready` deltaP `25.3472` edge `0.9731` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `13.6342` n `31` status `ready` deltaP `7.8125` edge `1.0841` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.6342` n `31` status `ready` deltaP `7.8125` edge `1.0841` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.2254` n `165` status `ready` deltaP `28.3965` edge `0.9462` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6509` n `165` status `ready` deltaP `7.2064` edge `0.511` maxDD `-0.0508`
- `risk_on_high->index_24h` score `4.4849` n `31` status `ready` deltaP `27.9514` edge `0.1874` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.4849` n `31` status `ready` deltaP `27.9514` edge `0.1874` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4432` n `32` status `ready` deltaP `8.003` edge `0.2701` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4432` n `32` status `ready` deltaP `8.003` edge `0.2701` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `3.0255` n `32` status `ready` deltaP `22.4848` edge `0.1227` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.0255` n `32` status `ready` deltaP `22.4848` edge `0.1227` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.8452` n `32` status `ready` deltaP `20.5793` edge `0.1371` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.8452` n `32` status `ready` deltaP `20.5793` edge `0.1371` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.5643` n `32` status `ready` deltaP `14.1006` edge `0.1285` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.5643` n `32` status `ready` deltaP `14.1006` edge `0.1285` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.716` n `31` status `ready` deltaP `-7.4709` edge `0.3375` maxDD `-1.7492`
- `risk_on_and_context->commodity_24h` score `1.716` n `31` status `ready` deltaP `-7.4709` edge `0.3375` maxDD `-1.7492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
