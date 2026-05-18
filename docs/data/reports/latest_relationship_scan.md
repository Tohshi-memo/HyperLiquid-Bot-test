# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T02:52:13.041906+00:00`
- Price records: `672`
- Market context records: `1076`
- Flow alert records: `5003`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8728`

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

- `market_context_high->crypto_major_24h` score `16.3497` n `161` status `ready` deltaP `35.0141` edge `1.1754` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.7765` n `161` status `ready` deltaP `12.0265` edge `0.5246` maxDD `-9.5387`
- `market_context_high->equity_24h` score `5.3572` n `161` status `ready` deltaP `14.6094` edge `0.3987` maxDD `-3.6396`
- `market_context_high->metal_24h` score `4.4592` n `161` status `ready` deltaP `-2.3379` edge `0.5539` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.4227` n `161` status `ready` deltaP `14.7246` edge `0.3012` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.5887` n `163` status `ready` deltaP `8.748` edge `0.1529` maxDD `-3.6396`
- `market_context_high->crypto_major_4h` score `1.4295` n `163` status `ready` deltaP `13.3688` edge `0.1986` maxDD `-6.4882`
- `market_context_high->index_4h` score `0.8527` n `163` status `ready` deltaP `7.2086` edge `0.0913` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6321` n `170` status `ready` deltaP `8.2599` edge `0.0293` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.6047` n `170` status `ready` deltaP `3.3832` edge `0.0656` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.4059` n `170` status `ready` deltaP `8.193` edge `0.0462` maxDD `-3.3594`
- `market_context_high->fx_1h` score `0.0503` n `170` status `ready` deltaP `7.2843` edge `0.0012` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.0808` n `170` status `ready` deltaP `7.3811` edge `0.0051` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.1886` n `170` status `ready` deltaP `3.2635` edge `0.0468` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.3697` n `163` status `ready` deltaP `7.2936` edge `0.171` maxDD `-13.0347`
- `market_context_high->fx_4h` score `-0.6672` n `163` status `ready` deltaP `1.861` edge `0.0017` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7187` n `170` status `ready` deltaP `-1.4336` edge `-0.0018` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-1.9332` n `163` status `ready` deltaP `4.5087` edge `-0.0825` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.3856` n `163` status `ready` deltaP `8.2934` edge `-0.1241` maxDD `-6.7322`
- `market_context_high->fx_24h` score `-3.0806` n `161` status `ready` deltaP `5.1135` edge `-0.0214` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
