# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T10:22:32.197159+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4482`

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

- `market_context_high->unknown_1h` score `20810.7479` n `67` status `ready` deltaP `0.925` edge `1734.239` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `13866.1018` n `67` status `ready` deltaP `4.9417` edge `1155.4894` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1294.9751` n `31` status `ready` deltaP `3.4286` edge `107.9093` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1136.0302` n `31` status `ready` deltaP `4.701` edge `94.6435` maxDD `-0.119`
- `news_risk_high->equity_24h` score `46.1677` n `31` status `ready` deltaP `51.7361` edge `3.5024` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `37.0533` n `31` status `ready` deltaP `48.6111` edge `2.7637` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.6128` n `31` status `ready` deltaP `48.7847` edge `2.3925` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.6415` n `31` status `ready` deltaP `52.3466` edge `0.8153` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.62` n `31` status `ready` deltaP `34.0234` edge `0.7064` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.188` n `31` status `ready` deltaP `22.3397` edge `0.7871` maxDD `-5.2957`
- `news_risk_high->index_24h` score `7.271` n `31` status `ready` deltaP `49.6528` edge `0.2749` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.4681` n `31` status `ready` deltaP `54.9059` edge `0.1858` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.2245` n `31` status `ready` deltaP `11.9001` edge `0.8604` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.6536` n `31` status `ready` deltaP `18.3407` edge `0.2009` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.3702` n `31` status `ready` deltaP `35.3954` edge `0.0709` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6495` n `31` status `ready` deltaP `31.0943` edge `0.022` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3488` n `31` status `ready` deltaP `8.9627` edge `0.2875` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9505` n `31` status `ready` deltaP `7.6154` edge `0.235` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4994` n `31` status `ready` deltaP `28.6845` edge `0.0289` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.427` n `31` status `ready` deltaP `19.8269` edge `0.1065` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
