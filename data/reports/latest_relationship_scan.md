# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T17:07:42.299976+00:00`
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

- `market_context_high->unknown_24h` score `1495.1792` n `98` status `ready` deltaP `3.4602` edge `124.5752` maxDD `0.0`
- `news_risk_high->equity_24h` score `60.9487` n `44` status `ready` deltaP `67.3325` edge `4.7008` maxDD `-3.6503`
- `news_risk_high->equity_4h` score `19.8282` n `44` status `ready` deltaP `54.878` edge `1.2865` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `18.5887` n `44` status `ready` deltaP `35.8053` edge `2.2588` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.8439` n `98` status `ready` deltaP `44.386` edge `1.9342` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.0744` n `98` status `ready` deltaP `30.4463` edge `1.8138` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.4976` n `44` status `ready` deltaP `58.6819` edge `0.4306` maxDD `-0.4279`
- `news_risk_high->crypto_alt_24h` score `8.8092` n `44` status `ready` deltaP `20.2422` edge `1.445` maxDD `-29.0448`
- `news_risk_high->commodity_24h` score `8.2893` n `44` status `ready` deltaP `54.6713` edge `0.3263` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.2218` n `44` status `ready` deltaP `34.2849` edge `0.5333` maxDD `-4.137`
- `news_risk_high->crypto_major_4h` score `7.501` n `44` status `ready` deltaP `27.1618` edge `0.4867` maxDD `-1.7491`
- `news_risk_high->metal_4h` score `6.6419` n `44` status `ready` deltaP `55.0444` edge `0.191` maxDD `-0.0246`
- `news_risk_high->equity_1h` score `5.5075` n `44` status `ready` deltaP `25.7213` edge `0.31` maxDD `-0.4683`
- `news_risk_high->index_4h` score `4.4017` n `44` status `ready` deltaP `38.7888` edge `0.1307` maxDD `-0.1319`
- `news_risk_high->crypto_major_1h` score `3.7404` n `44` status `ready` deltaP `22.2509` edge `0.1985` maxDD `-1.4777`
- `news_risk_high->crypto_alt_1h` score `3.1968` n `44` status `ready` deltaP `21.1758` edge `0.1779` maxDD `-2.5469`
- `news_risk_high->commodity_4h` score `2.9062` n `44` status `ready` deltaP `31.0699` edge `0.0604` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.7256` n `44` status `ready` deltaP `29.2188` edge `0.0541` maxDD `-0.0743`
- `news_risk_high->index_1h` score `1.821` n `44` status `ready` deltaP `21.4752` edge `0.0305` maxDD `-0.0869`
- `news_risk_high->metal_24h` score `0.3371` n `44` status `ready` deltaP `13.4555` edge `0.1708` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
