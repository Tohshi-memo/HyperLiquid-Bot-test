# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T06:22:29.758604+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7458`

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

- `news_risk_high->unknown_24h` score `1247.7268` n `135` status `ready` deltaP `1.9097` edge `103.9645` maxDD `0.0`
- `market_context_high->unknown_1h` score `802.5644` n `31` status `ready` deltaP `9.7305` edge `66.8155` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.5611` n `135` status `ready` deltaP `28.7268` edge `1.3762` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `8.4339` n `135` status `ready` deltaP `28.7269` edge `0.7462` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.9305` n `135` status `ready` deltaP `23.9931` edge `0.8163` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.919` n `135` status `ready` deltaP `34.919` edge `0.1416` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.5836` n `135` status `ready` deltaP `27.0949` edge `0.2454` maxDD `-2.192`
- `news_risk_high->equity_4h` score `3.0114` n `135` status `ready` deltaP `30.0858` edge `0.2105` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.9494` n `135` status `ready` deltaP `11.4171` edge `0.3523` maxDD `-15.9436`
- `market_context_high->crypto_alt_1h` score `1.742` n `31` status `ready` deltaP `14.067` edge `0.191` maxDD `-3.5821`
- `market_context_high->crypto_major_1h` score `1.3651` n `31` status `ready` deltaP `9.18` edge `0.1748` maxDD `-3.546`
- `market_context_high->fx_1h` score `1.3508` n `31` status `ready` deltaP `19.0071` edge `0.0081` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `1.1341` n `135` status `ready` deltaP `9.5509` edge `0.1219` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.9463` n `135` status `ready` deltaP `9.7006` edge `0.0765` maxDD `-1.6514`
- `market_context_high->equity_1h` score `0.9168` n `31` status `ready` deltaP `14.2167` edge `0.0653` maxDD `-2.4027`
- `news_risk_high->index_1h` score `0.546` n `135` status `ready` deltaP `9.4167` edge `0.0115` maxDD `-0.302`
- `market_context_high->index_1h` score `0.154` n `31` status `ready` deltaP `5.7369` edge `0.0152` maxDD `-0.3627`
- `market_context_high->metal_1h` score `0.046` n `31` status `ready` deltaP `2.5787` edge `0.0108` maxDD `-0.4338`
- `news_risk_high->index_4h` score `-0.0725` n `135` status `ready` deltaP `7.5587` edge `0.0289` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.5084` n `135` status `ready` deltaP `2.4894` edge `0.0693` maxDD `-7.2607`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
