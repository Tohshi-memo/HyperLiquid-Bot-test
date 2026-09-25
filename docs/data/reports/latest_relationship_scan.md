# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T20:07:27.559305+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11220`

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

- `market_context_high->unknown_1h` score `71.881` n `47` status `ready` deltaP `7.8704` edge `5.9447` maxDD `-0.2334`
- `news_risk_high->unknown_24h` score `67.512` n `69` status `ready` deltaP `-1.1021` edge `5.6378` maxDD `-0.0226`
- `market_context_high->crypto_major_24h` score `50.6101` n `47` status `ready` deltaP `30.9434` edge `4.0505` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.0668` n `47` status `ready` deltaP `24.782` edge `2.545` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3726` n `47` status `ready` deltaP `34.7628` edge `1.9182` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7189` n `47` status `ready` deltaP `34.9364` edge `0.4233` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.02` n `47` status `ready` deltaP `34.1903` edge `0.1309` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7241` n `47` status `ready` deltaP `17.2969` edge `0.1535` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.6786` n `47` status `ready` deltaP `30.9776` edge `0.0321` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.4401` n `47` status `ready` deltaP `11.5172` edge `0.11` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.1296` n `47` status `ready` deltaP `12.9634` edge `0.048` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.9124` n `111` status `ready` deltaP `9.179` edge `0.1059` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.89` n `47` status `ready` deltaP `13.8616` edge `0.0096` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4961` n `47` status `ready` deltaP `10.4089` edge `0.0076` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.383` n `47` status `ready` deltaP `4.6899` edge `0.0911` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.3027` n `47` status `ready` deltaP `5.0516` edge `0.0733` maxDD `-4.5405`
- `news_risk_high->metal_24h` score `0.224` n `69` status `ready` deltaP `19.1425` edge `0.0672` maxDD `-6.9545`
- `news_risk_high->crypto_major_1h` score `0.0819` n `111` status `ready` deltaP `4.3616` edge `0.0533` maxDD `-3.3776`
- `news_risk_high->equity_1h` score `0.0791` n `111` status `ready` deltaP `3.7628` edge `0.0358` maxDD `-2.0595`
- `market_context_high->fx_4h` score `0.0335` n `47` status `ready` deltaP `9.3215` edge `0.0074` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
