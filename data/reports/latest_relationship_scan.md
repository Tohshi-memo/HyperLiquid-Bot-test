# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T08:37:19.371754+00:00`
- Price records: `672`
- Market context records: `1304`
- Flow alert records: `5665`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8781`

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

- `market_context_high->crypto_major_24h` score `17.0315` n `128` status `ready` deltaP `41.2326` edge `1.2576` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.9206` n `128` status `ready` deltaP `11.2847` edge `1.1682` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.5904` n `128` status `ready` deltaP `28.3854` edge `0.8116` maxDD `-15.1306`
- `market_context_high->index_24h` score `6.0614` n `128` status `ready` deltaP `31.5972` edge `0.4031` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9961` n `128` status `ready` deltaP `24.8264` edge `0.5795` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.6221` n `157` status `ready` deltaP `13.1107` edge `0.2016` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.1779` n `128` status `ready` deltaP `0.1736` edge `0.4533` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `0.7873` n `128` status `ready` deltaP `-15.7986` edge `0.3191` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.6858` n `128` status `ready` deltaP `8.941` edge `0.044` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.2445` n `157` status `ready` deltaP `13.5253` edge `0.0733` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.202` n `157` status `ready` deltaP `3.6671` edge `0.0351` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.2005` n `157` status `ready` deltaP `5.9413` edge `0.095` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.1014` n `157` status `ready` deltaP `6.0624` edge `0.018` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0691` n `157` status `ready` deltaP `8.942` edge `0.0036` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4858` n `157` status `ready` deltaP `1.2577` edge `-0.0033` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.5533` n `157` status `ready` deltaP `1.1461` edge `0.0333` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.7941` n `157` status `ready` deltaP `10.6018` edge `0.1951` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-0.8563` n `157` status `ready` deltaP `-0.7676` edge `-0.0026` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-0.905` n `157` status `ready` deltaP `3.8683` edge `0.0853` maxDD `-11.1695`
- `market_context_high->commodity_1h` score `-0.9964` n `157` status `ready` deltaP `-2.153` edge `-0.0072` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
