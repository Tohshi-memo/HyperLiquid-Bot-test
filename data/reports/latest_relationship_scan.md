# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T14:22:39.947784+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11797`

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

- `market_context_high->unknown_24h` score `9.1769` n `100` status `ready` deltaP `3.8611` edge `0.7433` maxDD `-0.0104`
- `market_context_high->metal_24h` score `1.3182` n `100` status `ready` deltaP `4.2431` edge `0.1984` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.1131` n `111` status `ready` deltaP `13.243` edge `0.0891` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.472` n `100` status `ready` deltaP `20.3681` edge `0.0453` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3472` n `113` status `ready` deltaP `6.9498` edge `0.0242` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0319` n `113` status `ready` deltaP `6.3113` edge `-0.0044` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3265` n `111` status `ready` deltaP `6.7705` edge `-0.001` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.572` n `113` status `ready` deltaP `-2.4283` edge `-0.0077` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7257` n `111` status `ready` deltaP `3.3207` edge `0.0083` maxDD `-3.211`
- `market_context_high->index_1h` score `-1.0918` n `113` status `ready` deltaP `-3.0271` edge `-0.0174` maxDD `-1.6054`
- `market_context_high->crypto_alt_4h` score `-1.1443` n `111` status `ready` deltaP `3.583` edge `-0.0316` maxDD `-5.7857`
- `market_context_high->index_24h` score `-1.2035` n `100` status `ready` deltaP `-3.6319` edge `0.0894` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.3568` n `113` status `ready` deltaP `-4.022` edge `-0.0152` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.6062` n `113` status `ready` deltaP `2.692` edge `-0.0674` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.7293` n `111` status `ready` deltaP `-8.17` edge `-0.0418` maxDD `-4.7021`
- `market_context_high->crypto_alt_24h` score `-2.8415` n `100` status `ready` deltaP `-5.1875` edge `-0.0579` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-2.9674` n `113` status `ready` deltaP `-8.9926` edge `-0.05` maxDD `-7.6533`
- `market_context_high->equity_4h` score `-6.3701` n `111` status `ready` deltaP `-0.2417` edge `-0.2862` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.5157` n `100` status `ready` deltaP `7.9306` edge `-0.0117` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.5182` n `111` status `ready` deltaP `-7.1729` edge `-0.1575` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
