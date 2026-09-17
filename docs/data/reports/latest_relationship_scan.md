# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T18:07:39.458420+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9046`

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

- `news_risk_high->unknown_4h` score `421.5435` n `77` status `ready` deltaP `-20.8821` edge `35.3573` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.3635` n `52` status `ready` deltaP `50.1736` edge `0.4458` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.3635` n `52` status `ready` deltaP `50.1736` edge `0.4458` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.8327` n `74` status `ready` deltaP `29.0353` edge `0.6804` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `8.0643` n `149` status `ready` deltaP `43.4622` edge `0.4348` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `7.7692` n `74` status `ready` deltaP `28.6411` edge `0.6339` maxDD `-6.5262`
- `news_risk_high->crypto_major_24h` score `5.5715` n `74` status `ready` deltaP `20.3688` edge `0.778` maxDD `-13.2931`
- `news_risk_high->index_24h` score `5.4606` n `74` status `ready` deltaP `36.6976` edge `0.228` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.6231` n `74` status `ready` deltaP `27.3508` edge `0.165` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.9347` n `52` status `ready` deltaP `32.5399` edge `0.0626` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9347` n `52` status `ready` deltaP `32.5399` edge `0.0626` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.8344` n `149` status `ready` deltaP `29.0422` edge `0.0844` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.0119` n `52` status `ready` deltaP `27.7644` edge `-0.0132` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.0119` n `52` status `ready` deltaP `27.7644` edge `-0.0132` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.8771` n `149` status `ready` deltaP `24.9895` edge `0.0114` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1361` n `149` status `ready` deltaP `16.2109` edge `0.0243` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.893` n `77` status `ready` deltaP `14.4164` edge `0.0249` maxDD `-0.3938`
- `risk_on_high->commodity_1h` score `0.5128` n `52` status `ready` deltaP `9.293` edge `0.016` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5128` n `52` status `ready` deltaP `9.293` edge `0.016` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2127` n `149` status `ready` deltaP `10.4957` edge `0.0049` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
