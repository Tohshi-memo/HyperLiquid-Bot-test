# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T15:07:33.230887+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8508`

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

- `market_context_high->unknown_24h` score `1490.3615` n `136` status `ready` deltaP `-3.6255` edge `124.3137` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `22.1328` n `149` status `ready` deltaP `4.385` edge `1.8304` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.4957` n `136` status `ready` deltaP `25.2348` edge `0.0252` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1757` n `149` status `ready` deltaP `7.269` edge `0.002` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0211` n `149` status `ready` deltaP `8.2962` edge `0.0063` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0621` n `149` status `ready` deltaP `8.7761` edge `0.0082` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.2549` n `149` status `ready` deltaP `7.8779` edge `0.0431` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.375` n `149` status `ready` deltaP `7.3539` edge `0.0416` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.5135` n `136` status `ready` deltaP `11.0703` edge `0.0176` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.7039` n `149` status `ready` deltaP `-0.9394` edge `0.006` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7102` n `149` status `ready` deltaP `-3.0252` edge `-0.0026` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7332` n `149` status `ready` deltaP `9.2088` edge `-0.0013` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.3696` n `149` status `ready` deltaP `1.3885` edge `0.0064` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5159` n `149` status `ready` deltaP `3.1949` edge `0.0207` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-2.6392` n `136` status `ready` deltaP `3.6255` edge `0.0337` maxDD `-8.2244`
- `market_context_high->index_4h` score `-2.9592` n `149` status `ready` deltaP `-8.4169` edge `-0.0283` maxDD `-5.6417`
- `market_context_high->equity_24h` score `-2.9757` n `136` status `ready` deltaP `6.4134` edge `0.0057` maxDD `-15.7143`
- `market_context_high->crypto_major_24h` score `-3.2437` n `136` status `ready` deltaP `0.9089` edge `0.0638` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.4061` n `149` status `ready` deltaP `4.119` edge `-0.0322` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.3156` n `149` status `ready` deltaP `-2.8677` edge `-0.139` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
