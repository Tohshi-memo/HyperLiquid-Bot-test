# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T17:52:29.562609+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8174`

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

- `market_context_high->unknown_24h` score `1381.1376` n `40` status `ready` deltaP `-20.6597` edge `115.2689` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `57.7255` n `80` status `ready` deltaP `-6.4634` edge `4.9116` maxDD `-2.3109`
- `market_context_high->unknown_1h` score `10.1699` n `92` status `ready` deltaP `-2.5774` edge `0.8983` maxDD `-1.0231`
- `market_context_high->equity_24h` score `8.8008` n `40` status `ready` deltaP `27.6736` edge `0.5918` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.3868` n `40` status `ready` deltaP `52.4306` edge `0.1827` maxDD `0.0`
- `market_context_high->fx_24h` score `3.3005` n `40` status `ready` deltaP `37.2917` edge `0.0394` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.6069` n `40` status `ready` deltaP `-20.5903` edge `0.586` maxDD `-17.8526`
- `market_context_high->crypto_alt_1h` score `0.7921` n `92` status `ready` deltaP `8.1034` edge `0.1154` maxDD `-4.9401`
- `market_context_high->fx_4h` score `0.7776` n `80` status `ready` deltaP `12.7744` edge `0.008` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.2822` n `80` status `ready` deltaP `9.878` edge `0.011` maxDD `-1.6002`
- `market_context_high->crypto_major_1h` score `-0.016` n `92` status `ready` deltaP `1.7639` edge `0.0758` maxDD `-3.7778`
- `market_context_high->fx_1h` score `-0.0484` n `92` status `ready` deltaP `2.8183` edge `0.0014` maxDD `-0.271`
- `market_context_high->commodity_1h` score `-0.0868` n `92` status `ready` deltaP `2.4798` edge `0.0046` maxDD `-0.6025`
- `market_context_high->metal_1h` score `-0.0975` n `92` status `ready` deltaP `6.9383` edge `0.0045` maxDD `-0.7107`
- `market_context_high->metal_4h` score `-0.2896` n `80` status `ready` deltaP `4.1159` edge `0.0207` maxDD `-1.1153`
- `market_context_high->crypto_major_4h` score `-0.3848` n `80` status `ready` deltaP `-1.6463` edge `0.1722` maxDD `-11.1784`
- `market_context_high->index_1h` score `-0.629` n `92` status `ready` deltaP `-2.0958` edge `-0.0016` maxDD `-0.5392`
- `market_context_high->crypto_alt_4h` score `-0.7347` n `80` status `ready` deltaP `-5.1829` edge `0.1962` maxDD `-13.8008`
- `market_context_high->index_4h` score `-0.8012` n `80` status `ready` deltaP `-5.3963` edge `0.0033` maxDD `-0.9364`
- `market_context_high->equity_1h` score `-0.9069` n `92` status `ready` deltaP `-4.862` edge `0.0031` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
