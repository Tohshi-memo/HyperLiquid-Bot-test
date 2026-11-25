# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T03:22:35.923126+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4080`

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

- `market_context_high->unknown_1h` score `32251.1701` n `45` status `ready` deltaP `2.1656` edge `2687.5925` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21980.0677` n `45` status `ready` deltaP `3.1776` edge `1831.665` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1016.2151` n `31` status `ready` deltaP `2.3807` edge `84.6863` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `727.1202` n `31` status `ready` deltaP `4.3962` edge `60.5697` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.9519` n `31` status `ready` deltaP `50.1736` edge `2.9115` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.9165` n `31` status `ready` deltaP `44.2708` edge `2.9479` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.2271` n `31` status `ready` deltaP `48.9583` edge `2.6092` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.9566` n `31` status `ready` deltaP `27.8275` edge `0.8979` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.2046` n `31` status `ready` deltaP `41.2355` edge `0.6863` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.5371` n `31` status `ready` deltaP `35.243` edge `0.6912` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.4402` n `31` status `ready` deltaP `18.1501` edge `0.9746` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.8662` n `31` status `ready` deltaP `43.4028` edge `0.1995` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.4521` n `31` status `ready` deltaP `46.2254` edge `0.159` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7484` n `31` status `ready` deltaP `19.3886` edge `0.2018` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.1633` n `31` status `ready` deltaP `34.0234` edge `0.0628` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.754` n `31` status `ready` deltaP `12.5555` edge `0.3155` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.6303` n `31` status `ready` deltaP `31.0943` edge `0.0204` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.6102` n `45` status `ready` deltaP `31.9173` edge `0.0332` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4125` n `31` status `ready` deltaP `12.7052` edge `0.2603` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5796` n `31` status `ready` deltaP `30.0318` edge `0.0302` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
