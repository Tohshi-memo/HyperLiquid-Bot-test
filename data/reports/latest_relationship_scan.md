# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T17:22:29.250596+00:00`
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

- `market_context_high->unknown_24h` score `1494.9356` n `98` status `ready` deltaP `3.4602` edge `124.5549` maxDD `0.0`
- `news_risk_high->equity_24h` score `61.0909` n `44` status `ready` deltaP `67.5055` edge `4.7115` maxDD `-3.6503`
- `news_risk_high->equity_4h` score `19.8366` n `44` status `ready` deltaP `54.878` edge `1.2872` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `18.6265` n `44` status `ready` deltaP `35.9783` edge `2.2625` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.8818` n `98` status `ready` deltaP `44.559` edge `1.9379` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.106` n `98` status `ready` deltaP `30.6193` edge `1.8167` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.5234` n `44` status `ready` deltaP `58.8549` edge `0.4316` maxDD `-0.4279`
- `news_risk_high->crypto_alt_24h` score `8.8408` n `44` status `ready` deltaP `20.4152` edge `1.4479` maxDD `-29.0448`
- `news_risk_high->commodity_24h` score `8.3193` n `44` status `ready` deltaP `54.6713` edge `0.3288` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.2302` n `44` status `ready` deltaP `34.2849` edge `0.534` maxDD `-4.137`
- `news_risk_high->crypto_major_4h` score `7.5214` n `44` status `ready` deltaP `27.1618` edge `0.4884` maxDD `-1.7491`
- `news_risk_high->metal_4h` score `6.6261` n `44` status `ready` deltaP `54.8919` edge `0.1907` maxDD `-0.0246`
- `news_risk_high->equity_1h` score `5.4715` n `44` status `ready` deltaP `25.5716` edge `0.308` maxDD `-0.4683`
- `news_risk_high->index_4h` score `4.4017` n `44` status `ready` deltaP `38.7888` edge `0.1307` maxDD `-0.1319`
- `news_risk_high->crypto_major_1h` score `3.7224` n `44` status `ready` deltaP `22.2509` edge `0.197` maxDD `-1.4777`
- `news_risk_high->crypto_alt_1h` score `3.1836` n `44` status `ready` deltaP `21.1758` edge `0.1768` maxDD `-2.5469`
- `news_risk_high->commodity_4h` score `2.9292` n `44` status `ready` deltaP `31.2223` edge `0.0613` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.7088` n `44` status `ready` deltaP `29.0691` edge `0.0537` maxDD `-0.0743`
- `news_risk_high->index_1h` score `1.8066` n `44` status `ready` deltaP `21.3255` edge `0.0303` maxDD `-0.0869`
- `news_risk_high->metal_24h` score `0.3492` n `44` status `ready` deltaP `13.6285` edge `0.1712` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
