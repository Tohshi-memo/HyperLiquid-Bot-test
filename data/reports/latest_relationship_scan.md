# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T18:40:19.146668+00:00`
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

- `news_risk_high->unknown_24h` score `30.482` n `61` status `ready` deltaP `4.0556` edge `2.6105` maxDD `-4.1232`
- `news_risk_high->crypto_alt_24h` score `16.702` n `61` status `ready` deltaP `30.0006` edge `1.5294` maxDD `-22.3391`
- `risk_on_high->crypto_alt_4h` score `13.4672` n `31` status `ready` deltaP `50.3049` edge `0.7869` maxDD `0.0`
- `risk_on_and_context->crypto_alt_4h` score `13.4672` n `31` status `ready` deltaP `50.3049` edge `0.7869` maxDD `0.0`
- `market_context_high->unknown_24h` score `11.0311` n `104` status `ready` deltaP `20.9535` edge `0.8528` maxDD `-3.1917`
- `risk_on_high->crypto_major_4h` score `8.3609` n `31` status `ready` deltaP `38.6458` edge `0.4667` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `8.3609` n `31` status `ready` deltaP `38.6458` edge `0.4667` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `5.7062` n `70` status `ready` deltaP `8.014` edge `0.4811` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6994` n `104` status `ready` deltaP `34.415` edge `0.2641` maxDD `-3.1535`
- `risk_on_high->metal_4h` score `2.9443` n `31` status `ready` deltaP `32.2433` edge `0.039` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `2.9443` n `31` status `ready` deltaP `32.2433` edge `0.039` maxDD `-0.0208`
- `risk_on_high->unknown_4h` score `2.6916` n `31` status `ready` deltaP `36.5854` edge `-0.0196` maxDD `0.0`
- `risk_on_and_context->unknown_4h` score `2.6916` n `31` status `ready` deltaP `36.5854` edge `-0.0196` maxDD `0.0`
- `news_risk_high->unknown_1h` score `2.582` n `70` status `ready` deltaP `1.6296` edge `0.24` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.5158` n `131` status `ready` deltaP `19.7915` edge `0.1209` maxDD `-0.7887`
- `news_risk_high->fx_4h` score `1.5228` n `70` status `ready` deltaP `34.3467` edge `0.0212` maxDD `-0.3953`
- `risk_on_high->metal_1h` score `1.3785` n `42` status `ready` deltaP `19.0334` edge `0.0094` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.3785` n `42` status `ready` deltaP `19.0334` edge `0.0094` maxDD `-0.0463`
- `market_context_high->crypto_major_4h` score `0.9067` n `131` status `ready` deltaP `21.6056` edge `0.2766` maxDD `-20.9394`
- `market_context_high->unknown_1h` score `0.663` n `143` status `ready` deltaP `8.0033` edge `0.05` maxDD `-1.5148`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
