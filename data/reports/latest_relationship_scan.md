# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T12:07:31.302306+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11750`

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

- `market_context_high->equity_4h` score `1.9581` n `96` status `ready` deltaP `10.8485` edge `0.1797` maxDD `-2.4411`
- `market_context_high->crypto_major_24h` score `1.922` n `96` status `ready` deltaP `5.9027` edge `0.2416` maxDD `-4.9964`
- `market_context_high->equity_1h` score `1.7613` n `96` status `ready` deltaP `14.7019` edge `0.0789` maxDD `-0.4112`
- `market_context_high->metal_4h` score `1.2592` n `96` status `ready` deltaP `18.2418` edge `0.0409` maxDD `-1.273`
- `market_context_high->index_1h` score `0.9546` n `96` status `ready` deltaP `16.2113` edge `0.0102` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.9011` n `96` status `ready` deltaP `10.5437` edge `0.1069` maxDD `-3.1677`
- `market_context_high->commodity_24h` score `0.8092` n `96` status `ready` deltaP `11.1111` edge `0.213` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.2343` n `96` status `ready` deltaP `17.7083` edge `-0.0479` maxDD `-1.0505`
- `market_context_high->metal_1h` score `0.1716` n `96` status `ready` deltaP `6.119` edge `0.0122` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `0.1617` n `96` status `ready` deltaP `7.8593` edge `-0.0162` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.1404` n `96` status `ready` deltaP `9.3242` edge `0.0061` maxDD `-0.3539`
- `market_context_high->index_4h` score `0.1336` n `96` status `ready` deltaP `8.1046` edge `0.0226` maxDD `-0.5728`
- `market_context_high->crypto_alt_4h` score `0.045` n `96` status `ready` deltaP `8.8415` edge `0.0718` maxDD `-5.4926`
- `market_context_high->fx_1h` score `-0.3097` n `96` status `ready` deltaP `-1.023` edge `0.003` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.3339` n `96` status `ready` deltaP `3.5803` edge `0.0178` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.4346` n `96` status `ready` deltaP `1.9274` edge `0.0116` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.5718` n `96` status `ready` deltaP `0.8893` edge `0.0058` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.883` n `96` status `ready` deltaP `-7.5911` edge `-0.006` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2175` n `96` status `ready` deltaP `-3.6458` edge `0.0708` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.9326` n `96` status `ready` deltaP `-22.3958` edge `-0.0201` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
