# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T16:22:32.233577+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10784`

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

- `risk_on_high->unknown_4h` score `20.3354` n `133` status `ready` deltaP `7.6265` edge `1.7056` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.3354` n `133` status `ready` deltaP `7.6265` edge `1.7056` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.4705` n `133` status `ready` deltaP `-1.5027` edge `1.0236` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.4705` n `133` status `ready` deltaP `-1.5027` edge `1.0236` maxDD `-1.95`
- `market_context_high->unknown_1h` score `9.295` n `212` status `ready` deltaP `-0.8785` edge `0.8435` maxDD `-2.0446`
- `market_context_high->unknown_4h` score `8.982` n `210` status `ready` deltaP `9.2305` edge `0.7565` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `2.5954` n `53` status `ready` deltaP `19.4772` edge `0.1134` maxDD `-0.8236`
- `news_risk_high->commodity_4h` score `1.5003` n `53` status `ready` deltaP `11.732` edge `0.0669` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `1.2411` n `53` status `ready` deltaP `9.2571` edge `0.059` maxDD `-0.0495`
- `news_risk_high->equity_1h` score `0.6289` n `53` status `ready` deltaP `10.1401` edge `0.0521` maxDD `-0.7924`
- `news_risk_high->index_1h` score `0.4761` n `53` status `ready` deltaP `10.0187` edge `0.008` maxDD `-0.1`
- `news_risk_high->metal_4h` score `0.2469` n `53` status `ready` deltaP `7.3862` edge `0.0247` maxDD `-1.0498`
- `risk_on_high->metal_1h` score `0.1023` n `133` status `ready` deltaP `12.4128` edge `0.0016` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1023` n `133` status `ready` deltaP `12.4128` edge `0.0016` maxDD `-1.699`
- `news_risk_high->fx_4h` score `-0.0066` n `53` status `ready` deltaP `7.0783` edge `-0.0007` maxDD `-1.0961`
- `news_risk_high->metal_1h` score `-0.0835` n `53` status `ready` deltaP `3.22` edge `0.0028` maxDD `-0.7973`
- `news_risk_high->commodity_1h` score `-0.1089` n `53` status `ready` deltaP `5.5277` edge `-0.0013` maxDD `-0.9036`
- `news_risk_high->equity_24h` score `-0.1137` n `53` status `ready` deltaP `3.5606` edge `0.075` maxDD `-5.0655`
- `market_context_high->equity_24h` score `-0.1149` n `167` status `ready` deltaP `12.4636` edge `0.3419` maxDD `-20.7654`
- `news_risk_high->crypto_major_4h` score `-0.1926` n `53` status `ready` deltaP `3.1552` edge `0.0595` maxDD `-6.0848`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
