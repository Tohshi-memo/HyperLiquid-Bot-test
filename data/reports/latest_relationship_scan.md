# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T02:22:28.360339+00:00`
- Price records: `672`
- Market context records: `8471`
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

- `news_risk_high->unknown_24h` score `6265.9325` n `52` status `ready` deltaP `44.0438` edge `521.9095` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.3465` n `61` status `ready` deltaP `23.2007` edge `0.4339` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.2723` n `61` status `ready` deltaP `18.9324` edge `0.0822` maxDD `-0.191`
- `news_risk_high->equity_1h` score `2.1736` n `63` status `ready` deltaP `17.8667` edge `0.1004` maxDD `-1.737`
- `news_risk_high->crypto_alt_4h` score `1.2349` n `61` status `ready` deltaP `16.336` edge `0.1886` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `1.2126` n `63` status `ready` deltaP `10.826` edge `0.0725` maxDD `-1.1562`
- `news_risk_high->crypto_major_4h` score `1.1944` n `61` status `ready` deltaP `6.5398` edge `0.1789` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `0.8198` n `63` status `ready` deltaP `7.6823` edge `0.0583` maxDD `-1.2958`
- `news_risk_high->index_1h` score `0.1825` n `63` status `ready` deltaP `5.1374` edge `0.011` maxDD `-0.403`
- `news_risk_high->fx_1h` score `0.1749` n `63` status `ready` deltaP `6.9029` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0632` n `61` status `ready` deltaP `11.6429` edge `0.0234` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.1915` n `63` status `ready` deltaP `2.8016` edge `0.0057` maxDD `-0.5599`
- `news_risk_high->metal_4h` score `-0.481` n `61` status `ready` deltaP `-2.0742` edge `0.021` maxDD `-0.7801`
- `news_risk_high->commodity_1h` score `-1.5964` n `63` status `ready` deltaP `-3.4004` edge `-0.0318` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5681` n `52` status `ready` deltaP `-27.7244` edge `-0.047` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.4296` n `61` status `ready` deltaP `-18.5526` edge `-0.1647` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.2456` n `52` status `ready` deltaP `-36.6186` edge `-0.2493` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.909` n `52` status `ready` deltaP `-13.3013` edge `-0.3931` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-14.2023` n `52` status `ready` deltaP `-34.148` edge `-0.4056` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-40.2129` n `52` status `ready` deltaP `-29.4871` edge `-1.702` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
