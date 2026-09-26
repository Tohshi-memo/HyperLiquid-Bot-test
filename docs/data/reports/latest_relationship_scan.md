# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T08:37:27.521838+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11858`

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

- `news_risk_high->unknown_24h` score `3406.4208` n `100` status `ready` deltaP `-0.6528` edge `283.8772` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.9249` n `47` status `ready` deltaP `8.7687` edge `5.7757` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.8124` n `47` status `ready` deltaP `22.9573` edge `3.8706` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.0283` n `47` status `ready` deltaP `21.1362` edge `2.3161` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.4175` n `47` status `ready` deltaP `33.3739` edge `1.9312` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.1362` n `47` status `ready` deltaP `29.9017` edge `0.4083` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.3939` n `47` status `ready` deltaP `28.8084` edge `0.1146` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7131` n `47` status `ready` deltaP `17.1445` edge `0.1536` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5432` n `47` status `ready` deltaP `29.3007` edge `0.032` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.4173` n `47` status `ready` deltaP `11.5172` edge `0.1081` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.183` n `100` status `ready` deltaP `27.3403` edge `0.1355` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.0374` n `47` status `ready` deltaP `11.9155` edge `0.0473` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8062` n `47` status `ready` deltaP `12.8137` edge `0.0096` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.6138` n `47` status `ready` deltaP `5.9094` edge `0.1022` maxDD `-5.2359`
- `news_risk_high->index_24h` score `0.5601` n `100` status `ready` deltaP `14.2847` edge `0.0418` maxDD `-2.2287`
- `market_context_high->fx_1h` score `0.5201` n `47` status `ready` deltaP `10.7083` edge `0.0076` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.3506` n `47` status `ready` deltaP `5.351` edge `0.0753` maxDD `-4.5405`
- `news_risk_high->crypto_alt_1h` score `0.0446` n `137` status `ready` deltaP `5.6067` edge `0.0574` maxDD `-4.2849`
- `market_context_high->fx_4h` score `0.0359` n `47` status `ready` deltaP `9.3215` edge `0.0076` maxDD `-0.6736`
- `market_context_high->metal_1h` score `0.004` n `47` status `ready` deltaP `3.2775` edge `0.0103` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
