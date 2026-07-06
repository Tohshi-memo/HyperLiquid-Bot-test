# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T08:07:29.566159+00:00`
- Price records: `672`
- Market context records: `5860`
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
- `news_risk_high->crypto_major_1h` score `0.8542` n `30` status `ready` deltaP `11.3872` edge `0.0803` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.6268` n `248` status `ready` deltaP `7.0368` edge `0.1511` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.2318` n `30` status `ready` deltaP `5.02` edge `0.0424` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.349` n `248` status `ready` deltaP `0.5988` edge `-0.0002` maxDD `-0.5499`
- `news_risk_high->metal_1h` score `-0.4227` n `30` status `ready` deltaP `1.5369` edge `-0.0278` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4804` n `248` status `ready` deltaP `4.0588` edge `0.0336` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5353` n `248` status `ready` deltaP `3.0423` edge `0.0022` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5477` n `248` status `ready` deltaP `-1.2338` edge `-0.0019` maxDD `-2.1412`
- `market_context_high->index_1h` score `-0.6311` n `248` status `ready` deltaP `0.0242` edge `0.0037` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.759` n `248` status `ready` deltaP `4.1023` edge `0.0415` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.9163` n `248` status `ready` deltaP `2.7888` edge `0.0385` maxDD `-6.6758`
- `news_risk_high->index_1h` score `-1.2323` n `30` status `ready` deltaP `-12.3952` edge `-0.0239` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.2519` n `248` status `ready` deltaP `-0.595` edge `0.0122` maxDD `-3.165`
- `market_context_high->equity_24h` score `-1.4406` n `228` status `ready` deltaP `15.4422` edge `0.2849` maxDD `-31.6316`
- `news_risk_high->commodity_4h` score `-1.7668` n `30` status `ready` deltaP `-13.1199` edge `-0.0515` maxDD `-2.3372`
- `market_context_high->fx_4h` score `-1.803` n `248` status `ready` deltaP `-5.001` edge `-0.0029` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-1.8097` n `248` status `ready` deltaP `-3.5798` edge `-0.034` maxDD `-6.5986`
- `market_context_high->fx_24h` score `-1.821` n `228` status `ready` deltaP `4.8794` edge `0.0158` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
