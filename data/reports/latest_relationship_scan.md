# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T16:07:15.802314+00:00`
- Price records: `672`
- Market context records: `1753`
- Flow alert records: `6947`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8862`

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

- `market_context_high->metal_24h` score `7.173` n `164` status `ready` deltaP `27.113` edge `0.6596` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.9575` n `196` status `ready` deltaP `20.6664` edge `0.5353` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.383` n `196` status `ready` deltaP `22.2623` edge `0.4574` maxDD `-10.9117`
- `market_context_high->index_24h` score `4.1975` n `164` status `ready` deltaP `18.8601` edge `0.3469` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `3.9713` n `164` status `ready` deltaP `15.0576` edge `0.7626` maxDD `-35.8966`
- `news_risk_high->commodity_1h` score `3.1666` n `30` status `ready` deltaP `24.8703` edge `0.1298` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.0201` n `196` status `ready` deltaP `16.2643` edge `0.2527` maxDD `-5.0894`
- `market_context_high->unknown_4h` score `2.8587` n `196` status `ready` deltaP `12.7271` edge `0.3805` maxDD `-11.1695`
- `market_context_high->equity_24h` score `2.8207` n `164` status `ready` deltaP `17.1155` edge `0.6108` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.8613` n `196` status `ready` deltaP `11.5605` edge `0.1036` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.7933` n `196` status `ready` deltaP `7.5706` edge `0.118` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.5478` n `164` status `ready` deltaP `19.3851` edge `0.775` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.2376` n `196` status `ready` deltaP `4.8974` edge `0.0945` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.097` n `196` status `ready` deltaP `5.2701` edge `0.0538` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1652` n `196` status `ready` deltaP `4.2161` edge `0.0213` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.2459` n `196` status `ready` deltaP `12.444` edge `0.1547` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.498` n `196` status `ready` deltaP `6.095` edge `0.0291` maxDD `-6.3532`
- `news_risk_high->fx_1h` score `-0.5091` n `30` status `ready` deltaP `-5.7285` edge `-0.0009` maxDD `-0.0948`
- `news_risk_high->unknown_1h` score `-0.5674` n `30` status `ready` deltaP `15.9581` edge `-0.1319` maxDD `-2.1115`
- `market_context_high->fx_24h` score `-0.6235` n `164` status `ready` deltaP `6.9825` edge `0.0064` maxDD `-1.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
