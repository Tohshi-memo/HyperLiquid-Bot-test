# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T10:07:29.468803+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14748`

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

- `news_risk_high->unknown_24h` score `50.8913` n `50` status `ready` deltaP `11.5717` edge `4.1638` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.8584` n `50` status `ready` deltaP `37.6235` edge `1.2815` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6196` n `50` status `ready` deltaP `26.4695` edge `0.8851` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `4.8685` n `50` status `ready` deltaP `25.6235` edge `0.3277` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `4.0478` n `50` status `ready` deltaP `47.1829` edge `0.0318` maxDD `-0.0559`
- `news_risk_high->metal_24h` score `3.8724` n `50` status `ready` deltaP `42.5596` edge `0.0432` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `3.589` n `130` status `ready` deltaP `24.7772` edge `0.1746` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.9071` n `50` status `ready` deltaP `16.5269` edge `0.1677` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.783` n `50` status `ready` deltaP `30.6598` edge `0.0426` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `1.6629` n `129` status `ready` deltaP `5.3701` edge `0.176` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5084` n `50` status `ready` deltaP `20.2036` edge `0.008` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.3419` n `136` status `ready` deltaP `11.5269` edge `0.08` maxDD `-1.6015`
- `news_risk_high->equity_1h` score `1.1763` n `50` status `ready` deltaP `16.515` edge `0.0158` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `0.8283` n `50` status `ready` deltaP `18.5305` edge `0.0218` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5931` n `50` status `ready` deltaP `15.497` edge `0.004` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1507` n `50` status `ready` deltaP `7.8084` edge `0.0012` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0944` n `50` status `ready` deltaP `5.4012` edge `-0.0013` maxDD `-0.1413`
- `news_risk_high->index_4h` score `-0.0807` n `50` status `ready` deltaP `5.1037` edge `-0.0011` maxDD `-0.1719`
- `news_risk_high->metal_4h` score `-0.2604` n `50` status `ready` deltaP `6.0915` edge `-0.0092` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4422` n `136` status `ready` deltaP `2.6154` edge `-0.0009` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
