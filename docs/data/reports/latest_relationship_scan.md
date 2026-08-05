# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T12:07:31.565134+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11648`

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

- `market_context_high->unknown_24h` score `13.9699` n `89` status `ready` deltaP `9.2931` edge `1.1065` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4239` n `92` status `ready` deltaP `2.2402` edge `0.5366` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.7891` n `92` status `ready` deltaP `18.4384` edge `0.1108` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.1711` n `89` status `ready` deltaP `27.7076` edge `0.086` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.883` n `89` status `ready` deltaP `1.6268` edge `0.2192` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.4681` n `98` status `ready` deltaP `7.7417` edge `0.029` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.0669` n `92` status `ready` deltaP `13.1363` edge `0.007` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.048` n `98` status `ready` deltaP `6.3394` edge `-0.0033` maxDD `-0.7973`
- `market_context_high->metal_1h` score `-0.5832` n `98` status `ready` deltaP `-2.1783` edge `-0.0108` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6667` n `98` status `ready` deltaP `-1.9614` edge `-0.019` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.9266` n `92` status `ready` deltaP `1.2858` edge `-0.0039` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.9472` n `98` status `ready` deltaP `-4.2863` edge `-0.0218` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.4453` n `89` status `ready` deltaP `0.6768` edge `-0.0455` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.5758` n `92` status `ready` deltaP `-0.8749` edge `-0.0572` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7785` n `98` status `ready` deltaP `2.5144` edge `-0.0912` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1571` n `92` status `ready` deltaP `-13.3219` edge `-0.0623` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.4676` n `89` status `ready` deltaP `-10.7815` edge `-0.025` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.1469` n `98` status `ready` deltaP `4.7477` edge `-0.2492` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6236` n `98` status `ready` deltaP `-13.2653` edge `-0.0762` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.0453` n `89` status `ready` deltaP `10.8243` edge `-0.0322` maxDD `-50.8663`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
