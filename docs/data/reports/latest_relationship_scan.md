# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T09:22:26.060142+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4584`

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

- `market_context_high->unknown_1h` score `32328.4803` n `45` status `ready` deltaP `1.4171` edge `2694.04` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22192.4646` n `45` status `ready` deltaP `2.5678` edge `1849.3688` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1118.9509` n `31` status `ready` deltaP `1.6322` edge `93.2526` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `957.1115` n `31` status `ready` deltaP `3.7864` edge `79.7397` maxDD `-0.119`
- `news_risk_high->crypto_major_24h` score `35.4201` n `31` status `ready` deltaP `47.3958` edge `2.6357` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.721` n `31` status `ready` deltaP `41.4931` edge `2.6168` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.6387` n `31` status `ready` deltaP `45.1389` edge `2.2523` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.4033` n `31` status `ready` deltaP `41.4091` edge `0.7017` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.4744` n `31` status `ready` deltaP `22.9494` edge `0.8069` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.8721` n `31` status `ready` deltaP `31.5844` edge `0.577` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.7023` n `31` status `ready` deltaP `56.4684` edge `0.1949` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.6093` n `31` status `ready` deltaP `14.1866` edge `0.8945` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.2382` n `31` status `ready` deltaP `39.0625` edge `0.1761` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2577` n `31` status `ready` deltaP `17.8916` edge `0.1709` maxDD `-0.163`
- `market_context_high->fx_4h` score `2.9896` n `45` status `ready` deltaP `35.8807` edge `0.0384` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.7788` n `31` status `ready` deltaP `30.8222` edge `0.0521` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.5148` n `31` status `ready` deltaP `10.9088` edge `0.2958` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4781` n `31` status `ready` deltaP `29.5973` edge `0.0177` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.128` n `31` status `ready` deltaP `10.4597` edge `0.2388` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6365` n `31` status `ready` deltaP `31.0797` edge `0.0305` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
