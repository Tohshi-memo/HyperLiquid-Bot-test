# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T05:07:27.098738+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `2427.3213` n `42` status `ready` deltaP `20.8581` edge `202.1798` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `13.5231` n `40` status `ready` deltaP `51.4583` edge `0.8236` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0742` n `40` status `ready` deltaP `51.3194` edge `0.5935` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.2904` n `42` status `ready` deltaP `-0.2105` edge `0.2432` maxDD `-3.4427`
- `news_risk_high->index_4h` score `0.7652` n `42` status `ready` deltaP `7.0848` edge `0.0546` maxDD `-0.3783`
- `market_context_high->commodity_1h` score `0.3736` n `47` status `ready` deltaP `7.7143` edge `0.0339` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3263` n `47` status `ready` deltaP `5.0338` edge `0.0929` maxDD `-2.7703`
- `news_risk_high->metal_1h` score `0.1709` n `42` status `ready` deltaP `5.4962` edge `0.0096` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `0.1684` n `42` status `ready` deltaP `11.919` edge `-0.0147` maxDD `-1.4532`
- `market_context_high->fx_4h` score `0.0596` n `47` status `ready` deltaP `14.1801` edge `-0.0039` maxDD `-1.8531`
- `market_context_high->fx_1h` score `-0.0007` n `47` status `ready` deltaP `7.1155` edge `-0.0086` maxDD `-0.7804`
- `news_risk_high->metal_4h` score `-0.0543` n `42` status `ready` deltaP `3.8473` edge `0.0025` maxDD `-0.8085`
- `market_context_high->crypto_alt_4h` score `-0.204` n `47` status `ready` deltaP `2.2963` edge `0.0491` maxDD `-4.9116`
- `news_risk_high->crypto_alt_1h` score `-0.2135` n `42` status `ready` deltaP `5.9595` edge `0.0011` maxDD `-3.1233`
- `news_risk_high->index_1h` score `-0.2255` n `42` status `ready` deltaP `0.4349` edge `0.0005` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.2571` n `42` status `ready` deltaP `-0.5846` edge `0.0032` maxDD `-0.2475`
- `news_risk_high->equity_1h` score `-0.5443` n `42` status `ready` deltaP `-1.3615` edge `0.046` maxDD `-2.916`
- `news_risk_high->fx_24h` score `-0.5943` n `42` status `ready` deltaP `4.5883` edge `0.0256` maxDD `-3.2568`
- `news_risk_high->fx_4h` score `-0.6181` n `42` status `ready` deltaP `-1.4228` edge `0.026` maxDD `-0.6604`
- `news_risk_high->crypto_major_1h` score `-0.6447` n `42` status `ready` deltaP `1.9461` edge `-0.0236` maxDD `-3.762`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
