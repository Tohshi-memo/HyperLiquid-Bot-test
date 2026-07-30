# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T21:37:34.228783+00:00`
- Price records: `672`
- Market context records: `8449`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5785`

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

- `news_risk_high->unknown_24h` score `6260.4341` n `52` status `ready` deltaP `44.0438` edge `521.4513` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `4.9343` n `52` status `ready` deltaP `22.4085` edge `0.3215` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8681` n `58` status `ready` deltaP `20.6226` edge `0.1324` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.0386` n `52` status `ready` deltaP `18.1402` edge `0.068` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.8003` n `58` status `ready` deltaP `14.6139` edge `0.096` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.2462` n `58` status `ready` deltaP `9.4466` edge `0.0806` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.0801` n `52` status `ready` deltaP `3.5764` edge `0.184` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.8817` n `52` status `ready` deltaP `12.4531` edge `0.1692` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.6713` n `58` status `ready` deltaP `11.465` edge `0.0076` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.4025` n `58` status `ready` deltaP `6.3752` edge `0.0199` maxDD `-0.3089`
- `news_risk_high->metal_4h` score `-0.0754` n `52` status `ready` deltaP `1.2313` edge `0.0323` maxDD `-0.7433`
- `news_risk_high->metal_1h` score `-0.1537` n `58` status `ready` deltaP `3.1541` edge `0.0065` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.3282` n `52` status `ready` deltaP `6.0272` edge `0.0135` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.5923` n `58` status `ready` deltaP `-3.1541` edge `-0.0331` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6341` n `52` status `ready` deltaP `-27.7244` edge `-0.0525` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.4335` n `52` status `ready` deltaP `-26.3602` edge `-0.1963` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.9895` n `52` status `ready` deltaP `-35.5769` edge `-0.2349` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.7774` n `52` status `ready` deltaP `-12.7804` edge `-0.3856` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.3876` n `52` status `ready` deltaP `-30.8494` edge `-0.3597` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-38.9794` n `52` status `ready` deltaP `-26.1885` edge `-1.6212` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
