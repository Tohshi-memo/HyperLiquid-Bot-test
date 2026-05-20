# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T04:37:23.596656+00:00`
- Price records: `672`
- Market context records: `1287`
- Flow alert records: `5616`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `17.5777` n `128` status `ready` deltaP `41.5798` edge `1.3008` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.6916` n `128` status `ready` deltaP `8.5069` edge `1.0843` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.1437` n `128` status `ready` deltaP `26.4756` edge `0.7871` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.612` n `128` status `ready` deltaP `29.3403` edge `0.3807` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9187` n `128` status `ready` deltaP `25.3472` edge `0.5661` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.4018` n `145` status `ready` deltaP `12.172` edge `0.1895` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3802` n `128` status `ready` deltaP `1.5625` edge `0.4609` maxDD `-10.1706`
- `market_context_high->unknown_4h` score `1.9268` n `145` status `ready` deltaP `2.8343` edge `0.3499` maxDD `-10.3249`
- `market_context_high->commodity_24h` score `1.351` n `128` status `ready` deltaP `-14.0625` edge `0.3545` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.3736` n `128` status `ready` deltaP `6.1632` edge `0.0365` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.2785` n `154` status `ready` deltaP `4.3082` edge `0.0372` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.2352` n `145` status `ready` deltaP `6.7924` edge `0.089` maxDD `-3.3305`
- `market_context_high->metal_4h` score `0.1279` n `145` status `ready` deltaP `13.463` edge `0.064` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.1049` n `154` status `ready` deltaP `6.2039` edge `0.0175` maxDD `-1.6329`
- `market_context_high->metal_1h` score `0.0131` n `154` status `ready` deltaP `9.5945` edge `0.0061` maxDD `-2.8509`
- `market_context_high->crypto_alt_1h` score `-0.3851` n `154` status `ready` deltaP `0.5522` edge `0.034` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.5327` n `154` status `ready` deltaP `0.7019` edge `-0.0035` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.8068` n `154` status `ready` deltaP `-0.5502` edge `0.0023` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-0.8944` n `145` status `ready` deltaP `9.0276` edge `0.1571` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.9559` n `145` status `ready` deltaP `4.446` edge `0.1187` maxDD `-13.3376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
