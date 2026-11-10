# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T11:07:26.807723+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11130`

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

- `market_context_high->unknown_4h` score `45.6313` n `88` status `ready` deltaP `7.6774` edge `3.7962` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.9346` n `88` status `ready` deltaP `33.0412` edge `2.9314` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4728` n `88` status `ready` deltaP `25.8783` edge `0.3298` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.5298` n `88` status `ready` deltaP `22.6012` edge `0.9395` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.121` n `88` status `ready` deltaP `16.9036` edge `-0.0473` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.3879` n `88` status `ready` deltaP `2.089` edge `0.0046` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4299` n `88` status `ready` deltaP `3.1042` edge `0.0348` maxDD `-4.182`
- `market_context_high->metal_1h` score `-0.4432` n `88` status `ready` deltaP `3.0485` edge `0.0104` maxDD `-1.4122`
- `market_context_high->index_4h` score `-0.7458` n `88` status `ready` deltaP `1.5659` edge `-0.0083` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0337` n `88` status `ready` deltaP `-8.1042` edge `0.0046` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1872` n `88` status `ready` deltaP `-2.2727` edge `0.0013` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3249` n `88` status `ready` deltaP `-14.3576` edge `-0.0057` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7492` n `88` status `ready` deltaP `-8.8527` edge `0.0194` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9148` n `88` status `ready` deltaP `1.0819` edge `-0.0548` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.018` n `88` status `ready` deltaP `-4.9335` edge `-0.0077` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.4768` n `88` status `ready` deltaP `-3.3795` edge `-0.0239` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.0895` n `88` status `ready` deltaP `-4.212` edge `-0.1057` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.1429` n `88` status `ready` deltaP `-1.6768` edge `-0.2029` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.8648` n `88` status `ready` deltaP `2.3975` edge `-0.2429` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2128` n `88` status `ready` deltaP `-23.4698` edge `-0.0589` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
