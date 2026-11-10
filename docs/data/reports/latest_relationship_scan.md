# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T16:22:39.968376+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11470`

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

- `market_context_high->unknown_4h` score `53.7717` n `88` status `ready` deltaP `7.3725` edge `4.4766` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.8243` n `88` status `ready` deltaP `33.3878` edge `2.9199` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.5103` n `88` status `ready` deltaP `26.5716` edge `0.3283` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `5.2671` n `88` status `ready` deltaP `25.2009` edge `1.0167` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.9258` n `88` status `ready` deltaP `20.5432` edge `-0.0045` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3233` n `88` status `ready` deltaP `4.0964` edge `0.0134` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4043` n `88` status `ready` deltaP `2.2387` edge `0.0015` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4576` n `88` status `ready` deltaP `3.5615` edge `0.0282` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.5918` n `88` status `ready` deltaP `3.8525` edge `-0.0038` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9777` n `88` status `ready` deltaP `-7.206` edge `0.0058` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0384` n `88` status `ready` deltaP `-0.5959` edge `0.0092` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2798` n `88` status `ready` deltaP `-13.6091` edge `-0.0049` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5606` n `88` status `ready` deltaP `-7.206` edge `0.0326` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.8119` n `88` status `ready` deltaP `1.3813` edge `-0.0436` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.8828` n `88` status `ready` deltaP `-2.6469` edge `-0.0056` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.0992` n `88` status `ready` deltaP `0.26` edge `-0.0167` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.8767` n `88` status `ready` deltaP `-3.0144` edge `-0.0864` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.3296` n `88` status `ready` deltaP `0.9146` edge `-0.1524` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.5499` n `88` status `ready` deltaP `3.7694` edge `-0.2258` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2212` n `88` status `ready` deltaP `-23.4698` edge `-0.0596` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
