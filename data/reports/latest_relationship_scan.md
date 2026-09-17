# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T05:37:31.089508+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10533`

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

- `news_risk_high->unknown_4h` score `384.8222` n `83` status `ready` deltaP `-20.7483` edge `32.2963` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `15.5303` n `83` status `ready` deltaP `36.6152` edge `1.188` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `14.2465` n `83` status `ready` deltaP `28.6814` edge `1.1955` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `10.5354` n `83` status `ready` deltaP `37.9142` edge `0.8026` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `8.1632` n `52` status `ready` deltaP `44.9653` edge `0.3805` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.1632` n `52` status `ready` deltaP `44.9653` edge `0.3805` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.8641` n `149` status `ready` deltaP `38.2539` edge `0.3695` maxDD `-0.8682`
- `news_risk_high->index_24h` score `6.2659` n `83` status `ready` deltaP `43.3442` edge `0.2508` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.4562` n `83` status `ready` deltaP `31.9905` edge `0.2035` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.6006` n `52` status `ready` deltaP `33.6672` edge `-0.0035` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.6006` n `52` status `ready` deltaP `33.6672` edge `-0.0035` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4657` n `149` status `ready` deltaP `30.8923` edge `0.0211` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1483` n `52` status `ready` deltaP `27.5094` edge `0.0306` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1483` n `52` status `ready` deltaP `27.5094` edge `0.0306` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.048` n `149` status `ready` deltaP `24.0117` edge `0.0524` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9024` n `149` status `ready` deltaP `14.2648` edge `0.0178` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.411` n `83` status `ready` deltaP `12.4982` edge `0.0322` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2791` n `52` status `ready` deltaP `7.3469` edge `0.0095` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2791` n `52` status `ready` deltaP `7.3469` edge `0.0095` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1435` n `52` status `ready` deltaP `6.2644` edge `0.0072` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
