# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T07:26:33.207094+00:00`
- Price records: `672`
- Market context records: `8280`
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

- `news_risk_high->unknown_24h` score `6577.7934` n `50` status `ready` deltaP `39.7569` edge `547.8844` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.2273` n `54` status `ready` deltaP `26.2308` edge `0.4871` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9719` n `54` status `ready` deltaP `21.2298` edge `0.137` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7243` n `54` status `ready` deltaP `22.5722` edge `0.0956` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.057` n `54` status `ready` deltaP `9.8691` edge `0.2673` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7441` n `54` status `ready` deltaP `13.656` edge `0.0977` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.5389` n `54` status `ready` deltaP `17.2313` edge `0.2216` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.4483` n `54` status `ready` deltaP `9.7084` edge `0.0957` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `1.0101` n `54` status `ready` deltaP `9.1294` edge `0.0701` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4028` n `54` status `ready` deltaP `6.3041` edge `0.0204` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.193` n `54` status `ready` deltaP `7.4462` edge `0.0032` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1275` n `54` status `ready` deltaP `2.8055` edge `0.011` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.3994` n `54` status `ready` deltaP `5.5273` edge `0.0077` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1264` n `54` status `ready` deltaP `-8.6605` edge `-0.0409` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.738` n `50` status `ready` deltaP `-19.9514` edge `-0.0491` maxDD `-5.0181`
- `news_risk_high->metal_24h` score `-5.4591` n `50` status `ready` deltaP `-17.8333` edge `-0.0614` maxDD `-10.6379`
- `news_risk_high->commodity_4h` score `-8.8016` n `54` status `ready` deltaP `-30.9621` edge `-0.1963` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.1371` n `50` status `ready` deltaP `-24.7222` edge `-0.3222` maxDD `-27.2864`
- `news_risk_high->commodity_24h` score `-12.2999` n `50` status `ready` deltaP `-13.0972` edge `-0.3437` maxDD `-33.8515`
- `news_risk_high->crypto_major_24h` score `-34.6553` n `50` status `ready` deltaP `-16.9722` edge `-1.3223` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
