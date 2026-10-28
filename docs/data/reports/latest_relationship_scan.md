# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T17:22:36.484064+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8546`

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

- `market_context_high->unknown_24h` score `1274.5307` n `145` status `ready` deltaP `-2.4845` edge `106.3202` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.966` n `149` status `ready` deltaP `4.385` edge `1.8165` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.5195` n `145` status `ready` deltaP `24.7677` edge `0.0303` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1745` n `149` status `ready` deltaP `7.269` edge `0.0019` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.091` n `149` status `ready` deltaP `8.327` edge `0.0075` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.098` n `149` status `ready` deltaP `7.0767` edge `0.0045` maxDD `-0.4545`
- `market_context_high->crypto_major_1h` score `-0.2868` n `149` status `ready` deltaP `7.4288` edge `0.042` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4136` n `149` status `ready` deltaP `7.2015` edge `0.0394` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.4616` n `145` status `ready` deltaP `13.5249` edge `0.0286` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.6632` n `149` status `ready` deltaP `-0.4903` edge `0.0064` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7266` n `149` status `ready` deltaP `-3.3246` edge `-0.0027` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7411` n `149` status `ready` deltaP `9.0563` edge `-0.0013` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.3968` n `149` status `ready` deltaP `1.0891` edge `0.0049` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.4995` n `149` status `ready` deltaP `3.4943` edge `0.0208` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.6687` n `145` status `ready` deltaP `6.9959` edge `0.0274` maxDD `-15.7143`
- `market_context_high->index_4h` score `-3.0468` n `149` status `ready` deltaP `-9.3315` edge `-0.0295` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.1733` n `145` status `ready` deltaP `1.2129` edge `0.0708` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.1832` n `145` status `ready` deltaP `0.9328` edge `0.0235` maxDD `-9.5991`
- `market_context_high->crypto_major_4h` score `-3.3585` n `149` status `ready` deltaP `4.119` edge `-0.0261` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.3259` n `149` status `ready` deltaP `-3.0201` edge `-0.1393` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
