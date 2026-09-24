# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T07:07:30.509347+00:00`
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

- `market_context_high->unknown_1h` score `66.1662` n `47` status `ready` deltaP `10.5651` edge `5.4505` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `39.7584` n `46` status `ready` deltaP `27.0758` edge `3.1483` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `24.7259` n `46` status `ready` deltaP `22.0486` edge `1.9135` maxDD `0.0`
- `market_context_high->equity_24h` score `23.0026` n `46` status `ready` deltaP `24.4716` edge `1.7638` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.6443` n `46` status `ready` deltaP `33.4994` edge `0.4224` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `6.0172` n `103` status `ready` deltaP `-0.6152` edge `1.4098` maxDD `-63.6743`
- `news_risk_high->crypto_alt_4h` score `4.8603` n `103` status `ready` deltaP `14.6889` edge `0.4069` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.7857` n `103` status `ready` deltaP `18.6523` edge `0.3322` maxDD `-2.619`
- `market_context_high->metal_24h` score `2.8366` n `46` status `ready` deltaP `27.4759` edge `0.0766` maxDD `-0.2042`
- `market_context_high->index_4h` score `2.7385` n `47` status `ready` deltaP `31.8922` edge `0.031` maxDD `-0.2323`
- `news_risk_high->crypto_alt_24h` score `2.4638` n `103` status `ready` deltaP `-3.1941` edge `0.9279` maxDD `-49.7699`
- `news_risk_high->crypto_alt_1h` score `2.3273` n `110` status `ready` deltaP `12.6865` edge `0.1584` maxDD `-1.5895`
- `market_context_high->equity_4h` score `1.9948` n `47` status `ready` deltaP `14.7055` edge `0.11` maxDD `-1.3444`
- `news_risk_high->commodity_24h` score `1.9518` n `103` status `ready` deltaP `20.7962` edge `0.1419` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `1.7985` n `110` status `ready` deltaP `14.0229` edge `0.0999` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.6038` n `103` status `ready` deltaP `23.3765` edge `0.0414` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2351` n `103` status `ready` deltaP `29.6639` edge `0.1237` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.9008` n `47` status `ready` deltaP `14.0113` edge `0.0095` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.7701` n `47` status `ready` deltaP `10.1191` edge `0.037` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.5106` n `103` status `ready` deltaP `19.3501` edge `0.0813` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
