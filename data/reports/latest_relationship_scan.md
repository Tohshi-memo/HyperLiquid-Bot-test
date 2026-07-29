# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T08:37:30.642308+00:00`
- Price records: `672`
- Market context records: `8285`
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

- `news_risk_high->unknown_24h` score `6251.0937` n `52` status `ready` deltaP `36.7788` edge `520.6984` maxDD `-0.863`
- `news_risk_high->equity_4h` score `7.0699` n `54` status `ready` deltaP `26.0783` edge `0.475` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9731` n `54` status `ready` deltaP `21.2298` edge `0.1371` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6773` n `54` status `ready` deltaP `22.4198` edge `0.0927` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.036` n `54` status `ready` deltaP `9.8691` edge `0.2646` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.804` n `54` status `ready` deltaP `14.1051` edge `0.0997` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.5451` n `54` status `ready` deltaP `17.2313` edge `0.2224` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.525` n `54` status `ready` deltaP `10.3072` edge `0.0981` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `0.9981` n `54` status `ready` deltaP `9.1294` edge `0.0691` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4136` n `54` status `ready` deltaP `6.4538` edge `0.0203` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1681` n `54` status `ready` deltaP `6.9971` edge `0.003` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1383` n `54` status `ready` deltaP `2.6558` edge `0.0111` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4168` n `54` status `ready` deltaP `5.2224` edge `0.0075` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.0964` n `54` status `ready` deltaP `-8.3611` edge `-0.0404` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.8893` n `52` status `ready` deltaP `-20.2591` edge `-0.0488` maxDD `-5.2201`
- `news_risk_high->metal_24h` score `-5.542` n `52` status `ready` deltaP `-19.2575` edge `-0.0582` maxDD `-10.6864`
- `news_risk_high->commodity_4h` score `-8.7372` n `54` status `ready` deltaP `-30.3523` edge `-0.195` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.5924` n `52` status `ready` deltaP `-9.3082` edge `-0.31` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0818` n `52` status `ready` deltaP `-24.2388` edge `-0.3072` maxDD `-27.7089`
- `news_risk_high->crypto_major_24h` score `-33.2185` n `52` status `ready` deltaP `-14.2227` edge `-1.2209` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
