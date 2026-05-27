# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T08:22:19.318284+00:00`
- Price records: `672`
- Market context records: `2024`
- Flow alert records: `7719`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9091`

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

- `market_context_high->crypto_major_4h` score `8.9027` n `205` status `ready` deltaP `30.7927` edge `0.5896` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.3994` n `205` status `ready` deltaP `24.5427` edge `0.6508` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.9133` n `205` status `ready` deltaP `18.689` edge `0.4431` maxDD `-2.6599`
- `market_context_high->equity_4h` score `3.0167` n `205` status `ready` deltaP `17.2561` edge `0.2458` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5201` n `205` status `ready` deltaP `12.328` edge `0.1431` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.4294` n `205` status `ready` deltaP `12.9269` edge `0.1013` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2078` n `205` status `ready` deltaP `9.7831` edge `0.1468` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `0.5221` n `194` status `ready` deltaP `16.3871` edge `0.4663` maxDD `-35.8966`
- `market_context_high->equity_24h` score `0.2842` n `194` status `ready` deltaP `15.3492` edge `0.4112` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.2068` n `205` status `ready` deltaP `6.9104` edge `0.05` maxDD `-2.6402`
- `market_context_high->index_24h` score `0.0603` n `194` status `ready` deltaP `3.7001` edge `0.1032` maxDD `-4.1604`
- `market_context_high->unknown_1h` score `0.0302` n `205` status `ready` deltaP `3.7462` edge `0.0495` maxDD `-3.0902`
- `market_context_high->fx_24h` score `-0.3069` n `194` status `ready` deltaP `12.2476` edge `0.0243` maxDD `-2.1887`
- `market_context_high->index_1h` score `-0.3253` n `205` status `ready` deltaP `2.2543` edge `0.0169` maxDD `-1.3898`
- `market_context_high->metal_24h` score `-0.8459` n `194` status `ready` deltaP `11.0136` edge `0.1514` maxDD `-16.9583`
- `market_context_high->fx_1h` score `-0.8769` n `205` status `ready` deltaP `-1.5912` edge `0.0003` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.8994` n `205` status `ready` deltaP `3.6585` edge `0.0194` maxDD `-5.166`
- `market_context_high->metal_4h` score `-1.3442` n `205` status `ready` deltaP `7.9574` edge `0.0972` maxDD `-11.9812`
- `market_context_high->fx_4h` score `-1.5963` n `205` status `ready` deltaP `-6.4329` edge `-0.002` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.8138` n `205` status `ready` deltaP `3.2043` edge `0.0019` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
