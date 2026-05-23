# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T01:37:16.460062+00:00`
- Price records: `672`
- Market context records: `1583`
- Flow alert records: `6471`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `13.5603` n `182` status `ready` deltaP `28.331` edge `1.0412` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.9238` n `182` status `ready` deltaP `26.9974` edge `1.0153` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.2873` n `182` status `ready` deltaP `26.7399` edge `0.7922` maxDD `-8.0553`
- `market_context_high->equity_24h` score `4.3921` n `182` status `ready` deltaP `18.9293` edge `0.4725` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.1218` n `182` status `ready` deltaP `21.648` edge `0.3078` maxDD `-5.3574`
- `market_context_high->equity_4h` score `0.997` n `199` status `ready` deltaP `8.7495` edge `0.1342` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.2645` n `199` status `ready` deltaP `13.2545` edge `0.2775` maxDD `-19.5565`
- `market_context_high->fx_24h` score `0.1031` n `182` status `ready` deltaP `10.8001` edge `0.0415` maxDD `-1.3925`
- `market_context_high->crypto_major_4h` score `0.0731` n `199` status `ready` deltaP `9.2796` edge `0.2184` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.323` n `199` status `ready` deltaP `0.8177` edge `0.0555` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5467` n `199` status `ready` deltaP `0.9133` edge `0.0292` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6074` n `199` status `ready` deltaP `1.3729` edge `0.0034` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6102` n `199` status `ready` deltaP `-1.6948` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.6963` n `199` status `ready` deltaP `5.7466` edge `0.006` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.8084` n `199` status `ready` deltaP `-1.3954` edge `-0.0022` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8654` n `199` status `ready` deltaP `-0.4438` edge `0.0277` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.1468` n `199` status `ready` deltaP `-2.3058` edge `0.0287` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.2958` n `199` status `ready` deltaP `10.516` edge `0.0911` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.387` n `199` status `ready` deltaP `-10.5497` edge `-0.0146` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.2424` n `199` status `ready` deltaP `-14.7001` edge `-0.1114` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
