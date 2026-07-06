# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T07:37:29.504301+00:00`
- Price records: `672`
- Market context records: `5858`
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
- `news_risk_high->crypto_major_1h` score `0.8799` n `30` status `ready` deltaP `11.6866` edge `0.0816` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.6667` n `250` status `ready` deltaP `7.311` edge `0.1526` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.2598` n `30` status `ready` deltaP `5.3194` edge `0.044` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3706` n `250` status `ready` deltaP `0.1988` edge `-0.0003` maxDD `-0.5499`
- `news_risk_high->metal_1h` score `-0.3978` n `30` status `ready` deltaP `1.8363` edge `-0.0266` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4891` n `250` status `ready` deltaP `3.9653` edge `0.0335` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.5433` n `250` status `ready` deltaP `-1.1042` edge `-0.0022` maxDD `-2.1412`
- `market_context_high->metal_1h` score `-0.544` n `250` status `ready` deltaP `2.903` edge `0.0024` maxDD `-2.0339`
- `market_context_high->index_1h` score `-0.6243` n `250` status `ready` deltaP `0.1545` edge `0.0037` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.777` n `250` status `ready` deltaP `3.9533` edge `0.041` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.9332` n `250` status `ready` deltaP `2.6527` edge `0.038` maxDD `-6.6758`
- `news_risk_high->index_1h` score `-1.2237` n `30` status `ready` deltaP `-12.2455` edge `-0.0238` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.2427` n `250` status `ready` deltaP `-0.478` edge `0.0126` maxDD `-3.165`
- `market_context_high->equity_24h` score `-1.2626` n `228` status `ready` deltaP `15.9722` edge `0.2962` maxDD `-31.6316`
- `market_context_high->fx_4h` score `-1.7783` n `250` status `ready` deltaP `-4.572` edge `-0.0026` maxDD `-2.2593`
- `news_risk_high->commodity_4h` score `-1.7842` n `30` status `ready` deltaP `-13.4248` edge `-0.0517` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8179` n `228` status `ready` deltaP `4.8794` edge `0.0162` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-1.86` n `250` status `ready` deltaP `-3.6976` edge `-0.0343` maxDD `-7.0271`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
