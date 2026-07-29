# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T00:52:28.419065+00:00`
- Price records: `672`
- Market context records: `8251`
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

- `news_risk_high->unknown_24h` score `7957.6109` n `43` status `ready` deltaP `38.5417` edge `662.8773` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.2109` n `54` status `ready` deltaP `26.5357` edge `0.4837` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.0965` n `54` status `ready` deltaP `22.4274` edge `0.1394` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7141` n `54` status `ready` deltaP `23.0296` edge `0.0917` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.3369` n `54` status `ready` deltaP `11.5459` edge `0.292` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7919` n `54` status `ready` deltaP `14.5542` edge `0.0957` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7085` n `54` status `ready` deltaP `11.3551` edge `0.1064` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3418` n `54` status `ready` deltaP `16.6215` edge `0.2004` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.1448` n `54` status `ready` deltaP `10.3489` edge `0.0732` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4722` n `54` status `ready` deltaP `7.2023` edge `0.0202` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.158` n `54` status `ready` deltaP `6.8474` edge `0.0027` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.106` n `54` status `ready` deltaP `3.1049` edge `0.0108` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4666` n `54` status `ready` deltaP `4.4602` edge `0.0062` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1504` n `54` status `ready` deltaP `-8.6605` edge `-0.0429` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.0804` n `43` status `ready` deltaP `-18.6491` edge `-0.0441` maxDD `-4.0615`
- `news_risk_high->metal_24h` score `-5.6337` n `43` status `ready` deltaP `-19.9047` edge `-0.0853` maxDD `-10.1184`
- `news_risk_high->commodity_4h` score `-9.0007` n `54` status `ready` deltaP `-32.7913` edge `-0.2007` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.6912` n `43` status `ready` deltaP `-24.3096` edge `-0.3544` maxDD `-24.2912`
- `news_risk_high->commodity_24h` score `-14.0626` n `43` status `ready` deltaP `-18.6127` edge `-0.4647` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-34.1188` n `43` status `ready` deltaP `-23.4415` edge `-1.208` maxDD `-105.9832`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
