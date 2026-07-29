# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T04:37:25.171515+00:00`
- Price records: `672`
- Market context records: `8268`
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

- `news_risk_high->unknown_24h` score `7118.7458` n `47` status `ready` deltaP `39.0625` edge `592.9684` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.2359` n `54` status `ready` deltaP `26.3832` edge `0.4868` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.2813` n `54` status `ready` deltaP `22.5771` edge `0.1538` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7415` n `54` status `ready` deltaP `22.8771` edge `0.095` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1668` n `54` status `ready` deltaP `10.6313` edge `0.2763` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.9814` n `54` status `ready` deltaP `15.3027` edge `0.1065` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7265` n `54` status `ready` deltaP `11.2054` edge `0.1089` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4019` n `54` status `ready` deltaP `16.6215` edge `0.2081` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.1278` n `54` status `ready` deltaP `10.1965` edge `0.0728` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.5562` n `54` status `ready` deltaP `7.6514` edge `0.0242` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.2265` n `54` status `ready` deltaP `8.045` edge `0.0035` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0317` n `54` status `ready` deltaP `3.7037` edge `0.013` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4136` n `54` status `ready` deltaP `5.3748` edge `0.0069` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1863` n `54` status `ready` deltaP `-9.1096` edge `-0.0429` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.4598` n `47` status `ready` deltaP `-19.4408` edge `-0.047` maxDD `-4.6039`
- `news_risk_high->metal_24h` score `-5.9115` n `47` status `ready` deltaP `-21.3874` edge `-0.0754` maxDD `-10.6379`
- `news_risk_high->commodity_4h` score `-9.0161` n `54` status `ready` deltaP `-32.6389` edge `-0.203` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.0938` n `47` status `ready` deltaP `-25.2992` edge `-0.3408` maxDD `-26.2018`
- `news_risk_high->commodity_24h` score `-12.822` n `47` status `ready` deltaP `-14.4503` edge `-0.3867` maxDD `-33.1706`
- `news_risk_high->equity_24h` score `-35.5992` n `47` status `ready` deltaP `-24.4311` edge `-1.1808` maxDD `-116.1673`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
