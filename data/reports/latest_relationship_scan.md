# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T21:07:26.037198+00:00`
- Price records: `672`
- Market context records: `8551`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5919`

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

- `news_risk_high->unknown_24h` score `5192.5907` n `60` status `ready` deltaP `41.7708` edge `432.4795` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.5649` n `64` status `ready` deltaP `20.0457` edge `0.3898` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.9257` n `64` status `ready` deltaP `15.7393` edge `0.0746` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `1.898` n `62` status `ready` deltaP `13.3605` edge `0.1648` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.7229` n `64` status `ready` deltaP `16.2519` edge `0.0829` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9943` n `64` status `ready` deltaP `6.4405` edge `0.1621` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.6427` n `64` status `ready` deltaP `12.9573` edge `0.1352` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4742` n `64` status `ready` deltaP `8.4113` edge `0.0574` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.347` n `64` status `ready` deltaP `6.7646` edge `0.0506` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0729` n `64` status `ready` deltaP `4.9869` edge `0.0042` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0145` n `64` status `ready` deltaP `3.7706` edge `0.0084` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0506` n `64` status `ready` deltaP `1.5625` edge `0.0307` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `-0.0561` n `64` status `ready` deltaP `10.5564` edge `0.0207` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.1371` n `64` status `ready` deltaP `3.256` edge `0.0072` maxDD `-0.5599`
- `market_context_high->fx_4h` score `-0.2244` n `62` status `ready` deltaP `7.381` edge `0.0117` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `-0.2725` n `62` status `ready` deltaP `4.4572` edge `-0.0021` maxDD `-2.0038`
- `market_context_high->fx_1h` score `-0.2918` n `62` status `ready` deltaP `1.9123` edge `0.0001` maxDD `-0.6874`
- `market_context_high->crypto_alt_1h` score `-0.5026` n `62` status `ready` deltaP `-2.627` edge `0.0158` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7609` n `62` status `ready` deltaP `0.7968` edge `-0.0158` maxDD `-1.5667`
- `market_context_high->commodity_4h` score `-0.9763` n `62` status `ready` deltaP `1.7555` edge `0.0146` maxDD `-5.4508`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
