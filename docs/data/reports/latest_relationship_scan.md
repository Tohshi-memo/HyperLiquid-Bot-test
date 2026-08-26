# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T00:52:30.486660+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `45.7493` n `51` status `ready` deltaP `10.4167` edge `3.743` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.7468` n `53` status `ready` deltaP `25.2847` edge `0.9036` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.0977` n `51` status `ready` deltaP `29.9939` edge `0.4846` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.9824` n `51` status `ready` deltaP `40.2676` edge `0.0786` maxDD `-0.2147`
- `news_risk_high->crypto_alt_24h` score `3.8292` n `51` status `ready` deltaP `26.9097` edge `0.1397` maxDD `0.0`
- `news_risk_high->unknown_1h` score `3.4225` n `53` status `ready` deltaP `16.7608` edge `0.209` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `2.9045` n `53` status `ready` deltaP `34.8108` edge `0.0234` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.7882` n `133` status `ready` deltaP `23.4263` edge `0.117` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.593` n `53` status `ready` deltaP `18.9744` edge `0.0833` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.0854` n `53` status `ready` deltaP `15.1706` edge `0.0063` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `0.9185` n `51` status `ready` deltaP `28.4211` edge `-0.1087` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.5038` n `53` status `ready` deltaP `11.575` edge `-0.0039` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4661` n `53` status `ready` deltaP `13.3742` edge `0.007` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.4049` n `133` status `ready` deltaP `12.3204` edge `-0.0035` maxDD `-1.5916`
- `news_risk_high->index_4h` score `0.0077` n `53` status `ready` deltaP `5.4418` edge `0.0041` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0472` n `53` status `ready` deltaP `4.299` edge `0.0006` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4857` n `133` status `ready` deltaP `1.7503` edge `-0.0007` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5385` n `53` status `ready` deltaP `-1.5111` edge `-0.0122` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.6725` n `53` status `ready` deltaP `3.5952` edge `-0.0269` maxDD `-0.249`
- `market_context_high->unknown_24h` score `-0.7703` n `127` status `ready` deltaP `8.8419` edge `-0.1036` maxDD `-0.8965`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
