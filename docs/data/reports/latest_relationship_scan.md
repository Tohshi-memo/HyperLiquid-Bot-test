# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T01:07:25.734126+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4416`

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

- `market_context_high->unknown_4h` score `120.7835` n `37` status `ready` deltaP `-7.5972` edge `10.1607` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.4666` n `37` status `ready` deltaP `37.7348` edge `0.0463` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.179` n `37` status `ready` deltaP `9.6092` edge `0.2468` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8465` n `37` status `ready` deltaP `24.3738` edge `0.0384` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.7281` n `52` status `ready` deltaP `10.4567` edge `0.0964` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8682` n `52` status `ready` deltaP `7.1412` edge `0.1376` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7507` n `37` status `ready` deltaP `9.4514` edge `0.0581` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.508` n `37` status `ready` deltaP `8.1203` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.421` n `37` status `ready` deltaP `10.649` edge `0.0645` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.2377` n `52` status `ready` deltaP `8.6773` edge `0.0204` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.2032` n `52` status `ready` deltaP `6.851` edge `0.1472` maxDD `-6.6786`
- `market_context_high->index_1h` score `0.1991` n `37` status `ready` deltaP `0.7526` edge `0.0386` maxDD `-0.1621`
- `news_risk_high->fx_4h` score `0.1611` n `52` status `ready` deltaP `8.5248` edge `0.0077` maxDD `-0.1771`
- `market_context_high->commodity_1h` score `0.1545` n `37` status `ready` deltaP `9.6173` edge `0.0103` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `0.0264` n `37` status `ready` deltaP `3.7492` edge `0.0238` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0419` n `37` status `ready` deltaP `1.6508` edge `0.0164` maxDD `-0.6226`
- `news_risk_high->index_1h` score `-0.0621` n `52` status `ready` deltaP `5.1704` edge `0.0029` maxDD `-0.2931`
- `news_risk_high->fx_1h` score `-0.2873` n `52` status `ready` deltaP `-0.1957` edge `0.003` maxDD `-0.0826`
- `news_risk_high->equity_1h` score `-0.2924` n `52` status `ready` deltaP `-3.6965` edge `0.0421` maxDD `-1.396`
- `market_context_high->equity_4h` score `-0.755` n `37` status `ready` deltaP `21.6423` edge `0.0869` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
