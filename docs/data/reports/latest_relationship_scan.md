# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T21:07:23.825472+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_4h` score `13.3475` n `51` status `ready` deltaP `23.9538` edge `0.9572` maxDD `-0.0348`
- `risk_on_high->unknown_1h` score `3.9855` n `37` status `ready` deltaP `-8.8121` edge `0.6146` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `3.9855` n `37` status `ready` deltaP `-8.8121` edge `0.6146` maxDD `-1.5916`
- `news_risk_high->unknown_1h` score `3.1469` n `51` status `ready` deltaP `16.784` edge `0.1808` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.0229` n `51` status `ready` deltaP `35.7963` edge `0.0267` maxDD `-0.0746`
- `risk_on_high->equity_4h` score `2.8143` n `37` status `ready` deltaP `2.7934` edge `0.2589` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `2.8143` n `37` status `ready` deltaP `2.7934` edge `0.2589` maxDD `-0.773`
- `news_risk_high->equity_4h` score `2.5524` n `51` status `ready` deltaP `22.5072` edge `0.1397` maxDD `-2.164`
- `risk_on_high->metal_4h` score `2.2291` n `37` status `ready` deltaP `29.738` edge `-0.0037` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.2291` n `37` status `ready` deltaP `29.738` edge `-0.0037` maxDD `-0.0367`
- `news_risk_high->fx_1h` score `1.229` n `51` status `ready` deltaP `16.8457` edge `0.0071` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.1405` n `147` status `ready` deltaP `7.2202` edge `0.0918` maxDD `-1.5916`
- `market_context_high->crypto_alt_4h` score `0.9615` n `135` status `ready` deltaP `10.0734` edge `0.1594` maxDD `-7.0478`
- `risk_on_high->index_4h` score `0.941` n `37` status `ready` deltaP `12.3146` edge `0.0443` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `0.941` n `37` status `ready` deltaP `12.3146` edge `0.0443` maxDD `-0.1719`
- `market_context_high->commodity_24h` score `0.731` n `107` status `ready` deltaP `-1.0352` edge `0.1153` maxDD `-0.7984`
- `news_risk_high->equity_1h` score `0.6989` n `51` status `ready` deltaP `16.0972` edge `0.0187` maxDD `-0.9128`
- `market_context_high->unknown_4h` score `0.517` n `135` status `ready` deltaP `19.9887` edge `-0.073` maxDD `-0.3741`
- `news_risk_high->index_4h` score `0.4609` n `51` status `ready` deltaP `8.9759` edge `0.0183` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.229` n `51` status `ready` deltaP `8.9879` edge `-0.01` maxDD `-0.4666`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
