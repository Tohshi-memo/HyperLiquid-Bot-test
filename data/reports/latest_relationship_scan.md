# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T18:52:28.042811+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14824`

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

- `news_risk_high->unknown_4h` score `13.4521` n `51` status `ready` deltaP `24.1063` edge `0.9649` maxDD `-0.0348`
- `risk_on_high->unknown_1h` score `4.04` n `37` status `ready` deltaP `-8.5127` edge `0.6196` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `4.04` n `37` status `ready` deltaP `-8.5127` edge `0.6196` maxDD `-1.5916`
- `news_risk_high->unknown_1h` score `3.2309` n `51` status `ready` deltaP `17.0834` edge `0.1858` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.0047` n `51` status `ready` deltaP `35.6438` edge `0.0262` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.6554` n `51` status `ready` deltaP `23.2694` edge `0.1432` maxDD `-2.164`
- `risk_on_high->metal_4h` score `2.1513` n `33` status `ready` deltaP `28.8849` edge `-0.0045` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.1513` n `33` status `ready` deltaP `28.8849` edge `-0.0045` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `1.5543` n `33` status `ready` deltaP `-1.686` edge `0.2535` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `1.5543` n `33` status `ready` deltaP `-1.686` edge `0.2535` maxDD `-0.773`
- `news_risk_high->fx_1h` score `1.1631` n `51` status `ready` deltaP `16.0972` edge `0.0066` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `0.9836` n `140` status `ready` deltaP `6.1591` edge `0.0858` maxDD `-1.5916`
- `market_context_high->crypto_alt_4h` score `0.9585` n `129` status `ready` deltaP `8.8958` edge `0.167` maxDD `-7.0478`
- `risk_on_high->fx_4h` score `0.7396` n `33` status `ready` deltaP `17.1055` edge `0.004` maxDD `-0.1905`
- `risk_on_and_context->fx_4h` score `0.7396` n `33` status `ready` deltaP `17.1055` edge `0.004` maxDD `-0.1905`
- `news_risk_high->equity_1h` score `0.695` n `51` status `ready` deltaP `15.9475` edge `0.0192` maxDD `-0.9128`
- `market_context_high->commodity_24h` score `0.5781` n `109` status `ready` deltaP `-2.1518` edge `0.11` maxDD `-0.7984`
- `news_risk_high->index_4h` score `0.4669` n `51` status `ready` deltaP `8.9759` edge `0.0188` maxDD `-0.1788`
- `risk_on_high->index_4h` score `0.3544` n `33` status `ready` deltaP `7.7282` edge `0.0419` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `0.3544` n `33` status `ready` deltaP `7.7282` edge `0.0419` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
