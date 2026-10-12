# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T09:22:32.840420+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8290`

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

- `market_context_high->unknown_4h` score `33.929` n `116` status `ready` deltaP `-2.7071` edge `2.9101` maxDD `-1.8373`
- `market_context_high->crypto_major_24h` score `12.3233` n `49` status `ready` deltaP `25.7228` edge `1.6167` maxDD `-10.995`
- `market_context_high->crypto_alt_24h` score `10.8164` n `49` status `ready` deltaP `14.0908` edge `1.5663` maxDD `-16.2148`
- `risk_on_high->crypto_alt_4h` score `3.738` n `48` status `ready` deltaP `18.1911` edge `0.235` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.738` n `48` status `ready` deltaP `18.1911` edge `0.235` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.4269` n `48` status `ready` deltaP `32.6728` edge `0.3068` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.4269` n `48` status `ready` deltaP `32.6728` edge `0.3068` maxDD `-4.1548`
- `market_context_high->equity_24h` score `2.8498` n `49` status `ready` deltaP `6.5334` edge `0.4621` maxDD `-7.5571`
- `market_context_high->index_24h` score `1.9033` n `49` status `ready` deltaP `27.1578` edge `0.119` maxDD `-0.4833`
- `market_context_high->unknown_1h` score `1.1878` n `116` status `ready` deltaP `-5.8022` edge `0.1713` maxDD `-1.024`
- `market_context_high->crypto_alt_1h` score `0.7898` n `116` status `ready` deltaP `7.3508` edge `0.1119` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.768` n `48` status `ready` deltaP `5.3393` edge `0.0881` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.768` n `48` status `ready` deltaP `5.3393` edge `0.0881` maxDD `-2.4421`
- `market_context_high->crypto_major_4h` score `0.7136` n `116` status `ready` deltaP `10.4027` edge `0.2327` maxDD `-11.1784`
- `risk_on_high->crypto_major_1h` score `0.3072` n `48` status `ready` deltaP `4.3164` edge `0.0759` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.3072` n `48` status `ready` deltaP `4.3164` edge `0.0759` maxDD `-3.2233`
- `market_context_high->crypto_major_1h` score `0.1765` n `116` status `ready` deltaP `2.7359` edge `0.0807` maxDD `-3.4384`
- `market_context_high->metal_24h` score `0.0447` n `49` status `ready` deltaP `9.2297` edge `0.0419` maxDD `-2.4822`
- `market_context_high->crypto_alt_4h` score `0.0351` n `116` status `ready` deltaP `3.8951` edge `0.2328` maxDD `-13.8008`
- `market_context_high->metal_1h` score `-0.1679` n `116` status `ready` deltaP `5.5493` edge `0.0051` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
