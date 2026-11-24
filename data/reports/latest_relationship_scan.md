# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T05:22:29.015137+00:00`
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

- `market_context_high->unknown_1h` score `32360.3054` n `45` status `ready` deltaP `2.0159` edge `2696.6881` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22196.2223` n `45` status `ready` deltaP `1.958` edge `1849.686` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1150.776` n `31` status `ready` deltaP `2.231` edge `95.9007` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `960.8691` n `31` status `ready` deltaP `3.1766` edge `80.0569` maxDD `-0.119`
- `news_risk_high->equity_24h` score `35.6594` n `31` status `ready` deltaP `41.4931` edge `2.695` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9243` n `31` status `ready` deltaP `45.8333` edge `2.6048` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.5412` n `31` status `ready` deltaP `44.4444` edge `2.2488` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.6349` n `31` status `ready` deltaP `41.4091` edge `0.721` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.6288` n `31` status `ready` deltaP `23.5592` edge `0.8157` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6227` n `31` status `ready` deltaP `30.8222` edge `0.5613` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6651` n `31` status `ready` deltaP `56.4684` edge `0.1918` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.6171` n `31` status `ready` deltaP `14.1866` edge `0.8955` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.411` n `31` status `ready` deltaP `39.0625` edge `0.1905` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.1869` n `31` status `ready` deltaP `17.4425` edge `0.168` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1308` n `45` status `ready` deltaP `37.4051` edge `0.04` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.7096` n `31` status `ready` deltaP `30.2125` edge `0.0504` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.5101` n `31` status `ready` deltaP `10.9088` edge `0.2952` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.423` n `31` status `ready` deltaP `28.9985` edge `0.0171` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.1195` n `31` status `ready` deltaP `10.31` edge `0.2387` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6419` n `31` status `ready` deltaP `31.2294` edge `0.0302` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
