# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T00:52:15.969289+00:00`
- Price records: `503`
- Market context records: `597`
- Flow alert records: `1688`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.5325` n `146` status `ready` deltaP `6.9318` edge `0.3363` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.5256` n `146` status `ready` deltaP `10.454` edge `0.2575` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0567` n `146` status `ready` deltaP `11.2213` edge `0.0196` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3217` n `146` status `ready` deltaP `1.8998` edge `0.0039` maxDD `-0.291`
- `market_context_high->index_1h` score `-0.6362` n `146` status `ready` deltaP `0.9589` edge `-0.0026` maxDD `-2.8282`
- `market_context_high->commodity_1h` score `-0.6609` n `146` status `ready` deltaP `1.0765` edge `0.0352` maxDD `-3.7959`
- `market_context_high->unknown_1h` score `-1.1309` n `146` status `ready` deltaP `-3.9915` edge `-0.0073` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2056` n `146` status `ready` deltaP `5.2654` edge `-0.0041` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2114` n `146` status `ready` deltaP `-1.6674` edge `-0.0088` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.8069` n `146` status `ready` deltaP `4.8796` edge `-0.0108` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0754` n `146` status `ready` deltaP `3.3346` edge `0.0618` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2023` n `146` status `ready` deltaP `0.4722` edge `-0.0344` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.4499` n `146` status `ready` deltaP `-6.7422` edge `0.0403` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-2.7492` n `146` status `ready` deltaP `12.7802` edge `0.0563` maxDD `-22.648`
- `market_context_high->equity_4h` score `-3.24` n `146` status `ready` deltaP `-3.2545` edge `-0.0331` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2895` n `146` status `ready` deltaP `-4.5749` edge `-0.0477` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8364` n `146` status `ready` deltaP `-7.5753` edge `0.0809` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.3466` n `146` status `ready` deltaP `-3.491` edge `-0.0168` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.4732` n `146` status `ready` deltaP `-10.5136` edge `-0.0422` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-5.0322` n `146` status `ready` deltaP `0.8649` edge `-0.2373` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
