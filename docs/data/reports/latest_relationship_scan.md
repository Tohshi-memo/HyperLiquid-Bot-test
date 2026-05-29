# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T10:07:21.499475+00:00`
- Price records: `672`
- Market context records: `2234`
- Flow alert records: `8325`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9203`

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

- `news_risk_high->crypto_alt_24h` score `25.3983` n `33` status `ready` deltaP `55.9186` edge `1.8026` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `14.3357` n `33` status `ready` deltaP `46.2753` edge `0.9301` maxDD `-3.1836`
- `market_context_high->crypto_alt_4h` score `12.9824` n `131` status `ready` deltaP `37.1695` edge `0.9277` maxDD `-5.1574`
- `news_risk_high->equity_24h` score `12.2047` n `33` status `ready` deltaP `37.2475` edge `0.8002` maxDD `-2.1831`
- `market_context_high->crypto_major_4h` score `11.7591` n `131` status `ready` deltaP `42.2129` edge `0.7515` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.2349` n `33` status `ready` deltaP `36.8213` edge `0.5467` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `7.2528` n `33` status `ready` deltaP `18.7658` edge `0.8628` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `5.9251` n `131` status `ready` deltaP `22.6715` edge `0.388` maxDD `-1.6306`
- `market_context_high->equity_4h` score `4.1199` n `131` status `ready` deltaP `24.3705` edge `0.2441` maxDD `-2.7265`
- `news_risk_high->commodity_4h` score `3.9639` n `43` status `ready` deltaP `33.377` edge `0.3528` maxDD `-3.0367`
- `market_context_high->unknown_24h` score `3.6938` n `128` status `ready` deltaP `24.9131` edge `0.4956` maxDD `-23.9762`
- `market_context_high->index_4h` score `3.6561` n `131` status `ready` deltaP `27.8754` edge `0.1643` maxDD `-0.9702`
- `market_context_high->crypto_major_1h` score `3.1281` n `143` status `ready` deltaP `17.3831` edge `0.1925` maxDD `-1.817`
- `news_risk_high->fx_24h` score `2.9556` n `33` status `ready` deltaP `31.0606` edge `0.0577` maxDD `-0.1442`
- `market_context_high->crypto_alt_1h` score `2.9051` n `143` status `ready` deltaP `16.2839` edge `0.2199` maxDD `-4.9097`
- `news_risk_high->commodity_24h` score `2.2926` n `33` status `ready` deltaP `-2.2886` edge `0.288` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.1488` n `43` status `ready` deltaP `27.2794` edge `0.0156` maxDD `-0.1382`
- `market_context_high->index_24h` score `2.0755` n `128` status `ready` deltaP `9.6354` edge `0.2042` maxDD `-3.3048`
- `market_context_high->crypto_major_24h` score `1.8841` n `128` status `ready` deltaP `15.1909` edge `0.8361` maxDD `-49.6659`
- `market_context_high->metal_4h` score `1.363` n `131` status `ready` deltaP `17.4793` edge `0.1358` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
