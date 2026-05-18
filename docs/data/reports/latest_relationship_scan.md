# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T02:22:12.588834+00:00`
- Price records: `672`
- Market context records: `1074`
- Flow alert records: `4997`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8728`

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

- `market_context_high->crypto_major_24h` score `16.1144` n `163` status `ready` deltaP `34.9075` edge `1.1565` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.5973` n `163` status `ready` deltaP `11.9915` edge `0.5099` maxDD `-9.5387`
- `market_context_high->equity_24h` score `5.1253` n `163` status `ready` deltaP `14.1259` edge `0.3826` maxDD `-3.6396`
- `market_context_high->index_24h` score `4.3112` n `163` status `ready` deltaP `14.6806` edge `0.2922` maxDD `-2.1308`
- `market_context_high->metal_24h` score `4.2808` n `163` status `ready` deltaP `-2.1529` edge `0.5378` maxDD `-6.3373`
- `market_context_high->equity_4h` score `1.4553` n `165` status `ready` deltaP `8.1753` edge `0.1456` maxDD `-3.6396`
- `market_context_high->crypto_major_4h` score `1.1132` n `165` status `ready` deltaP `12.5508` edge `0.1777` maxDD `-6.4882`
- `market_context_high->index_4h` score `0.7648` n `165` status `ready` deltaP `6.6658` edge `0.0876` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5646` n `170` status `ready` deltaP `7.8214` edge `0.0266` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4133` n `170` status `ready` deltaP `2.5061` edge `0.0555` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.234` n `170` status `ready` deltaP `7.7545` edge `0.0348` maxDD `-3.3594`
- `market_context_high->fx_1h` score `-0.0211` n `170` status `ready` deltaP `6.4072` edge `0.0011` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.1843` n `170` status `ready` deltaP `6.9426` edge `-0.0006` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.4604` n `170` status `ready` deltaP `2.3864` edge `0.03` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.6349` n `170` status `ready` deltaP `-0.5565` edge `0.0031` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-0.6547` n `165` status `ready` deltaP `6.431` edge `0.153` maxDD `-13.0347`
- `market_context_high->fx_4h` score `-0.6846` n `165` status `ready` deltaP `1.4967` edge `0.0019` maxDD `-1.6381`
- `market_context_high->metal_4h` score `-1.9845` n `165` status `ready` deltaP `4.1814` edge `-0.0869` maxDD `-9.2991`
- `market_context_high->fx_24h` score `-3.0608` n `163` status `ready` deltaP `5.4338` edge `-0.021` maxDD `-19.2774`
- `market_context_high->unknown_4h` score `-3.0883` n `165` status `ready` deltaP `7.8695` edge `-0.1715` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
