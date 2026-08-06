# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T13:52:26.264474+00:00`
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

- `market_context_high->unknown_24h` score `13.8509` n `100` status `ready` deltaP `3.8611` edge `1.1328` maxDD `-0.0104`
- `market_context_high->metal_24h` score `1.3664` n `100` status `ready` deltaP `4.5903` edge `0.2001` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.0454` n `109` status `ready` deltaP `12.5322` edge `0.0882` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.472` n `100` status `ready` deltaP `20.3681` edge `0.0453` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3088` n `113` status `ready` deltaP `6.6504` edge `0.023` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0439` n `113` status `ready` deltaP `6.461` edge `-0.0044` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3559` n `109` status `ready` deltaP `6.2654` edge `-0.0014` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5533` n `113` status `ready` deltaP `-2.1289` edge `-0.0073` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.658` n `109` status `ready` deltaP `4.1565` edge `0.0114` maxDD `-3.211`
- `market_context_high->index_1h` score `-1.0858` n `113` status `ready` deltaP `-3.0271` edge `-0.0169` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.238` n `100` status `ready` deltaP `-3.9792` edge `0.0873` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.3137` n `113` status `ready` deltaP `-3.7226` edge `-0.0136` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5688` n `113` status `ready` deltaP `2.692` edge `-0.0626` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.7996` n `109` status `ready` deltaP `-9.1618` edge `-0.0442` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.8754` n `109` status `ready` deltaP `3.0613` edge `-0.0377` maxDD `-5.7857`
- `market_context_high->crypto_alt_24h` score `-2.7465` n `100` status `ready` deltaP `-4.8403` edge `-0.0523` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-2.9566` n `113` status `ready` deltaP `-8.9926` edge `-0.0491` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.5196` n `100` status `ready` deltaP `7.9306` edge `-0.0122` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-6.5878` n `109` status `ready` deltaP `-1.0517` edge `-0.3087` maxDD `-34.9766`
- `market_context_high->crypto_major_4h` score `-7.603` n `109` status `ready` deltaP `-7.4989` edge `-0.1624` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
