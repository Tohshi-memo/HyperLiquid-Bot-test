# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T00:52:31.554762+00:00`
- Price records: `672`
- Market context records: `8464`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5828`

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

- `news_risk_high->unknown_24h` score `6264.1925` n `52` status `ready` deltaP `44.0438` edge `521.7645` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.135` n `59` status `ready` deltaP `23.3929` edge `0.415` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8481` n `61` status `ready` deltaP `20.3127` edge `0.1328` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.2049` n `59` status `ready` deltaP `19.1246` edge `0.0753` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5649` n `61` status `ready` deltaP `12.4521` edge `0.0908` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.2284` n `59` status `ready` deltaP `6.4437` edge `0.1839` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.2231` n `61` status `ready` deltaP `9.3084` edge `0.0796` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.1904` n `59` status `ready` deltaP `16.559` edge `0.1814` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.4807` n `61` status `ready` deltaP `9.3231` edge `0.006` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.4515` n `61` status `ready` deltaP `7.2126` edge `0.0184` maxDD `-0.3089`
- `news_risk_high->metal_1h` score `-0.0248` n `61` status `ready` deltaP `4.6751` edge `0.0071` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.0285` n `59` status `ready` deltaP `10.8903` edge `0.0195` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `-0.2382` n `59` status `ready` deltaP `-0.1292` edge `0.0278` maxDD `-0.7433`
- `news_risk_high->commodity_1h` score `-1.5259` n `61` status `ready` deltaP `-2.594` edge `-0.0313` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5837` n `52` status `ready` deltaP `-27.7244` edge `-0.0483` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.2651` n `59` status `ready` deltaP `-16.8561` edge `-0.1623` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.218` n `52` status `ready` deltaP `-36.6186` edge `-0.247` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.8958` n `52` status `ready` deltaP `-13.3013` edge `-0.392` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.9581` n `52` status `ready` deltaP `-33.1063` edge `-0.3922` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-39.9028` n `52` status `ready` deltaP `-28.4455` edge `-1.6831` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
