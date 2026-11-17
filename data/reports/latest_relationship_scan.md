# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T17:52:25.770772+00:00`
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

- `market_context_high->unknown_24h` score `1494.7028` n `98` status `ready` deltaP `3.4602` edge `124.5355` maxDD `0.0`
- `news_risk_high->equity_24h` score `61.421` n `44` status `ready` deltaP `67.8515` edge `4.7367` maxDD `-3.6503`
- `news_risk_high->equity_4h` score `19.8774` n `44` status `ready` deltaP `54.878` edge `1.2906` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `18.7014` n `44` status `ready` deltaP `36.3243` edge `2.2698` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.9567` n `98` status `ready` deltaP `44.905` edge `1.9452` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.1708` n `98` status `ready` deltaP `30.9653` edge `1.8227` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.5799` n `44` status `ready` deltaP `59.201` edge `0.434` maxDD `-0.4279`
- `news_risk_high->crypto_alt_24h` score `8.9056` n `44` status `ready` deltaP `20.7612` edge `1.4539` maxDD `-29.0448`
- `news_risk_high->commodity_24h` score `8.3685` n `44` status `ready` deltaP `54.6713` edge `0.3329` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.2746` n `44` status `ready` deltaP `34.2849` edge `0.5377` maxDD `-4.137`
- `news_risk_high->crypto_major_4h` score `7.613` n `44` status `ready` deltaP `27.4667` edge `0.494` maxDD `-1.7491`
- `news_risk_high->metal_4h` score `6.5993` n `44` status `ready` deltaP `54.5871` edge `0.1905` maxDD `-0.0246`
- `news_risk_high->equity_1h` score `5.3899` n `44` status `ready` deltaP `25.2722` edge `0.3032` maxDD `-0.4683`
- `news_risk_high->index_4h` score `4.4053` n `44` status `ready` deltaP `38.7888` edge `0.131` maxDD `-0.1319`
- `news_risk_high->crypto_major_1h` score `3.6661` n `44` status `ready` deltaP `21.9515` edge `0.1943` maxDD `-1.4777`
- `news_risk_high->crypto_alt_1h` score `3.1405` n `44` status `ready` deltaP `21.0261` edge `0.1742` maxDD `-2.5469`
- `news_risk_high->commodity_4h` score `2.9582` n `44` status `ready` deltaP `31.3748` edge `0.0627` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.6776` n `44` status `ready` deltaP `28.7697` edge `0.0531` maxDD `-0.0743`
- `news_risk_high->index_1h` score `1.7767` n `44` status `ready` deltaP `21.0261` edge `0.0298` maxDD `-0.0869`
- `news_risk_high->metal_24h` score `0.3735` n `44` status `ready` deltaP `13.9746` edge `0.172` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
