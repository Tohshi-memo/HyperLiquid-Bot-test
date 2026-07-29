# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T06:22:31.403726+00:00`
- Price records: `672`
- Market context records: `8275`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5892`

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

- `news_risk_high->unknown_24h` score `6577.5794` n `50` status `ready` deltaP `39.0625` edge `547.8712` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.2743` n `54` status `ready` deltaP `26.3832` edge `0.49` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.057` n `54` status `ready` deltaP `21.6789` edge `0.1411` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7643` n `54` status `ready` deltaP `22.8771` edge `0.0969` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.079` n `54` status `ready` deltaP `10.0215` edge `0.2691` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8172` n `54` status `ready` deltaP `14.2548` edge `0.0998` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.5239` n `54` status `ready` deltaP `10.1575` edge `0.099` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4761` n `54` status `ready` deltaP `16.774` edge `0.2166` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.0586` n `54` status `ready` deltaP `9.5867` edge `0.0711` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4579` n `54` status `ready` deltaP `6.7532` edge `0.022` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.2016` n `54` status `ready` deltaP `7.5959` edge `0.0033` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0796` n `54` status `ready` deltaP `3.2546` edge `0.012` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4097` n `54` status `ready` deltaP `5.3748` edge `0.0074` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1779` n `54` status `ready` deltaP `-9.1096` edge `-0.0422` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.7392` n `50` status `ready` deltaP `-19.9514` edge `-0.0492` maxDD `-5.0181`
- `news_risk_high->metal_24h` score `-5.4091` n `50` status `ready` deltaP `-17.3125` edge `-0.0607` maxDD `-10.6379`
- `news_risk_high->commodity_4h` score `-8.8768` n `54` status `ready` deltaP `-31.5718` edge `-0.1985` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.2203` n `50` status `ready` deltaP `-25.4167` edge `-0.3245` maxDD `-27.2864`
- `news_risk_high->commodity_24h` score `-12.404` n `50` status `ready` deltaP `-13.6181` edge `-0.3489` maxDD `-33.8515`
- `news_risk_high->crypto_major_24h` score `-34.5634` n `50` status `ready` deltaP `-16.7986` edge `-1.3158` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
