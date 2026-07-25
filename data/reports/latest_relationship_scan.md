# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T19:07:29.257626+00:00`
- Price records: `672`
- Market context records: `7909`
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

- `market_context_high->equity_24h` score `15.7547` n `92` status `ready` deltaP `28.6912` edge `1.2558` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.4732` n `92` status `ready` deltaP `36.9471` edge `0.3851` maxDD `-0.0249`
- `market_context_high->equity_4h` score `6.0805` n `98` status `ready` deltaP `21.9434` edge `0.4497` maxDD `-5.1426`
- `market_context_high->index_4h` score `2.3778` n `98` status `ready` deltaP `24.5459` edge `0.0705` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.1776` n `98` status `ready` deltaP `19.0362` edge `0.1168` maxDD `-0.979`
- `market_context_high->commodity_24h` score `2.0849` n `92` status `ready` deltaP `20.788` edge `0.1935` maxDD `-7.0012`
- `market_context_high->index_24h` score `1.5413` n `92` status `ready` deltaP `7.4653` edge `0.1457` maxDD `-1.3621`
- `market_context_high->crypto_alt_4h` score `1.4118` n `98` status `ready` deltaP `10.7205` edge `0.1579` maxDD `-3.9374`
- `market_context_high->equity_1h` score `1.4068` n `101` status `ready` deltaP `11.114` edge `0.1249` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.141` n `92` status `ready` deltaP `31.5519` edge `0.0447` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `1.1095` n `98` status `ready` deltaP `12.7146` edge `0.1795` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0051` n `101` status `ready` deltaP `12.4681` edge `0.0415` maxDD `-1.6021`
- `market_context_high->index_1h` score `0.8028` n `101` status `ready` deltaP `13.3663` edge `0.0208` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.4782` n `101` status `ready` deltaP `7.4835` edge `0.0278` maxDD `-0.6936`
- `market_context_high->crypto_alt_1h` score `0.2668` n `101` status `ready` deltaP `4.5132` edge `0.0354` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.1483` n `101` status `ready` deltaP `2.447` edge `0.0014` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.1508` n `98` status `ready` deltaP `7.3394` edge `0.0065` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.2139` n `98` status `ready` deltaP `4.6496` edge `0.016` maxDD `-2.2874`
- `market_context_high->commodity_1h` score `-0.4171` n `101` status `ready` deltaP `0.6124` edge `-0.0007` maxDD `-1.5486`
- `market_context_high->unknown_1h` score `-2.1916` n `101` status `ready` deltaP `6.1362` edge `-0.1812` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
