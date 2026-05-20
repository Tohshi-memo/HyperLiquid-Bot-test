# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T05:52:15.071480+00:00`
- Price records: `672`
- Market context records: `1292`
- Flow alert records: `5631`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `17.4445` n `128` status `ready` deltaP `41.5798` edge `1.2897` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.1474` n `128` status `ready` deltaP `9.375` edge `1.1165` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.3504` n `128` status `ready` deltaP `27.1701` edge `0.7997` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.7967` n `128` status `ready` deltaP `30.2083` edge `0.3903` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9881` n `128` status `ready` deltaP `25.3472` edge `0.575` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.3791` n `150` status `ready` deltaP `12.2784` edge `0.1869` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.373` n `128` status `ready` deltaP `1.5625` edge `0.4603` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.0475` n `128` status `ready` deltaP `-14.9306` edge `0.335` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.4658` n `128` status `ready` deltaP `7.0313` edge `0.0384` maxDD `-0.3831`
- `market_context_high->unknown_4h` score `0.4078` n `150` status `ready` deltaP `2.9553` edge `0.2414` maxDD `-11.1695`
- `market_context_high->equity_1h` score `0.1852` n `157` status `ready` deltaP `3.5174` edge `0.0347` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.1205` n `150` status `ready` deltaP `5.6321` edge `0.0868` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.1069` n `157` status `ready` deltaP `6.2121` edge `0.0177` maxDD `-1.6329`
- `market_context_high->metal_1h` score `0.0843` n `157` status `ready` deltaP `10.1396` edge `0.0084` maxDD `-2.8509`
- `market_context_high->metal_4h` score `0.0234` n `150` status `ready` deltaP `12.7418` edge `0.0601` maxDD `-6.4478`
- `market_context_high->fx_1h` score `-0.5373` n `157` status `ready` deltaP `0.6589` edge `-0.0036` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6097` n `157` status `ready` deltaP `0.8467` edge `0.0306` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.7427` n `150` status `ready` deltaP `9.6362` edge `0.1725` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-0.8268` n `157` status `ready` deltaP `-0.3185` edge `-0.0018` maxDD `-5.8323`
- `market_context_high->crypto_major_4h` score `-0.8649` n `150` status `ready` deltaP `5.4309` edge `0.1238` maxDD `-13.3376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
