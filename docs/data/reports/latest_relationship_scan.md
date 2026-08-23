# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T02:37:24.360565+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `news_risk_high->unknown_4h` score `12.0504` n `32` status `ready` deltaP `30.0305` edge `0.804` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.6833` n `32` status `ready` deltaP `47.2561` edge `0.2419` maxDD `0.0`
- `news_risk_high->unknown_1h` score `5.6385` n `44` status `ready` deltaP `28.3342` edge `0.2928` maxDD `-0.2787`
- `news_risk_high->fx_4h` score `3.1305` n `32` status `ready` deltaP `36.6616` edge `0.0299` maxDD `-0.0746`
- `news_risk_high->metal_4h` score `2.0158` n `32` status `ready` deltaP `25.9909` edge `0.0031` maxDD `-0.0045`
- `market_context_high->unknown_1h` score `1.5441` n `135` status `ready` deltaP `6.314` edge `0.1093` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.3965` n `44` status `ready` deltaP `18.9848` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3412` n `44` status `ready` deltaP `25.9527` edge `0.0271` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `1.1144` n `135` status `ready` deltaP `20.4009` edge `-0.0218` maxDD `-0.3736`
- `news_risk_high->commodity_1h` score `0.3679` n `44` status `ready` deltaP `13.0648` edge `-0.0091` maxDD `-0.4666`
- `news_risk_high->index_4h` score `0.3167` n `32` status `ready` deltaP `8.5366` edge `0.0223` maxDD `-0.0884`
- `market_context_high->fx_4h` score `0.1046` n `135` status `ready` deltaP `8.2588` edge `0.0086` maxDD `-0.3527`
- `news_risk_high->metal_1h` score `0.0667` n `44` status `ready` deltaP `5.6206` edge `-0.0066` maxDD `-0.1184`
- `news_risk_high->commodity_4h` score `0.0664` n `32` status `ready` deltaP `9.8323` edge `-0.0192` maxDD `-1.0273`
- `news_risk_high->crypto_major_4h` score `0.0161` n `32` status `ready` deltaP `-4.497` edge `0.168` maxDD `-6.9344`
- `news_risk_high->index_1h` score `-0.0344` n `44` status `ready` deltaP `4.2461` edge `0.0026` maxDD `-0.1583`
- `market_context_high->index_1h` score `-0.0703` n `135` status `ready` deltaP `5.9969` edge `0.0041` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1505` n `135` status `ready` deltaP `1.8131` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.361` n `135` status `ready` deltaP `4.185` edge `0.0328` maxDD `-5.2257`
- `news_risk_high->crypto_major_1h` score `-0.4204` n `44` status `ready` deltaP `8.2744` edge `-0.0213` maxDD `-5.0209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
