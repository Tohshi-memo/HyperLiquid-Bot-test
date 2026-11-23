# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T10:37:39.735377+00:00`
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

- `market_context_high->unknown_1h` score `21150.1271` n `66` status `ready` deltaP `0.7893` edge `1762.5215` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `14124.7797` n `66` status `ready` deltaP `4.8965` edge `1177.0462` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1297.8311` n `31` status `ready` deltaP `3.4286` edge `108.1473` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1131.6118` n `31` status `ready` deltaP `4.701` edge `94.2753` maxDD `-0.119`
- `news_risk_high->equity_24h` score `46.0374` n `31` status `ready` deltaP `51.5625` edge `3.4927` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `37.0485` n `31` status `ready` deltaP `48.6111` edge `2.7633` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.6044` n `31` status `ready` deltaP `48.7847` edge `2.3918` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.6181` n `31` status `ready` deltaP `52.173` edge `0.8145` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.5766` n `31` status `ready` deltaP `33.871` edge `0.7038` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.1674` n `31` status `ready` deltaP `22.1872` edge `0.7864` maxDD `-5.2957`
- `news_risk_high->index_24h` score `7.2463` n `31` status `ready` deltaP `49.4792` edge `0.274` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.4495` n `31` status `ready` deltaP `54.7323` edge `0.1854` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.2119` n `31` status `ready` deltaP `11.7476` edge `0.8598` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.6524` n `31` status `ready` deltaP `18.3407` edge `0.2008` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.3544` n `31` status `ready` deltaP `35.243` edge `0.0706` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6363` n `31` status `ready` deltaP `30.9446` edge `0.0219` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3628` n `31` status `ready` deltaP `9.1124` edge `0.2883` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9505` n `31` status `ready` deltaP `7.6154` edge `0.235` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5096` n `31` status `ready` deltaP `28.8342` edge `0.0292` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4357` n `31` status `ready` deltaP `19.9793` edge `0.1066` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
