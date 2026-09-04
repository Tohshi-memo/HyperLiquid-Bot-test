# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T22:07:25.793896+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10662`

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

- `risk_on_high->unknown_4h` score `19.8435` n `133` status `ready` deltaP `8.6936` edge `1.6575` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.8435` n `133` status `ready` deltaP `8.6936` edge `1.6575` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `10.2837` n `133` status `ready` deltaP `-1.6524` edge `0.9257` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `10.2837` n `133` status `ready` deltaP `-1.6524` edge `0.9257` maxDD `-1.95`
- `market_context_high->unknown_4h` score `9.346` n `217` status `ready` deltaP `9.1302` edge `0.7875` maxDD `-2.563`
- `market_context_high->unknown_1h` score `7.5052` n `217` status `ready` deltaP `-0.7065` edge `0.6932` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `4.4158` n `46` status `ready` deltaP `20.8862` edge `0.2557` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `2.3157` n `46` status `ready` deltaP `10.0345` edge `0.1744` maxDD `-1.5324`
- `news_risk_high->commodity_24h` score `1.951` n `46` status `ready` deltaP `11.1715` edge `0.1053` maxDD `-0.042`
- `news_risk_high->metal_4h` score `1.6887` n `46` status `ready` deltaP `17.7757` edge `0.0485` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.5943` n `46` status `ready` deltaP `15.3801` edge `0.0694` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.4511` n `46` status `ready` deltaP `9.9615` edge `0.0746` maxDD `-0.2737`
- `news_risk_high->index_1h` score `1.1469` n `46` status `ready` deltaP `14.6967` edge `0.011` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `0.7652` n `46` status `ready` deltaP `9.8217` edge `0.0176` maxDD `-0.2118`
- `news_risk_high->fx_4h` score `0.2799` n `46` status `ready` deltaP `10.2532` edge `0.0002` maxDD `-0.9514`
- `news_risk_high->commodity_1h` score `0.2233` n `46` status `ready` deltaP `8.93` edge `0.0037` maxDD `-0.9036`
- `news_risk_high->crypto_alt_1h` score `0.2215` n `46` status `ready` deltaP `4.2047` edge `0.0207` maxDD `-1.0885`
- `risk_on_high->metal_1h` score `0.1217` n `133` status `ready` deltaP `12.8619` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1217` n `133` status `ready` deltaP `12.8619` edge `0.0011` maxDD `-1.699`
- `news_risk_high->crypto_major_1h` score `0.1162` n `46` status `ready` deltaP `0.2278` edge `0.0426` maxDD `-1.0047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
