# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T09:37:27.606515+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `47.0458` n `127` status `ready` deltaP `-18.7803` edge `4.2911` maxDD `-9.6329`
- `market_context_high->commodity_24h` score `2.0246` n `127` status `ready` deltaP `12.9915` edge `0.1708` maxDD `-3.0953`
- `risk_on_high->commodity_1h` score `1.2408` n `32` status `ready` deltaP `12.762` edge `0.0416` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2408` n `32` status `ready` deltaP `12.762` edge `0.0416` maxDD `-0.1957`
- `market_context_high->commodity_4h` score `0.8835` n `178` status `ready` deltaP `11.4877` edge `0.0685` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7815` n `181` status `ready` deltaP `10.3103` edge `0.0301` maxDD `-0.6965`
- `market_context_high->fx_24h` score `0.479` n `127` status `ready` deltaP `16.5408` edge `0.0319` maxDD `-1.4613`
- `risk_on_high->index_1h` score `0.2267` n `32` status `ready` deltaP `8.9072` edge `0.0072` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2267` n `32` status `ready` deltaP `8.9072` edge `0.0072` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.149` n `32` status `ready` deltaP `4.9027` edge `0.0025` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.149` n `32` status `ready` deltaP `4.9027` edge `0.0025` maxDD `-0.1547`
- `market_context_high->fx_1h` score `-0.0933` n `181` status `ready` deltaP `4.4538` edge `0.0007` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.1455` n `178` status `ready` deltaP `5.4913` edge `0.0052` maxDD `-0.504`
- `risk_on_high->equity_1h` score `-0.7957` n `32` status `ready` deltaP `-4.6594` edge `-0.0166` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `-0.7957` n `32` status `ready` deltaP `-4.6594` edge `-0.0166` maxDD `-1.6811`
- `market_context_high->index_1h` score `-0.9114` n `181` status `ready` deltaP `-8.2889` edge `-0.0039` maxDD `-0.948`
- `market_context_high->metal_1h` score `-1.1458` n `181` status `ready` deltaP `-8.1748` edge `-0.0163` maxDD `-2.0884`
- `risk_on_high->crypto_major_1h` score `-1.4701` n `32` status `ready` deltaP `0.7298` edge `-0.0692` maxDD `-2.6536`
- `risk_on_and_context->crypto_major_1h` score `-1.4701` n `32` status `ready` deltaP `0.7298` edge `-0.0692` maxDD `-2.6536`
- `market_context_high->equity_1h` score `-1.5057` n `181` status `ready` deltaP `-7.5082` edge `-0.0153` maxDD `-6.8818`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
