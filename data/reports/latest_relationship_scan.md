# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T07:52:27.705083+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4790`

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

- `market_context_high->unknown_4h` score `125.1748` n `37` status `ready` deltaP `-4.396` edge `10.5053` maxDD `-0.9139`
- `market_context_high->equity_1h` score `3.2664` n `37` status `ready` deltaP `10.5074` edge `0.2481` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.2217` n `37` status `ready` deltaP `34.8385` edge `0.0452` maxDD `-0.0521`
- `market_context_high->index_4h` score `2.0438` n `37` status `ready` deltaP `26.6604` edge `0.0396` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.6946` n `49` status `ready` deltaP `9.4529` edge `0.1003` maxDD `-0.1014`
- `market_context_high->crypto_major_1h` score `0.7807` n `37` status `ready` deltaP `9.7508` edge `0.0586` maxDD `-3.0172`
- `news_risk_high->equity_4h` score `0.7339` n `49` status `ready` deltaP `5.6527` edge `0.1303` maxDD `-4.2454`
- `market_context_high->crypto_alt_1h` score `0.5168` n `37` status `ready` deltaP `11.6969` edge `0.0698` maxDD `-3.1881`
- `market_context_high->fx_1h` score `0.4086` n `37` status `ready` deltaP `6.9227` edge `0.015` maxDD `-0.1681`
- `news_risk_high->fx_4h` score `0.3521` n `49` status `ready` deltaP `9.6317` edge `0.0085` maxDD `-0.136`
- `market_context_high->index_1h` score `0.3093` n `37` status `ready` deltaP `2.0999` edge `0.0388` maxDD `-0.1621`
- `news_risk_high->index_4h` score `0.2526` n `49` status `ready` deltaP `8.8446` edge `0.0212` maxDD `-0.4888`
- `market_context_high->commodity_1h` score `0.1273` n `37` status `ready` deltaP `9.1682` edge `0.0098` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.1087` n `52` status `ready` deltaP `8.4408` edge `0.003` maxDD `-0.2931`
- `news_risk_high->index_24h` score `0.0519` n `49` status `ready` deltaP `4.4962` edge `0.1435` maxDD `-6.6786`
- `market_context_high->commodity_4h` score `0.0295` n `37` status `ready` deltaP `3.7492` edge `0.0242` maxDD `-1.633`
- `news_risk_high->equity_1h` score `-0.0091` n `52` status `ready` deltaP `1.0479` edge `0.0468` maxDD `-1.396`
- `market_context_high->metal_1h` score `-0.0248` n `37` status `ready` deltaP `1.9502` edge `0.0166` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.1441` n `52` status `ready` deltaP `2.4528` edge `0.0037` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.6378` n `37` status `ready` deltaP `22.8618` edge `0.0938` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
