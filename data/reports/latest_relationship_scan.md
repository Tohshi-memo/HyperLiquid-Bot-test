# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T09:37:17.171905+00:00`
- Price records: `672`
- Market context records: `1308`
- Flow alert records: `5677`
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

- `market_context_high->crypto_major_24h` score `16.8129` n `128` status `ready` deltaP `40.8854` edge `1.2417` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.1045` n `128` status `ready` deltaP `11.9792` edge `1.1789` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.582` n `128` status `ready` deltaP `28.3854` edge `0.8109` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.9976` n `128` status `ready` deltaP `31.25` edge `0.4001` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.8688` n `128` status `ready` deltaP `24.1319` edge `0.5678` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.5885` n `157` status `ready` deltaP `13.1107` edge `0.1988` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.1556` n `128` status `ready` deltaP `0.0` edge `0.4526` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `0.898` n `128` status `ready` deltaP `-15.1042` edge `0.3237` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.769` n `128` status `ready` deltaP `9.6355` edge `0.0463` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.2049` n `157` status `ready` deltaP `13.5253` edge `0.07` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.2044` n `157` status `ready` deltaP `3.6671` edge `0.0353` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.1927` n `157` status `ready` deltaP `5.9413` edge `0.094` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.1007` n `157` status `ready` deltaP `6.0624` edge `0.0179` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.1002` n `157` status `ready` deltaP `8.6426` edge `0.003` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4858` n `157` status `ready` deltaP `1.2577` edge `-0.0033` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6181` n `157` status `ready` deltaP `0.697` edge `0.0309` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.8689` n `157` status `ready` deltaP `10.2969` edge `0.1909` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-0.8984` n `157` status `ready` deltaP `-1.2167` edge `-0.005` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-0.9474` n `157` status `ready` deltaP `3.5634` edge `0.0819` maxDD `-11.1695`
- `market_context_high->commodity_1h` score `-0.988` n `157` status `ready` deltaP `-2.153` edge `-0.0065` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
