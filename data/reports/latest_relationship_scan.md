# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T13:22:30.641067+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11781`

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

- `market_context_high->unknown_24h` score `18.5093` n `100` status `ready` deltaP `3.8611` edge `1.521` maxDD `-0.0104`
- `market_context_high->metal_24h` score `1.4122` n `100` status `ready` deltaP `4.9375` edge `0.2016` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.0394` n `109` status `ready` deltaP `12.5322` edge `0.0877` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.4916` n `100` status `ready` deltaP `20.7153` edge `0.0455` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2752` n `113` status `ready` deltaP `6.351` edge `0.0222` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0631` n `113` status `ready` deltaP `6.6107` edge `-0.0038` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3448` n `109` status `ready` deltaP `6.4179` edge `-0.001` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.572` n `113` status `ready` deltaP `-2.4283` edge `-0.0077` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6863` n `109` status `ready` deltaP `3.8516` edge `0.0098` maxDD `-3.211`
- `market_context_high->index_1h` score `-1.105` n `113` status `ready` deltaP `-3.1768` edge `-0.0175` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.2896` n `100` status `ready` deltaP `-4.3264` edge `0.083` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.3269` n `113` status `ready` deltaP `-3.7226` edge `-0.0147` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.6327` n `113` status `ready` deltaP `2.5423` edge `-0.0698` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.8138` n `109` status `ready` deltaP `-9.3142` edge `-0.045` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.873` n `109` status `ready` deltaP `3.0613` edge `-0.0375` maxDD `-5.7857`
- `market_context_high->crypto_alt_24h` score `-2.6923` n `100` status `ready` deltaP `-4.4931` edge `-0.0501` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-2.9926` n `113` status `ready` deltaP `-9.1423` edge `-0.0511` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.5328` n `100` status `ready` deltaP `7.9306` edge `-0.0139` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-6.6581` n `109` status `ready` deltaP `-1.2041` edge `-0.3167` maxDD `-34.9766`
- `market_context_high->crypto_major_4h` score `-7.6742` n `109` status `ready` deltaP `-7.8037` edge `-0.1663` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
