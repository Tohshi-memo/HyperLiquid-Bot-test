# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T01:07:30.743808+00:00`
- Price records: `672`
- Market context records: `8570`
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

- `news_risk_high->unknown_24h` score `4964.5441` n `62` status `ready` deltaP `39.2081` edge `413.4927` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.9232` n `64` status `ready` deltaP `21.5701` edge `0.4095` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.1628` n `64` status `ready` deltaP `18.1784` edge `0.0781` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.002` n `62` status `ready` deltaP `13.9703` edge `0.1694` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.7505` n `64` status `ready` deltaP `16.4016` edge `0.0842` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.1422` n `64` status `ready` deltaP `7.9649` edge `0.1709` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7103` n `64` status `ready` deltaP `13.5671` edge `0.1398` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4555` n `64` status `ready` deltaP `8.2616` edge `0.056` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3843` n `64` status `ready` deltaP `7.3634` edge `0.0514` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1072` n `64` status `ready` deltaP `5.5857` edge `0.0046` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0606` n `64` status `ready` deltaP `11.7759` edge `0.0223` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0177` n `64` status `ready` deltaP `3.7706` edge `0.0088` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0341` n `64` status `ready` deltaP `1.7149` edge `0.0318` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.0964` n `64` status `ready` deltaP `3.7051` edge `0.0076` maxDD `-0.5599`
- `market_context_high->fx_4h` score `-0.1076` n `62` status `ready` deltaP `8.6005` edge `0.0133` maxDD `-1.3685`
- `market_context_high->fx_1h` score `-0.2575` n `62` status `ready` deltaP `2.5111` edge `0.0005` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.32` n `62` status `ready` deltaP `4.0081` edge `-0.0052` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5213` n `62` status `ready` deltaP `-2.7767` edge `0.0144` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7561` n `62` status `ready` deltaP `0.7968` edge `-0.0154` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9374` n `62` status `ready` deltaP `-2.5449` edge `-0.0117` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
