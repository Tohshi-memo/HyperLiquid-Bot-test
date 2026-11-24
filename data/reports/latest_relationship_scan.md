# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T04:07:36.531111+00:00`
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

- `market_context_high->unknown_1h` score `32366.5418` n `45` status `ready` deltaP `2.1656` edge `2697.2068` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22211.0274` n `45` status `ready` deltaP `2.5678` edge `1850.9157` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1157.0124` n `31` status `ready` deltaP `2.3807` edge `96.4194` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `975.6743` n `31` status `ready` deltaP `3.7864` edge `81.2866` maxDD `-0.119`
- `news_risk_high->equity_24h` score `36.2195` n `31` status `ready` deltaP `42.0139` edge `2.7382` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9928` n `31` status `ready` deltaP `46.1806` edge `2.6082` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.7414` n `31` status `ready` deltaP `45.3125` edge `2.2597` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.7503` n `31` status `ready` deltaP `41.7563` edge `0.7283` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.7364` n `31` status `ready` deltaP `24.1689` edge `0.8206` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6323` n `31` status `ready` deltaP `30.8222` edge `0.5621` maxDD `-2.1911`
- `news_risk_high->crypto_major_4h` score `6.6508` n `31` status `ready` deltaP `14.3391` edge `0.8988` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.6447` n `31` status `ready` deltaP `56.4684` edge `0.1901` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.5235` n `31` status `ready` deltaP `39.5833` edge `0.1964` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.29` n `31` status `ready` deltaP `18.191` edge `0.1716` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1552` n `45` status `ready` deltaP `37.71` edge `0.04` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.7388` n `31` status `ready` deltaP `30.5173` edge `0.0508` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.5755` n `31` status `ready` deltaP `11.3579` edge `0.3006` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4745` n `31` status `ready` deltaP `29.5973` edge `0.0174` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.1927` n `31` status `ready` deltaP `10.7591` edge `0.2451` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6232` n `31` status `ready` deltaP `30.93` edge `0.0298` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
