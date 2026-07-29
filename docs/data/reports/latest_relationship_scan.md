# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T07:37:34.092641+00:00`
- Price records: `672`
- Market context records: `8281`
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

- `news_risk_high->unknown_24h` score `6577.8456` n `50` status `ready` deltaP `39.9306` edge `547.8876` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.2045` n `54` status `ready` deltaP `26.2308` edge `0.4852` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9491` n `54` status `ready` deltaP `21.0801` edge `0.1361` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7183` n `54` status `ready` deltaP `22.5722` edge `0.0951` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0539` n `54` status `ready` deltaP `9.8691` edge `0.2669` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7441` n `54` status `ready` deltaP `13.656` edge `0.0977` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.5451` n `54` status `ready` deltaP `17.2313` edge `0.2224` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.4483` n `54` status `ready` deltaP `9.7084` edge `0.0957` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `1.0077` n `54` status `ready` deltaP `9.1294` edge `0.0699` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3872` n `54` status `ready` deltaP `6.1544` edge `0.0201` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1852` n `54` status `ready` deltaP `7.2965` edge `0.0032` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1419` n `54` status `ready` deltaP `2.6558` edge `0.0108` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.3986` n `54` status `ready` deltaP `5.5273` edge `0.0078` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1096` n `54` status `ready` deltaP `-8.5108` edge `-0.0405` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.7368` n `50` status `ready` deltaP `-19.9514` edge `-0.049` maxDD `-5.0181`
- `news_risk_high->metal_24h` score `-5.4742` n `50` status `ready` deltaP `-18.0069` edge `-0.0615` maxDD `-10.6379`
- `news_risk_high->commodity_4h` score `-8.7846` n `54` status `ready` deltaP `-30.8096` edge `-0.1959` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.1172` n `50` status `ready` deltaP `-24.5486` edge `-0.3217` maxDD `-27.2864`
- `news_risk_high->commodity_24h` score `-12.2692` n `50` status `ready` deltaP `-12.9236` edge `-0.3423` maxDD `-33.8515`
- `news_risk_high->crypto_major_24h` score `-34.6745` n `50` status `ready` deltaP `-16.9722` edge `-1.3239` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
