# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T13:52:29.264621+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12058`

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

- `market_context_high->unknown_24h` score `4754.3218` n `100` status `ready` deltaP `13.4514` edge `396.109` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `1892.1385` n `53` status `ready` deltaP `15.4514` edge `157.5752` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `1892.1385` n `53` status `ready` deltaP `15.4514` edge `157.5752` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.2779` n `82` status `ready` deltaP `-4.8014` edge `32.014` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.6136` n `59` status `ready` deltaP `54.8522` edge `1.7755` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `18.0979` n `53` status `ready` deltaP `39.3507` edge `1.2688` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `18.0979` n `53` status `ready` deltaP `39.3507` edge `1.2688` maxDD `-0.8386`
- `news_risk_high->crypto_alt_24h` score `17.6681` n `59` status `ready` deltaP `30.1406` edge `1.3202` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `15.6819` n `100` status `ready` deltaP `32.7847` edge `1.171` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `12.433` n `59` status `ready` deltaP `34.8046` edge `0.8139` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `8.9488` n `53` status `ready` deltaP `38.1944` edge `0.4911` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.9488` n `53` status `ready` deltaP `38.1944` edge `0.4911` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.7234` n `53` status `ready` deltaP `42.6628` edge `0.4797` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.7234` n `53` status `ready` deltaP `42.6628` edge `0.4797` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.692` n `100` status `ready` deltaP `38.1944` edge `0.4697` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.4759` n `59` status `ready` deltaP `54.5139` edge `0.3429` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9383` n `59` status `ready` deltaP `51.8185` edge `0.3254` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.8671` n `53` status `ready` deltaP `49.5479` edge `0.0795` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8671` n `53` status `ready` deltaP `49.5479` edge `0.0795` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.1825` n `53` status `ready` deltaP `37.2699` edge `0.1094` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
