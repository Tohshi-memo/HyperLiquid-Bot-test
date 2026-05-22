# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T08:07:17.328623+00:00`
- Price records: `672`
- Market context records: `1508`
- Flow alert records: `6252`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8791`

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

- `market_context_high->metal_24h` score `13.8788` n `161` status `ready` deltaP `23.403` edge `1.1006` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1505` n `161` status `ready` deltaP `28.8658` edge `0.9384` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.6138` n `161` status `ready` deltaP `27.5966` edge `0.8137` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.7045` n `161` status `ready` deltaP `19.7765` edge `0.2855` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.5205` n `161` status `ready` deltaP `12.9788` edge `0.3562` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.9917` n `161` status `ready` deltaP `18.847` edge `0.0619` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.9236` n `187` status `ready` deltaP `5.7389` edge `0.1217` maxDD `-3.6396`
- `market_context_high->equity_1h` score `-0.3185` n `191` status `ready` deltaP `0.6262` edge `0.0293` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.327` n `191` status `ready` deltaP `1.9736` edge `0.0061` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.5342` n `191` status `ready` deltaP `-0.3386` edge `-0.003` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.6918` n `191` status `ready` deltaP `1.0072` edge `0.038` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.7398` n `191` status `ready` deltaP `5.5695` edge `0.0016` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-0.7703` n `187` status `ready` deltaP `8.9108` edge `0.1738` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.8023` n `187` status `ready` deltaP `5.165` edge `0.1336` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-0.8242` n `191` status `ready` deltaP `-1.2344` edge `-0.0053` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.022` n `191` status `ready` deltaP `-1.0863` edge `0.0119` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.2206` n `187` status `ready` deltaP `10.8102` edge `0.0954` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.2813` n `187` status `ready` deltaP `-4.0465` edge `0.0291` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.6061` n `187` status `ready` deltaP `-4.6131` edge `-0.0102` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-2.376` n `161` status `ready` deltaP `-1.9701` edge `0.0881` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
