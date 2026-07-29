# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T14:56:30.906823+00:00`
- Price records: `672`
- Market context records: `8313`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5886`

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

- `news_risk_high->unknown_24h` score `6250.9574` n `52` status `ready` deltaP `35.1896` edge `520.7206` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.6994` n `52` status `ready` deltaP `25.1524` edge `0.4503` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8212` n `52` status `ready` deltaP `20.8314` edge `0.1271` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.551` n `52` status `ready` deltaP `21.9512` edge `0.0853` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.043` n `52` status `ready` deltaP `9.674` edge `0.2668` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7958` n `52` status `ready` deltaP `13.6573` edge `0.102` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6278` n `52` status `ready` deltaP `11.1124` edge `0.1013` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6274` n `52` status `ready` deltaP `18.0934` edge `0.2272` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.2083` n `52` status `ready` deltaP `10.3776` edge `0.0783` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2684` n `52` status `ready` deltaP `5.0438` edge `0.0176` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1444` n `52` status `ready` deltaP `6.5408` edge `0.003` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `0.0228` n `52` status `ready` deltaP `4.445` edge `0.0126` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4843` n `52` status `ready` deltaP `4.0455` edge `0.0067` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2879` n `52` status `ready` deltaP `-9.9148` edge `-0.046` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0033` n `52` status `ready` deltaP `-20.2591` edge `-0.0497` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-5.6901` n `52` status `ready` deltaP `-21.5144` edge `-0.0537` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.209` n `52` status `ready` deltaP `-33.22` edge `-0.2152` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.7196` n `52` status `ready` deltaP `-9.3082` edge `-0.3206` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1792` n `52` status `ready` deltaP `-23.9049` edge `-0.3053` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-33.416` n `52` status `ready` deltaP `-15.251` edge `-1.2305` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
