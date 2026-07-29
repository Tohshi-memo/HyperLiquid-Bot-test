# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T01:22:38.650551+00:00`
- Price records: `672`
- Market context records: `8254`
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

- `news_risk_high->unknown_24h` score `7957.6872` n `43` status `ready` deltaP `38.7153` edge `662.8825` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.1735` n `54` status `ready` deltaP `26.3832` edge `0.4816` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1241` n `54` status `ready` deltaP `22.4274` edge `0.1417` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6983` n `54` status `ready` deltaP `22.8771` edge `0.0914` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.3109` n `54` status `ready` deltaP `11.241` edge `0.2907` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8015` n `54` status `ready` deltaP `14.5542` edge `0.0965` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7073` n `54` status `ready` deltaP `11.3551` edge `0.1063` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3403` n `54` status `ready` deltaP `16.6215` edge `0.2002` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.1824` n `54` status `ready` deltaP `10.6538` edge `0.0743` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4782` n `54` status `ready` deltaP `7.2023` edge `0.0207` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1743` n `54` status `ready` deltaP `7.1468` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0676` n `54` status `ready` deltaP `3.4043` edge `0.012` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4571` n `54` status `ready` deltaP `4.6127` edge `0.0064` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.148` n `54` status `ready` deltaP `-8.6605` edge `-0.0427` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.0756` n `43` status `ready` deltaP `-18.6491` edge `-0.0437` maxDD `-4.0615`
- `news_risk_high->metal_24h` score `-5.5916` n `43` status `ready` deltaP `-19.5575` edge `-0.0841` maxDD `-10.1184`
- `news_risk_high->commodity_4h` score `-9.0187` n `54` status `ready` deltaP `-32.7913` edge `-0.2022` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.6924` n `43` status `ready` deltaP `-24.3096` edge `-0.3545` maxDD `-24.2912`
- `news_risk_high->commodity_24h` score `-13.9988` n `43` status `ready` deltaP `-18.2655` edge `-0.4617` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-34.1068` n `43` status `ready` deltaP `-23.4415` edge `-1.207` maxDD `-105.9832`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
