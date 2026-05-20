# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T20:07:16.009365+00:00`
- Price records: `672`
- Market context records: `1352`
- Flow alert records: `5807`
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

- `market_context_high->crypto_major_24h` score `13.6544` n `128` status `ready` deltaP `33.5937` edge `1.0271` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.7211` n `128` status `ready` deltaP `11.8056` edge `1.1481` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.3696` n `128` status `ready` deltaP `28.3854` edge `0.7932` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1003` n `128` status `ready` deltaP `23.9583` edge `0.2906` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `3.333` n `128` status `ready` deltaP `-7.8125` edge `0.478` maxDD `-6.8535`
- `market_context_high->equity_4h` score `2.2784` n `157` status `ready` deltaP `11.7388` edge `0.1821` maxDD `-3.6396`
- `market_context_high->equity_24h` score `1.9179` n `128` status `ready` deltaP `16.8403` edge `0.3663` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.5206` n `128` status `ready` deltaP `16.4063` edge `0.0638` maxDD `-0.3831`
- `market_context_high->unknown_24h` score `0.566` n `128` status `ready` deltaP `-5.0347` edge `0.3537` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.1303` n `164` status `ready` deltaP `5.8457` edge `0.0173` maxDD `-1.6329`
- `market_context_high->metal_4h` score `0.0651` n `157` status `ready` deltaP `13.068` edge `0.0614` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.0298` n `164` status `ready` deltaP `2.5193` edge `0.0284` maxDD `-1.7505`
- `market_context_high->index_4h` score `-0.0055` n `157` status `ready` deltaP `4.8742` edge `0.0757` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.1512` n `164` status `ready` deltaP `8.3358` edge `0.0008` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.3723` n `164` status `ready` deltaP `2.6325` edge `-0.003` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.537` n `164` status `ready` deltaP `0.7704` edge `0.0116` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8572` n `164` status `ready` deltaP `-0.3724` edge `0.0181` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.1509` n `164` status `ready` deltaP `-3.3044` edge `-0.019` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.3621` n `157` status `ready` deltaP `8.4676` edge `0.162` maxDD `-19.5565`
- `market_context_high->unknown_4h` score `-1.3891` n `157` status `ready` deltaP `1.4292` edge `0.0395` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
