# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T19:52:27.481157+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10794`

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

- `risk_on_high->unknown_4h` score `19.6492` n `133` status `ready` deltaP `7.779` edge `1.6474` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.6492` n `133` status `ready` deltaP `7.779` edge `1.6474` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.4922` n `133` status `ready` deltaP `-2.1015` edge `1.0294` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.4922` n `133` status `ready` deltaP `-2.1015` edge `1.0294` maxDD `-1.95`
- `market_context_high->unknown_4h` score `10.0614` n `213` status `ready` deltaP `9.2086` edge `0.8466` maxDD `-2.563`
- `market_context_high->unknown_1h` score `8.7137` n `217` status `ready` deltaP `-1.1556` edge `0.7969` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `3.8312` n `46` status `ready` deltaP `19.3237` edge `0.2174` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `2.1937` n `46` status `ready` deltaP `9.4247` edge `0.1683` maxDD `-1.5324`
- `news_risk_high->commodity_24h` score `2.088` n `46` status `ready` deltaP `12.734` edge `0.1063` maxDD `-0.042`
- `news_risk_high->equity_1h` score `1.6674` n `46` status `ready` deltaP `16.1286` edge `0.0705` maxDD `-0.7924`
- `news_risk_high->metal_4h` score `1.6241` n `46` status `ready` deltaP `17.0135` edge `0.0482` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.5204` n `46` status `ready` deltaP `10.7237` edge `0.0753` maxDD `-0.2737`
- `news_risk_high->index_1h` score `1.1217` n `46` status `ready` deltaP `14.3973` edge `0.0109` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `0.7041` n `46` status `ready` deltaP `9.0732` edge `0.0175` maxDD `-0.2118`
- `news_risk_high->fx_4h` score `0.2811` n `46` status `ready` deltaP `10.2532` edge `0.0003` maxDD `-0.9514`
- `news_risk_high->commodity_1h` score `0.1861` n `46` status `ready` deltaP `8.4809` edge `0.0036` maxDD `-0.9036`
- `news_risk_high->crypto_alt_1h` score `0.1544` n `46` status `ready` deltaP `3.7556` edge `0.0181` maxDD `-1.0885`
- `risk_on_high->metal_1h` score `0.082` n `133` status `ready` deltaP `12.1134` edge `0.001` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.082` n `133` status `ready` deltaP `12.1134` edge `0.001` maxDD `-1.699`
- `news_risk_high->crypto_major_1h` score `0.0461` n `46` status `ready` deltaP `-0.6704` edge `0.0396` maxDD `-1.0047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
