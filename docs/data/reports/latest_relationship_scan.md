# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T06:37:30.146956+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8682`

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

- `news_risk_high->unknown_4h` score `384.7208` n `83` status `ready` deltaP `-21.2056` edge `32.2909` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `15.1351` n `83` status `ready` deltaP `35.9208` edge `1.1597` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `13.9246` n `83` status `ready` deltaP `27.9869` edge `1.1733` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `10.2447` n `83` status `ready` deltaP `37.2198` edge `0.783` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `8.3472` n `52` status `ready` deltaP `45.6597` edge `0.3912` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.3472` n `52` status `ready` deltaP `45.6597` edge `0.3912` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.048` n `149` status `ready` deltaP `38.9483` edge `0.3802` maxDD `-0.8682`
- `news_risk_high->index_24h` score `6.1815` n `83` status `ready` deltaP `42.6498` edge `0.2484` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.3698` n `83` status `ready` deltaP `31.9905` edge `0.1963` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.6193` n `52` status `ready` deltaP `33.8408` edge `-0.0031` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.6193` n `52` status `ready` deltaP `33.8408` edge `-0.0031` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4844` n `149` status `ready` deltaP `31.0659` edge `0.0215` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.2198` n `52` status `ready` deltaP `28.1191` edge `0.0325` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2198` n `52` status `ready` deltaP `28.1191` edge `0.0325` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.1196` n `149` status `ready` deltaP `24.6214` edge `0.0543` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9072` n `149` status `ready` deltaP `14.2648` edge `0.0182` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.4007` n `83` status `ready` deltaP `12.3457` edge `0.0319` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2839` n `52` status `ready` deltaP `7.3469` edge `0.0099` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2839` n `52` status `ready` deltaP `7.3469` edge `0.0099` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.135` n `52` status `ready` deltaP `6.1147` edge `0.0071` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
