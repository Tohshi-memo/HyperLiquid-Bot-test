# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T05:07:31.691794+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4560`

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

- `market_context_high->unknown_1h` score `32360.321` n `45` status `ready` deltaP `2.0159` edge `2696.6894` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22199.1985` n `45` status `ready` deltaP `2.1105` edge `1849.933` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1150.7916` n `31` status `ready` deltaP `2.231` edge `95.902` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `963.8453` n `31` status `ready` deltaP `3.3291` edge `80.3039` maxDD `-0.119`
- `news_risk_high->equity_24h` score `35.7518` n `31` status `ready` deltaP `41.4931` edge `2.7027` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9279` n `31` status `ready` deltaP `45.8333` edge `2.6051` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.579` n `31` status `ready` deltaP `44.6181` edge `2.2508` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.6505` n `31` status `ready` deltaP `41.4091` edge `0.7223` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.6602` n `31` status `ready` deltaP `23.7116` edge `0.8173` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6275` n `31` status `ready` deltaP `30.8222` edge `0.5617` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6615` n `31` status `ready` deltaP `56.4684` edge `0.1915` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.6249` n `31` status `ready` deltaP `14.1866` edge `0.8965` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.4242` n `31` status `ready` deltaP `39.0625` edge `0.1916` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2109` n `31` status `ready` deltaP `17.5922` edge `0.169` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1308` n `45` status `ready` deltaP `37.4051` edge `0.04` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.7108` n `31` status `ready` deltaP `30.2125` edge `0.0505` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.528` n `31` status `ready` deltaP `11.0585` edge `0.2965` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.435` n `31` status `ready` deltaP `29.1482` edge `0.0171` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.139` n `31` status `ready` deltaP `10.4597` edge `0.2402` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6435` n `31` status `ready` deltaP `31.2294` edge `0.0304` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
