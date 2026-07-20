# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T01:37:27.790697+00:00`
- Price records: `672`
- Market context records: `7308`
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

- `risk_on_high->crypto_major_1h` score `1.3293` n `32` status `ready` deltaP `20.3825` edge `0.059` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.3293` n `32` status `ready` deltaP `20.3825` edge `0.059` maxDD `-0.957`
- `risk_on_high->equity_1h` score `0.3005` n `32` status `ready` deltaP `4.7904` edge `0.0443` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.3005` n `32` status `ready` deltaP `4.7904` edge `0.0443` maxDD `-1.3497`
- `risk_on_high->commodity_1h` score `0.2265` n `32` status `ready` deltaP `4.1542` edge `0.0191` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2265` n `32` status `ready` deltaP `4.1542` edge `0.0191` maxDD `-0.2339`
- `risk_on_high->crypto_alt_1h` score `0.1539` n `32` status `ready` deltaP `0.2985` edge `0.0548` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1539` n `32` status `ready` deltaP `0.2985` edge `0.0548` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.2338` n `129` status `ready` deltaP `2.8896` edge `-0.0003` maxDD `-0.5821`
- `market_context_high->index_1h` score `-0.7281` n `129` status `ready` deltaP `-4.1243` edge `-0.005` maxDD `-1.868`
- `market_context_high->commodity_1h` score `-0.7289` n `129` status `ready` deltaP `-3.2586` edge `-0.0145` maxDD `-1.5775`
- `market_context_high->crypto_major_1h` score `-0.7598` n `129` status `ready` deltaP `3.5463` edge `0.02` maxDD `-7.6171`
- `market_context_high->fx_24h` score `-0.7739` n `111` status `ready` deltaP `2.9963` edge `0.0036` maxDD `-2.1564`
- `market_context_high->commodity_4h` score `-0.7973` n `118` status `ready` deltaP `1.1575` edge `-0.0131` maxDD `-2.4139`
- `risk_on_high->index_1h` score `-0.9321` n `32` status `ready` deltaP `-13.9596` edge `0.0064` maxDD `-0.2932`
- `risk_on_and_context->index_1h` score `-0.9321` n `32` status `ready` deltaP `-13.9596` edge `0.0064` maxDD `-0.2932`
- `market_context_high->crypto_alt_1h` score `-1.0218` n `129` status `ready` deltaP `-0.8643` edge `0.0245` maxDD `-5.9775`
- `market_context_high->fx_4h` score `-1.0602` n `118` status `ready` deltaP `2.3176` edge `0.0086` maxDD `-1.4649`
- `risk_on_high->unknown_1h` score `-1.232` n `32` status `ready` deltaP `-4.0112` edge `-0.083` maxDD `-0.8568`
- `risk_on_and_context->unknown_1h` score `-1.232` n `32` status `ready` deltaP `-4.0112` edge `-0.083` maxDD `-0.8568`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
