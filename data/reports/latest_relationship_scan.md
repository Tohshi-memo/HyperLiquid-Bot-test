# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T18:37:25.031846+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11330`

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

- `news_risk_high->unknown_24h` score `30.4832` n `61` status `ready` deltaP `4.0556` edge `2.6106` maxDD `-4.1232`
- `news_risk_high->crypto_alt_24h` score `16.7032` n `61` status `ready` deltaP `30.0006` edge `1.5295` maxDD `-22.3391`
- `risk_on_high->crypto_alt_4h` score `13.454` n `31` status `ready` deltaP `50.3049` edge `0.7858` maxDD `0.0`
- `risk_on_and_context->crypto_alt_4h` score `13.454` n `31` status `ready` deltaP `50.3049` edge `0.7858` maxDD `0.0`
- `market_context_high->unknown_24h` score `11.0323` n `104` status `ready` deltaP `20.9535` edge `0.8529` maxDD `-3.1917`
- `risk_on_high->crypto_major_4h` score `8.3465` n `31` status `ready` deltaP `38.6458` edge `0.4655` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `8.3465` n `31` status `ready` deltaP `38.6458` edge `0.4655` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `5.7208` n `70` status `ready` deltaP `8.1664` edge `0.4813` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6994` n `104` status `ready` deltaP `34.415` edge `0.2641` maxDD `-3.1535`
- `risk_on_high->metal_4h` score `2.9455` n `31` status `ready` deltaP `32.2433` edge `0.0391` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `2.9455` n `31` status `ready` deltaP `32.2433` edge `0.0391` maxDD `-0.0208`
- `news_risk_high->unknown_1h` score `2.5952` n `70` status `ready` deltaP `1.7793` edge `0.2401` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.4585` n `131` status `ready` deltaP `19.1805` edge `0.1202` maxDD `-0.7887`
- `risk_on_high->unknown_4h` score `2.3357` n `31` status `ready` deltaP `33.512` edge `-0.0232` maxDD `-0.1122`
- `risk_on_and_context->unknown_4h` score `2.3357` n `31` status `ready` deltaP `33.512` edge `-0.0232` maxDD `-0.1122`
- `news_risk_high->fx_4h` score `1.5228` n `70` status `ready` deltaP `34.3467` edge `0.0212` maxDD `-0.3953`
- `risk_on_high->metal_1h` score `1.3785` n `42` status `ready` deltaP `19.0334` edge `0.0094` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.3785` n `42` status `ready` deltaP `19.0334` edge `0.0094` maxDD `-0.0463`
- `market_context_high->crypto_major_4h` score `0.9043` n `131` status `ready` deltaP `21.6056` edge `0.2764` maxDD `-20.9394`
- `risk_on_high->equity_4h` score `0.6259` n `31` status `ready` deltaP `3.6438` edge `0.0528` maxDD `-0.3281`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
