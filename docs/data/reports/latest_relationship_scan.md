# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T03:22:29.567715+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7162`

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

- `news_risk_high->unknown_24h` score `1166.4268` n `132` status `ready` deltaP `1.9097` edge `97.1895` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.2059` n `132` status `ready` deltaP `30.7765` edge `1.4996` maxDD `-1.0093`
- `news_risk_high->crypto_major_24h` score `9.2548` n `132` status `ready` deltaP `25.7576` edge `0.9149` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `9.0422` n `132` status `ready` deltaP `30.2715` edge `0.7866` maxDD `-9.4579`
- `news_risk_high->index_24h` score `4.1652` n `132` status `ready` deltaP `36.6319` edge `0.1507` maxDD `-0.4916`
- `news_risk_high->equity_4h` score `2.9654` n `135` status `ready` deltaP `29.7809` edge `0.2087` maxDD `-9.143`
- `news_risk_high->metal_24h` score `2.4932` n `132` status `ready` deltaP `28.2355` edge `0.2588` maxDD `-2.192`
- `news_risk_high->crypto_alt_4h` score `2.1522` n `135` status `ready` deltaP `12.3317` edge `0.3631` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.133` n `135` status `ready` deltaP `9.4012` edge `0.1228` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.9547` n `135` status `ready` deltaP `9.8503` edge `0.0762` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.5341` n `135` status `ready` deltaP `9.267` edge `0.0115` maxDD `-0.302`
- `news_risk_high->index_4h` score `-0.0481` n `135` status `ready` deltaP `7.8636` edge `0.0289` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4592` n `135` status `ready` deltaP `2.7888` edge `0.0714` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.4814` n `135` status `ready` deltaP `1.1577` edge `0.0151` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2366` n `135` status `ready` deltaP `-7.2369` edge `0.0305` maxDD `-2.9297`
- `news_risk_high->crypto_major_4h` score `-1.4093` n `135` status `ready` deltaP `-3.0736` edge `0.1113` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.4566` n `135` status `ready` deltaP `6.4657` edge `-0.0085` maxDD `-3.0414`
- `news_risk_high->commodity_1h` score `-1.8296` n `135` status `ready` deltaP `-8.6682` edge `-0.0093` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.8912` n `135` status `ready` deltaP `-9.8037` edge `-0.0042` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2466` n `135` status `ready` deltaP `-8.8449` edge `0.0128` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
