# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T06:22:29.021133+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11632`

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

- `market_context_high->unknown_24h` score `14.812` n `88` status `ready` deltaP `13.0997` edge `1.1513` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.6891` n `90` status `ready` deltaP `2.5101` edge `0.5569` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5944` n `90` status `ready` deltaP `17.3849` edge `0.1016` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.171` n `88` status `ready` deltaP `2.6199` edge `0.2495` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.1664` n `88` status `ready` deltaP `27.5568` edge `0.0864` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3374` n `92` status `ready` deltaP `6.333` edge `0.0275` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.0735` n `90` status `ready` deltaP `13.1572` edge `0.0077` maxDD `-1.8797`
- `market_context_high->fx_1h` score `-0.0127` n `92` status `ready` deltaP `5.7017` edge `-0.0041` maxDD `-0.7973`
- `market_context_high->metal_1h` score `-0.4617` n `92` status `ready` deltaP `-0.4426` edge `-0.0068` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6463` n `92` status `ready` deltaP `-1.3733` edge `-0.0203` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7907` n `90` status `ready` deltaP `2.8794` edge `0.0029` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.8492` n `92` status `ready` deltaP `-3.0331` edge `-0.0176` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.0043` n `88` status `ready` deltaP `4.0878` edge `-0.0117` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.3161` n `90` status `ready` deltaP `1.8089` edge `-0.0418` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8687` n `92` status `ready` deltaP `2.4148` edge `-0.1021` maxDD `-10.619`
- `market_context_high->index_24h` score `-1.9825` n `88` status `ready` deltaP `-7.1969` edge `0.0133` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.1209` n `90` status `ready` deltaP `-13.0454` edge `-0.0595` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.2931` n `92` status `ready` deltaP `2.8899` edge `-0.249` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.324` n `92` status `ready` deltaP `-10.7199` edge `-0.0682` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.5467` n `88` status `ready` deltaP `7.3548` edge `-0.0922` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
