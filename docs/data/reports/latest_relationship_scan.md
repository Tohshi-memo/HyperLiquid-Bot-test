# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T14:07:29.028371+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11136`

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

- `market_context_high->unknown_4h` score `39.6253` n `88` status `ready` deltaP `7.6774` edge `3.2957` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.7762` n `88` status `ready` deltaP `33.0412` edge `2.9182` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4452` n `88` status `ready` deltaP `25.8783` edge `0.3275` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.9369` n `88` status `ready` deltaP `23.8144` edge `0.9836` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.5946` n `88` status `ready` deltaP `18.9834` edge `-0.0217` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3269` n `88` status `ready` deltaP `4.0964` edge `0.0131` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3848` n `88` status `ready` deltaP `2.3884` edge `0.003` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.5223` n `88` status `ready` deltaP `2.6469` edge `0.026` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.6218` n `88` status `ready` deltaP `3.3952` edge `-0.0046` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.987` n `88` status `ready` deltaP `-7.3557` edge `0.0056` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0408` n `88` status `ready` deltaP `-0.5959` edge `0.0089` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3086` n `88` status `ready` deltaP `-14.0582` edge `-0.0056` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.6065` n `88` status `ready` deltaP `-7.8048` edge `0.0307` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.8477` n `88` status `ready` deltaP `1.3813` edge `-0.0482` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.9571` n `88` status `ready` deltaP `-3.8664` edge `-0.007` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.2684` n `88` status `ready` deltaP `-1.2998` edge `-0.0204` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.01` n `88` status `ready` deltaP `-3.7629` edge `-0.0985` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.5394` n `88` status `ready` deltaP `0.1524` edge `-0.1648` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.556` n `88` status `ready` deltaP `3.617` edge `-0.2253` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.256` n `88` status `ready` deltaP `-23.4698` edge `-0.0625` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
