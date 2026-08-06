# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T13:37:34.440084+00:00`
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

- `market_context_high->unknown_24h` score `16.1813` n `100` status `ready` deltaP `3.8611` edge `1.327` maxDD `-0.0104`
- `market_context_high->metal_24h` score `1.3899` n `100` status `ready` deltaP `4.7639` edge `0.2009` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.0418` n `109` status `ready` deltaP `12.5322` edge `0.0879` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.4818` n `100` status `ready` deltaP `20.5417` edge `0.0454` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2908` n `113` status `ready` deltaP `6.5007` edge `0.0225` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0571` n `113` status `ready` deltaP `6.6107` edge `-0.0043` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3472` n `109` status `ready` deltaP `6.4179` edge `-0.0013` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5619` n `113` status `ready` deltaP `-2.2786` edge `-0.0074` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6714` n `109` status `ready` deltaP `4.004` edge `0.0107` maxDD `-3.211`
- `market_context_high->index_1h` score `-1.0882` n `113` status `ready` deltaP `-3.0271` edge `-0.0171` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.2642` n `100` status `ready` deltaP `-4.1528` edge `0.0851` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.3185` n `113` status `ready` deltaP `-3.7226` edge `-0.014` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5899` n `113` status `ready` deltaP `2.692` edge `-0.0653` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.802` n `109` status `ready` deltaP `-9.1618` edge `-0.0445` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.873` n `109` status `ready` deltaP `3.0613` edge `-0.0375` maxDD `-5.7857`
- `market_context_high->crypto_alt_24h` score `-2.7206` n `100` status `ready` deltaP `-4.6667` edge `-0.0513` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-2.9662` n `113` status `ready` deltaP `-8.9926` edge `-0.0499` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.5266` n `100` status `ready` deltaP `7.9306` edge `-0.0131` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-6.6119` n `109` status `ready` deltaP `-1.0517` edge `-0.3118` maxDD `-34.9766`
- `market_context_high->crypto_major_4h` score `-7.6356` n `109` status `ready` deltaP `-7.6513` edge `-0.1641` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
