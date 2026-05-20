# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T18:52:23.647018+00:00`
- Price records: `672`
- Market context records: `1347`
- Flow alert records: `5792`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8793`

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

- `market_context_high->crypto_major_24h` score `14.0346` n `128` status `ready` deltaP `34.4618` edge `1.053` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.8483` n `128` status `ready` deltaP `11.8056` edge `1.1587` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.414` n `128` status `ready` deltaP `28.3854` edge `0.7969` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.3473` n `128` status `ready` deltaP `24.8264` edge `0.3054` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `2.9563` n `128` status `ready` deltaP `-8.6806` edge `0.4524` maxDD `-6.8535`
- `market_context_high->equity_4h` score `2.2196` n `157` status `ready` deltaP `11.7388` edge `0.1772` maxDD `-3.6396`
- `market_context_high->equity_24h` score `2.1323` n `128` status `ready` deltaP `17.7083` edge `0.388` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.4308` n `128` status `ready` deltaP `15.5382` edge `0.0621` maxDD `-0.3831`
- `market_context_high->unknown_24h` score `0.668` n `128` status `ready` deltaP `-5.0347` edge `0.3622` maxDD `-10.1706`
- `market_context_high->equity_1h` score `0.0765` n `159` status `ready` deltaP `2.864` edge `0.03` maxDD `-1.7505`
- `market_context_high->index_1h` score `0.0199` n `159` status `ready` deltaP `4.9599` edge `0.0149` maxDD `-1.6329`
- `market_context_high->index_4h` score `-0.0086` n `157` status `ready` deltaP `4.8742` edge `0.0753` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-0.0153` n `157` status `ready` deltaP `13.068` edge `0.0547` maxDD `-6.4478`
- `market_context_high->metal_1h` score `-0.0608` n `159` status `ready` deltaP `9.241` edge `0.0023` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.3983` n `159` status `ready` deltaP `2.2917` edge `-0.0029` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.6705` n `159` status `ready` deltaP `-0.4642` edge `0.0087` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.9904` n `159` status `ready` deltaP `-1.1816` edge `0.0124` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.1772` n `159` status `ready` deltaP `-3.7877` edge `-0.0236` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-1.3883` n `157` status `ready` deltaP `1.4292` edge `0.0396` maxDD `-11.1695`
- `market_context_high->crypto_alt_4h` score `-1.5145` n `157` status `ready` deltaP `8.4676` edge `0.1493` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
