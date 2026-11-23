# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T21:37:28.421412+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4572`

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

- `market_context_high->unknown_1h` score `32435.7769` n `45` status `ready` deltaP `2.6147` edge `2702.9734` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22268.415` n `45` status `ready` deltaP `3.4824` edge `1855.6919` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1226.2475` n `31` status `ready` deltaP `2.8298` edge `102.186` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1033.0618` n `31` status `ready` deltaP `4.701` edge `86.0628` maxDD `-0.119`
- `news_risk_high->equity_24h` score `39.2518` n `31` status `ready` deltaP `44.0972` edge `2.977` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `35.0666` n `31` status `ready` deltaP `46.0069` edge `2.6155` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.959` n `31` status `ready` deltaP `46.0069` edge `2.2732` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.4483` n `31` status `ready` deltaP `45.5758` edge `0.761` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.181` n `31` status `ready` deltaP `22.4921` edge `0.7855` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6721` n `31` status `ready` deltaP `30.9747` edge `0.5644` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.4429` n `31` status `ready` deltaP `54.9059` edge `0.1837` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.2701` n `31` status `ready` deltaP `12.3574` edge `0.8632` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.0666` n `31` status `ready` deltaP `42.1875` edge `0.2243` maxDD `0.0`
- `market_context_high->fx_4h` score `3.266` n `45` status `ready` deltaP `38.9295` edge `0.0411` maxDD `-0.2774`
- `news_risk_high->equity_1h` score `3.2528` n `31` status `ready` deltaP `18.191` edge `0.1685` maxDD `-0.163`
- `news_risk_high->index_4h` score `2.9393` n `31` status `ready` deltaP `32.499` edge `0.0543` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5189` n `31` status `ready` deltaP `30.0464` edge `0.0181` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.51` n `31` status `ready` deltaP `11.2082` edge `0.2932` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1335` n `31` status `ready` deltaP `10.4597` edge `0.2395` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5461` n `31` status `ready` deltaP `29.8821` edge `0.0269` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
