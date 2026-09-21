# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T00:22:29.228783+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9118`

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

- `news_risk_high->crypto_major_24h` score `24.8189` n `98` status `ready` deltaP `12.7906` edge `2.6688` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.2875` n `98` status `ready` deltaP `15.0935` edge `2.0781` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.682` n `101` status `ready` deltaP `20.5958` edge `0.3738` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.8509` n `101` status `ready` deltaP `20.4434` edge `0.3104` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.7246` n `101` status `ready` deltaP `16.5308` edge `0.1634` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.0148` n `101` status `ready` deltaP `18.0278` edge `0.1` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `0.985` n `98` status `ready` deltaP `22.2541` edge `0.1085` maxDD `-3.4467`
- `market_context_high->fx_4h` score `0.938` n `42` status `ready` deltaP `14.4744` edge `0.0099` maxDD `-0.2586`
- `market_context_high->fx_1h` score `0.9016` n `51` status `ready` deltaP `12.6248` edge `0.0089` maxDD `-0.1012`
- `market_context_high->equity_1h` score `0.8581` n `51` status `ready` deltaP `7.2062` edge `0.0488` maxDD `-0.36`
- `market_context_high->index_1h` score `0.7158` n `51` status `ready` deltaP `10.4996` edge `0.0152` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.6448` n `101` status `ready` deltaP `14.8974` edge `0.0146` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.5814` n `101` status `ready` deltaP `16.7939` edge `0.0419` maxDD `-2.0994`
- `market_context_high->commodity_4h` score `0.3922` n `42` status `ready` deltaP `20.1147` edge `-0.0109` maxDD `-2.4997`
- `news_risk_high->fx_4h` score `0.2103` n `101` status `ready` deltaP `8.7931` edge `0.0225` maxDD `-0.421`
- `news_risk_high->equity_24h` score `0.2043` n `98` status `ready` deltaP `15.0085` edge `0.0579` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.1581` n `51` status `ready` deltaP `4.4529` edge `0.0143` maxDD `-0.1314`
- `news_risk_high->equity_1h` score `0.0135` n `101` status `ready` deltaP `3.867` edge `0.0159` maxDD `-0.9112`
- `market_context_high->index_4h` score `-0.0167` n `42` status `ready` deltaP `10.2061` edge `-0.0065` maxDD `-1.0949`
- `news_risk_high->metal_24h` score `-0.0425` n `98` status `ready` deltaP `13.4212` edge `-0.0105` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
