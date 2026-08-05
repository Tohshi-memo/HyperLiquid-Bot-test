# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T06:07:32.348457+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11632`

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

- `market_context_high->unknown_24h` score `14.8475` n `88` status `ready` deltaP `13.2733` edge `1.1531` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.7061` n `90` status `ready` deltaP `2.6626` edge `0.5573` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5944` n `90` status `ready` deltaP `17.3849` edge `0.1016` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.1988` n `88` status `ready` deltaP `2.7935` edge `0.2519` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.1574` n `88` status `ready` deltaP `27.3832` edge `0.0864` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3138` n `91` status `ready` deltaP `5.993` edge `0.0278` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.0735` n `90` status `ready` deltaP `13.1572` edge `0.0077` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.0404` n `91` status `ready` deltaP `6.3467` edge `-0.0041` maxDD `-0.7878`
- `market_context_high->metal_1h` score `-0.5058` n `91` status `ready` deltaP `-0.9442` edge `-0.0091` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6243` n `91` status `ready` deltaP `-0.8899` edge `-0.0207` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7758` n `90` status `ready` deltaP `3.0318` edge `0.0038` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.8322` n `91` status `ready` deltaP `-2.6453` edge `-0.018` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-0.9867` n `88` status `ready` deltaP `4.2614` edge `-0.0106` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.3169` n `90` status `ready` deltaP `1.8089` edge `-0.0419` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8412` n `91` status `ready` deltaP `2.9579` edge `-0.1022` maxDD `-10.619`
- `market_context_high->index_24h` score `-1.9625` n `88` status `ready` deltaP `-7.0233` edge `0.0147` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.1256` n `90` status `ready` deltaP `-13.0454` edge `-0.0601` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.2987` n `91` status `ready` deltaP `2.5499` edge `-0.2472` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3076` n `91` status `ready` deltaP `-10.4396` edge `-0.0687` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.5854` n `88` status `ready` deltaP `7.1812` edge `-0.096` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
