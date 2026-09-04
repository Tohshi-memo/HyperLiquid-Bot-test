# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T23:52:26.664805+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10684`

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

- `risk_on_high->unknown_4h` score `19.9435` n `133` status `ready` deltaP `8.9985` edge `1.6638` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.9435` n `133` status `ready` deltaP `8.9985` edge `1.6638` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `9.446` n `217` status `ready` deltaP `9.4351` edge `0.7938` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `5.0034` n `44` status `ready` deltaP `21.2122` edge `0.3025` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `2.5708` n `44` status `ready` deltaP `11.1835` edge `0.187` maxDD `-1.4523`
- `news_risk_high->commodity_24h` score `2.4808` n `44` status `ready` deltaP `15.1989` edge `0.1226` maxDD `-0.042`
- `news_risk_high->commodity_4h` score `1.6296` n `44` status `ready` deltaP `11.3082` edge `0.0805` maxDD `-0.2737`
- `news_risk_high->metal_4h` score `1.6259` n `44` status `ready` deltaP `16.796` edge `0.0498` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.551` n `44` status `ready` deltaP `14.4938` edge `0.0717` maxDD `-0.7924`
- `news_risk_high->index_1h` score `1.2185` n `44` status `ready` deltaP `15.4872` edge `0.0117` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `0.6636` n `44` status `ready` deltaP `8.4921` edge `0.018` maxDD `-0.2118`
- `news_risk_high->commodity_1h` score `0.2906` n `44` status `ready` deltaP `9.6217` edge `0.0047` maxDD `-0.9036`
- `news_risk_high->fx_4h` score `0.2515` n `44` status `ready` deltaP `10.0471` edge `-0.0008` maxDD `-0.9514`
- `news_risk_high->crypto_major_1h` score `0.2186` n `44` status `ready` deltaP `0.4763` edge `0.0483` maxDD `-0.8762`
- `risk_on_high->metal_1h` score `0.1459` n `133` status `ready` deltaP `13.311` edge `0.0012` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1459` n `133` status `ready` deltaP `13.311` edge `0.0012` maxDD `-1.699`
- `news_risk_high->crypto_alt_1h` score `0.1096` n `44` status `ready` deltaP `2.7763` edge `0.0209` maxDD `-1.0885`
- `news_risk_high->crypto_alt_4h` score `0.0704` n `44` status `ready` deltaP `1.9124` edge `0.0283` maxDD `-1.4811`
- `risk_on_high->index_1h` score `-0.2213` n `133` status `ready` deltaP `2.9445` edge `-0.0035` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.2213` n `133` status `ready` deltaP `2.9445` edge `-0.0035` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
