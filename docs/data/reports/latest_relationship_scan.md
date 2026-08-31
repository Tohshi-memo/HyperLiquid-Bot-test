# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T05:22:26.234113+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11668`

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

- `risk_on_high->crypto_alt_24h` score `21.4942` n `55` status `ready` deltaP `47.4053` edge `1.5232` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `21.4942` n `55` status `ready` deltaP `47.4053` edge `1.5232` maxDD `-3.1772`
- `risk_on_high->crypto_major_24h` score `9.4787` n `55` status `ready` deltaP `28.6932` edge `0.7404` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `9.4787` n `55` status `ready` deltaP `28.6932` edge `0.7404` maxDD `-9.0103`
- `risk_on_high->unknown_4h` score `8.8642` n `98` status `ready` deltaP `25.7467` edge `0.6224` maxDD `-2.0954`
- `risk_on_and_context->unknown_4h` score `8.8642` n `98` status `ready` deltaP `25.7467` edge `0.6224` maxDD `-2.0954`
- `market_context_high->unknown_4h` score `7.0266` n `150` status `ready` deltaP `22.0732` edge `0.4973` maxDD `-2.3788`
- `risk_on_high->fx_24h` score `6.2452` n `55` status `ready` deltaP `69.9653` edge `0.054` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.2452` n `55` status `ready` deltaP `69.9653` edge `0.054` maxDD `0.0`
- `market_context_high->metal_24h` score `5.224` n `96` status `ready` deltaP `37.1527` edge `0.2485` maxDD `-1.8678`
- `risk_on_high->metal_24h` score `4.4044` n `55` status `ready` deltaP `40.5808` edge `0.1437` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.4044` n `55` status `ready` deltaP `40.5808` edge `0.1437` maxDD `-0.7767`
- `market_context_high->crypto_alt_24h` score `4.2609` n `96` status `ready` deltaP `21.875` edge `0.8194` maxDD `-27.517`
- `market_context_high->crypto_major_24h` score `3.5394` n `96` status `ready` deltaP `19.7917` edge `0.4121` maxDD `-17.2607`
- `risk_on_high->unknown_1h` score `2.6864` n `107` status `ready` deltaP `8.0125` edge `0.2281` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.6864` n `107` status `ready` deltaP `8.0125` edge `0.2281` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.4638` n `159` status `ready` deltaP `7.3542` edge `0.2193` maxDD `-2.041`
- `market_context_high->fx_24h` score `1.0019` n `96` status `ready` deltaP `36.632` edge `0.0301` maxDD `-1.6688`
- `risk_on_high->commodity_24h` score `0.8179` n `55` status `ready` deltaP `9.6528` edge `0.1393` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8179` n `55` status `ready` deltaP `9.6528` edge `0.1393` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
