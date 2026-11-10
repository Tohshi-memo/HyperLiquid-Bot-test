# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T22:37:26.499559+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11740`

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

- `market_context_high->unknown_4h` score `61.8743` n `88` status `ready` deltaP `7.525` edge `5.1508` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.2808` n `88` status `ready` deltaP `33.6489` edge `2.9562` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `6.758` n `88` status `ready` deltaP `29.4665` edge `1.1794` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.9961` n `88` status `ready` deltaP `30.6344` edge `0.3417` maxDD `-2.3671`
- `market_context_high->metal_24h` score `2.1574` n `88` status `ready` deltaP `24.779` edge `0.0699` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3533` n `88` status `ready` deltaP `3.797` edge `0.0129` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3568` n `88` status `ready` deltaP `3.2866` edge `0.0006` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.5507` n `88` status `ready` deltaP `4.4623` edge `-0.0026` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.5533` n `88` status `ready` deltaP `2.9518` edge `0.02` maxDD `-4.182`
- `market_context_high->index_1h` score `-0.9823` n `88` status `ready` deltaP `-7.3557` edge `0.0062` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.03` n `88` status `ready` deltaP `-0.7483` edge `0.0113` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2167` n `88` status `ready` deltaP `-12.4115` edge `-0.0048` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5325` n `88` status `ready` deltaP `-7.206` edge `0.0362` maxDD `-8.1039`
- `market_context_high->fx_24h` score `-1.6773` n `88` status `ready` deltaP `4.5139` edge `-0.0099` maxDD `-3.4642`
- `market_context_high->fx_4h` score `-1.8148` n `88` status `ready` deltaP `-1.5798` edge `-0.004` maxDD `-2.4506`
- `market_context_high->crypto_alt_1h` score `-1.8165` n `88` status `ready` deltaP `1.0819` edge `-0.0422` maxDD `-10.8319`
- `market_context_high->crypto_major_1h` score `-2.946` n `88` status `ready` deltaP `-3.7629` edge `-0.0903` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.0317` n `88` status `ready` deltaP `2.1341` edge `-0.1357` maxDD `-25.16`
- `market_context_high->crypto_major_24h` score `-7.1273` n `88` status `ready` deltaP `6.2816` edge `0.5267` maxDD `-80.6681`
- `market_context_high->crypto_alt_4h` score `-8.2393` n `88` status `ready` deltaP `4.5316` edge `-0.205` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
