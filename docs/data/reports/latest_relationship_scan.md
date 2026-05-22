# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T06:52:18.658917+00:00`
- Price records: `672`
- Market context records: `1503`
- Flow alert records: `6236`
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

- `market_context_high->metal_24h` score `13.3768` n `166` status `ready` deltaP `23.1426` edge `1.0605` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1718` n `166` status `ready` deltaP `28.922` edge `0.9398` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.3702` n `166` status `ready` deltaP `27.2067` edge `0.796` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.7855` n `166` status `ready` deltaP `20.0385` edge `0.2905` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.8012` n `166` status `ready` deltaP `13.2781` edge `0.3776` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.0588` n `192` status `ready` deltaP `6.1992` edge `0.1299` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.9955` n `166` status `ready` deltaP `19.3148` edge `0.0591` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.2472` n `193` status `ready` deltaP `2.7908` edge `0.0073` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.3241` n `193` status `ready` deltaP `0.7066` edge `0.0283` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.5241` n `193` status `ready` deltaP `-0.1443` edge `-0.003` maxDD `-0.3914`
- `market_context_high->crypto_alt_4h` score `-0.5505` n `192` status `ready` deltaP `9.5528` edge `0.1977` maxDD `-19.5565`
- `market_context_high->crypto_alt_1h` score `-0.618` n `193` status `ready` deltaP `1.3295` edge `0.042` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.6994` n `193` status `ready` deltaP `6.0617` edge `0.0035` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-1.0126` n `192` status `ready` deltaP `5.4751` edge `0.15` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.0336` n `193` status `ready` deltaP `-1.2496` edge `0.0115` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.1444` n `192` status `ready` deltaP `-3.0996` edge `0.0342` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.1737` n `192` status `ready` deltaP `11.217` edge `0.0966` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.3016` n `193` status `ready` deltaP `-1.5947` edge `-0.0057` maxDD `-4.7041`
- `market_context_high->fx_4h` score `-1.5163` n `192` status `ready` deltaP `-3.5951` edge `-0.0095` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-3.9338` n `166` status `ready` deltaP `-0.9224` edge `-0.0487` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
