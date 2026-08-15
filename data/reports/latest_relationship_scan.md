# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T20:52:26.297798+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `167.0914` n `117` status `ready` deltaP `-28.1444` edge `14.3996` maxDD `-9.3486`
- `risk_on_high->unknown_24h` score `33.8609` n `32` status `ready` deltaP `-36.1839` edge `4.6574` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.8609` n `32` status `ready` deltaP `-36.1839` edge `4.6574` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.9719` n `36` status `ready` deltaP `26.6609` edge `0.9412` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.7431` n `36` status `ready` deltaP `39.939` edge `0.379` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.3016` n `117` status `ready` deltaP `36.0722` edge `0.2904` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.4213` n `32` status `ready` deltaP `37.7816` edge `0.1999` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.4213` n `32` status `ready` deltaP `37.7816` edge `0.1999` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.0774` n `32` status `ready` deltaP `27.6809` edge `0.4538` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.0774` n `32` status `ready` deltaP `27.6809` edge `0.4538` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.7209` n `36` status `ready` deltaP `31.1958` edge `0.1021` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9511` n `32` status `ready` deltaP `21.2652` edge `0.1224` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9511` n `32` status `ready` deltaP `21.2652` edge `0.1224` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.025` n `117` status `ready` deltaP `19.2086` edge `0.0878` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.9656` n `36` status `ready` deltaP `22.6626` edge `0.0259` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.749` n `36` status `ready` deltaP `8.2835` edge `0.1224` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3605` n `32` status `ready` deltaP `14.5584` edge `0.0396` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3605` n `32` status `ready` deltaP `14.5584` edge `0.0396` maxDD `-0.1957`
- `risk_on_high->equity_24h` score `0.7856` n `32` status `ready` deltaP `15.2026` edge `0.1773` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `0.7856` n `32` status `ready` deltaP `15.2026` edge `0.1773` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
