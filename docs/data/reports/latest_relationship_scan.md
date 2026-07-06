# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T07:07:25.621555+00:00`
- Price records: `672`
- Market context records: `5856`
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
- `news_risk_high->crypto_major_1h` score `0.9041` n `30` status `ready` deltaP `11.986` edge `0.0827` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.6967` n `252` status `ready` deltaP `7.5808` edge `0.1533` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.2863` n `30` status `ready` deltaP `5.6188` edge `0.0454` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.349` n `252` status `ready` deltaP `0.5988` edge `-0.0002` maxDD `-0.5499`
- `news_risk_high->metal_1h` score `-0.3962` n `30` status `ready` deltaP `1.8363` edge `-0.0264` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4539` n `252` status `ready` deltaP `4.2701` edge `0.0344` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5115` n `252` status `ready` deltaP `3.2649` edge `0.0027` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5529` n `252` status `ready` deltaP `-1.2285` edge `-0.0026` maxDD `-2.1412`
- `market_context_high->index_1h` score `-0.6031` n `252` status `ready` deltaP `0.5323` edge `0.0039` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.8015` n `252` status `ready` deltaP `3.8114` edge `0.0399` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.9579` n `252` status `ready` deltaP `2.5235` edge `0.0368` maxDD `-6.6758`
- `market_context_high->equity_24h` score `-1.0714` n `228` status `ready` deltaP `16.5022` edge `0.3086` maxDD `-31.6316`
- `market_context_high->index_4h` score `-1.2207` n `252` status `ready` deltaP `-0.1161` edge `0.013` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2237` n `30` status `ready` deltaP `-12.2455` edge `-0.0238` maxDD `-1.1161`
- `market_context_high->fx_4h` score `-1.7548` n `252` status `ready` deltaP `-4.1498` edge `-0.0024` maxDD `-2.2593`
- `news_risk_high->commodity_4h` score `-1.7819` n `30` status `ready` deltaP `-13.4248` edge `-0.0514` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8148` n `228` status `ready` deltaP `4.8794` edge `0.0166` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-1.9427` n `252` status `ready` deltaP `-3.8086` edge `-0.0359` maxDD `-7.6883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
