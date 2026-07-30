# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T19:07:33.241110+00:00`
- Price records: `672`
- Market context records: `8438`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5742`

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

- `news_risk_high->unknown_24h` score `6257.5366` n `52` status `ready` deltaP `43.8702` edge `521.211` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.1871` n `52` status `ready` deltaP `23.0183` edge `0.3385` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.2228` n `52` status `ready` deltaP `18.5859` edge `0.0922` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1174` n `52` status `ready` deltaP `18.75` edge `0.0705` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.52` n `52` status `ready` deltaP `12.1603` edge `0.089` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.2034` n `52` status `ready` deltaP `8.7172` edge `0.0819` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.1413` n `52` status `ready` deltaP `4.0338` edge `0.1888` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.9902` n `52` status `ready` deltaP `13.5202` edge `0.176` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.1826` n `52` status `ready` deltaP `6.9899` edge `0.0049` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.001` n `52` status `ready` deltaP `1.841` edge `0.0346` maxDD `-0.7433`
- `news_risk_high->index_1h` score `-0.0527` n `52` status `ready` deltaP `1.7504` edge `0.0128` maxDD `-0.3089`
- `news_risk_high->fx_4h` score `-0.3195` n `52` status `ready` deltaP `6.1797` edge `0.0136` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.5044` n `52` status `ready` deltaP `-0.3454` edge `0.0006` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.8842` n `52` status `ready` deltaP `-5.7232` edge `-0.0403` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6821` n `52` status `ready` deltaP `-27.7244` edge `-0.0565` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.5258` n `52` status `ready` deltaP `-27.2748` edge `-0.1979` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.782` n `52` status `ready` deltaP `-34.7088` edge `-0.2234` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.721` n `52` status `ready` deltaP `-12.7804` edge `-0.3809` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.9739` n `52` status `ready` deltaP `-29.1133` edge `-0.3368` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-37.8313` n `52` status `ready` deltaP `-27.2035` edge `-1.1837` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
