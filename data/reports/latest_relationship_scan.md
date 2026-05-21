# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T01:22:16.846262+00:00`
- Price records: `672`
- Market context records: `1376`
- Flow alert records: `5873`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.3091` n `148` status `ready` deltaP `30.687` edge `1.0177` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.07` n `148` status `ready` deltaP `13.4478` edge `1.0829` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.0138` n `148` status `ready` deltaP `28.7022` edge `0.9281` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1692` n `148` status `ready` deltaP `21.7905` edge `0.3108` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7041` n `148` status `ready` deltaP `14.8836` edge `0.3588` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5835` n `173` status `ready` deltaP `8.9481` edge `0.1553` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0151` n `148` status `ready` deltaP `8.7556` edge `0.0435` maxDD `-1.3821`
- `market_context_high->metal_4h` score `-0.0635` n `173` status `ready` deltaP `11.1765` edge `0.0633` maxDD `-6.4478`
- `market_context_high->index_1h` score `-0.0896` n `185` status `ready` deltaP `3.6956` edge `0.0144` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0971` n `185` status `ready` deltaP `2.5895` edge `0.0305` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.3603` n `173` status `ready` deltaP `0.5569` edge `0.059` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.3997` n `185` status `ready` deltaP `2.4074` edge `-0.0028` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.5921` n `185` status `ready` deltaP `6.4986` edge `0.0062` maxDD `-3.5762`
- `market_context_high->crypto_alt_1h` score `-0.6679` n `185` status `ready` deltaP `0.4944` edge `0.0281` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.7159` n `185` status `ready` deltaP `-0.3868` edge `0.0044` maxDD `-2.252`
- `market_context_high->crypto_major_1h` score `-1.3857` n `185` status `ready` deltaP `-1.6426` edge `0.002` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.5055` n `173` status `ready` deltaP `7.4545` edge `0.1568` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.6386` n `173` status `ready` deltaP `3.7255` edge `0.1095` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.9817` n `173` status `ready` deltaP `-8.0828` edge `-0.0142` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.255` n `173` status `ready` deltaP `2.5817` edge `-0.2074` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
