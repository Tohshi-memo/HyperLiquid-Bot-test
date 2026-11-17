# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T17:37:31.185440+00:00`
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

- `market_context_high->unknown_24h` score `1494.8216` n `98` status `ready` deltaP `3.4602` edge `124.5454` maxDD `0.0`
- `news_risk_high->equity_24h` score `61.2571` n `44` status `ready` deltaP `67.6785` edge `4.7242` maxDD `-3.6503`
- `news_risk_high->equity_4h` score `19.8606` n `44` status `ready` deltaP `54.878` edge `1.2892` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `18.6667` n `44` status `ready` deltaP `36.1513` edge `2.2665` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.9219` n `98` status `ready` deltaP `44.732` edge `1.9419` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.1392` n `98` status `ready` deltaP `30.7923` edge `1.8198` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.5517` n `44` status `ready` deltaP `59.028` edge `0.4328` maxDD `-0.4279`
- `news_risk_high->crypto_alt_24h` score `8.874` n `44` status `ready` deltaP `20.5882` edge `1.451` maxDD `-29.0448`
- `news_risk_high->commodity_24h` score `8.3457` n `44` status `ready` deltaP `54.6713` edge `0.331` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.2554` n `44` status `ready` deltaP `34.2849` edge `0.5361` maxDD `-4.137`
- `news_risk_high->crypto_major_4h` score `7.5732` n `44` status `ready` deltaP `27.3143` edge `0.4917` maxDD `-1.7491`
- `news_risk_high->metal_4h` score `6.6127` n `44` status `ready` deltaP `54.7395` edge `0.1906` maxDD `-0.0246`
- `news_risk_high->equity_1h` score `5.4379` n `44` status `ready` deltaP `25.4219` edge `0.3062` maxDD `-0.4683`
- `news_risk_high->index_4h` score `4.4041` n `44` status `ready` deltaP `38.7888` edge `0.1309` maxDD `-0.1319`
- `news_risk_high->crypto_major_1h` score `3.7008` n `44` status `ready` deltaP `22.1012` edge `0.1962` maxDD `-1.4777`
- `news_risk_high->crypto_alt_1h` score `3.1764` n `44` status `ready` deltaP `21.1758` edge `0.1762` maxDD `-2.5469`
- `news_risk_high->commodity_4h` score `2.951` n `44` status `ready` deltaP `31.3748` edge `0.0621` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.6932` n `44` status `ready` deltaP `28.9194` edge `0.0534` maxDD `-0.0743`
- `news_risk_high->index_1h` score `1.7934` n `44` status `ready` deltaP `21.1758` edge `0.0302` maxDD `-0.0869`
- `news_risk_high->metal_24h` score `0.3614` n `44` status `ready` deltaP `13.8016` edge `0.1716` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
