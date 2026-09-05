# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T00:07:25.902896+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10456`

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

- `risk_on_high->unknown_4h` score `19.9483` n `133` status `ready` deltaP `8.9985` edge `1.6642` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.9483` n `133` status `ready` deltaP `8.9985` edge `1.6642` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `9.4508` n `217` status `ready` deltaP `9.4351` edge `0.7942` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `5.2253` n `43` status `ready` deltaP `20.9101` edge `0.323` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `2.8716` n `43` status `ready` deltaP `12.7163` edge `0.1986` maxDD `-1.1927`
- `news_risk_high->commodity_24h` score `2.7561` n `43` status `ready` deltaP `17.2602` edge `0.1318` maxDD `-0.042`
- `news_risk_high->metal_4h` score `1.8238` n `43` status `ready` deltaP `18.4345` edge `0.0512` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.6168` n `43` status `ready` deltaP `10.7735` edge `0.083` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5363` n `43` status `ready` deltaP `14.0092` edge `0.0737` maxDD `-0.7924`
- `news_risk_high->index_1h` score `1.3514` n `43` status `ready` deltaP `17.0728` edge `0.0122` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `0.7867` n `43` status `ready` deltaP `9.8663` edge `0.0191` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `0.6005` n `43` status `ready` deltaP `1.5423` edge `0.0582` maxDD `-0.4752`
- `news_risk_high->crypto_alt_4h` score `0.3466` n `43` status `ready` deltaP `3.187` edge `0.0405` maxDD `-1.296`
- `news_risk_high->crypto_alt_1h` score `0.3333` n `43` status `ready` deltaP `3.9479` edge `0.028` maxDD `-0.7901`
- `news_risk_high->fx_4h` score `0.1555` n `43` status `ready` deltaP `8.9372` edge `-0.0014` maxDD `-0.9514`
- `news_risk_high->commodity_1h` score `0.1515` n `43` status `ready` deltaP `8.9786` edge `0.0042` maxDD `-0.9036`
- `risk_on_high->metal_1h` score `0.1459` n `133` status `ready` deltaP `13.311` edge `0.0012` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1459` n `133` status `ready` deltaP `13.311` edge `0.0012` maxDD `-1.699`
- `risk_on_high->index_1h` score `-0.2213` n `133` status `ready` deltaP `2.9445` edge `-0.0035` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.2213` n `133` status `ready` deltaP `2.9445` edge `-0.0035` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
