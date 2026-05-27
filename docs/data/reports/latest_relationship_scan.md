# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T04:37:19.661461+00:00`
- Price records: `672`
- Market context records: `2008`
- Flow alert records: `7673`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9107`

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

- `market_context_high->crypto_major_4h` score `8.8458` n `211` status `ready` deltaP `30.6822` edge `0.5856` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.2756` n `211` status `ready` deltaP `24.4047` edge `0.6414` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.6823` n `211` status `ready` deltaP `18.8006` edge `0.4231` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.7454` n `211` status `ready` deltaP `15.8154` edge `0.2328` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5214` n `211` status `ready` deltaP `12.4344` edge `0.1425` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.2127` n `211` status `ready` deltaP `9.8895` edge `0.1465` maxDD `-4.9097`
- `market_context_high->index_4h` score `1.1628` n `211` status `ready` deltaP `11.1092` edge `0.0912` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `1.1047` n `185` status `ready` deltaP `15.6599` edge `0.5197` maxDD `-35.8966`
- `market_context_high->metal_24h` score `0.7296` n `185` status `ready` deltaP `14.1596` edge `0.209` maxDD `-12.7414`
- `market_context_high->equity_24h` score `0.5332` n `185` status `ready` deltaP `14.4715` edge `0.4378` maxDD `-33.1875`
- `market_context_high->fx_24h` score `0.4489` n `185` status `ready` deltaP `15.5257` edge `0.028` maxDD `-1.8611`
- `market_context_high->equity_1h` score `0.0677` n `211` status `ready` deltaP `5.8469` edge `0.0455` maxDD `-2.6402`
- `market_context_high->index_24h` score `-0.0723` n `185` status `ready` deltaP `2.7472` edge `0.0985` maxDD `-4.1604`
- `market_context_high->index_1h` score `-0.4487` n `211` status `ready` deltaP `1.2076` edge `0.0136` maxDD `-1.3898`
- `market_context_high->unknown_1h` score `-0.6325` n `211` status `ready` deltaP `3.6531` edge `-0.0051` maxDD `-3.0902`
- `market_context_high->fx_1h` score `-0.7953` n `211` status `ready` deltaP `-0.6612` edge `0.0009` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.0302` n `211` status `ready` deltaP `-6.3346` edge `-0.0017` maxDD `-1.0513`
- `market_context_high->metal_1h` score `-1.1012` n `211` status `ready` deltaP `2.6811` edge `0.0091` maxDD `-5.166`
- `market_context_high->crypto_major_24h` score `-1.2369` n `185` status `ready` deltaP `17.836` edge `0.6366` maxDD `-62.3533`
- `market_context_high->metal_4h` score `-1.6276` n `211` status `ready` deltaP `6.9053` edge `0.0806` maxDD `-11.9812`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
