# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T18:52:31.092109+00:00`
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

- `market_context_high->unknown_24h` score `1492.8169` n `98` status `ready` deltaP `3.4662` edge `124.3783` maxDD `0.0`
- `news_risk_high->equity_24h` score `60.3983` n `42` status `ready` deltaP `67.8633` edge `4.6514` maxDD `-3.6503`
- `news_risk_high->equity_4h` score `20.0962` n `42` status `ready` deltaP `55.1829` edge `1.3068` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `18.1465` n `42` status `ready` deltaP `35.3429` edge `2.2052` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `15.15` n `98` status `ready` deltaP `45.547` edge `1.9657` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.3532` n `98` status `ready` deltaP `31.6079` edge `1.8418` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.504` n `42` status `ready` deltaP `59.1978` edge `0.4277` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.2273` n `42` status `ready` deltaP `54.766` edge `0.3205` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.1171` n `42` status `ready` deltaP `19.0228` edge `1.3644` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `8.071` n `42` status `ready` deltaP `33.66` edge `0.5249` maxDD `-4.137`
- `news_risk_high->crypto_major_4h` score `7.1004` n `42` status `ready` deltaP `26.6696` edge `0.4566` maxDD `-1.7491`
- `news_risk_high->metal_4h` score `6.6718` n `42` status `ready` deltaP `55.0885` edge `0.1932` maxDD `-0.0246`
- `news_risk_high->equity_1h` score `5.6829` n `42` status `ready` deltaP `26.3544` edge `0.3197` maxDD `-0.4122`
- `news_risk_high->index_4h` score `4.4152` n `42` status `ready` deltaP `38.5525` edge `0.1334` maxDD `-0.1319`
- `news_risk_high->crypto_major_1h` score `3.4899` n `42` status `ready` deltaP `20.844` edge `0.187` maxDD `-1.4777`
- `news_risk_high->commodity_4h` score `2.8827` n `42` status `ready` deltaP `30.4007` edge `0.0629` maxDD `-0.3611`
- `news_risk_high->crypto_alt_1h` score `2.868` n `42` status `ready` deltaP `19.6607` edge `0.1606` maxDD `-2.5469`
- `news_risk_high->metal_1h` score `2.8235` n `42` status `ready` deltaP `30.2181` edge `0.0556` maxDD `-0.0743`
- `news_risk_high->index_1h` score `2.055` n `42` status `ready` deltaP `24.1232` edge `0.0322` maxDD `-0.0751`
- `news_risk_high->metal_24h` score `0.0986` n `42` status `ready` deltaP `10.9392` edge `0.157` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
