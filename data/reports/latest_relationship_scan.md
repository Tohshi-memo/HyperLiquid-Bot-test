# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T07:52:26.773750+00:00`
- Price records: `672`
- Market context records: `8282`
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

- `news_risk_high->unknown_24h` score `6577.8931` n `50` status `ready` deltaP `40.1042` edge `547.8904` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.1805` n `54` status `ready` deltaP `26.2308` edge `0.4832` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9479` n `54` status `ready` deltaP `21.0801` edge `0.136` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7135` n `54` status `ready` deltaP `22.5722` edge `0.0947` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0469` n `54` status `ready` deltaP `9.8691` edge `0.266` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.762` n `54` status `ready` deltaP `13.8057` edge `0.0982` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.5475` n `54` status `ready` deltaP `17.2313` edge `0.2227` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.4627` n `54` status `ready` deltaP `9.8581` edge `0.0959` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `1.0041` n `54` status `ready` deltaP `9.1294` edge `0.0696` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3872` n `54` status `ready` deltaP `6.1544` edge `0.0201` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1775` n `54` status `ready` deltaP `7.1468` edge `0.0032` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1539` n `54` status `ready` deltaP `2.5061` edge `0.0108` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.3986` n `54` status `ready` deltaP `5.5273` edge `0.0078` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1084` n `54` status `ready` deltaP `-8.5108` edge `-0.0404` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.7368` n `50` status `ready` deltaP `-19.9514` edge `-0.049` maxDD `-5.0181`
- `news_risk_high->metal_24h` score `-5.4917` n `50` status `ready` deltaP `-18.1806` edge `-0.0618` maxDD `-10.6379`
- `news_risk_high->commodity_4h` score `-8.7688` n `54` status `ready` deltaP `-30.6572` edge `-0.1956` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.0974` n `50` status `ready` deltaP `-24.375` edge `-0.3212` maxDD `-27.2864`
- `news_risk_high->commodity_24h` score `-12.2548` n `50` status `ready` deltaP `-12.9236` edge `-0.3411` maxDD `-33.8515`
- `news_risk_high->crypto_major_24h` score `-34.6949` n `50` status `ready` deltaP `-16.9722` edge `-1.3256` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
