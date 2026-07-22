# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T13:22:34.959836+00:00`
- Price records: `672`
- Market context records: `7568`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14496`

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

- `market_context_high->commodity_4h` score `0.1462` n `170` status `ready` deltaP `8.9081` edge `0.0288` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.1169` n `170` status `ready` deltaP `5.5185` edge `0.0078` maxDD `-1.7657`
- `market_context_high->commodity_24h` score `-0.2396` n `153` status `ready` deltaP `12.4024` edge `0.0557` maxDD `-7.0012`
- `market_context_high->fx_1h` score `-0.2683` n `170` status `ready` deltaP `2.2399` edge `0.0006` maxDD `-0.6615`
- `market_context_high->commodity_1h` score `-0.3045` n `170` status `ready` deltaP `4.3561` edge `0.0028` maxDD `-1.5775`
- `market_context_high->unknown_1h` score `-0.5367` n `170` status `ready` deltaP `2.0747` edge `0.0038` maxDD `-1.3217`
- `market_context_high->index_4h` score `-0.5639` n `170` status `ready` deltaP `10.9876` edge `0.0308` maxDD `-3.774`
- `market_context_high->unknown_4h` score `-0.5831` n `170` status `ready` deltaP `10.8465` edge `0.0888` maxDD `-6.2031`
- `market_context_high->crypto_major_1h` score `-0.7003` n `170` status `ready` deltaP `5.0053` edge `0.0179` maxDD `-7.6171`
- `market_context_high->crypto_alt_1h` score `-0.725` n `170` status `ready` deltaP `-0.1286` edge `0.0118` maxDD `-5.9775`
- `market_context_high->metal_1h` score `-0.7514` n `170` status `ready` deltaP `0.3522` edge `0.0117` maxDD `-1.4971`
- `market_context_high->fx_24h` score `-0.8276` n `153` status `ready` deltaP `8.9488` edge `0.0154` maxDD `-3.8554`
- `market_context_high->unknown_24h` score `-1.4186` n `154` status `ready` deltaP `5.4631` edge `0.0566` maxDD `-9.9917`
- `market_context_high->equity_1h` score `-1.4699` n `170` status `ready` deltaP `3.9039` edge `0.0266` maxDD `-14.6193`
- `market_context_high->metal_4h` score `-1.5151` n `170` status `ready` deltaP `0.6959` edge `0.0493` maxDD `-4.8549`
- `market_context_high->crypto_alt_4h` score `-1.9031` n `170` status `ready` deltaP `-0.0879` edge `0.0309` maxDD `-15.2776`
- `market_context_high->fx_4h` score `-2.0046` n `170` status `ready` deltaP `-0.1781` edge `0.0026` maxDD `-2.1439`
- `market_context_high->crypto_major_4h` score `-2.5127` n `170` status `ready` deltaP `4.618` edge `0.0365` maxDD `-23.4879`
- `market_context_high->equity_4h` score `-2.6043` n `170` status `ready` deltaP `2.9286` edge `0.1774` maxDD `-29.4646`
- `market_context_high->index_24h` score `-4.196` n `153` status `ready` deltaP `-19.7604` edge `-0.0083` maxDD `-17.166`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
