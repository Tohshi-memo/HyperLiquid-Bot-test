# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T09:22:27.983577+00:00`
- Price records: `672`
- Market context records: `5865`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10106`

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

- `news_risk_high->fx_4h` score `3.7035` n `30` status `ready` deltaP `38.628` edge `0.0557` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `1.9639` n `30` status `ready` deltaP `23.7824` edge `0.019` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9181` n `30` status `ready` deltaP `11.986` edge `0.0845` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.5862` n `243` status `ready` deltaP `6.484` edge `0.1514` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.2995` n `30` status `ready` deltaP `5.7685` edge `0.0461` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3691` n `243` status `ready` deltaP `0.2433` edge `-0.0004` maxDD `-0.5499`
- `market_context_high->metal_1h` score `-0.4138` n `243` status `ready` deltaP `4.021` edge `0.0058` maxDD `-2.0339`
- `market_context_high->equity_1h` score `-0.4219` n `243` status `ready` deltaP `4.6549` edge `0.0345` maxDD `-5.0555`
- `news_risk_high->metal_1h` score `-0.4391` n `30` status `ready` deltaP `1.3872` edge `-0.0289` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5812` n `243` status `ready` deltaP `-1.7761` edge `-0.0031` maxDD `-2.0987`
- `market_context_high->index_1h` score `-0.6085` n `243` status `ready` deltaP `0.4294` edge `0.0039` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.7667` n `243` status `ready` deltaP `3.7967` edge `0.0429` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.9206` n `243` status `ready` deltaP `2.5997` edge `0.0394` maxDD `-6.6758`
- `news_risk_high->index_1h` score `-1.2245` n `30` status `ready` deltaP `-12.2455` edge `-0.0239` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.2483` n `243` status `ready` deltaP `-0.4962` edge `0.012` maxDD `-3.165`
- `market_context_high->metal_4h` score `-1.7273` n `243` status `ready` deltaP `-3.2551` edge `-0.0332` maxDD `-5.9901`
- `news_risk_high->commodity_4h` score `-1.8079` n `30` status `ready` deltaP `-13.7296` edge `-0.0527` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8296` n `228` status `ready` deltaP `4.8794` edge `0.0147` maxDD `-5.5435`
- `market_context_high->equity_24h` score `-1.8633` n `228` status `ready` deltaP `14.1174` edge `0.2585` maxDD `-31.6316`
- `market_context_high->fx_4h` score `-1.8674` n `243` status `ready` deltaP `-6.1045` edge `-0.0038` maxDD `-2.2593`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
