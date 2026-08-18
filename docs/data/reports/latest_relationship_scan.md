# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T09:28:21.764506+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.1825` n `83` status `ready` deltaP `6.9846` edge `0.2561` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.4796` n `83` status `ready` deltaP `16.2035` edge `0.265` maxDD `-4.666`
- `market_context_high->equity_1h` score `0.9991` n `97` status `ready` deltaP `8.8756` edge `0.0545` maxDD `-0.4329`
- `market_context_high->crypto_major_4h` score `0.784` n `97` status `ready` deltaP `9.874` edge `0.1016` maxDD `-3.1677`
- `market_context_high->metal_4h` score `0.7034` n `97` status `ready` deltaP `14.0699` edge `0.0224` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6267` n `97` status `ready` deltaP `12.5023` edge `0.0076` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5267` n `97` status `ready` deltaP `9.4605` edge `0.0035` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.4305` n `97` status `ready` deltaP `11.5508` edge `0.1099` maxDD `-5.5373`
- `market_context_high->metal_1h` score `-0.0102` n `97` status `ready` deltaP `4.3567` edge `0.0088` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.0494` n `83` status `ready` deltaP `13.8` edge `-0.0773` maxDD `-0.1719`
- `market_context_high->fx_4h` score `-0.2644` n `97` status `ready` deltaP `2.5051` edge `-0.0001` maxDD `-0.3734`
- `market_context_high->equity_4h` score `-0.277` n `97` status `ready` deltaP `1.1205` edge `0.0599` maxDD `-2.5696`
- `market_context_high->crypto_alt_1h` score `-0.2894` n `97` status `ready` deltaP `3.1591` edge `0.022` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.4` n `97` status `ready` deltaP `3.6522` edge `0.0094` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.4452` n `97` status `ready` deltaP `1.6791` edge `0.0162` maxDD `-2.7581`
- `market_context_high->fx_1h` score `-0.4775` n `97` status `ready` deltaP `-3.8907` edge `0.0009` maxDD `-0.2273`
- `market_context_high->index_4h` score `-0.6551` n `97` status `ready` deltaP `0.2703` edge `0.0091` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.9011` n `97` status `ready` deltaP `-7.1332` edge `-0.0067` maxDD `-1.5684`
- `market_context_high->metal_24h` score `-1.8074` n `83` status `ready` deltaP `-6.3019` edge `0.0209` maxDD `-6.5149`
- `market_context_high->index_24h` score `-4.1715` n `83` status `ready` deltaP `-14.1175` edge `-0.1742` maxDD `-10.9857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
