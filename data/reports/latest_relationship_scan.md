# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T02:07:28.644473+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4422`

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

- `market_context_high->unknown_4h` score `120.9555` n `37` status `ready` deltaP `-7.2923` edge `10.173` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.4288` n `37` status `ready` deltaP `37.2775` edge `0.0462` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.2341` n `37` status `ready` deltaP `10.208` edge `0.2474` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8477` n `37` status `ready` deltaP `24.3738` edge `0.0385` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.7492` n `52` status `ready` deltaP `10.6303` edge `0.097` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8737` n `52` status `ready` deltaP `7.1412` edge `0.1383` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7879` n `37` status `ready` deltaP `9.7508` edge `0.0592` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.4948` n `37` status `ready` deltaP `7.9706` edge `0.0152` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.4561` n `37` status `ready` deltaP `10.9484` edge `0.067` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.2385` n `52` status `ready` deltaP `8.6773` edge `0.0205` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.235` n `37` status `ready` deltaP `1.2017` edge `0.0386` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2134` n `52` status `ready` deltaP `6.851` edge `0.1485` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `0.1365` n `52` status `ready` deltaP `8.0675` edge `0.0076` maxDD `-0.1771`
- `market_context_high->commodity_1h` score `0.1273` n `37` status `ready` deltaP `9.1682` edge `0.0098` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `0.0438` n `37` status `ready` deltaP `4.0541` edge `0.024` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0178` n `37` status `ready` deltaP `2.0999` edge `0.0165` maxDD `-0.6226`
- `news_risk_high->index_1h` score `-0.0387` n `52` status `ready` deltaP `5.6195` edge `0.0029` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.2566` n `52` status `ready` deltaP `-3.0977` edge `0.0427` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.2959` n `52` status `ready` deltaP `-0.3454` edge `0.0029` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.7496` n `37` status `ready` deltaP `21.6423` edge `0.0876` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
