# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T10:37:26.218925+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11807`

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

- `market_context_high->unknown_24h` score `3089.183` n `113` status `ready` deltaP `13.6815` edge `257.3459` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.2477` n `82` status `ready` deltaP `-3.4541` edge `32.0025` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.4034` n `59` status `ready` deltaP `54.505` edge `1.7603` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `20.9881` n `64` status `ready` deltaP `40.7986` edge `1.5` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.9881` n `64` status `ready` deltaP `40.7986` edge `1.5` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `17.7065` n `113` status `ready` deltaP `34.4518` edge `1.3286` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.6134` n `59` status `ready` deltaP `29.967` edge `1.3168` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.2291` n `59` status `ready` deltaP `33.9366` edge `0.8027` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0329` n `64` status `ready` deltaP `37.3264` edge `0.5039` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0329` n `64` status `ready` deltaP `37.3264` edge `0.5039` maxDD `0.0`
- `market_context_high->equity_24h` score `8.7065` n `113` status `ready` deltaP `37.3264` edge `0.4767` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.3734` n `59` status `ready` deltaP `53.4722` edge `0.3413` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.2014` n `64` status `ready` deltaP `42.378` edge `0.4381` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.2014` n `64` status `ready` deltaP `42.378` edge `0.4381` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.9105` n `59` status `ready` deltaP `51.4713` edge `0.3254` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.9675` n `64` status `ready` deltaP `50.1736` edge `0.0837` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.9675` n `64` status `ready` deltaP `50.1736` edge `0.0837` maxDD `-0.0051`
- `risk_on_high->crypto_major_4h` score `4.8859` n `64` status `ready` deltaP `24.6189` edge `0.3289` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8859` n `64` status `ready` deltaP `24.6189` edge `0.3289` maxDD `-3.8693`
- `risk_on_high->equity_4h` score `4.2155` n `64` status `ready` deltaP `38.5671` edge `0.1035` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
