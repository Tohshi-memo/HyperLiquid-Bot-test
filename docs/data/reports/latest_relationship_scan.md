# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T23:37:28.208291+00:00`
- Price records: `672`
- Market context records: `4771`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7476`

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

- `market_context_high->unknown_1h` score `8.0514` n `123` status `ready` deltaP `12.3461` edge `0.6304` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.3986` n `123` status `ready` deltaP `17.4288` edge `0.6214` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.9748` n `108` status `ready` deltaP `11.8055` edge `0.1782` maxDD `-4.7201`
- `market_context_high->commodity_4h` score `0.1257` n `123` status `ready` deltaP `11.8394` edge `0.0544` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.0961` n `123` status `ready` deltaP `5.2614` edge `0.0317` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.4174` n `123` status `ready` deltaP `3.3028` edge `0.0021` maxDD `-1.5439`
- `market_context_high->index_4h` score `-0.542` n `123` status `ready` deltaP `5.2337` edge `0.0025` maxDD `-5.5505`
- `market_context_high->equity_4h` score `-0.6398` n `123` status `ready` deltaP `5.8435` edge `0.0476` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-0.8793` n `123` status `ready` deltaP `-0.8142` edge `-0.0029` maxDD `-0.8626`
- `market_context_high->equity_1h` score `-1.0129` n `123` status `ready` deltaP `0.3213` edge `-0.0098` maxDD `-4.1397`
- `market_context_high->index_1h` score `-1.4972` n `123` status `ready` deltaP `-2.4378` edge `-0.0081` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.0285` n `108` status `ready` deltaP `21.1227` edge `0.11` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3068` n `123` status `ready` deltaP `-1.3924` edge `-0.0689` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-3.2865` n `108` status `ready` deltaP `-14.0046` edge `-0.021` maxDD `-3.4277`
- `market_context_high->crypto_alt_1h` score `-3.453` n `123` status `ready` deltaP `-0.4065` edge `-0.0576` maxDD `-15.5285`
- `market_context_high->crypto_major_1h` score `-4.7775` n `123` status `ready` deltaP `-0.8994` edge `-0.0831` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-5.1441` n `123` status `ready` deltaP `3.4553` edge `-0.0401` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.7517` n `108` status `ready` deltaP `-5.6135` edge `-0.1053` maxDD `-18.9266`
- `market_context_high->crypto_major_4h` score `-8.4481` n `123` status `ready` deltaP `2.2358` edge `-0.1749` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.6252` n `123` status `ready` deltaP `3.9126` edge `-0.3078` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
