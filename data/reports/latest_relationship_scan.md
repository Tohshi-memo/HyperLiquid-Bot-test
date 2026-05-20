# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T08:52:15.892052+00:00`
- Price records: `672`
- Market context records: `1305`
- Flow alert records: `5668`
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

- `market_context_high->crypto_major_24h` score `16.9859` n `128` status `ready` deltaP `41.2326` edge `1.2538` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.9669` n `128` status `ready` deltaP `11.4583` edge `1.1709` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.5928` n `128` status `ready` deltaP `28.3854` edge `0.8118` maxDD `-15.1306`
- `market_context_high->index_24h` score `6.059` n `128` status `ready` deltaP `31.5972` edge `0.4029` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9723` n `128` status `ready` deltaP `24.6528` edge `0.5776` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.6149` n `157` status `ready` deltaP `13.1107` edge `0.201` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.1719` n `128` status `ready` deltaP `0.1736` edge `0.4528` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `0.8108` n `128` status `ready` deltaP `-15.625` edge `0.3199` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.7069` n `128` status `ready` deltaP `9.1146` edge `0.0446` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.2265` n `157` status `ready` deltaP `13.5253` edge `0.0718` maxDD `-6.4478`
- `market_context_high->index_4h` score `0.199` n `157` status `ready` deltaP `5.9413` edge `0.0948` maxDD `-3.7119`
- `market_context_high->equity_1h` score `0.1984` n `157` status `ready` deltaP `3.6671` edge `0.0348` maxDD `-1.7505`
- `market_context_high->index_1h` score `0.0991` n `157` status `ready` deltaP `6.0624` edge `0.0177` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0907` n `157` status `ready` deltaP `8.7923` edge `0.0028` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4858` n `157` status `ready` deltaP `1.2577` edge `-0.0033` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.5749` n `157` status `ready` deltaP `0.9964` edge `0.0325` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.8339` n `157` status `ready` deltaP `10.4493` edge `0.1928` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-0.8719` n `157` status `ready` deltaP `-0.9173` edge `-0.0036` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-0.9286` n `157` status `ready` deltaP `3.7158` edge `0.0833` maxDD `-11.1695`
- `market_context_high->commodity_1h` score `-0.9904` n `157` status `ready` deltaP `-2.153` edge `-0.0067` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
