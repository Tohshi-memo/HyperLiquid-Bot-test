# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T16:22:25.903057+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4053`

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

- `market_context_high->unknown_24h` score `1495.7588` n `98` status `ready` deltaP `3.4602` edge `124.6235` maxDD `0.0`
- `news_risk_high->equity_24h` score `59.9388` n `47` status `ready` deltaP `67.6838` edge `4.6143` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.5907` n `47` status `ready` deltaP `31.5983` edge `2.1589` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `16.1811` n `47` status `ready` deltaP `48.495` edge `1.1004` maxDD `-5.0217`
- `market_context_high->crypto_major_24h` score `14.8642` n `98` status `ready` deltaP `44.386` edge `1.9368` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.1033` n `98` status `ready` deltaP `30.4463` edge `1.8175` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.3901` n `47` status `ready` deltaP `59.0333` edge `0.4193` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.8334` n `47` status `ready` deltaP `54.1522` edge `0.3751` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.1433` n `47` status `ready` deltaP `17.0507` edge `1.3809` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `5.8005` n `47` status `ready` deltaP `29.3526` edge `0.3874` maxDD `-5.977`
- `news_risk_high->metal_4h` score `5.7682` n `47` status `ready` deltaP `48.8065` edge `0.1727` maxDD `-0.3915`
- `news_risk_high->crypto_major_4h` score `5.354` n `47` status `ready` deltaP `22.6647` edge `0.3723` maxDD `-4.5116`
- `news_risk_high->equity_1h` score `3.7081` n `47` status `ready` deltaP `21.3785` edge `0.2295` maxDD `-3.7082`
- `news_risk_high->index_4h` score `3.6604` n `47` status `ready` deltaP `33.1311` edge `0.1114` maxDD `-0.5128`
- `news_risk_high->commodity_4h` score `3.2255` n `47` status `ready` deltaP `32.3755` edge `0.0783` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.3322` n `47` status `ready` deltaP `26.2645` edge `0.0447` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3011` n `47` status `ready` deltaP `17.4226` edge `0.0224` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.8333` n `47` status `ready` deltaP `18.0532` edge `0.0751` maxDD `-5.7566`
- `news_risk_high->crypto_alt_1h` score `0.7114` n `47` status `ready` deltaP `16.9735` edge `0.065` maxDD `-5.2896`
- `news_risk_high->metal_24h` score `0.6821` n `47` status `ready` deltaP `17.4336` edge `0.1885` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
