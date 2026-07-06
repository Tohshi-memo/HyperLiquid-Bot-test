# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T08:22:33.305451+00:00`
- Price records: `672`
- Market context records: `5861`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10104`

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

- `news_risk_high->fx_4h` score `3.7011` n `30` status `ready` deltaP `38.628` edge `0.0555` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `1.9747` n `30` status `ready` deltaP `23.9321` edge `0.0189` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.855` n `30` status `ready` deltaP `11.3872` edge `0.0804` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.6121` n `247` status `ready` deltaP `6.898` edge `0.1508` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.2411` n `30` status `ready` deltaP `5.1697` edge `0.0426` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3385` n `247` status `ready` deltaP `0.8012` edge `-0.0002` maxDD `-0.5499`
- `news_risk_high->metal_1h` score `-0.4328` n `30` status `ready` deltaP `1.3872` edge `-0.0281` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4556` n `247` status `ready` deltaP `4.3086` edge `0.034` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5259` n `247` status `ready` deltaP `3.1146` edge `0.0025` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5497` n `247` status `ready` deltaP `-1.3013` edge `-0.0017` maxDD `-2.1412`
- `market_context_high->index_1h` score `-0.6279` n `247` status `ready` deltaP `0.0867` edge `0.0037` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.7745` n `247` status `ready` deltaP `3.9243` edge `0.0414` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.9178` n `247` status `ready` deltaP `2.754` edge `0.0386` maxDD `-6.6758`
- `news_risk_high->index_1h` score `-1.2401` n `30` status `ready` deltaP `-12.5449` edge `-0.0239` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.2491` n `247` status `ready` deltaP `-0.527` edge `0.0121` maxDD `-3.165`
- `market_context_high->equity_24h` score `-1.5278` n `228` status `ready` deltaP `15.1772` edge `0.2794` maxDD `-31.6316`
- `news_risk_high->commodity_4h` score `-1.7668` n `30` status `ready` deltaP `-13.1199` edge `-0.0515` maxDD `-2.3372`
- `market_context_high->metal_4h` score `-1.783` n `247` status `ready` deltaP `-3.5185` edge `-0.0337` maxDD `-6.381`
- `market_context_high->fx_4h` score `-1.815` n `247` status `ready` deltaP `-5.2182` edge `-0.003` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.8226` n `228` status `ready` deltaP `4.8794` edge `0.0156` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
