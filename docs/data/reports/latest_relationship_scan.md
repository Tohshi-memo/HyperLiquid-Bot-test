# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T01:52:23.442629+00:00`
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

- `market_context_high->unknown_4h` score `120.9109` n `37` status `ready` deltaP `-7.4448` edge `10.1703` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.441` n `37` status `ready` deltaP `37.43` edge `0.0462` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.2209` n `37` status `ready` deltaP `10.0583` edge `0.2473` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8355` n `37` status `ready` deltaP `24.2213` edge `0.0385` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.7468` n `52` status `ready` deltaP `10.6303` edge `0.0968` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8713` n `52` status `ready` deltaP `7.1412` edge `0.138` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7855` n `37` status `ready` deltaP `9.7508` edge `0.059` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.508` n `37` status `ready` deltaP `8.1203` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.4522` n `37` status `ready` deltaP `10.9484` edge `0.0665` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.2305` n `52` status `ready` deltaP `8.5248` edge `0.0205` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.223` n `37` status `ready` deltaP `1.052` edge `0.0386` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2103` n `52` status `ready` deltaP `6.851` edge `0.1481` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `0.1445` n `52` status `ready` deltaP `8.22` edge `0.0076` maxDD `-0.1771`
- `market_context_high->commodity_1h` score `0.1273` n `37` status `ready` deltaP `9.1682` edge `0.0098` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `0.0351` n `37` status `ready` deltaP `3.9017` edge `0.0239` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0264` n `37` status `ready` deltaP `1.9502` edge `0.0164` maxDD `-0.6226`
- `news_risk_high->index_1h` score `-0.0465` n `52` status `ready` deltaP `5.4698` edge `0.0029` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.2652` n `52` status `ready` deltaP `-3.2474` edge `0.0426` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.2873` n `52` status `ready` deltaP `-0.1957` edge `0.003` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.7519` n `37` status `ready` deltaP `21.6423` edge `0.0873` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
