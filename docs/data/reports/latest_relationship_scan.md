# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T08:52:30.163974+00:00`
- Price records: `672`
- Market context records: `8499`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5871`

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

- `news_risk_high->unknown_24h` score `6273.3653` n `52` status `ready` deltaP `44.0438` edge `522.5289` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.0364` n `64` status `ready` deltaP `21.875` edge `0.4169` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0363` n `64` status `ready` deltaP `16.8064` edge `0.0767` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7194` n `64` status `ready` deltaP `15.8028` edge `0.0856` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9485` n `64` status `ready` deltaP `5.8308` edge `0.1603` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.9264` n `64` status `ready` deltaP `14.4817` edge `0.1614` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.6074` n `64` status `ready` deltaP `9.9083` edge `0.0645` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3914` n `64` status `ready` deltaP `7.3634` edge `0.0523` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1687` n `64` status `ready` deltaP `6.7833` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0742` n `64` status `ready` deltaP `12.0808` edge `0.0214` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0309` n `64` status `ready` deltaP `4.07` edge `0.0085` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.1052` n `64` status `ready` deltaP `0.6479` edge `0.0298` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1766` n `64` status `ready` deltaP `2.8069` edge `0.0069` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.6519` n `64` status `ready` deltaP `-3.8548` edge `-0.0334` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5213` n `52` status `ready` deltaP `-27.7244` edge `-0.0431` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.6501` n `64` status `ready` deltaP `-20.6174` edge `-0.1673` maxDD `-13.2872`
- `news_risk_high->metal_24h` score `-9.5081` n `52` status `ready` deltaP `-37.1394` edge `-0.2677` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.9078` n `52` status `ready` deltaP `-13.3013` edge `-0.393` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-15.3158` n `52` status `ready` deltaP `-38.6619` edge `-0.4683` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-41.5976` n `52` status `ready` deltaP `-34.001` edge `-1.7873` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
