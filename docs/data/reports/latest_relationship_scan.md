# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T04:52:29.386449+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11768`

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

- `news_risk_high->unknown_24h` score `3199.629` n `95` status `ready` deltaP `-0.7054` edge `266.6449` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `70.3426` n `47` status `ready` deltaP `8.0201` edge `5.8155` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.8692` n `47` status `ready` deltaP `25.5614` edge `3.9413` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.281` n `47` status `ready` deltaP `23.2195` edge `2.4066` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2903` n `47` status `ready` deltaP `33.3739` edge `1.9206` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.3781` n `47` status `ready` deltaP `32.5059` edge `0.4111` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.5396` n `47` status `ready` deltaP `29.85` edge `0.1198` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7167` n `47` status `ready` deltaP `17.1445` edge `0.1539` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5164` n `47` status `ready` deltaP `28.9958` edge `0.0318` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.1186` n `47` status `ready` deltaP `10.6026` edge `0.0893` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.0954` n `95` status `ready` deltaP `26.9608` edge `0.1268` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.0781` n `47` status `ready` deltaP `12.3646` edge `0.0477` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7702` n `47` status `ready` deltaP `12.3646` edge `0.0096` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5093` n `47` status `ready` deltaP `10.5586` edge `0.0077` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.4105` n `95` status `ready` deltaP `13.6257` edge `0.0435` maxDD `-2.344`
- `market_context_high->crypto_major_1h` score `0.3386` n `47` status `ready` deltaP `5.2013` edge `0.0753` maxDD `-4.5405`
- `market_context_high->crypto_major_4h` score `0.3248` n `47` status `ready` deltaP `4.2326` edge `0.0893` maxDD `-5.2359`
- `news_risk_high->index_1h` score `0.1898` n `124` status `ready` deltaP `6.0846` edge `0.0045` maxDD `-0.3395`
- `news_risk_high->crypto_alt_1h` score `0.0402` n `124` status `ready` deltaP `6.3164` edge `0.0541` maxDD `-4.2849`
- `market_context_high->metal_1h` score `0.0281` n `47` status `ready` deltaP `3.7266` edge `0.0104` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
