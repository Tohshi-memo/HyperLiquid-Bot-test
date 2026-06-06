# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T17:37:27.565287+00:00`
- Price records: `672`
- Market context records: `3096`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6921`

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

- `market_context_high->crypto_alt_24h` score `16.4629` n `83` status `ready` deltaP `13.9432` edge `2.5453` maxDD `-33.5432`
- `market_context_high->commodity_24h` score `15.1623` n `83` status `ready` deltaP `45.233` edge `1.0048` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.7409` n `83` status `ready` deltaP `22.9209` edge `1.1244` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.8046` n `83` status `ready` deltaP `32.48` edge `0.9201` maxDD `-14.8998`
- `market_context_high->equity_24h` score `7.5863` n `83` status `ready` deltaP `18.6161` edge `1.3692` maxDD `-35.9896`
- `market_context_high->commodity_4h` score `3.0521` n `117` status `ready` deltaP `18.2015` edge `0.1788` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.9282` n `117` status `ready` deltaP `5.8058` edge `0.1084` maxDD `-2.914`
- `market_context_high->commodity_1h` score `-0.0413` n `121` status `ready` deltaP `1.7729` edge `0.027` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5197` n `121` status `ready` deltaP `3.5631` edge `0.0159` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.6896` n `121` status `ready` deltaP `-7.4021` edge `-0.0018` maxDD `-0.3147`
- `market_context_high->fx_24h` score `-0.726` n `83` status `ready` deltaP `3.0497` edge `-0.0039` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.827` n `121` status `ready` deltaP `3.1858` edge `0.0857` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.3366` n `121` status `ready` deltaP `-3.0423` edge `-0.0025` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3654` n `117` status `ready` deltaP `-12.8232` edge `-0.0052` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4259` n `117` status `ready` deltaP `9.6441` edge `0.0438` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-2.2946` n `121` status `ready` deltaP `-1.4141` edge `0.0445` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.4074` n `121` status `ready` deltaP `-7.3428` edge `-0.0123` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.7115` n `121` status `ready` deltaP `2.9829` edge `-0.0614` maxDD `-12.7554`
- `market_context_high->crypto_alt_4h` score `-3.6998` n `117` status `ready` deltaP `13.597` edge `0.2395` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.0938` n `117` status `ready` deltaP `5.708` edge `-0.0368` maxDD `-36.4212`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
