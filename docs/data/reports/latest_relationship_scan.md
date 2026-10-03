# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T04:22:37.177590+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `366.2493` n `50` status `ready` deltaP `11.4731` edge `30.4492` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.4559` n `50` status `ready` deltaP `10.8232` edge `24.3825` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.2874` n `50` status `ready` deltaP `22.9583` edge `0.9579` maxDD `-11.6271`
- `news_risk_high->crypto_alt_24h` score `10.7242` n `70` status `ready` deltaP `20.3869` edge `0.9013` maxDD `-7.816`
- `news_risk_high->equity_24h` score `10.5278` n `70` status `ready` deltaP `33.7351` edge `0.7009` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `8.9794` n `50` status `ready` deltaP `31.3056` edge `0.6812` maxDD `-9.3299`
- `news_risk_high->crypto_alt_4h` score `7.7904` n `92` status `ready` deltaP `31.9062` edge `0.5709` maxDD `-6.4195`
- `news_risk_high->crypto_major_4h` score `7.7634` n `92` status `ready` deltaP `29.9973` edge `0.4838` maxDD `-0.9466`
- `market_context_high->crypto_major_4h` score `7.2383` n `50` status `ready` deltaP `16.4756` edge `0.5637` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.8128` n `50` status `ready` deltaP `16.0366` edge `0.5064` maxDD `-7.6465`
- `news_risk_high->crypto_major_24h` score `5.6084` n `70` status `ready` deltaP `12.1627` edge `0.552` maxDD `-9.5909`
- `news_risk_high->index_24h` score `3.6148` n `70` status `ready` deltaP `31.7857` edge `0.1052` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.435` n `92` status `ready` deltaP `27.618` edge `0.1634` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.1475` n `50` status `ready` deltaP `14.0539` edge `0.2349` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9689` n `50` status `ready` deltaP `13.2515` edge `0.2041` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7665` n `50` status `ready` deltaP `30.8598` edge `0.0383` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.016` n `92` status `ready` deltaP `10.1211` edge `0.1444` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `1.7945` n `92` status `ready` deltaP `7.8365` edge `0.1492` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4352` n `50` status `ready` deltaP `20.1916` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2805` n `70` status `ready` deltaP `9.6329` edge `0.1762` maxDD `-3.6969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
