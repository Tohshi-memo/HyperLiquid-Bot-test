# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T19:22:18.289755+00:00`
- Price records: `672`
- Market context records: `1349`
- Flow alert records: `5798`
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

- `market_context_high->crypto_major_24h` score `13.8845` n `128` status `ready` deltaP `34.1145` edge `1.0428` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.7919` n `128` status `ready` deltaP `11.8056` edge `1.154` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.39` n `128` status `ready` deltaP `28.3854` edge `0.7949` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.2535` n `128` status `ready` deltaP `24.4792` edge `0.2999` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `3.1089` n `128` status `ready` deltaP `-8.3333` edge `0.4628` maxDD `-6.8535`
- `market_context_high->equity_4h` score `2.2412` n `157` status `ready` deltaP `11.7388` edge `0.179` maxDD `-3.6396`
- `market_context_high->equity_24h` score `2.0511` n `128` status `ready` deltaP `17.3611` edge `0.3799` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.4658` n `128` status `ready` deltaP `15.8855` edge `0.0627` maxDD `-0.3831`
- `market_context_high->unknown_24h` score `0.6488` n `128` status `ready` deltaP `-5.0347` edge `0.3606` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.0752` n `161` status `ready` deltaP `5.3818` edge `0.0158` maxDD `-1.6329`
- `market_context_high->equity_1h` score `0.0145` n `161` status `ready` deltaP `2.3431` edge `0.0283` maxDD `-1.7505`
- `market_context_high->metal_4h` score `0.0051` n `157` status `ready` deltaP `13.068` edge `0.0564` maxDD `-6.4478`
- `market_context_high->index_4h` score `-0.0078` n `157` status `ready` deltaP `4.8742` edge `0.0754` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.0958` n `161` status `ready` deltaP `8.9077` edge `0.0016` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.3611` n `161` status `ready` deltaP `2.7123` edge `-0.0026` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.6109` n `161` status `ready` deltaP `0.0112` edge `0.0105` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-1.0202` n `161` status `ready` deltaP `-1.2246` edge `0.0102` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.2514` n `161` status `ready` deltaP `-4.2474` edge `-0.0256` maxDD `-6.1883`
- `market_context_high->unknown_4h` score `-1.3821` n `157` status `ready` deltaP `1.4292` edge `0.0404` maxDD `-11.1695`
- `market_context_high->crypto_alt_4h` score `-1.4617` n `157` status `ready` deltaP `8.4676` edge `0.1537` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
