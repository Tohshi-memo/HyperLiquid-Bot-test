# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T07:52:33.448293+00:00`
- Price records: `672`
- Market context records: `8071`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->equity_24h` score `20.0777` n `80` status `ready` deltaP `36.1005` edge `1.5235` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.3554` n `87` status `ready` deltaP `32.4205` edge `0.5281` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2844` n `80` status `ready` deltaP `35.8752` edge `0.4512` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.8637` n `40` status `ready` deltaP `32.1108` edge `0.1395` maxDD `-1.1944`
- `market_context_high->commodity_24h` score `3.4505` n `80` status `ready` deltaP `30.4701` edge `0.273` maxDD `-10.0877`
- `market_context_high->index_4h` score `3.2821` n `87` status `ready` deltaP `31.5881` edge `0.0817` maxDD `-0.5022`
- `news_risk_high->unknown_1h` score `3.2176` n `40` status `ready` deltaP `4.7455` edge `0.2642` maxDD `-0.8826`
- `market_context_high->index_24h` score `2.8153` n `80` status `ready` deltaP `17.0299` edge `0.1881` maxDD `-1.3621`
- `market_context_high->metal_4h` score `2.4104` n `87` status `ready` deltaP `22.2158` edge `0.115` maxDD `-0.979`
- `market_context_high->equity_1h` score `2.343` n `87` status `ready` deltaP `14.7257` edge `0.1404` maxDD `-2.1322`
- `market_context_high->fx_24h` score `2.1912` n `80` status `ready` deltaP `29.9177` edge `0.0535` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.1146` n `87` status `ready` deltaP `14.8221` edge `0.0208` maxDD `-0.4716`
- `news_risk_high->crypto_major_1h` score `1.0223` n `40` status `ready` deltaP `4.1018` edge `0.0839` maxDD `-0.751`
- `market_context_high->metal_1h` score `0.7512` n `87` status `ready` deltaP `10.775` edge `0.0286` maxDD `-0.6936`
- `news_risk_high->index_1h` score `0.5625` n `40` status `ready` deltaP `7.006` edge `0.0207` maxDD `-0.3089`
- `news_risk_high->crypto_alt_1h` score `0.5071` n `40` status `ready` deltaP `5.5988` edge `0.0567` maxDD `-0.6543`
- `market_context_high->crypto_major_1h` score `0.4716` n `87` status `ready` deltaP `8.8719` edge `0.0212` maxDD `-1.6171`
- `market_context_high->crypto_alt_4h` score `0.3676` n `87` status `ready` deltaP `3.7427` edge `0.1174` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `0.2096` n `87` status `ready` deltaP `6.5812` edge `0.1454` maxDD `-6.7444`
- `news_risk_high->fx_1h` score `0.202` n `40` status `ready` deltaP `6.9461` edge `0.0059` maxDD `-0.1053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
