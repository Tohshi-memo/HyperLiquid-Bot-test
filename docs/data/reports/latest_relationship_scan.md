# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T20:22:19.030231+00:00`
- Price records: `672`
- Market context records: `1353`
- Flow alert records: `5810`
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

- `market_context_high->crypto_major_24h` score `13.5841` n `128` status `ready` deltaP `33.4201` edge `1.0224` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.7007` n `128` status `ready` deltaP `11.8056` edge `1.1464` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.3684` n `128` status `ready` deltaP `28.3854` edge `0.7931` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.0516` n `128` status `ready` deltaP `23.7847` edge `0.2877` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `3.4117` n `128` status `ready` deltaP `-7.6389` edge `0.4834` maxDD `-6.8535`
- `market_context_high->equity_4h` score `2.3014` n `157` status `ready` deltaP `11.8912` edge `0.183` maxDD `-3.6396`
- `market_context_high->equity_24h` score `1.8784` n `128` status `ready` deltaP `16.6667` edge `0.3624` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.5417` n `128` status `ready` deltaP `16.5799` edge `0.0644` maxDD `-0.3831`
- `market_context_high->unknown_24h` score `0.5516` n `128` status `ready` deltaP `-5.0347` edge `0.3525` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.1026` n `165` status `ready` deltaP `5.5889` edge `0.0167` maxDD `-1.6329`
- `market_context_high->metal_4h` score `0.0843` n `157` status `ready` deltaP `13.068` edge `0.063` maxDD `-6.4478`
- `market_context_high->index_4h` score `-0.0024` n `157` status `ready` deltaP `4.8742` edge `0.0761` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0196` n `165` status `ready` deltaP `2.2736` edge `0.0267` maxDD `-1.8125`
- `market_context_high->metal_1h` score `-0.1798` n `165` status `ready` deltaP `8.0975` edge `0.0` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.3905` n `165` status `ready` deltaP `2.4497` edge `-0.0033` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5678` n `165` status `ready` deltaP `0.46` edge `0.0111` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8776` n `165` status `ready` deltaP `-0.5516` edge `0.0176` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.1657` n `165` status `ready` deltaP `-3.454` edge `-0.0199` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.3357` n `157` status `ready` deltaP `8.4676` edge `0.1642` maxDD `-19.5565`
- `market_context_high->unknown_4h` score `-1.3914` n `157` status `ready` deltaP `1.4292` edge `0.0392` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
