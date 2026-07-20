# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T02:07:30.712012+00:00`
- Price records: `672`
- Market context records: `7309`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14799`

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

- `risk_on_high->crypto_major_1h` score `1.3129` n `32` status `ready` deltaP `20.2332` edge `0.0579` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.3129` n `32` status `ready` deltaP `20.2332` edge `0.0579` maxDD `-0.957`
- `risk_on_high->equity_1h` score `0.2935` n `32` status `ready` deltaP `4.7904` edge `0.0434` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2935` n `32` status `ready` deltaP `4.7904` edge `0.0434` maxDD `-1.3497`
- `risk_on_high->commodity_1h` score `0.2277` n `32` status `ready` deltaP `4.1542` edge `0.0192` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2277` n `32` status `ready` deltaP `4.1542` edge `0.0192` maxDD `-0.2339`
- `risk_on_high->crypto_alt_1h` score `0.1383` n `32` status `ready` deltaP `0.1493` edge `0.0538` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1383` n `32` status `ready` deltaP `0.1493` edge `0.0538` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.2253` n `129` status `ready` deltaP `3.0393` edge `-0.0002` maxDD `-0.5821`
- `market_context_high->commodity_1h` score `-0.7281` n `129` status `ready` deltaP `-3.2586` edge `-0.0144` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.7304` n `129` status `ready` deltaP `-4.1243` edge `-0.0053` maxDD `-1.868`
- `market_context_high->fx_24h` score `-0.7699` n `111` status `ready` deltaP `3.0877` edge `0.0035` maxDD `-2.1564`
- `market_context_high->crypto_major_1h` score `-0.7761` n `129` status `ready` deltaP `3.397` edge `0.0189` maxDD `-7.6171`
- `market_context_high->commodity_4h` score `-0.8167` n `119` status `ready` deltaP `0.9056` edge `-0.0139` maxDD `-2.4139`
- `risk_on_high->index_1h` score `-0.9344` n `32` status `ready` deltaP `-13.9596` edge `0.0061` maxDD `-0.2932`
- `risk_on_and_context->index_1h` score `-0.9344` n `32` status `ready` deltaP `-13.9596` edge `0.0061` maxDD `-0.2932`
- `market_context_high->crypto_alt_1h` score `-1.0457` n `129` status `ready` deltaP `-1.0135` edge `0.0235` maxDD `-5.9775`
- `market_context_high->fx_4h` score `-1.0697` n `119` status `ready` deltaP `2.1514` edge `0.0085` maxDD `-1.4649`
- `risk_on_high->unknown_1h` score `-1.2204` n `32` status `ready` deltaP `-3.8619` edge `-0.0825` maxDD `-0.8568`
- `risk_on_and_context->unknown_1h` score `-1.2204` n `32` status `ready` deltaP `-3.8619` edge `-0.0825` maxDD `-0.8568`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
