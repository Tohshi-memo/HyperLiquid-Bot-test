# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T19:07:34.307375+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10053`

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

- `market_context_high->unknown_1h` score `87.1339` n `47` status `ready` deltaP `10.116` edge `7.2008` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `44.5721` n `47` status `ready` deltaP `30.4226` edge `3.5508` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.74` n `47` status `ready` deltaP `24.782` edge `2.3511` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.7573` n `47` status `ready` deltaP `30.5962` edge `1.8947` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.831` n `47` status `ready` deltaP `34.7628` edge `0.4338` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.8954` n `47` status `ready` deltaP `33.3223` edge `0.1263` maxDD `-0.2401`
- `news_risk_high->crypto_major_24h` score `3.4951` n `86` status `ready` deltaP `-1.5665` edge `1.3628` maxDD `-63.6743`
- `news_risk_high->crypto_alt_1h` score `3.4243` n `111` status `ready` deltaP `16.6937` edge `0.2231` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.9765` n `47` status `ready` deltaP `34.0263` edge `0.0366` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.8423` n `111` status `ready` deltaP `18.6398` edge `0.1561` maxDD `-1.8141`
- `news_risk_high->crypto_alt_4h` score `2.5637` n `107` status `ready` deltaP `9.085` edge `0.3982` maxDD `-15.9436`
- `news_risk_high->crypto_major_4h` score `2.5209` n `107` status `ready` deltaP `16.6543` edge `0.3122` maxDD `-13.719`
- `market_context_high->equity_4h` score `2.4407` n `47` status `ready` deltaP `17.1445` edge `0.1309` maxDD `-1.3444`
- `news_risk_high->fx_4h` score `1.789` n `107` status `ready` deltaP `25.5414` edge `0.0424` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.6335` n `86` status `ready` deltaP `19.1215` edge `0.0893` maxDD `-1.7857`
- `news_risk_high->crypto_alt_24h` score `1.4934` n `86` status `ready` deltaP `-3.3229` edge `0.9149` maxDD `-49.7699`
- `news_risk_high->metal_1h` score `1.4731` n `111` status `ready` deltaP `18.7598` edge `0.0262` maxDD `-0.6142`
- `market_context_high->index_1h` score `1.011` n `47` status `ready` deltaP `15.2089` edge `0.0107` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.9755` n `86` status `ready` deltaP `23.9705` edge `0.1101` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `0.9323` n `86` status `ready` deltaP `25.222` edge `0.1145` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
