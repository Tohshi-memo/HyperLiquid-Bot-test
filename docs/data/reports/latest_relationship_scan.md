# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T21:52:16.643501+00:00`
- Price records: `672`
- Market context records: `1259`
- Flow alert records: `5532`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_major_24h` score `17.9509` n `128` status `ready` deltaP `41.5798` edge `1.3319` maxDD `-8.0553`
- `market_context_high->metal_24h` score `8.9478` n `128` status `ready` deltaP `3.8194` edge `0.8869` maxDD `-6.3373`
- `market_context_high->unknown_4h` score `8.0371` n `128` status `ready` deltaP `5.221` edge `0.7566` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.903` n `128` status `ready` deltaP `23.177` edge `0.7057` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.4313` n `128` status `ready` deltaP `24.8264` edge `0.3124` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.489` n `128` status `ready` deltaP `18.3117` edge `0.235` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.4218` n `128` status `ready` deltaP `22.9167` edge `0.5186` maxDD `-14.2815`
- `market_context_high->commodity_24h` score `2.8104` n `128` status `ready` deltaP `-10.0694` edge `0.4495` maxDD `-6.8535`
- `market_context_high->unknown_24h` score `2.2386` n `128` status `ready` deltaP `1.5625` edge `0.4491` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.635` n `128` status `ready` deltaP `14.3483` edge `0.1089` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.8684` n `130` status `ready` deltaP `11.679` edge `0.0262` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.7911` n `130` status `ready` deltaP `7.2754` edge `0.0543` maxDD `-1.2834`
- `market_context_high->metal_4h` score `0.5665` n `128` status `ready` deltaP `17.1304` edge `0.0761` maxDD `-6.4478`
- `market_context_high->metal_1h` score `0.4385` n `130` status `ready` deltaP `12.4321` edge `0.0147` maxDD `-2.2164`
- `market_context_high->fx_24h` score `0.1735` n `128` status `ready` deltaP `4.4271` edge `0.0314` maxDD `-0.3831`
- `market_context_high->crypto_major_4h` score `0.1402` n `128` status `ready` deltaP `7.6792` edge `0.1589` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.1926` n `130` status `ready` deltaP `4.6983` edge `-0.0018` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.2381` n `130` status `ready` deltaP `1.6421` edge `0.0428` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4421` n `130` status `ready` deltaP `1.7089` edge `0.0085` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.4925` n `128` status `ready` deltaP `8.708` edge `0.1753` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
