# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T20:07:29.691149+00:00`
- Price records: `672`
- Market context records: `7597`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14551`

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

- `market_context_high->equity_24h` score `1.3232` n `142` status `ready` deltaP `18.5798` edge `0.5838` maxDD `-38.3748`
- `market_context_high->unknown_24h` score `0.6551` n `143` status `ready` deltaP `13.4106` edge `0.122` maxDD `-5.1929`
- `market_context_high->commodity_24h` score `0.5547` n `142` status `ready` deltaP `16.5407` edge `0.0943` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.0855` n `147` status `ready` deltaP `7.0448` edge `0.0119` maxDD `-0.8324`
- `market_context_high->commodity_4h` score `-0.0976` n `147` status `ready` deltaP `7.2708` edge `0.0194` maxDD `-2.4139`
- `market_context_high->crypto_major_1h` score `-0.1454` n `147` status `ready` deltaP `8.0543` edge `0.0237` maxDD `-4.0162`
- `market_context_high->commodity_1h` score `-0.2201` n `147` status `ready` deltaP `4.29` edge `0.0004` maxDD `-1.5775`
- `market_context_high->crypto_alt_1h` score `-0.2214` n `147` status `ready` deltaP `2.1498` edge `0.0205` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.2278` n `142` status `ready` deltaP `10.242` edge `0.0215` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4454` n `147` status `ready` deltaP `6.5147` edge `0.0557` maxDD `-7.8324`
- `market_context_high->index_4h` score `-0.6199` n `147` status `ready` deltaP `9.2836` edge `0.0304` maxDD `-3.4082`
- `market_context_high->metal_1h` score `-0.6238` n `147` status `ready` deltaP `1.5112` edge `0.0145` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6495` n `147` status `ready` deltaP `-0.3585` edge `-0.0018` maxDD `-0.6615`
- `market_context_high->unknown_1h` score `-0.9716` n `147` status `ready` deltaP `-0.4216` edge `-0.0594` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.0669` n `147` status `ready` deltaP `2.5334` edge `0.052` maxDD `-9.7866`
- `market_context_high->crypto_major_4h` score `-1.1615` n `147` status `ready` deltaP `8.7264` edge `0.0649` maxDD `-14.7592`
- `market_context_high->equity_4h` score `-1.4855` n `147` status `ready` deltaP `3.0924` edge `0.2139` maxDD `-20.9976`
- `market_context_high->metal_4h` score `-1.6362` n `147` status `ready` deltaP `-1.373` edge `0.0457` maxDD `-4.7051`
- `market_context_high->metal_24h` score `-1.7823` n `143` status `ready` deltaP `-1.3233` edge `0.1211` maxDD `-8.2622`
- `market_context_high->fx_4h` score `-2.5345` n `147` status `ready` deltaP `-5.826` edge `-0.0039` maxDD `-2.1439`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
