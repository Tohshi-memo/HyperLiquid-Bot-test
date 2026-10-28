# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T16:55:03.774455+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8506`

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

- `market_context_high->unknown_24h` score `1319.9458` n `143` status `ready` deltaP `-2.7256` edge `110.1064` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `22.074` n `149` status `ready` deltaP `4.385` edge `1.8255` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.518` n `143` status `ready` deltaP `24.8835` edge `0.0294` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1745` n `149` status `ready` deltaP `7.269` edge `0.0019` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0677` n `149` status `ready` deltaP `7.3815` edge `0.005` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0816` n `149` status `ready` deltaP `8.4767` edge `0.0077` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.2752` n `149` status `ready` deltaP `7.5785` edge `0.0425` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4076` n `149` status `ready` deltaP `7.2015` edge `0.0399` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.5134` n `143` status `ready` deltaP `13.2066` edge `0.0264` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.6932` n `149` status `ready` deltaP `-0.7897` edge `0.0059` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7266` n `149` status `ready` deltaP `-3.3246` edge `-0.0027` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7419` n `149` status `ready` deltaP `9.0563` edge `-0.0014` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.3859` n `149` status `ready` deltaP `1.2388` edge `0.0053` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5112` n `149` status `ready` deltaP `3.3446` edge `0.0203` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.694` n `143` status `ready` deltaP `6.8898` edge `0.026` maxDD `-15.7143`
- `market_context_high->index_4h` score `-3.0176` n `149` status `ready` deltaP `-9.0267` edge `-0.0291` maxDD `-5.6417`
- `market_context_high->metal_24h` score `-3.0518` n `143` status `ready` deltaP `1.5018` edge `0.026` maxDD `-9.2264`
- `market_context_high->crypto_major_24h` score `-3.127` n `143` status `ready` deltaP `1.7434` edge `0.0732` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.3554` n `149` status `ready` deltaP `4.119` edge `-0.0257` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.3078` n `149` status `ready` deltaP `-2.8677` edge `-0.138` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
