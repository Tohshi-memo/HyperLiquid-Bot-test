# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T06:37:19.715111+00:00`
- Price records: `672`
- Market context records: `2637`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.5304` n `139` status `ready` deltaP `18.0543` edge `0.54` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.0858` n `139` status `ready` deltaP `24.6622` edge `0.5273` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.4141` n `139` status `ready` deltaP `14.0716` edge `0.3717` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `2.1573` n `139` status `ready` deltaP `5.3457` edge `0.7153` maxDD `-36.0263`
- `market_context_high->index_24h` score `1.2557` n `139` status `ready` deltaP `11.552` edge `0.1257` maxDD `-2.5127`
- `market_context_high->crypto_alt_1h` score `1.1882` n `139` status `ready` deltaP `10.4026` edge `0.1484` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0602` n `139` status `ready` deltaP `7.0539` edge `0.1463` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.6367` n `139` status `ready` deltaP `7.6455` edge `0.1215` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.4351` n `139` status `ready` deltaP `10.2606` edge `0.052` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0713` n `139` status `ready` deltaP `3.5411` edge `0.0246` maxDD `-1.665`
- `market_context_high->index_1h` score `-0.2519` n `139` status `ready` deltaP `2.672` edge `0.0106` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3452` n `139` status `ready` deltaP `5.8448` edge `0.0201` maxDD `-4.3601`
- `market_context_high->metal_4h` score `-0.4188` n `139` status `ready` deltaP `3.4941` edge `0.0293` maxDD `-2.9992`
- `market_context_high->fx_1h` score `-0.5402` n `139` status `ready` deltaP `-0.5676` edge `0.0034` maxDD `-0.2373`
- `market_context_high->metal_1h` score `-0.6568` n `139` status `ready` deltaP `0.3888` edge `0.0066` maxDD `-2.114`
- `market_context_high->fx_24h` score `-0.8588` n `139` status `ready` deltaP `3.4873` edge `-0.002` maxDD `-1.0922`
- `market_context_high->commodity_4h` score `-0.9499` n `139` status `ready` deltaP `4.9625` edge `0.0394` maxDD `-10.2078`
- `market_context_high->fx_4h` score `-0.9631` n `139` status `ready` deltaP `-1.1647` edge `0.0106` maxDD `-0.6474`
- `market_context_high->equity_1h` score `-1.0603` n `139` status `ready` deltaP `-2.6256` edge `0.013` maxDD `-2.7085`
- `market_context_high->equity_4h` score `-1.3108` n `139` status `ready` deltaP `2.2964` edge `0.0159` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
