# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T03:52:25.198353+00:00`
- Price records: `672`
- Market context records: `8477`
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

- `news_risk_high->unknown_24h` score `6267.6785` n `52` status `ready` deltaP `44.0438` edge `522.055` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.2315` n `61` status `ready` deltaP `22.4385` edge `0.4294` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.1972` n `61` status `ready` deltaP `18.3226` edge `0.08` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7589` n `64` status `ready` deltaP `16.2519` edge `0.0859` maxDD `-2.4803`
- `news_risk_high->crypto_alt_4h` score `1.348` n `61` status `ready` deltaP `17.2506` edge `0.197` maxDD `-5.8012`
- `news_risk_high->crypto_major_4h` score `1.3371` n `61` status `ready` deltaP `7.4545` edge `0.1911` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `0.6206` n `64` status `ready` deltaP `10.2077` edge `0.0642` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3501` n `64` status `ready` deltaP `7.064` edge `0.049` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1087` n `64` status `ready` deltaP `5.7354` edge `0.0038` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.044` n `61` status `ready` deltaP `11.6429` edge `0.0218` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0379` n `64` status `ready` deltaP `4.2197` edge `0.0084` maxDD `-0.5338`
- `news_risk_high->metal_1h` score `-0.2557` n `64` status `ready` deltaP `2.0584` edge `0.0053` maxDD `-0.5599`
- `news_risk_high->metal_4h` score `-0.4156` n `61` status `ready` deltaP `-1.6169` edge `0.0234` maxDD `-0.7801`
- `news_risk_high->commodity_1h` score `-1.5129` n `64` status `ready` deltaP `-2.5075` edge `-0.0308` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5525` n `52` status `ready` deltaP `-27.7244` edge `-0.0457` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.42` n `61` status `ready` deltaP `-18.5526` edge `-0.1639` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.2804` n `52` status `ready` deltaP `-36.6186` edge `-0.2522` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.9378` n `52` status `ready` deltaP `-13.3013` edge `-0.3955` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-14.4416` n `52` status `ready` deltaP `-35.1896` edge `-0.4186` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-40.4618` n `52` status `ready` deltaP `-30.5288` edge `-1.7158` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
