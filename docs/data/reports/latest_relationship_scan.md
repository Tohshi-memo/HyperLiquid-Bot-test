# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T22:22:28.982816+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11650`

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

- `news_risk_high->unknown_24h` score `1002.8534` n `78` status `ready` deltaP `-0.9349` edge `83.5818` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `71.3662` n `47` status `ready` deltaP `8.1698` edge `5.8998` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.3305` n `47` status `ready` deltaP `29.7281` edge `4.0353` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.816` n `47` status `ready` deltaP `24.782` edge `2.5241` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2279` n `47` status `ready` deltaP `33.3739` edge `1.9154` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.6317` n `47` status `ready` deltaP `34.4156` edge `0.4195` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.8705` n `47` status `ready` deltaP `32.8014` edge `0.1277` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7727` n `47` status `ready` deltaP `17.7542` edge `0.1545` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5884` n `47` status `ready` deltaP `29.9105` edge `0.0317` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.3785` n `47` status `ready` deltaP `11.2124` edge `0.1069` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0901` n `47` status `ready` deltaP `12.5143` edge `0.0477` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.9472` n `111` status `ready` deltaP `9.3287` edge `0.1078` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.8157` n `47` status `ready` deltaP `12.9634` edge `0.0094` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.5614` n `78` status `ready` deltaP `22.4359` edge `0.0885` maxDD `-6.9545`
- `market_context_high->fx_1h` score `0.5464` n `47` status `ready` deltaP `11.0077` edge `0.0078` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.3914` n `47` status `ready` deltaP `4.6899` edge `0.0918` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.2859` n `47` status `ready` deltaP `4.7522` edge `0.0739` maxDD `-4.5405`
- `news_risk_high->crypto_major_1h` score `0.0651` n `111` status `ready` deltaP `4.0622` edge `0.0539` maxDD `-3.3776`
- `market_context_high->fx_4h` score `0.0591` n `47` status `ready` deltaP `9.6264` edge `0.0075` maxDD `-0.6736`
- `news_risk_high->equity_1h` score `0.0534` n `111` status `ready` deltaP `3.3137` edge `0.0355` maxDD `-2.0595`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
