# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T13:52:34.954605+00:00`
- Price records: `672`
- Market context records: `4522`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9771`

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

- `risk_on_high->unknown_4h` score `156.9363` n `41` status `ready` deltaP `17.0732` edge `13.0833` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `156.9363` n `41` status `ready` deltaP `17.0732` edge `13.0833` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `48.2944` n `188` status `ready` deltaP `6.3766` edge `4.0404` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `28.2299` n `188` status `ready` deltaP `8.1733` edge `2.4546` maxDD `-7.5275`
- `risk_on_high->crypto_major_4h` score `7.076` n `41` status `ready` deltaP `38.5671` edge `0.3419` maxDD `-0.0812`
- `risk_on_and_context->crypto_major_4h` score `7.076` n `41` status `ready` deltaP `38.5671` edge `0.3419` maxDD `-0.0812`
- `risk_on_high->unknown_24h` score `5.6616` n `41` status `ready` deltaP `17.5347` edge `0.3549` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5.6616` n `41` status `ready` deltaP `17.5347` edge `0.3549` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.3196` n `41` status `ready` deltaP `42.2256` edge `0.1618` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.3196` n `41` status `ready` deltaP `42.2256` edge `0.1618` maxDD `0.0`
- `risk_on_high->metal_24h` score `3.5319` n `41` status `ready` deltaP `-7.3298` edge `0.5996` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `3.5319` n `41` status `ready` deltaP `-7.3298` edge `0.5996` maxDD `-4.834`
- `risk_on_high->crypto_major_1h` score `2.0916` n `41` status `ready` deltaP `13.3088` edge `0.1073` maxDD `-0.7379`
- `risk_on_and_context->crypto_major_1h` score `2.0916` n `41` status `ready` deltaP `13.3088` edge `0.1073` maxDD `-0.7379`
- `risk_on_high->equity_1h` score `1.9964` n `41` status `ready` deltaP `20.3703` edge `0.0503` maxDD `-0.2457`
- `risk_on_and_context->equity_1h` score `1.9964` n `41` status `ready` deltaP `20.3703` edge `0.0503` maxDD `-0.2457`
- `risk_on_high->crypto_alt_4h` score `1.6245` n `41` status `ready` deltaP `9.1463` edge `0.131` maxDD `-1.8615`
- `risk_on_and_context->crypto_alt_4h` score `1.6245` n `41` status `ready` deltaP `9.1463` edge `0.131` maxDD `-1.8615`
- `risk_on_high->metal_4h` score `1.3999` n `41` status `ready` deltaP `16.311` edge `0.1043` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.3999` n `41` status `ready` deltaP `16.311` edge `0.1043` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
