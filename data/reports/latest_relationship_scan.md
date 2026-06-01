# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T12:07:26.673189+00:00`
- Price records: `672`
- Market context records: `2559`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9198`

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

- `market_context_high->crypto_alt_4h` score `5.7441` n `149` status `ready` deltaP `25.1658` edge `0.5788` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `5.0495` n `118` status `ready` deltaP `18.7823` edge `0.3284` maxDD `-1.626`
- `market_context_high->crypto_major_24h` score `4.8229` n `118` status `ready` deltaP `12.1704` edge `0.5861` maxDD `-15.2264`
- `market_context_high->crypto_major_4h` score `3.9363` n `149` status `ready` deltaP `17.4486` edge `0.3927` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.6283` n `149` status `ready` deltaP `9.6998` edge `0.176` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.2384` n `149` status `ready` deltaP `10.0259` edge `0.1551` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.1856` n `118` status `ready` deltaP `18.9972` edge `0.0305` maxDD `-2.0014`
- `market_context_high->crypto_major_1h` score `0.6814` n `149` status `ready` deltaP `8.2345` edge `0.1213` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6696` n `118` status `ready` deltaP `6.6119` edge `0.1098` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.1542` n `118` status `ready` deltaP `-0.9592` edge `0.6666` maxDD `-39.2351`
- `market_context_high->index_4h` score `0.0658` n `149` status `ready` deltaP `7.2945` edge `0.041` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1621` n `149` status `ready` deltaP `3.7486` edge `0.0109` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.3456` n `149` status `ready` deltaP `2.1169` edge `0.0261` maxDD `-2.8543`
- `market_context_high->metal_1h` score `-0.4425` n `149` status `ready` deltaP `1.1614` edge `0.0103` maxDD `-2.9823`
- `market_context_high->commodity_1h` score `-0.535` n `149` status `ready` deltaP `4.2077` edge `0.0152` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.5405` n `149` status `ready` deltaP `0.635` edge `0.0042` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.7506` n `149` status `ready` deltaP `0.1507` edge `0.0203` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.7659` n `118` status `ready` deltaP `0.9093` edge `0.0034` maxDD `-1.946`
- `market_context_high->fx_4h` score `-0.8439` n `149` status `ready` deltaP `0.4562` edge `0.0126` maxDD `-0.8774`
- `market_context_high->metal_4h` score `-0.8878` n `149` status `ready` deltaP `3.5348` edge `0.0412` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
