# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T10:52:31.558363+00:00`
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

- `market_context_high->unknown_1h` score `32338.6119` n `45` status `ready` deltaP `1.5668` edge `2694.8833` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22177.9458` n `45` status `ready` deltaP `2.5678` edge `1848.1589` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1129.0825` n `31` status `ready` deltaP `1.7819` edge `94.0959` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `942.5927` n `31` status `ready` deltaP `3.7864` edge `78.5298` maxDD `-0.119`
- `news_risk_high->crypto_major_24h` score `35.8382` n `31` status `ready` deltaP `48.4375` edge `2.6636` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.8122` n `31` status `ready` deltaP `41.4931` edge `2.6244` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.0028` n `31` status `ready` deltaP `46.1806` edge `2.2757` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.3385` n `31` status `ready` deltaP `41.4091` edge `0.6963` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.8704` n `31` status `ready` deltaP `23.864` edge `0.8338` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.3053` n `31` status `ready` deltaP `32.499` edge `0.607` maxDD `-2.1911`
- `news_risk_high->crypto_major_4h` score `6.8379` n `31` status `ready` deltaP `15.1013` edge `0.9177` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.7047` n `31` status `ready` deltaP `56.4684` edge `0.1951` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.2202` n `31` status `ready` deltaP `39.0625` edge `0.1746` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4628` n `31` status `ready` deltaP `18.6401` edge `0.183` maxDD `-0.163`
- `market_context_high->fx_4h` score `2.9593` n `45` status `ready` deltaP `35.5759` edge `0.0379` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.8868` n `31` status `ready` deltaP `31.7369` edge `0.055` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.5763` n `31` status `ready` deltaP `11.2082` edge `0.3017` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5656` n `31` status `ready` deltaP `30.4955` edge `0.019` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2255` n `31` status `ready` deltaP `11.0585` edge `0.2473` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6668` n `31` status `ready` deltaP `31.5288` edge `0.0314` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
