# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T02:52:24.043059+00:00`
- Price records: `672`
- Market context records: `6455`
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

- `news_risk_high->crypto_alt_24h` score `11.7888` n `32` status `ready` deltaP `30.3819` edge `0.7946` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.7266` n `145` status `ready` deltaP `17.0414` edge `0.8603` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.307` n `32` status `ready` deltaP `52.2569` edge `0.1772` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.084` n `32` status `ready` deltaP `42.4543` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.7213` n `32` status `ready` deltaP `32.8125` edge `0.1119` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.4365` n `32` status `ready` deltaP `12.5` edge `0.4352` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4578` n `32` status `ready` deltaP `29.6407` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4485` n `32` status `ready` deltaP `13.0801` edge `0.1452` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.4366` n `174` status `ready` deltaP `-6.0414` edge `0.2501` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.8061` n `32` status `ready` deltaP `8.9259` edge `0.09` maxDD `-1.6923`
- `market_context_high->crypto_alt_4h` score `0.2536` n `174` status `ready` deltaP `8.4455` edge `0.1202` maxDD `-6.7632`
- `market_context_high->index_4h` score `0.2312` n `174` status `ready` deltaP `9.0447` edge `0.0266` maxDD `-0.4108`
- `market_context_high->commodity_24h` score `0.1744` n `145` status `ready` deltaP `5.6789` edge `0.1635` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `0.1518` n `174` status `ready` deltaP `-15.1774` edge `0.3544` maxDD `-10.5788`
- `market_context_high->metal_4h` score `0.0108` n `174` status `ready` deltaP `9.9927` edge `0.0431` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.2655` n `32` status `ready` deltaP `5.6325` edge `-0.0252` maxDD `-0.7581`
- `market_context_high->crypto_alt_1h` score `-0.5006` n `174` status `ready` deltaP `7.0222` edge `0.0203` maxDD `-5.8368`
- `news_risk_high->metal_1h` score `-0.5059` n `32` status `ready` deltaP `1.3473` edge `-0.0241` maxDD `-1.6464`
- `news_risk_high->index_24h` score `-0.5484` n `32` status `ready` deltaP `3.4722` edge `-0.0063` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.5562` n `174` status `ready` deltaP `0.7726` edge `0.0013` maxDD `-1.8877`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
