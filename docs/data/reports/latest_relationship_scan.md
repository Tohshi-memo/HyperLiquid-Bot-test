# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T12:52:25.319568+00:00`
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

- `market_context_high->crypto_alt_24h` score `30.5935` n `40` status `ready` deltaP `38.8542` edge `2.3245` maxDD `-1.7253`
- `market_context_high->crypto_major_24h` score `28.5377` n `40` status `ready` deltaP `50.4861` edge `2.0714` maxDD `-1.3864`
- `risk_on_high->crypto_alt_4h` score `3.942` n `48` status `ready` deltaP `18.1911` edge `0.252` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.942` n `48` status `ready` deltaP `18.1911` edge `0.252` maxDD `-1.9151`
- `market_context_high->metal_24h` score `3.6908` n `40` status `ready` deltaP `32.1875` edge `0.1047` maxDD `-0.2709`
- `risk_on_high->crypto_major_4h` score `3.5435` n `48` status `ready` deltaP `33.1301` edge `0.3187` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.5435` n `48` status `ready` deltaP `33.1301` edge `0.3187` maxDD `-4.1548`
- `market_context_high->crypto_alt_4h` score `2.6331` n `102` status `ready` deltaP `11.9411` edge `0.3051` maxDD `-10.8892`
- `market_context_high->crypto_major_4h` score `2.5363` n `102` status `ready` deltaP `15.7281` edge `0.2843` maxDD `-8.5569`
- `market_context_high->crypto_alt_1h` score `1.5514` n `102` status `ready` deltaP `12.3107` edge `0.1423` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.8723` n `48` status `ready` deltaP `5.9381` edge `0.0928` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.8723` n `48` status `ready` deltaP `5.9381` edge `0.0928` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.5758` n `102` status `ready` deltaP `3.8394` edge `0.0987` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.3765` n `48` status `ready` deltaP `5.0649` edge `0.0798` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.3765` n `48` status `ready` deltaP `5.0649` edge `0.0798` maxDD `-3.2233`
- `market_context_high->index_24h` score `0.3287` n `40` status `ready` deltaP `10.6597` edge `0.0578` maxDD `-1.2711`
- `market_context_high->index_1h` score `-0.0225` n `102` status `ready` deltaP `4.1535` edge `0.0025` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.073` n `102` status `ready` deltaP `6.7952` edge `0.0047` maxDD `-0.4868`
- `risk_on_high->metal_1h` score `-0.3267` n `48` status `ready` deltaP `3.1188` edge `0.0039` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.3267` n `48` status `ready` deltaP `3.1188` edge `0.0039` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
