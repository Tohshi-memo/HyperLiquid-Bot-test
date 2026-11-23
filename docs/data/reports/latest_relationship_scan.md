# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T19:52:27.882935+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4664`

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

- `market_context_high->unknown_1h` score `32466.9553` n `45` status `ready` deltaP `2.6147` edge `2705.5716` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22306.3146` n `45` status `ready` deltaP `3.4824` edge `1858.8502` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1257.4259` n `31` status `ready` deltaP `2.8298` edge `104.7842` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1070.9614` n `31` status `ready` deltaP `4.701` edge `89.2211` maxDD `-0.119`
- `news_risk_high->equity_24h` score `40.3479` n `31` status `ready` deltaP `45.1389` edge `3.0614` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `35.3218` n `31` status `ready` deltaP `46.5278` edge `2.6333` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.1758` n `31` status `ready` deltaP `46.5278` edge `2.2878` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.6276` n `31` status `ready` deltaP `46.6174` edge `0.769` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `9.9854` n `31` status `ready` deltaP `22.4921` edge `0.7692` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.5935` n `31` status `ready` deltaP `30.5173` edge `0.5609` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.3277` n `31` status `ready` deltaP `53.6907` edge `0.1822` maxDD `-0.0262`
- `news_risk_high->index_24h` score `6.267` n `31` status `ready` deltaP `43.4028` edge `0.2329` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.1297` n `31` status `ready` deltaP `12.3574` edge `0.8452` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.266` n `31` status `ready` deltaP `18.191` edge `0.1696` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1868` n `45` status `ready` deltaP `38.0149` edge `0.0406` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.9113` n `31` status `ready` deltaP `32.1942` edge `0.054` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.532` n `31` status `ready` deltaP `30.1961` edge `0.0182` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4344` n `31` status `ready` deltaP `10.7591` edge `0.2865` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0525` n `31` status `ready` deltaP `9.7112` edge `0.2341` maxDD `-1.5232`
- `market_context_high->commodity_24h` score `1.6343` n `39` status `ready` deltaP `4.0599` edge `0.2645` maxDD `-2.5636`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
