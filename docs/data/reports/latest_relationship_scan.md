# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T08:22:27.847115+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14747`

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

- `news_risk_high->unknown_24h` score `50.5913` n `50` status `ready` deltaP `11.5717` edge `4.1388` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.172` n `50` status `ready` deltaP `37.6235` edge `1.2243` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.598` n `50` status `ready` deltaP `26.4695` edge `0.8833` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.1205` n `50` status `ready` deltaP `25.6235` edge `0.3487` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.9687` n `50` status `ready` deltaP `46.2683` edge `0.0313` maxDD `-0.0559`
- `news_risk_high->metal_24h` score `3.5921` n `50` status `ready` deltaP `41.3506` edge `0.0279` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `3.5371` n `132` status `ready` deltaP `24.8937` edge `0.1695` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.8665` n `50` status `ready` deltaP `31.1779` edge `0.0461` maxDD `-0.2064`
- `news_risk_high->unknown_1h` score `2.864` n `50` status `ready` deltaP `16.0778` edge `0.1671` maxDD `-0.8495`
- `market_context_high->unknown_1h` score `1.5484` n `132` status `ready` deltaP `12.593` edge `0.0901` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `1.4821` n `50` status `ready` deltaP `19.9042` edge `0.0078` maxDD `-0.0257`
- `market_context_high->unknown_24h` score `1.4004` n `131` status `ready` deltaP `5.4648` edge `0.1535` maxDD `-3.1917`
- `news_risk_high->equity_1h` score `1.2111` n `50` status `ready` deltaP `16.6647` edge `0.0177` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.1501` n `50` status `ready` deltaP `19.5976` edge `0.0415` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.6016` n `50` status `ready` deltaP `15.6467` edge `0.0041` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1366` n `50` status `ready` deltaP `7.509` edge `0.0014` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0913` n `50` status `ready` deltaP `5.4012` edge `-0.0017` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.0371` n `50` status `ready` deltaP `6.1707` edge `0.0016` maxDD `-0.1719`
- `news_risk_high->metal_4h` score `-0.2688` n `50` status `ready` deltaP `6.0915` edge `-0.0099` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4091` n `132` status `ready` deltaP `3.2072` edge `-0.0006` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
