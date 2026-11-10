# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T00:07:31.117575+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9892`

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

- `market_context_high->unknown_4h` score `29.6215` n `88` status `ready` deltaP `7.2201` edge `2.4651` maxDD `-0.9153`
- `market_context_high->equity_24h` score `18.8441` n `60` status `ready` deltaP `27.6863` edge `2.4718` maxDD `-16.9034`
- `market_context_high->index_24h` score `3.2362` n `60` status `ready` deltaP `22.8076` edge `0.3091` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `1.2993` n `60` status `ready` deltaP `11.3258` edge `0.6005` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.2702` n `60` status `ready` deltaP `12.048` edge `-0.0025` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3892` n `88` status `ready` deltaP `3.4976` edge `0.0119` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5483` n `88` status `ready` deltaP `-0.1565` edge `-0.001` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.8469` n `88` status `ready` deltaP `0.0416` edge `-0.0111` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.8711` n `88` status `ready` deltaP `-2.2311` edge `0.0138` maxDD `-4.182`
- `market_context_high->index_1h` score `-1.0859` n `88` status `ready` deltaP `-9.0024` edge `0.0039` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1467` n `88` status `ready` deltaP `-2.2727` edge `0.0065` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3436` n `88` status `ready` deltaP `-14.657` edge `-0.0061` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7664` n `88` status `ready` deltaP `-8.4036` edge `0.0142` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9444` n `88` status `ready` deltaP `0.4831` edge `-0.0546` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1438` n `88` status `ready` deltaP `-7.0676` edge `-0.0096` maxDD `-2.4506`
- `market_context_high->commodity_24h` score `-2.3414` n `60` status `ready` deltaP `-15.9936` edge `0.0436` maxDD `-9.6389`
- `market_context_high->fx_24h` score `-2.452` n `60` status `ready` deltaP `-15.5257` edge `-0.0521` maxDD `-3.3667`
- `market_context_high->crypto_major_1h` score `-3.2383` n `88` status `ready` deltaP `-5.709` edge `-0.1148` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.4033` n `88` status `ready` deltaP `-2.5915` edge `-0.2185` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1062` n `88` status `ready` deltaP `2.245` edge `-0.262` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
