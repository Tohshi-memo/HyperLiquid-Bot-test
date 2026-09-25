# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T19:52:32.213730+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11312`

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

- `market_context_high->unknown_1h` score `74.5378` n `47` status `ready` deltaP `7.8704` edge `6.1661` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.6185` n `47` status `ready` deltaP `30.9434` edge `4.0512` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.0704` n `47` status `ready` deltaP `24.782` edge `2.5453` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3889` n `47` status `ready` deltaP `34.9364` edge `1.9184` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7237` n `47` status `ready` deltaP `34.9364` edge `0.4237` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.0375` n `47` status `ready` deltaP `34.3639` edge `0.1312` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7181` n `47` status `ready` deltaP `17.2969` edge `0.153` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.6786` n `47` status `ready` deltaP `30.9776` edge `0.0321` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.4437` n `47` status `ready` deltaP `11.5172` edge `0.1103` maxDD `-3.3417`
- `news_risk_high->unknown_1h` score `1.1278` n `111` status `ready` deltaP `3.1167` edge `0.0871` maxDD `-0.4452`
- `market_context_high->equity_1h` score `1.1272` n `47` status `ready` deltaP `12.9634` edge `0.0478` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.9052` n `111` status `ready` deltaP `9.179` edge `0.1053` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.902` n `47` status `ready` deltaP `14.0113` edge `0.0096` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4949` n `47` status `ready` deltaP `10.4089` edge `0.0075` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.4048` n `47` status `ready` deltaP `4.8423` edge `0.0919` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.2883` n `47` status `ready` deltaP `4.9019` edge `0.0731` maxDD `-4.5405`
- `news_risk_high->metal_24h` score `0.1856` n `68` status `ready` deltaP `18.7193` edge `0.0651` maxDD `-6.9545`
- `news_risk_high->equity_1h` score `0.0775` n `111` status `ready` deltaP `3.7628` edge `0.0356` maxDD `-2.0595`
- `news_risk_high->crypto_major_1h` score `0.0675` n `111` status `ready` deltaP `4.2119` edge `0.0531` maxDD `-3.3776`
- `market_context_high->fx_4h` score `0.0335` n `47` status `ready` deltaP `9.3215` edge `0.0074` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
