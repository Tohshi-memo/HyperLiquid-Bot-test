# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T07:22:19.224824+00:00`
- Price records: `672`
- Market context records: `1821`
- Flow alert records: `7139`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4474`

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

- `market_context_high->metal_24h` score `6.8716` n `178` status `ready` deltaP `27.5905` edge `0.6313` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.8645` n `185` status `ready` deltaP `22.322` edge `0.5377` maxDD `-5.1574`
- `news_risk_high->commodity_4h` score `6.5448` n `30` status `ready` deltaP `29.4106` edge `0.4148` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `6.4676` n `185` status `ready` deltaP `26.231` edge `0.4887` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.6415` n `185` status `ready` deltaP `17.0831` edge `0.4753` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.6322` n `178` status `ready` deltaP `17.8683` edge `0.3064` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.2446` n `30` status `ready` deltaP `24.7206` edge `0.1373` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.0142` n `185` status `ready` deltaP `15.9196` edge `0.2545` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.5589` n `178` status `ready` deltaP `17.2772` edge `0.5879` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.5037` n `178` status `ready` deltaP `13.6919` edge `0.6494` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.905` n `30` status `ready` deltaP `21.6362` edge `-0.001` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8393` n `185` status `ready` deltaP `11.7057` edge `0.1008` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4374` n `192` status `ready` deltaP `6.1596` edge `0.094` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.3327` n `192` status `ready` deltaP `6.3748` edge `0.0966` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.2887` n `30` status `ready` deltaP `9.065` edge `0.0489` maxDD `-2.7857`
- `market_context_high->equity_1h` score `-0.0976` n `192` status `ready` deltaP `4.4162` edge `0.0418` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.1546` n `178` status `ready` deltaP `18.1648` edge `0.7246` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.2152` n `178` status `ready` deltaP `11.2614` edge `0.0119` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.39` n `192` status `ready` deltaP `0.1903` edge `0.0119` maxDD `-1.7205`
- `news_risk_high->unknown_1h` score `-0.4138` n `30` status `ready` deltaP `16.8563` edge `-0.1182` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
