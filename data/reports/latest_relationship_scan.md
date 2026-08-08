# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T15:52:33.808512+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11573`

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

- `market_context_high->equity_24h` score `3.4343` n `99` status `ready` deltaP `3.8668` edge `0.5664` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.4726` n `99` status `ready` deltaP `11.3321` edge `0.1881` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4812` n `103` status `ready` deltaP `14.1339` edge `0.0965` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.0883` n `99` status `ready` deltaP `25.3788` edge `0.057` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `1.0094` n `103` status `ready` deltaP `11.6868` edge `0.0405` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.3939` n `99` status `ready` deltaP `8.0019` edge `0.1503` maxDD `-5.9181`
- `market_context_high->equity_1h` score `-0.4664` n `103` status `ready` deltaP `3.449` edge `0.021` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.4998` n `103` status `ready` deltaP `2.0551` edge `-0.0058` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5131` n `103` status `ready` deltaP `-3.6335` edge `-0.0068` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.6397` n `103` status `ready` deltaP `-4.0099` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6469` n `103` status `ready` deltaP `-1.7287` edge `-0.0109` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.8783` n `103` status `ready` deltaP `1.1751` edge `-0.0057` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0304` n `103` status `ready` deltaP `-2.7631` edge `-0.0128` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.9778` n `103` status `ready` deltaP `2.1312` edge `-0.0453` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-2.0236` n `103` status `ready` deltaP `-11.4775` edge `-0.0292` maxDD `-2.3669`
- `market_context_high->crypto_major_24h` score `-2.3573` n `99` status `ready` deltaP `5.7765` edge `-0.0913` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.5272` n `103` status `ready` deltaP `-8.3338` edge `-0.0554` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-2.7451` n `99` status `ready` deltaP `-14.0151` edge `-0.1142` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.2712` n `103` status `ready` deltaP `-11.6461` edge `-0.1131` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.9717` n `103` status `ready` deltaP `-14.7111` edge `-0.2271` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
