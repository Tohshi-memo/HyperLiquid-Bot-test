# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T19:37:37.995341+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10365`

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

- `risk_on_high->unknown_24h` score `249.9657` n `103` status `ready` deltaP `25.2124` edge `20.6723` maxDD `-0.1262`
- `risk_on_and_context->unknown_24h` score `249.9657` n `103` status `ready` deltaP `25.2124` edge `20.6723` maxDD `-0.1262`
- `risk_on_high->crypto_major_24h` score `19.9303` n `103` status `ready` deltaP `32.376` edge `1.498` maxDD `-2.2384`
- `risk_on_and_context->crypto_major_24h` score `19.9303` n `103` status `ready` deltaP `32.376` edge `1.498` maxDD `-2.2384`
- `risk_on_high->crypto_alt_24h` score `11.8917` n `103` status `ready` deltaP `24.9747` edge `0.8908` maxDD `-3.3056`
- `risk_on_and_context->crypto_alt_24h` score `11.8917` n `103` status `ready` deltaP `24.9747` edge `0.8908` maxDD `-3.3056`
- `market_context_high->crypto_alt_24h` score `7.2556` n `196` status `ready` deltaP `20.5463` edge `0.5593` maxDD `-4.665`
- `market_context_high->equity_24h` score `6.4377` n `196` status `ready` deltaP `22.0805` edge `0.4039` maxDD `-0.17`
- `risk_on_high->equity_24h` score `5.5712` n `103` status `ready` deltaP `20.6985` edge `0.3409` maxDD `-0.17`
- `risk_on_and_context->equity_24h` score `5.5712` n `103` status `ready` deltaP `20.6985` edge `0.3409` maxDD `-0.17`
- `risk_on_high->index_24h` score `1.8734` n `103` status `ready` deltaP `18.6927` edge `0.0772` maxDD `-0.9893`
- `risk_on_and_context->index_24h` score `1.8734` n `103` status `ready` deltaP `18.6927` edge `0.0772` maxDD `-0.9893`
- `market_context_high->index_24h` score `1.7038` n `196` status `ready` deltaP `19.2673` edge `0.0906` maxDD `-1.4987`
- `risk_on_high->crypto_alt_4h` score `1.6371` n `118` status `ready` deltaP `25.2817` edge `0.2223` maxDD `-17.6868`
- `risk_on_and_context->crypto_alt_4h` score `1.6371` n `118` status `ready` deltaP `25.2817` edge `0.2223` maxDD `-17.6868`
- `risk_on_high->metal_24h` score `0.8894` n `103` status `ready` deltaP `14.7013` edge `0.0921` maxDD `-3.9457`
- `risk_on_and_context->metal_24h` score `0.8894` n `103` status `ready` deltaP `14.7013` edge `0.0921` maxDD `-3.9457`
- `risk_on_high->crypto_alt_1h` score `0.3244` n `129` status `ready` deltaP `3.8516` edge `0.0689` maxDD `-3.7368`
- `risk_on_and_context->crypto_alt_1h` score `0.3244` n `129` status `ready` deltaP `3.8516` edge `0.0689` maxDD `-3.7368`
- `risk_on_high->crypto_major_4h` score `0.1829` n `118` status `ready` deltaP `19.3261` edge `0.1614` maxDD `-19.0001`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
