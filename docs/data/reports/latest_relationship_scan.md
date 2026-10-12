# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T11:52:31.979432+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7870`

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

- `market_context_high->crypto_alt_24h` score `26.6085` n `42` status `ready` deltaP `30.3819` edge `2.1037` maxDD `-4.7762`
- `market_context_high->crypto_major_24h` score `25.924` n `42` status `ready` deltaP `42.0139` edge `1.9489` maxDD `-3.1591`
- `risk_on_high->crypto_alt_4h` score `3.8676` n `48` status `ready` deltaP `18.1911` edge `0.2458` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.8676` n `48` status `ready` deltaP `18.1911` edge `0.2458` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.4698` n `48` status `ready` deltaP `32.6728` edge `0.3123` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.4698` n `48` status `ready` deltaP `32.6728` edge `0.3123` maxDD `-4.1548`
- `market_context_high->metal_24h` score `2.7036` n `42` status `ready` deltaP `25.6944` edge `0.0885` maxDD `-0.7598`
- `market_context_high->crypto_major_4h` score `2.4389` n `106` status `ready` deltaP `15.7703` edge `0.2759` maxDD `-8.5569`
- `market_context_high->crypto_alt_4h` score `1.9557` n `106` status `ready` deltaP `9.4253` edge `0.2845` maxDD `-11.4155`
- `market_context_high->crypto_alt_1h` score `1.3308` n `106` status `ready` deltaP `10.6626` edge `0.1349` maxDD `-4.9401`
- `market_context_high->index_24h` score `0.9604` n `42` status `ready` deltaP `16.9891` edge `0.0843` maxDD `-0.9544`
- `risk_on_high->crypto_alt_1h` score `0.846` n `48` status `ready` deltaP `5.7884` edge `0.0916` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.846` n `48` status `ready` deltaP `5.7884` edge `0.0916` maxDD `-2.4421`
- `market_context_high->equity_24h` score `0.7244` n `42` status `ready` deltaP `-6.6965` edge `0.3387` maxDD `-11.4282`
- `market_context_high->unknown_4h` score `0.6328` n `106` status `ready` deltaP `-4.415` edge `0.1468` maxDD `-1.8373`
- `market_context_high->crypto_major_1h` score `0.5525` n `106` status `ready` deltaP `4.2227` edge `0.0942` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.3345` n `48` status `ready` deltaP `4.6158` edge `0.0774` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.3345` n `48` status `ready` deltaP `4.6158` edge `0.0774` maxDD `-3.2233`
- `market_context_high->index_1h` score `-0.0297` n `106` status `ready` deltaP `3.9685` edge `0.0028` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1278` n `106` status `ready` deltaP `6.1999` edge `0.0041` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
