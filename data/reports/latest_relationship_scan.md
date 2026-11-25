# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T17:37:33.467475+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3744`

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

- `market_context_high->unknown_1h` score `32182.7581` n `45` status `ready` deltaP `2.1656` edge `2681.8915` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21863.1425` n `45` status `ready` deltaP `2.5678` edge `1821.9253` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `947.8031` n `31` status `ready` deltaP `2.3807` edge `78.9853` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `610.195` n `31` status `ready` deltaP `3.7864` edge `50.83` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `346.1099` n `31` status `ready` deltaP `5.7292` edge `28.8043` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.3467` n `31` status `ready` deltaP `52.0833` edge `3.515` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.4776` n `31` status `ready` deltaP `53.8194` edge `3.181` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.7363` n `31` status `ready` deltaP `55.7292` edge `2.8565` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.0374` n `31` status `ready` deltaP `41.2355` edge `0.7557` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.9455` n `31` status `ready` deltaP `27.5226` edge `0.899` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `11.625` n `31` status `ready` deltaP `38.5966` edge `0.7595` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.4579` n `31` status `ready` deltaP `18.7598` edge `0.9728` maxDD `-7.6714`
- `news_risk_high->index_24h` score `7.4317` n `31` status `ready` deltaP `52.9514` edge `0.2663` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.4723` n `31` status `ready` deltaP `47.0934` edge `0.1549` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.9702` n `31` status `ready` deltaP `20.5862` edge `0.2123` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.502` n `31` status `ready` deltaP `37.0722` edge `0.0707` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7058` n `31` status `ready` deltaP `31.8428` edge `0.0217` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.6457` n `31` status `ready` deltaP `11.3579` edge `0.3096` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.4396` n `45` status `ready` deltaP `29.9356` edge `0.0322` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.3922` n `31` status `ready` deltaP `13.304` edge `0.2537` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
