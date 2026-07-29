# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T00:22:37.619636+00:00`
- Price records: `672`
- Market context records: `8249`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5924`

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

- `news_risk_high->unknown_24h` score `7957.5581` n `43` status `ready` deltaP `38.5417` edge `662.8729` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.2796` n `54` status `ready` deltaP `26.8405` edge `0.4874` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1361` n `54` status `ready` deltaP `22.5771` edge `0.1417` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7469` n `54` status `ready` deltaP `23.3344` edge `0.0924` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.3629` n `54` status `ready` deltaP `11.8508` edge `0.2933` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7943` n `54` status `ready` deltaP `14.5542` edge `0.0959` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7157` n `54` status `ready` deltaP `11.3551` edge `0.107` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3647` n `54` status `ready` deltaP `16.9264` edge `0.2013` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.1316` n `54` status `ready` deltaP `10.3489` edge `0.0721` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.489` n `54` status `ready` deltaP `7.352` edge `0.0206` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1658` n `54` status `ready` deltaP `6.9971` edge `0.0027` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1096` n `54` status `ready` deltaP `3.1049` edge `0.0105` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4666` n `54` status `ready` deltaP `4.4602` edge `0.0062` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1516` n `54` status `ready` deltaP `-8.6605` edge `-0.043` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.0828` n `43` status `ready` deltaP `-18.6491` edge `-0.0443` maxDD `-4.0615`
- `news_risk_high->metal_24h` score `-5.6795` n `43` status `ready` deltaP `-20.2519` edge `-0.0868` maxDD `-10.1184`
- `news_risk_high->commodity_4h` score `-8.9779` n `54` status `ready` deltaP `-32.7913` edge `-0.1988` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.6714` n `43` status `ready` deltaP `-24.136` edge `-0.3539` maxDD `-24.2912`
- `news_risk_high->commodity_24h` score `-14.1276` n `43` status `ready` deltaP `-18.9599` edge `-0.4678` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-34.126` n `43` status `ready` deltaP `-23.4415` edge `-1.2086` maxDD `-105.9832`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
