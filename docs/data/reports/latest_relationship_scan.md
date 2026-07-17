# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T08:22:30.473818+00:00`
- Price records: `672`
- Market context records: `7009`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11541`

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

- `market_context_high->unknown_24h` score `-0.2142` n `220` status `ready` deltaP `-5.363` edge `0.4633` maxDD `-18.7342`
- `market_context_high->fx_1h` score `-0.2709` n `233` status `ready` deltaP `1.9011` edge `0.0011` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4651` n `233` status `ready` deltaP `2.1112` edge `0.0336` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6311` n `233` status `ready` deltaP `1.292` edge `0.0016` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.6687` n `233` status `ready` deltaP `-1.373` edge `0.0002` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-0.7584` n `233` status `ready` deltaP `-1.6917` edge `-0.0138` maxDD `-2.4388`
- `market_context_high->crypto_major_1h` score `-0.9115` n `233` status `ready` deltaP `4.1672` edge `0.0315` maxDD `-7.1523`
- `market_context_high->fx_4h` score `-0.9715` n `233` status `ready` deltaP `11.2982` edge `0.0065` maxDD `-2.1765`
- `market_context_high->unknown_1h` score `-1.3314` n `233` status `ready` deltaP `-2.0316` edge `-0.0073` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6479` n `233` status `ready` deltaP `-3.9575` edge `-0.0359` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7465` n `233` status `ready` deltaP `8.2494` edge `-0.009` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.7847` n `233` status `ready` deltaP `4.2764` edge `-0.0019` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.8815` n `233` status `ready` deltaP `6.931` edge `0.0109` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.5079` n `233` status `ready` deltaP `-5.7803` edge `0.0661` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-2.6695` n `233` status `ready` deltaP `2.1001` edge `0.0223` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-3.4302` n `220` status `ready` deltaP `-5.3851` edge `-0.0899` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.3397` n `220` status `ready` deltaP `-6.6193` edge `-0.0164` maxDD `-5.4226`
- `market_context_high->crypto_major_4h` score `-4.798` n `233` status `ready` deltaP `2.072` edge `0.0148` maxDD `-24.6094`
- `market_context_high->equity_4h` score `-7.2946` n `233` status `ready` deltaP `5.5663` edge `-0.0506` maxDD `-66.7371`
- `market_context_high->metal_24h` score `-13.3414` n `220` status `ready` deltaP `-8.7974` edge `-0.0562` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
