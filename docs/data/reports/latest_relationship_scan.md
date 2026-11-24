# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T13:07:30.323412+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4344`

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

- `market_context_high->unknown_1h` score `32315.5131` n `45` status `ready` deltaP `1.5668` edge `2692.9584` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22145.5458` n `45` status `ready` deltaP `2.5678` edge `1845.4589` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1105.9837` n `31` status `ready` deltaP `1.7819` edge `92.171` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `910.1927` n `31` status `ready` deltaP `3.7864` edge `75.8298` maxDD `-0.119`
- `news_risk_high->crypto_major_24h` score `36.1596` n `31` status `ready` deltaP `49.3056` edge `2.6846` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.4992` n `31` status `ready` deltaP `40.625` edge `2.6041` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.3248` n `31` status `ready` deltaP `46.875` edge `2.2979` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.1626` n `31` status `ready` deltaP `41.2355` edge `0.6828` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.004` n `31` status `ready` deltaP `24.1689` edge `0.8429` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.2921` n `31` status `ready` deltaP `32.499` edge `0.6059` maxDD `-2.1911`
- `news_risk_high->crypto_major_4h` score `6.8216` n `31` status `ready` deltaP `15.2537` edge `0.9146` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.665` n `31` status `ready` deltaP `56.1212` edge `0.1941` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.0829` n `31` status `ready` deltaP `38.0208` edge `0.1701` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.5107` n `31` status `ready` deltaP `18.7898` edge `0.186` maxDD `-0.163`
- `market_context_high->fx_4h` score `2.9473` n `45` status `ready` deltaP `35.5759` edge `0.0369` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.8952` n `31` status `ready` deltaP `31.7369` edge `0.0557` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.6122` n `31` status `ready` deltaP `11.6573` edge `0.3033` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5704` n `31` status `ready` deltaP `30.4955` edge `0.0194` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2902` n `31` status `ready` deltaP `11.5076` edge `0.2526` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5983` n `31` status `ready` deltaP `30.4809` edge `0.0296` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
