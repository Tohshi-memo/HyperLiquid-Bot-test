# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T10:07:13.449141+00:00`
- Price records: `540`
- Market context records: `636`
- Flow alert records: `1801`
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

- `market_context_high->crypto_major_24h` score `6.0862` n `146` status `ready` deltaP `17.2313` edge `0.4257` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.5175` n `146` status `ready` deltaP `7.6484` edge `0.4136` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.0991` n `146` status `ready` deltaP `8.7961` edge `0.0158` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3352` n `146` status `ready` deltaP `1.7741` edge `0.003` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4917` n `146` status `ready` deltaP `2.0805` edge `0.0426` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6905` n `146` status `ready` deltaP `-0.1313` edge `-0.0023` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1536` n `146` status `ready` deltaP `-4.2297` edge `-0.0076` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.1999` n `146` status `ready` deltaP `5.8015` edge `-0.0072` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3506` n `146` status `ready` deltaP `-2.7629` edge `-0.0131` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7063` n `146` status `ready` deltaP `5.6711` edge `-0.0077` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0982` n `146` status `ready` deltaP `3.9789` edge `0.0556` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.384` n `146` status `ready` deltaP `-1.47` edge `-0.0366` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.5537` n `146` status `ready` deltaP `13.1392` edge `0.0702` maxDD `-22.648`
- `market_context_high->index_24h` score `-3.0471` n `146` status `ready` deltaP `-8.5367` edge `0.0025` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.3802` n `146` status `ready` deltaP `-5.3688` edge `0.1042` maxDD `-13.0076`
- `market_context_high->metal_1h` score `-3.4518` n `146` status `ready` deltaP `-5.2827` edge `-0.0565` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.4684` n `146` status `ready` deltaP `-4.3546` edge `-0.0448` maxDD `-10.5498`
- `market_context_high->fx_24h` score `-4.3528` n `146` status `ready` deltaP `-3.5056` edge `-0.0175` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.8002` n `146` status `ready` deltaP `1.4849` edge `-0.2221` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.9079` n `146` status `ready` deltaP `-11.703` edge `-0.0705` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
