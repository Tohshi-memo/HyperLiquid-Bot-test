# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T17:52:58.173689+00:00`
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

- `market_context_high->unknown_24h` score `13.168` n `90` status `ready` deltaP `5.6597` edge `1.0639` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.0979` n `100` status `ready` deltaP `0.5` edge `0.4377` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.4873` n `100` status `ready` deltaP `16.0305` edge `0.1017` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.95` n `90` status `ready` deltaP `2.0139` edge `0.2252` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.9301` n `90` status `ready` deltaP `24.7223` edge `0.075` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4353` n `107` status `ready` deltaP `7.7215` edge `0.0264` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0116` n `107` status `ready` deltaP `5.5123` edge `-0.0027` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0443` n `100` status `ready` deltaP `10.878` edge `0.0078` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5458` n `107` status `ready` deltaP `-1.9685` edge `-0.0074` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7667` n `100` status `ready` deltaP `2.7866` edge `0.0066` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.7765` n `107` status `ready` deltaP `-4.0279` edge `-0.0193` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.91` n `107` status `ready` deltaP `-4.0965` edge `-0.0183` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.4172` n `90` status `ready` deltaP `0.9027` edge `-0.0434` maxDD `-4.5445`
- `market_context_high->equity_1h` score `-1.7687` n `107` status `ready` deltaP `1.802` edge `-0.0852` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0745` n `100` status `ready` deltaP `-11.8232` edge `-0.0617` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.5073` n `90` status `ready` deltaP `-11.4237` edge `-0.0258` maxDD `-7.8922`
- `market_context_high->crypto_alt_4h` score `-2.6671` n `100` status `ready` deltaP `-1.811` edge `-0.0712` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-3.2717` n `107` status `ready` deltaP `-10.7113` edge `-0.0639` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.5559` n `107` status `ready` deltaP `2.1098` edge `-0.2657` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0253` n `90` status `ready` deltaP `11.007` edge `-0.0244` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
