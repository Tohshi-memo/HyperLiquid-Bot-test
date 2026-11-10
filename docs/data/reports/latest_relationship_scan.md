# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T18:37:33.578628+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11754`

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

- `market_context_high->unknown_4h` score `52.3375` n `88` status `ready` deltaP `7.2201` edge `4.3581` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.0516` n `88` status `ready` deltaP `33.6489` edge `2.9371` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `5.9123` n `88` status `ready` deltaP `26.6887` edge `1.0895` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.6647` n `88` status `ready` deltaP `27.8567` edge `0.3326` maxDD `-2.3671`
- `market_context_high->metal_24h` score `1.31` n `88` status `ready` deltaP `22.0012` edge `0.0178` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3089` n `88` status `ready` deltaP `4.2461` edge `0.0136` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4089` n `88` status `ready` deltaP `2.3884` edge `-0.0001` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4919` n `88` status `ready` deltaP `3.5615` edge `0.0238` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.5753` n `88` status `ready` deltaP `4.005` edge `-0.0027` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9488` n `88` status `ready` deltaP `-6.7569` edge `0.0065` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0197` n `88` status `ready` deltaP `-0.5959` edge `0.0116` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2478` n `88` status `ready` deltaP `-13.0103` edge `-0.0048` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.4935` n `88` status `ready` deltaP `-6.7569` edge `0.0382` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.7963` n `88` status `ready` deltaP `1.3813` edge `-0.0416` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.7989` n `88` status `ready` deltaP `-1.275` edge `-0.004` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-1.9451` n `88` status `ready` deltaP `1.7361` edge `-0.0137` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.8673` n `88` status `ready` deltaP `-3.0144` edge `-0.0852` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.156` n `88` status `ready` deltaP `1.5244` edge `-0.142` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.3047` n `88` status `ready` deltaP `4.0743` edge `-0.2074` maxDD `-34.2787`
- `market_context_high->crypto_major_24h` score `-8.8639` n `88` status `ready` deltaP `3.5038` edge `0.4005` maxDD `-80.6681`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
