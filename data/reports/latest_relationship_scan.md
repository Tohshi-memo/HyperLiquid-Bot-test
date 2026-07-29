# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T07:07:24.221524+00:00`
- Price records: `672`
- Market context records: `8278`
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

- `news_risk_high->unknown_24h` score `6577.7423` n `50` status `ready` deltaP `39.5833` edge `547.8813` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.2405` n `54` status `ready` deltaP `26.2308` edge `0.4882` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.0007` n `54` status `ready` deltaP `21.3795` edge `0.1384` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7279` n `54` status `ready` deltaP `22.5722` edge `0.0959` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0594` n `54` status `ready` deltaP `9.8691` edge `0.2676` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7632` n `54` status `ready` deltaP `13.8057` edge `0.0983` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.5216` n `54` status `ready` deltaP `17.0789` edge `0.2204` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.4699` n `54` status `ready` deltaP `9.8581` edge `0.0965` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `1.0125` n `54` status `ready` deltaP `9.1294` edge `0.0703` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4196` n `54` status `ready` deltaP `6.4538` edge `0.0208` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.193` n `54` status `ready` deltaP `7.4462` edge `0.0032` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1263` n `54` status `ready` deltaP `2.8055` edge `0.0111` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4081` n `54` status `ready` deltaP `5.3748` edge `0.0076` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1432` n `54` status `ready` deltaP `-8.8102` edge `-0.0413` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.738` n `50` status `ready` deltaP `-19.9514` edge `-0.0491` maxDD `-5.0181`
- `news_risk_high->metal_24h` score `-5.4591` n `50` status `ready` deltaP `-17.8333` edge `-0.0614` maxDD `-10.6379`
- `news_risk_high->commodity_4h` score `-8.8174` n `54` status `ready` deltaP `-31.1145` edge `-0.1966` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.1594` n `50` status `ready` deltaP `-24.8958` edge `-0.3229` maxDD `-27.2864`
- `news_risk_high->commodity_24h` score `-12.3143` n `50` status `ready` deltaP `-13.0972` edge `-0.3449` maxDD `-33.8515`
- `news_risk_high->crypto_major_24h` score `-34.6409` n `50` status `ready` deltaP `-16.9722` edge `-1.3211` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
