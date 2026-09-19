# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T18:07:26.581833+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8502`

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

- `news_risk_high->crypto_major_24h` score `51.4877` n `72` status `ready` deltaP `28.8194` edge `4.1877` maxDD `-5.8019`
- `market_context_high->unknown_4h` score `45.5972` n `126` status `ready` deltaP `-3.0318` edge `3.8433` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `45.0341` n `72` status `ready` deltaP `34.0278` edge `3.6639` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `22.5502` n `36` status `ready` deltaP `-14.1429` edge `1.996` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `22.5502` n `36` status `ready` deltaP `-14.1429` edge `1.996` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.5013` n `36` status `ready` deltaP `48.6111` edge `0.4677` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.5013` n `36` status `ready` deltaP `48.6111` edge `0.4677` maxDD `0.0`
- `news_risk_high->equity_24h` score `9.2598` n `72` status `ready` deltaP `38.368` edge `0.5201` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.6637` n `126` status `ready` deltaP `40.6746` edge `0.42` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.6344` n `98` status `ready` deltaP `21.161` edge `0.4494` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.2373` n `98` status `ready` deltaP `21.3134` edge `0.3368` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2975` n `98` status `ready` deltaP `19.2228` edge `0.1932` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.5629` n `126` status `ready` deltaP `26.9527` edge `0.0757` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.3959` n `98` status `ready` deltaP `19.9713` edge `0.1188` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.2269` n `36` status `ready` deltaP `25.7622` edge `0.0488` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2269` n `36` status `ready` deltaP `25.7622` edge `0.0488` maxDD `-0.1313`
- `news_risk_high->metal_24h` score `1.7285` n `72` status `ready` deltaP `22.5694` edge `0.078` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.4221` n `126` status `ready` deltaP `17.7455` edge `0.0254` maxDD `-0.3491`
- `news_risk_high->metal_4h` score `0.8636` n `98` status `ready` deltaP `19.5868` edge `0.0468` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7566` n `98` status `ready` deltaP `16.0546` edge `0.0162` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
