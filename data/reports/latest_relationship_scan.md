# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T11:22:13.758694+00:00`
- Price records: `672`
- Market context records: `970`
- Flow alert records: `2718`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `15.1236` n `150` status `ready` deltaP `34.5139` edge `1.0636` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `9.5673` n `150` status `ready` deltaP `11.1111` edge `0.7232` maxDD `0.0`
- `market_context_high->equity_24h` score `1.3036` n `150` status `ready` deltaP `0.8264` edge `0.3636` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.6059` n `150` status `ready` deltaP `-0.9444` edge `0.2563` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.2648` n `207` status `ready` deltaP `3.0179` edge `0.0386` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.3579` n `207` status `ready` deltaP `1.6634` edge `0.0011` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.6327` n `207` status `ready` deltaP `1.2815` edge `0.0156` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.6329` n `195` status `ready` deltaP `2.4601` edge `0.0021` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7144` n `207` status `ready` deltaP `3.0779` edge `0.0053` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.0936` n `207` status `ready` deltaP `5.9092` edge `-0.0073` maxDD `-11.4508`
- `market_context_high->unknown_1h` score `-1.2191` n `207` status `ready` deltaP `-1.6228` edge `-0.0136` maxDD `-3.5069`
- `market_context_high->equity_4h` score `-1.4339` n `195` status `ready` deltaP `1.2023` edge `0.0877` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.638` n `195` status `ready` deltaP `-1.2649` edge `0.0242` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8575` n `207` status `ready` deltaP `-1.8477` edge `-0.0299` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.0148` n `207` status `ready` deltaP `0.3703` edge `-0.0264` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.4816` n `195` status `ready` deltaP `9.2104` edge `0.1024` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-2.9586` n `195` status `ready` deltaP `-1.4079` edge `0.0796` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.1585` n `195` status `ready` deltaP `7.9213` edge `-0.1282` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.1923` n `195` status `ready` deltaP `-1.4877` edge `0.0217` maxDD `-15.2248`
- `market_context_high->unknown_24h` score `-4.0034` n `150` status `ready` deltaP `5.0139` edge `0.0039` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
