# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T01:37:31.859693+00:00`
- Price records: `672`
- Market context records: `8255`
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

- `news_risk_high->unknown_24h` score `7957.7395` n `43` status `ready` deltaP `38.8889` edge `662.8857` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.1663` n `54` status `ready` deltaP `26.3832` edge `0.481` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1349` n `54` status `ready` deltaP `22.4274` edge `0.1426` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6983` n `54` status `ready` deltaP `22.8771` edge `0.0914` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.3085` n `54` status `ready` deltaP `11.241` edge `0.2904` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8075` n `54` status `ready` deltaP `14.5542` edge `0.097` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7085` n `54` status `ready` deltaP `11.3551` edge `0.1064` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3426` n `54` status `ready` deltaP `16.6215` edge `0.2005` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.186` n `54` status `ready` deltaP `10.6538` edge `0.0746` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4938` n `54` status `ready` deltaP `7.352` edge `0.021` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1743` n `54` status `ready` deltaP `7.1468` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0616` n `54` status `ready` deltaP `3.4043` edge `0.0125` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4571` n `54` status `ready` deltaP `4.6127` edge `0.0064` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1468` n `54` status `ready` deltaP `-8.6605` edge `-0.0426` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.0744` n `43` status `ready` deltaP `-18.6491` edge `-0.0436` maxDD `-4.0615`
- `news_risk_high->metal_24h` score `-5.5717` n `43` status `ready` deltaP `-19.3839` edge `-0.0836` maxDD `-10.1184`
- `news_risk_high->commodity_4h` score `-9.0295` n `54` status `ready` deltaP `-32.7913` edge `-0.2031` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.69` n `43` status `ready` deltaP `-24.3096` edge `-0.3543` maxDD `-24.2912`
- `news_risk_high->commodity_24h` score `-13.9681` n `43` status `ready` deltaP `-18.0919` edge `-0.4603` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-34.0864` n `43` status `ready` deltaP `-23.4415` edge `-1.2053` maxDD `-105.9832`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
