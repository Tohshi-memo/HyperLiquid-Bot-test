# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T02:37:25.753278+00:00`
- Price records: `672`
- Market context records: `8259`
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

- `news_risk_high->unknown_24h` score `7957.8986` n `43` status `ready` deltaP `39.0625` edge `662.8978` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.1567` n `54` status `ready` deltaP `26.3832` edge `0.4802` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1985` n `54` status `ready` deltaP `22.4274` edge `0.1479` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7055` n `54` status `ready` deltaP `22.8771` edge `0.092` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.278` n `54` status `ready` deltaP `11.0886` edge `0.2875` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8723` n `54` status `ready` deltaP `14.8536` edge `0.1004` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7205` n `54` status `ready` deltaP `11.3551` edge `0.1074` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3559` n `54` status `ready` deltaP `16.6215` edge `0.2022` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.197` n `54` status `ready` deltaP `10.8062` edge `0.0745` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.5286` n `54` status `ready` deltaP `7.5017` edge `0.0229` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1985` n `54` status `ready` deltaP `7.5959` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0604` n `54` status `ready` deltaP `3.4043` edge `0.0126` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4231` n `54` status `ready` deltaP `5.2224` edge `0.0067` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1612` n `54` status `ready` deltaP `-8.8102` edge `-0.0428` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.0732` n `43` status `ready` deltaP `-18.6491` edge `-0.0435` maxDD `-4.0615`
- `news_risk_high->metal_24h` score `-5.5578` n `43` status `ready` deltaP `-19.2103` edge `-0.0836` maxDD `-10.1184`
- `news_risk_high->commodity_4h` score `-9.0901` n `54` status `ready` deltaP `-33.2487` edge `-0.2051` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.6684` n `43` status `ready` deltaP `-24.3096` edge `-0.3525` maxDD `-24.2912`
- `news_risk_high->commodity_24h` score `-13.855` n `43` status `ready` deltaP `-17.3974` edge `-0.4555` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-33.976` n `43` status `ready` deltaP `-23.4415` edge `-1.1961` maxDD `-105.9832`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
