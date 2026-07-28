# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T21:02:28.533354+00:00`
- Price records: `672`
- Market context records: `8233`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5930`

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

- `news_risk_high->unknown_24h` score `7957.2737` n `43` status `ready` deltaP `38.5417` edge `662.8492` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.4916` n `54` status `ready` deltaP `27.4503` edge `0.501` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1337` n `54` status `ready` deltaP `22.4274` edge `0.1425` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7127` n `54` status `ready` deltaP `22.8771` edge `0.0926` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.336` n `54` status `ready` deltaP `11.3934` edge `0.2929` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7763` n `54` status `ready` deltaP `14.4045` edge `0.0954` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7204` n `54` status `ready` deltaP `11.6545` edge `0.1054` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3513` n `54` status `ready` deltaP `16.774` edge `0.2006` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.9101` n `54` status `ready` deltaP `8.8245` edge `0.0638` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.507` n `54` status `ready` deltaP `7.5017` edge `0.0211` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1673` n `54` status `ready` deltaP `6.9971` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1395` n `54` status `ready` deltaP `2.8055` edge `0.01` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5078` n `54` status `ready` deltaP `3.698` edge `0.006` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1084` n `54` status `ready` deltaP `-8.6605` edge `-0.0394` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.0948` n `43` status `ready` deltaP `-18.6491` edge `-0.0453` maxDD `-4.0615`
- `news_risk_high->metal_24h` score `-6.0293` n `43` status `ready` deltaP `-22.5089` edge `-0.1009` maxDD `-10.1184`
- `news_risk_high->commodity_4h` score `-8.8831` n `54` status `ready` deltaP `-32.7913` edge `-0.1909` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.6995` n `43` status `ready` deltaP `-23.9624` edge `-0.3574` maxDD `-24.2912`
- `news_risk_high->commodity_24h` score `-14.5805` n `43` status `ready` deltaP `-21.2169` edge `-0.4905` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-34.5244` n `43` status `ready` deltaP `-23.4415` edge `-1.2418` maxDD `-105.9832`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
