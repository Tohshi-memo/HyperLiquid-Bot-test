# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T08:37:30.802659+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11430`

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

- `market_context_high->unknown_4h` score `38.0485` n `88` status `ready` deltaP `7.6774` edge `3.1643` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.3282` n `88` status `ready` deltaP `33.0412` edge `2.9642` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.5352` n `88` status `ready` deltaP `25.8783` edge `0.335` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.2778` n `88` status `ready` deltaP `22.6012` edge `0.9072` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.1035` n `88` status `ready` deltaP `16.557` edge `-0.0637` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.4175` n `88` status `ready` deltaP `1.6399` edge `0.0038` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4803` n `88` status `ready` deltaP `2.4945` edge `0.0324` maxDD `-4.182`
- `market_context_high->metal_1h` score `-0.5007` n `88` status `ready` deltaP `2.4497` edge `0.0096` maxDD `-1.4122`
- `market_context_high->index_4h` score `-0.8225` n `88` status `ready` deltaP `0.3464` edge `-0.01` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.103` n `88` status `ready` deltaP `-9.3018` edge `0.0037` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2942` n `88` status `ready` deltaP `-3.3398` edge `-0.0053` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3343` n `88` status `ready` deltaP `-14.5073` edge `-0.0059` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.8466` n `88` status `ready` deltaP `-9.6012` edge `0.0119` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-2.0161` n `88` status `ready` deltaP `0.034` edge `-0.0608` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.0782` n `88` status `ready` deltaP `-6.0006` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.6586` n `88` status `ready` deltaP `-5.1127` edge `-0.0275` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.2009` n `88` status `ready` deltaP `-5.2599` edge `-0.113` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.3767` n `88` status `ready` deltaP `-2.439` edge `-0.2173` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.2756` n `88` status `ready` deltaP `1.178` edge `-0.269` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.3124` n `88` status `ready` deltaP `-23.4698` edge `-0.0672` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
