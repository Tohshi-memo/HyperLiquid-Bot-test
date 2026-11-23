# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T11:52:28.282571+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4482`

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

- `market_context_high->unknown_1h` score `23154.4598` n `61` status `ready` deltaP `0.3435` edge `1929.5522` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `15549.6579` n `61` status `ready` deltaP `4.6481` edge `1295.7877` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1297.6942` n `31` status `ready` deltaP `3.728` edge `108.1339` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1111.4386` n `31` status `ready` deltaP `4.701` edge `92.5942` maxDD `-0.119`
- `news_risk_high->equity_24h` score `45.4484` n `31` status `ready` deltaP `50.6944` edge `3.4494` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.9981` n `31` status `ready` deltaP `48.6111` edge `2.7591` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.5828` n `31` status `ready` deltaP `48.7847` edge `2.39` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.4898` n `31` status `ready` deltaP `51.3049` edge `0.8096` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.3992` n `31` status `ready` deltaP `33.1088` edge `0.6941` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.1778` n `31` status `ready` deltaP `21.8823` edge `0.7893` maxDD `-5.2957`
- `news_risk_high->index_24h` score `7.1313` n `31` status `ready` deltaP `48.6111` edge `0.2702` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.3536` n `31` status `ready` deltaP `53.8643` edge `0.1832` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.2046` n `31` status `ready` deltaP `11.4427` edge `0.8609` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7027` n `31` status `ready` deltaP `18.7898` edge `0.202` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.2803` n `31` status `ready` deltaP `34.4808` edge `0.0695` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6363` n `31` status `ready` deltaP `30.9446` edge `0.0219` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3745` n `31` status `ready` deltaP `9.1124` edge `0.2898` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9715` n `31` status `ready` deltaP `7.7651` edge `0.2367` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5228` n `31` status `ready` deltaP `28.9839` edge `0.0299` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4642` n `31` status `ready` deltaP `20.4366` edge `0.1072` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
