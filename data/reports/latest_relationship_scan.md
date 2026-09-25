# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T20:22:28.037524+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `10996`

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

- `news_risk_high->unknown_24h` score `185.6009` n `70` status `ready` deltaP `-1.0814` edge `15.4784` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.4666` n `47` status `ready` deltaP `7.8704` edge `5.7435` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.5957` n `47` status `ready` deltaP `30.9434` edge `4.0493` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.0512` n `47` status `ready` deltaP `24.782` edge `2.5437` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3527` n `47` status `ready` deltaP `34.5892` edge `1.9177` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.699` n `47` status `ready` deltaP `34.7628` edge `0.4228` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.0001` n `47` status `ready` deltaP `34.0167` edge `0.1304` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7399` n `47` status `ready` deltaP `17.4494` edge `0.1538` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.6652` n `47` status `ready` deltaP `30.8251` edge `0.032` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.4329` n `47` status `ready` deltaP `11.5172` edge `0.1094` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.1308` n `47` status `ready` deltaP `12.9634` edge `0.0481` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.9112` n `111` status `ready` deltaP `9.179` edge `0.1058` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.878` n `47` status `ready` deltaP `13.7119` edge `0.0096` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4973` n `47` status `ready` deltaP `10.4089` edge `0.0077` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.3624` n `47` status `ready` deltaP `4.5375` edge `0.0904` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.2859` n `47` status `ready` deltaP `4.9019` edge `0.0729` maxDD `-4.5405`
- `news_risk_high->metal_24h` score `0.2677` n `70` status `ready` deltaP `19.5486` edge `0.0701` maxDD `-6.9545`
- `news_risk_high->equity_1h` score `0.0799` n `111` status `ready` deltaP `3.7628` edge `0.0359` maxDD `-2.0595`
- `news_risk_high->crypto_major_1h` score `0.0651` n `111` status `ready` deltaP `4.2119` edge `0.0529` maxDD `-3.3776`
- `market_context_high->fx_4h` score `0.0335` n `47` status `ready` deltaP `9.3215` edge `0.0074` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
