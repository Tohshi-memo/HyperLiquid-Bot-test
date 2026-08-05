# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T18:07:41.328892+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->unknown_24h` score `13.1361` n `90` status `ready` deltaP `5.4861` edge `1.0624` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.0907` n `100` status `ready` deltaP `0.5` edge `0.4371` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.4873` n `100` status `ready` deltaP `16.0305` edge `0.1017` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.95` n `90` status `ready` deltaP `2.0139` edge `0.2252` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.9254` n `90` status `ready` deltaP `24.7223` edge `0.0744` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4341` n `107` status `ready` deltaP `7.7215` edge `0.0263` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0004` n `107` status `ready` deltaP `5.662` edge `-0.0027` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0356` n `100` status `ready` deltaP `11.0305` edge `0.0079` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5403` n `107` status `ready` deltaP `-1.9685` edge `-0.0067` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7667` n `100` status `ready` deltaP `2.7866` edge `0.0066` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.7726` n `107` status `ready` deltaP `-4.0279` edge `-0.0188` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.9038` n `107` status `ready` deltaP `-4.0965` edge `-0.0175` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.4218` n `90` status `ready` deltaP `0.9027` edge `-0.044` maxDD `-4.5445`
- `market_context_high->equity_1h` score `-1.7531` n `107` status `ready` deltaP `1.802` edge `-0.0832` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0784` n `100` status `ready` deltaP `-11.8232` edge `-0.0622` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.492` n `90` status `ready` deltaP `-11.25` edge `-0.025` maxDD `-7.8922`
- `market_context_high->crypto_alt_4h` score `-2.7021` n `100` status `ready` deltaP `-1.9634` edge `-0.0731` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-3.2657` n `107` status `ready` deltaP `-10.7113` edge `-0.0634` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.5571` n `107` status `ready` deltaP `2.1098` edge `-0.2658` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.026` n `90` status `ready` deltaP `11.007` edge `-0.0245` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
