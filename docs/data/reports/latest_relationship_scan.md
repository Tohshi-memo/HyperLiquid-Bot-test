# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T10:22:31.321797+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4308`

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

- `market_context_high->unknown_1h` score `32338.7415` n `45` status `ready` deltaP `1.4171` edge `2694.8951` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22183.6326` n `45` status `ready` deltaP `2.5678` edge `1848.6328` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1129.2121` n `31` status `ready` deltaP `1.6322` edge `94.1077` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `948.2795` n `31` status `ready` deltaP `3.7864` edge `79.0037` maxDD `-0.119`
- `news_risk_high->crypto_major_24h` score `35.6796` n `31` status `ready` deltaP `48.0903` edge `2.6527` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.7654` n `31` status `ready` deltaP `41.4931` edge `2.6205` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.8635` n `31` status `ready` deltaP `45.8333` edge `2.2664` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.3613` n `31` status `ready` deltaP `41.4091` edge `0.6982` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.7296` n `31` status `ready` deltaP `23.5592` edge `0.8241` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.1585` n `31` status `ready` deltaP `32.1942` edge `0.5968` maxDD `-2.1911`
- `news_risk_high->crypto_major_4h` score `6.7526` n `31` status `ready` deltaP `14.7964` edge `0.9088` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.7035` n `31` status `ready` deltaP `56.4684` edge `0.195` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.2226` n `31` status `ready` deltaP `39.0625` edge `0.1748` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.3572` n `31` status `ready` deltaP `18.3407` edge `0.1762` maxDD `-0.163`
- `market_context_high->fx_4h` score `2.9605` n `45` status `ready` deltaP `35.5759` edge `0.038` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.8504` n `31` status `ready` deltaP `31.432` edge `0.054` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5332` n `31` status `ready` deltaP `30.1961` edge `0.0183` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5241` n `31` status `ready` deltaP `10.9088` edge `0.297` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1725` n `31` status `ready` deltaP `10.7591` edge `0.2425` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6559` n `31` status `ready` deltaP `31.3791` edge `0.031` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
