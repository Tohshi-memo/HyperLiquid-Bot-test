# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T02:22:35.489929+00:00`
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

- `market_context_high->unknown_4h` score `120.9929` n `37` status `ready` deltaP `-7.1399` edge `10.1751` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.4154` n `37` status `ready` deltaP `37.1251` edge `0.0461` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.2353` n `37` status `ready` deltaP `10.208` edge `0.2475` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8611` n `37` status `ready` deltaP `24.5262` edge `0.0386` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.7516` n `52` status `ready` deltaP `10.6303` edge `0.0972` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8752` n `52` status `ready` deltaP `7.1412` edge `0.1385` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7891` n `37` status `ready` deltaP `9.7508` edge `0.0593` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.4829` n `37` status `ready` deltaP `7.8209` edge `0.0152` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.4553` n `37` status `ready` deltaP `10.9484` edge `0.0669` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.2472` n `52` status `ready` deltaP `8.8297` edge `0.0206` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.247` n `37` status `ready` deltaP `1.3514` edge `0.0386` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2165` n `52` status `ready` deltaP `6.851` edge `0.1489` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `0.1278` n `52` status `ready` deltaP `7.9151` edge `0.0075` maxDD `-0.1771`
- `market_context_high->commodity_1h` score `0.1195` n `37` status `ready` deltaP `9.0185` edge `0.0098` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `0.0525` n `37` status `ready` deltaP `4.2065` edge `0.0241` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.01` n `37` status `ready` deltaP `2.2496` edge `0.0165` maxDD `-0.6226`
- `news_risk_high->index_1h` score `-0.031` n `52` status `ready` deltaP `5.7692` edge `0.0029` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.2559` n `52` status `ready` deltaP `-3.0977` edge `0.0428` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.3037` n `52` status `ready` deltaP `-0.4951` edge `0.0029` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.748` n `37` status `ready` deltaP `21.6423` edge `0.0878` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
