# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T08:22:28.438676+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9897`

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

- `market_context_high->unknown_1h` score `66.1062` n `47` status `ready` deltaP `10.5651` edge `5.4455` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `40.5611` n `46` status `ready` deltaP `27.9439` edge `3.2094` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `25.7049` n `46` status `ready` deltaP `22.9167` edge `1.9893` maxDD `0.0`
- `market_context_high->equity_24h` score `23.5172` n `46` status `ready` deltaP `25.3397` edge `1.8009` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.7929` n `46` status `ready` deltaP `34.3675` edge `0.429` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `6.8199` n `103` status `ready` deltaP `0.2529` edge `1.4709` maxDD `-63.6743`
- `news_risk_high->crypto_alt_4h` score `4.7374` n `103` status `ready` deltaP `14.2316` edge `0.3997` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.6518` n `103` status `ready` deltaP `18.0426` edge `0.3251` maxDD `-2.619`
- `news_risk_high->crypto_alt_24h` score `3.4428` n `103` status `ready` deltaP `-2.326` edge `1.0037` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.0105` n `46` status `ready` deltaP `28.3439` edge `0.0853` maxDD `-0.2042`
- `market_context_high->index_4h` score `2.8151` n `47` status `ready` deltaP `32.6544` edge `0.0323` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.3602` n `114` status `ready` deltaP `13.0975` edge `0.1584` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.1158` n `47` status `ready` deltaP `15.4677` edge `0.115` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `1.9893` n `114` status `ready` deltaP `15.1933` edge `0.108` maxDD `-1.8141`
- `news_risk_high->commodity_24h` score `1.7816` n `103` status `ready` deltaP `19.9282` edge `0.1335` maxDD `-2.431`
- `news_risk_high->fx_4h` score `1.6014` n `103` status `ready` deltaP `23.3765` edge `0.0412` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2746` n `103` status `ready` deltaP `30.1847` edge `0.1253` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.89` n `47` status `ready` deltaP `13.8616` edge `0.0096` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.812` n `47` status `ready` deltaP `10.4185` edge `0.0385` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.6236` n `103` status `ready` deltaP `20.2181` edge `0.09` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
