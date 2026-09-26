# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T03:07:31.325749+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11730`

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

- `news_risk_high->unknown_24h` score `2906.8991` n `88` status `ready` deltaP `-0.7892` edge `242.2513` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `70.9678` n `47` status `ready` deltaP `8.3196` edge `5.8656` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.4092` n `47` status `ready` deltaP `26.7767` edge `3.9782` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.947` n `47` status `ready` deltaP `24.4348` edge `2.454` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2747` n `47` status `ready` deltaP `33.3739` edge `1.9193` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.5017` n `47` status `ready` deltaP `33.7212` edge `0.4133` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.6716` n `47` status `ready` deltaP `31.0653` edge `0.1227` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7241` n `47` status `ready` deltaP `17.2969` edge `0.1535` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5274` n `47` status `ready` deltaP `29.1483` edge `0.0317` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.1136` n `47` status `ready` deltaP `10.4502` edge `0.0899` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0805` n `47` status `ready` deltaP `12.3646` edge `0.0479` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.9506` n `88` status `ready` deltaP `25.9154` edge `0.1152` maxDD `-6.9545`
- `market_context_high->index_1h` score `0.7942` n `47` status `ready` deltaP `12.664` edge `0.0096` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5344` n `47` status `ready` deltaP `10.858` edge `0.0078` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.3589` n `88` status `ready` deltaP `12.8315` edge `0.0445` maxDD `-2.344`
- `market_context_high->crypto_major_1h` score `0.2979` n `47` status `ready` deltaP `4.9019` edge `0.0739` maxDD `-4.5405`
- `market_context_high->crypto_major_4h` score `0.274` n `47` status `ready` deltaP `3.9277` edge `0.0871` maxDD `-5.2359`
- `news_risk_high->index_1h` score `0.2343` n `117` status `ready` deltaP `6.5357` edge `0.0052` maxDD `-0.3395`
- `news_risk_high->crypto_alt_1h` score `0.2133` n `117` status `ready` deltaP `7.8152` edge `0.0663` maxDD `-4.2849`
- `news_risk_high->equity_4h` score `0.1699` n `105` status `ready` deltaP `16.8917` edge `0.0701` maxDD `-9.2079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
