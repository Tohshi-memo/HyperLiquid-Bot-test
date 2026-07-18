# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T12:22:24.716070+00:00`
- Price records: `672`
- Market context records: `7139`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11692`

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

- `market_context_high->fx_4h` score `0.6981` n `141` status `ready` deltaP `16.991` edge `0.0149` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1496` n `153` status `ready` deltaP `4.493` edge `0.0027` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4677` n `153` status `ready` deltaP `-2.2622` edge `0.0403` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.607` n `153` status `ready` deltaP `-0.0274` edge `0.0254` maxDD `-5.91`
- `market_context_high->crypto_major_1h` score `-0.6641` n `153` status `ready` deltaP `3.2406` edge `0.0343` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.714` n `153` status `ready` deltaP `-1.9588` edge `-0.0164` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7193` n `153` status `ready` deltaP `1.6995` edge `-0.0048` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.3779` n `153` status `ready` deltaP `-5.0409` edge `-0.0051` maxDD `-2.0897`
- `market_context_high->commodity_4h` score `-2.1325` n `141` status `ready` deltaP `-5.2456` edge `-0.0392` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-2.2454` n `141` status `ready` deltaP `-5.3862` edge `0.0189` maxDD `-5.2753`
- `market_context_high->metal_4h` score `-2.8183` n `141` status `ready` deltaP `-8.1106` edge `-0.0124` maxDD `-5.2551`
- `market_context_high->crypto_major_4h` score `-3.4083` n `141` status `ready` deltaP `0.2152` edge `-0.0069` maxDD `-24.8534`
- `market_context_high->equity_1h` score `-3.5007` n `153` status `ready` deltaP `-0.1262` edge `-0.0448` maxDD `-15.02`
- `market_context_high->index_4h` score `-3.953` n `141` status `ready` deltaP `-1.5017` edge `-0.0495` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.4928` n `133` status `ready` deltaP `-13.4581` edge `-0.1538` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9863` n `133` status `ready` deltaP `-16.0518` edge `-0.0258` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-5.5333` n `141` status `ready` deltaP `-3.6758` edge `-0.0434` maxDD `-23.4564`
- `market_context_high->unknown_24h` score `-10.1239` n `133` status `ready` deltaP `-32.8765` edge `-0.1098` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-14.0063` n `141` status `ready` deltaP `-2.1514` edge `-0.2527` maxDD `-64.6785`
- `market_context_high->metal_24h` score `-14.4574` n `133` status `ready` deltaP `-29.6927` edge `-0.1887` maxDD `-40.7836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
