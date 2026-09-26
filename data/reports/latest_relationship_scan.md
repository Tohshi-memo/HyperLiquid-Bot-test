# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T08:52:28.616360+00:00`
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

- `news_risk_high->unknown_24h` score `3467.1628` n `99` status `ready` deltaP `-0.6629` edge `288.9391` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.9093` n `47` status `ready` deltaP `8.619` edge `5.7754` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.7422` n `47` status `ready` deltaP `22.7837` edge `3.8659` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.9304` n `47` status `ready` deltaP `20.9626` edge `2.3091` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.4295` n `47` status `ready` deltaP `33.3739` edge `1.9322` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.135` n `47` status `ready` deltaP `29.9017` edge `0.4082` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.3927` n `47` status `ready` deltaP `28.8084` edge `0.1145` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7119` n `47` status `ready` deltaP `17.1445` edge `0.1535` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5554` n `47` status `ready` deltaP `29.4532` edge `0.032` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.4221` n `47` status `ready` deltaP `11.5172` edge `0.1085` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.172` n `99` status `ready` deltaP `27.0676` edge `0.1359` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.0374` n `47` status `ready` deltaP `11.9155` edge `0.0473` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7942` n `47` status `ready` deltaP `12.664` edge `0.0096` maxDD `-0.2275`
- `news_risk_high->index_24h` score `0.6947` n `99` status `ready` deltaP `15.0726` edge `0.0436` maxDD `-2.2287`
- `market_context_high->crypto_major_4h` score `0.6332` n `47` status `ready` deltaP `6.0619` edge `0.1028` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.5332` n `47` status `ready` deltaP `10.858` edge `0.0077` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.335` n `47` status `ready` deltaP `5.2013` edge `0.075` maxDD `-4.5405`
- `market_context_high->fx_4h` score `0.0481` n `47` status `ready` deltaP `9.4739` edge `0.0076` maxDD `-0.6736`
- `news_risk_high->index_1h` score `0.0429` n `137` status `ready` deltaP `4.3708` edge `0.0036` maxDD `-0.3331`
- `news_risk_high->crypto_alt_1h` score `0.0235` n `137` status `ready` deltaP `5.6067` edge `0.0567` maxDD `-4.2849`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
