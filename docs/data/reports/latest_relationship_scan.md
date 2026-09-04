# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T17:37:28.459153+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10802`

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

- `risk_on_high->unknown_4h` score `19.5286` n `133` status `ready` deltaP `7.3216` edge `1.6404` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.5286` n `133` status `ready` deltaP `7.3216` edge `1.6404` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.4718` n `133` status `ready` deltaP `-1.9518` edge `1.0267` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.4718` n `133` status `ready` deltaP `-1.9518` edge `1.0267` maxDD `-1.95`
- `market_context_high->unknown_4h` score `10.201` n `212` status `ready` deltaP `9.1233` edge `0.8588` maxDD `-2.563`
- `market_context_high->unknown_1h` score `8.991` n `215` status `ready` deltaP `-0.8537` edge `0.818` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `3.163` n `48` status `ready` deltaP `18.5764` edge `0.1667` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `1.8355` n `48` status `ready` deltaP `11.6319` edge `0.0926` maxDD `-0.042`
- `news_risk_high->commodity_4h` score `1.6441` n `48` status `ready` deltaP `12.4492` edge `0.0741` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.2423` n `48` status `ready` deltaP `12.8992` edge `0.0566` maxDD `-0.7924`
- `news_risk_high->crypto_major_4h` score `1.103` n `48` status `ready` deltaP `8.7906` edge `0.1415` maxDD `-2.3624`
- `news_risk_high->metal_4h` score `0.8122` n `48` status `ready` deltaP `13.2622` edge `0.042` maxDD `-0.7692`
- `news_risk_high->index_1h` score `0.5987` n `48` status `ready` deltaP `12.1881` edge `0.0091` maxDD `-0.0879`
- `news_risk_high->metal_1h` score `0.2974` n `48` status `ready` deltaP `6.986` edge `0.0123` maxDD `-0.3266`
- `news_risk_high->fx_4h` score `0.2508` n `48` status `ready` deltaP `11.3821` edge `0.0015` maxDD `-0.9514`
- `risk_on_high->metal_1h` score `0.1077` n `133` status `ready` deltaP `12.5625` edge `0.0013` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1077` n `133` status `ready` deltaP `12.5625` edge `0.0013` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `-0.0637` n `48` status `ready` deltaP `5.7635` edge `0.0009` maxDD `-0.9036`
- `news_risk_high->crypto_alt_1h` score `-0.1366` n `48` status `ready` deltaP `3.2435` edge `-0.001` maxDD `-1.7172`
- `risk_on_high->index_1h` score `-0.205` n `133` status `ready` deltaP `3.2439` edge `-0.0034` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
