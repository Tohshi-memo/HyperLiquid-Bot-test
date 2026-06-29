# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T02:52:29.227175+00:00`
- Price records: `672`
- Market context records: `5103`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10340`

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

- `market_context_high->unknown_24h` score `18.819` n `79` status `ready` deltaP `27.7206` edge `1.4177` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `8.272` n `110` status `ready` deltaP `22.5526` edge `0.6412` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `6.6525` n `122` status `ready` deltaP `3.9487` edge `0.5922` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `2.9564` n `110` status `ready` deltaP `14.1214` edge `0.4448` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.2791` n `110` status `ready` deltaP `12.4556` edge `0.4384` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.7342` n `110` status `ready` deltaP `9.0964` edge `0.1633` maxDD `-6.3852`
- `market_context_high->crypto_alt_1h` score `0.559` n `122` status `ready` deltaP `7.5341` edge `0.1176` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.4457` n `122` status `ready` deltaP `8.3685` edge `0.1259` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.4201` n `122` status `ready` deltaP `8.2752` edge `0.058` maxDD `-2.745`
- `market_context_high->metal_1h` score `0.3327` n `122` status `ready` deltaP `9.3305` edge `0.0301` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.0768` n `122` status `ready` deltaP `4.3978` edge `0.0112` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.1613` n `110` status `ready` deltaP `5.6347` edge `0.0309` maxDD `-2.132`
- `market_context_high->metal_4h` score `-0.4055` n `110` status `ready` deltaP `3.6807` edge `0.0645` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.8388` n `122` status `ready` deltaP `-6.3218` edge `-0.0013` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.886` n `122` status `ready` deltaP `0.3068` edge `-0.0001` maxDD `-2.062`
- `market_context_high->fx_24h` score `-1.6233` n `79` status `ready` deltaP `-3.837` edge `-0.0085` maxDD `-1.7626`
- `market_context_high->commodity_24h` score `-1.6745` n `79` status `ready` deltaP `7.7004` edge `0.0302` maxDD `-15.0303`
- `market_context_high->fx_4h` score `-1.8372` n `110` status `ready` deltaP `-6.2112` edge `-0.0044` maxDD `-1.9169`
- `market_context_high->commodity_4h` score `-2.1663` n `110` status `ready` deltaP `2.0205` edge `-0.0231` maxDD `-7.3384`
- `market_context_high->metal_24h` score `-4.5519` n `79` status `ready` deltaP `-6.5995` edge `0.0059` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
