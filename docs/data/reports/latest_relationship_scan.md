# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T07:52:32.308405+00:00`
- Price records: `672`
- Market context records: `5859`
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
- `news_risk_high->crypto_major_1h` score `0.8667` n `30` status `ready` deltaP `11.5369` edge `0.0809` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.6498` n `249` status `ready` deltaP `7.1745` edge `0.1521` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.2458` n `30` status `ready` deltaP `5.1697` edge `0.0432` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3603` n `249` status `ready` deltaP `0.398` edge `-0.0003` maxDD `-0.5499`
- `news_risk_high->metal_1h` score `-0.4102` n `30` status `ready` deltaP `1.6866` edge `-0.0272` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4919` n `249` status `ready` deltaP `3.9608` edge `0.0333` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5397` n `249` status `ready` deltaP `2.9718` edge `0.0023` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5451` n `249` status `ready` deltaP `-1.1682` edge `-0.002` maxDD `-2.1412`
- `market_context_high->index_1h` score `-0.6343` n `249` status `ready` deltaP `-0.0367` edge `0.0037` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.7663` n `249` status `ready` deltaP `4.0269` edge `0.0414` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.923` n `249` status `ready` deltaP `2.7199` edge `0.0384` maxDD `-6.6758`
- `news_risk_high->index_1h` score `-1.2237` n `30` status `ready` deltaP `-12.2455` edge `-0.0238` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.24` n `249` status `ready` deltaP `-0.412` edge `0.0125` maxDD `-3.165`
- `market_context_high->equity_24h` score `-1.357` n `228` status `ready` deltaP `15.7072` edge `0.2901` maxDD `-31.6316`
- `news_risk_high->commodity_4h` score `-1.7755` n `30` status `ready` deltaP `-13.2723` edge `-0.0516` maxDD `-2.3372`
- `market_context_high->fx_4h` score `-1.7902` n `249` status `ready` deltaP `-4.7857` edge `-0.0027` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.8195` n `228` status `ready` deltaP `4.8794` edge `0.016` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-1.8263` n `249` status `ready` deltaP `-3.6396` edge `-0.034` maxDD `-6.7367`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
