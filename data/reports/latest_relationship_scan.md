# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T21:37:28.871693+00:00`
- Price records: `672`
- Market context records: `7920`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14745`

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

- `market_context_high->equity_24h` score `16.4868` n `83` status `ready` deltaP `26.0982` edge `1.3341` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.3506` n `83` status `ready` deltaP `39.688` edge `0.4313` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7013` n `92` status `ready` deltaP `25.0831` edge `0.4805` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.2244` n `83` status `ready` deltaP `26.7403` edge `0.2437` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.7917` n `92` status `ready` deltaP `28.8193` edge `0.0765` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.7195` n `92` status `ready` deltaP `24.43` edge `0.126` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.7054` n `92` status `ready` deltaP `13.001` edge `0.1372` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `1.3224` n `92` status `ready` deltaP `9.4976` edge `0.1586` maxDD `-3.9374`
- `market_context_high->index_24h` score `1.3128` n `83` status `ready` deltaP `11.1509` edge `0.161` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.2749` n `83` status `ready` deltaP `26.8804` edge `0.0358` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `1.0297` n `92` status `ready` deltaP `10.7569` edge `0.1859` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.0186` n `92` status `ready` deltaP `15.7037` edge `0.0232` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6081` n `92` status `ready` deltaP `8.6566` edge `0.0308` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.599` n `92` status `ready` deltaP `11.169` edge `0.0432` maxDD `-1.6021`
- `market_context_high->crypto_alt_1h` score `0.2462` n `92` status `ready` deltaP `5.0573` edge `0.0411` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.3559` n `92` status `ready` deltaP `0.865` edge `0.0013` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.4519` n `92` status `ready` deltaP `0.2579` edge `-0.0028` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.4935` n `92` status `ready` deltaP `2.8853` edge `0.0161` maxDD `-2.4502`
- `market_context_high->fx_4h` score `-0.5295` n `92` status `ready` deltaP `3.7562` edge `0.0056` maxDD `-0.9813`
- `market_context_high->unknown_1h` score `-1.9051` n `92` status `ready` deltaP `7.7975` edge `-0.1684` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
