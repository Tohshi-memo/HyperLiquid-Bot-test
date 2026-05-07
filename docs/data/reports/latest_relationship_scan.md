# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T22:07:20.052128+00:00`
- Price records: `588`
- Market context records: `689`
- Flow alert records: `1950`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `9.9596` n `146` status `ready` deltaP `24.5044` edge `0.7` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6001` n `146` status `ready` deltaP `8.4614` edge `0.4984` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1988` n `148` status `ready` deltaP `7.4039` edge `0.0123` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2698` n `149` status `ready` deltaP `3.0629` edge `0.0028` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5582` n `149` status `ready` deltaP `1.9243` edge `0.0381` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5586` n `149` status `ready` deltaP `1.2648` edge `0.0053` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1006` n `149` status `ready` deltaP `-1.303` edge `-0.002` maxDD `-4.4826`
- `market_context_high->crypto_major_4h` score `-1.1941` n `148` status `ready` deltaP `15.5263` edge `0.114` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.2298` n `149` status `ready` deltaP `-4.4176` edge `-0.0127` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3728` n `149` status `ready` deltaP `4.5256` edge `-0.0131` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.5761` n `148` status `ready` deltaP `3.2737` edge `-0.0009` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6512` n `149` status `ready` deltaP `5.8208` edge `-0.0041` maxDD `-11.4508`
- `market_context_high->index_24h` score `-1.697` n `146` status `ready` deltaP `-5.1314` edge `0.0923` maxDD `-5.9609`
- `market_context_high->crypto_alt_4h` score `-1.9542` n `148` status `ready` deltaP `4.4887` edge `0.0642` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.6115` n `148` status `ready` deltaP `-1.1277` edge `0.0051` maxDD `-10.5498`
- `market_context_high->equity_24h` score `-3.0713` n `146` status `ready` deltaP `-7.2395` edge `0.0528` maxDD `-10.5047`
- `market_context_high->metal_1h` score `-3.2645` n `149` status `ready` deltaP `-4.4865` edge `-0.0462` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7813` n `148` status `ready` deltaP `-6.0621` edge `0.0754` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.4847` n `148` status `ready` deltaP `2.1735` edge `-0.2004` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.895` n `146` status `ready` deltaP `-10.1673` edge `-0.0426` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
