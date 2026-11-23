# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T19:37:29.647847+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4518`

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

- `market_context_high->unknown_1h` score `32463.9241` n `45` status `ready` deltaP `2.6147` edge `2705.319` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22305.3894` n `45` status `ready` deltaP `3.4824` edge `1858.7731` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1254.3947` n `31` status `ready` deltaP `2.8298` edge `104.5316` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1070.0362` n `31` status `ready` deltaP `4.701` edge `89.144` maxDD `-0.119`
- `news_risk_high->equity_24h` score `40.5214` n `31` status `ready` deltaP `45.3125` edge `3.0747` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `35.3777` n `31` status `ready` deltaP `46.7014` edge `2.6368` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.2317` n `31` status `ready` deltaP `46.7014` edge `2.2913` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.6559` n `31` status `ready` deltaP `46.791` edge `0.7702` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `9.9518` n `31` status `ready` deltaP `22.4921` edge `0.7664` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.5839` n `31` status `ready` deltaP `30.5173` edge `0.5601` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.3114` n `31` status `ready` deltaP `53.517` edge `0.182` maxDD `-0.0262`
- `news_risk_high->index_24h` score `6.2965` n `31` status `ready` deltaP `43.5764` edge `0.2342` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.0867` n `31` status `ready` deltaP `12.2049` edge `0.8407` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.2672` n `31` status `ready` deltaP `18.191` edge `0.1697` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1856` n `45` status `ready` deltaP `38.0149` edge `0.0405` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.9101` n `31` status `ready` deltaP `32.1942` edge `0.0539` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.532` n `31` status `ready` deltaP `30.1961` edge `0.0182` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4181` n `31` status `ready` deltaP `10.6094` edge `0.2854` maxDD `-1.6897`
- `market_context_high->commodity_24h` score `2.0347` n `38` status `ready` deltaP `5.2358` edge `0.308` maxDD `-2.5636`
- `news_risk_high->crypto_alt_1h` score `2.0337` n `31` status `ready` deltaP `9.5615` edge `0.2327` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
