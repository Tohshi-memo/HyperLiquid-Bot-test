# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T13:52:31.292793+00:00`
- Price records: `672`
- Market context records: `8308`
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

- `news_risk_high->unknown_24h` score `6099.0538` n `53` status `ready` deltaP `35.3347` edge `508.061` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.7583` n `53` status `ready` deltaP `25.3193` edge `0.4541` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9351` n `53` status `ready` deltaP `20.8903` edge `0.1362` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5544` n `53` status `ready` deltaP `21.8132` edge `0.0865` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0802` n `53` status `ready` deltaP `10.015` edge `0.2693` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8843` n `53` status `ready` deltaP `14.4193` edge `0.1043` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7224` n `53` status `ready` deltaP `11.8744` edge `0.1041` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6616` n `53` status `ready` deltaP `18.3618` edge `0.2298` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.2427` n `53` status `ready` deltaP `10.9872` edge `0.0771` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3117` n `53` status `ready` deltaP `5.3158` edge `0.0194` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1141` n `53` status `ready` deltaP `5.9739` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `0.0937` n `53` status `ready` deltaP `5.0164` edge `0.0147` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4956` n `53` status `ready` deltaP `3.857` edge `0.0065` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1416` n `53` status `ready` deltaP `-8.6403` edge `-0.0423` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0228` n `53` status `ready` deltaP `-20.4042` edge `-0.0493` maxDD `-5.326`
- `news_risk_high->metal_24h` score `-5.7972` n `53` status `ready` deltaP `-21.8488` edge `-0.0604` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.9562` n `53` status `ready` deltaP `-31.5146` edge `-0.2055` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.2459` n `53` status `ready` deltaP `-7.6028` edge `-0.2925` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1068` n `53` status `ready` deltaP `-24.05` edge `-0.2983` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-32.9852` n `53` status `ready` deltaP `-15.1009` edge `-1.1956` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
