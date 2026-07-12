# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T02:22:29.814597+00:00`
- Price records: `672`
- Market context records: `6453`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.7298` n `32` status `ready` deltaP `30.0347` edge `0.792` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.9263` n `145` status `ready` deltaP `17.5574` edge `0.8735` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.307` n `32` status `ready` deltaP `52.2569` edge `0.1772` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0962` n `32` status `ready` deltaP `42.6067` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.7791` n `32` status `ready` deltaP `33.1597` edge `0.1144` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.3888` n `32` status `ready` deltaP `12.1528` edge `0.4314` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4697` n `32` status `ready` deltaP `29.7904` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4672` n `32` status `ready` deltaP `13.2298` edge `0.1466` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.3919` n `176` status `ready` deltaP `-5.8655` edge `0.2452` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.8295` n `32` status `ready` deltaP `9.2253` edge `0.091` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.1621` n `176` status `ready` deltaP `8.2871` edge `0.0259` maxDD `-0.4108`
- `market_context_high->crypto_alt_4h` score `0.0573` n `176` status `ready` deltaP `7.7467` edge `0.1085` maxDD `-6.7632`
- `market_context_high->commodity_24h` score `0.0019` n `145` status `ready` deltaP `4.6468` edge `0.156` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `-0.019` n `176` status `ready` deltaP `-15.2578` edge `0.3407` maxDD `-10.5788`
- `market_context_high->metal_4h` score `-0.0509` n `176` status `ready` deltaP `9.3265` edge `0.0424` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.2475` n `32` status `ready` deltaP `5.7822` edge `-0.0247` maxDD `-0.7581`
- `news_risk_high->metal_1h` score `-0.5059` n `32` status `ready` deltaP `1.3473` edge `-0.0241` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.5361` n `176` status `ready` deltaP `6.6685` edge `0.0181` maxDD `-5.8368`
- `news_risk_high->index_24h` score `-0.5719` n `32` status `ready` deltaP `3.125` edge `-0.007` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.5862` n `176` status `ready` deltaP `0.2109` edge `0.0012` maxDD `-1.8877`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
