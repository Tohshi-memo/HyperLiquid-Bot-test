# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T18:07:21.475475+00:00`
- Price records: `672`
- Market context records: `1344`
- Flow alert records: `5782`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8783`

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

- `market_context_high->crypto_major_24h` score `14.2611` n `128` status `ready` deltaP `34.9826` edge `1.0684` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.9227` n `128` status `ready` deltaP `11.8056` edge `1.1649` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.4404` n `128` status `ready` deltaP `28.3854` edge `0.7991` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.4706` n `128` status `ready` deltaP `25.3472` edge `0.3122` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `2.7119` n `128` status `ready` deltaP `-9.2014` edge `0.4355` maxDD `-6.8535`
- `market_context_high->equity_24h` score `2.2428` n `128` status `ready` deltaP `18.2292` edge `0.3987` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.2208` n `157` status `ready` deltaP `11.7388` edge `0.1773` maxDD `-3.6396`
- `market_context_high->fx_24h` score `1.3747` n `128` status `ready` deltaP `15.0174` edge `0.0609` maxDD `-0.3831`
- `market_context_high->unknown_24h` score `0.7328` n `128` status `ready` deltaP `-5.0347` edge `0.3676` maxDD `-10.1706`
- `market_context_high->equity_1h` score `0.0857` n `157` status `ready` deltaP `2.9186` edge `0.0304` maxDD `-1.7505`
- `market_context_high->index_1h` score `0.0204` n `157` status `ready` deltaP `5.0145` edge `0.0146` maxDD `-1.6329`
- `market_context_high->index_4h` score `-0.0078` n `157` status `ready` deltaP `4.8742` edge `0.0754` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-0.0225` n `157` status `ready` deltaP `13.068` edge `0.0541` maxDD `-6.4478`
- `market_context_high->metal_1h` score `-0.1027` n `157` status `ready` deltaP `8.942` edge `0.0008` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4487` n `157` status `ready` deltaP `1.7068` edge `-0.0032` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.7494` n `157` status `ready` deltaP `-1.1051` edge `0.0064` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.9047` n `157` status `ready` deltaP `-0.6503` edge `0.016` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.1104` n `157` status `ready` deltaP `-3.1628` edge `-0.0192` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-1.3774` n `157` status `ready` deltaP `1.4292` edge `0.041` maxDD `-11.1695`
- `market_context_high->crypto_alt_4h` score `-1.5493` n `157` status `ready` deltaP `8.4676` edge `0.1464` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
