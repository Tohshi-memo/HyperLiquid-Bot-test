# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T05:52:15.965072+00:00`
- Price records: `672`
- Market context records: `1814`
- Flow alert records: `7120`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4514`

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

- `market_context_high->crypto_alt_4h` score `7.0617` n `183` status `ready` deltaP `22.9708` edge `0.5498` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.8584` n `178` status `ready` deltaP `27.5905` edge `0.6302` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.6413` n `183` status `ready` deltaP `26.9625` edge `0.4983` maxDD `-4.9684`
- `news_risk_high->commodity_4h` score `6.5545` n `30` status `ready` deltaP `29.563` edge `0.4146` maxDD `-3.5713`
- `market_context_high->unknown_4h` score `4.7425` n `183` status `ready` deltaP `17.6846` edge `0.4797` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.6646` n `178` status `ready` deltaP `17.8683` edge `0.3091` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.3321` n `30` status `ready` deltaP `25.3194` edge `0.1406` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9725` n `183` status `ready` deltaP `15.6537` edge `0.2528` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.803` n `178` status `ready` deltaP `18.3189` edge `0.6013` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.3732` n `178` status `ready` deltaP `13.1711` edge `0.642` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.9065` n `30` status `ready` deltaP `21.6362` edge `-0.0008` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8066` n `183` status `ready` deltaP `11.3572` edge `0.1004` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4976` n `190` status `ready` deltaP `6.4025` edge `0.0974` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.423` n `190` status `ready` deltaP `6.9335` edge `0.1004` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.401` n `30` status `ready` deltaP `9.9796` edge `0.0572` maxDD `-2.7857`
- `market_context_high->equity_1h` score `-0.0941` n `190` status `ready` deltaP `4.4753` edge `0.0417` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.2424` n `178` status `ready` deltaP `17.8176` edge `0.7196` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.3393` n `178` status `ready` deltaP `10.2197` edge `0.0085` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.4169` n `30` status `ready` deltaP `16.8563` edge `-0.1186` maxDD `-2.1115`
- `market_context_high->metal_4h` score `-0.4537` n `183` status `ready` deltaP `12.2434` edge `0.1294` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
