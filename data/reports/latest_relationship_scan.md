# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T06:52:30.162325+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9714`

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

- `market_context_high->crypto_alt_4h` score `7.3822` n `115` status `ready` deltaP `18.8653` edge `0.6343` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.6631` n `115` status `ready` deltaP `22.7041` edge `0.5598` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.5538` n `52` status `ready` deltaP `20.6379` edge `0.37` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.5538` n `52` status `ready` deltaP `20.6379` edge `0.37` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.3362` n `48` status `ready` deltaP `30.087` edge `0.2441` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.3362` n `48` status `ready` deltaP `30.087` edge `0.2441` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.7485` n `52` status `ready` deltaP `35.6472` edge `0.4564` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.7485` n `52` status `ready` deltaP `35.6472` edge `0.4564` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `2.8885` n `115` status `ready` deltaP `-3.4743` edge `0.3285` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `1.8192` n `117` status `ready` deltaP `13.2671` edge `0.1699` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.4144` n `117` status `ready` deltaP `7.1588` edge `0.1507` maxDD `-3.7781`
- `market_context_high->metal_4h` score `-0.0179` n `115` status `ready` deltaP `11.5867` edge `0.0258` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.237` n `54` status `ready` deltaP `2.6004` edge `0.0245` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.237` n `54` status `ready` deltaP `2.6004` edge `0.0245` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3576` n `117` status `ready` deltaP `0.9471` edge `0.0019` maxDD `-0.3742`
- `market_context_high->index_1h` score `-0.5165` n `117` status `ready` deltaP `1.5246` edge `-0.0016` maxDD `-1.3154`
- `market_context_high->metal_1h` score `-0.5399` n `117` status `ready` deltaP `5.6183` edge `0.0045` maxDD `-0.9556`
- `risk_on_high->crypto_alt_1h` score `-0.5508` n `54` status `ready` deltaP `3.0107` edge `0.0119` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.5508` n `54` status `ready` deltaP `3.0107` edge `0.0119` maxDD `-5.8734`
- `risk_on_high->metal_1h` score `-0.5653` n `54` status `ready` deltaP `0.2052` edge `-0.0007` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
