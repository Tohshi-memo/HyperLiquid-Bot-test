# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T12:52:28.245331+00:00`
- Price records: `672`
- Market context records: `2970`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `16.6784` n `112` status `ready` deltaP `9.7718` edge `1.7164` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `9.4168` n `112` status `ready` deltaP `16.245` edge `0.7229` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `9.2072` n `112` status `ready` deltaP `33.879` edge `0.5905` maxDD `-1.5939`
- `market_context_high->equity_24h` score `7.2829` n `112` status `ready` deltaP `16.6171` edge `0.6965` maxDD `-12.6963`
- `market_context_high->index_24h` score `3.745` n `112` status `ready` deltaP `15.7738` edge `0.305` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.1023` n `113` status `ready` deltaP `16.1046` edge `0.1901` maxDD `-0.7819`
- `market_context_high->index_4h` score `1.7306` n `113` status `ready` deltaP `18.1119` edge `0.1023` maxDD `-1.9733`
- `market_context_high->crypto_alt_4h` score `1.4145` n `113` status `ready` deltaP `23.2908` edge `0.4822` maxDD `-30.8239`
- `market_context_high->equity_1h` score `0.9364` n `113` status `ready` deltaP `6.8571` edge `0.0658` maxDD `-1.012`
- `market_context_high->crypto_alt_1h` score `0.3264` n `113` status `ready` deltaP `10.6128` edge `0.1346` maxDD `-10.747`
- `market_context_high->index_1h` score `0.323` n `113` status `ready` deltaP `6.9101` edge `0.0228` maxDD `-1.023`
- `market_context_high->commodity_4h` score `0.1942` n `113` status `ready` deltaP `9.3595` edge `0.067` maxDD `-5.6933`
- `market_context_high->crypto_major_1h` score `0.0874` n `113` status `ready` deltaP `10.067` edge `0.0977` maxDD `-9.622`
- `market_context_high->unknown_4h` score `-0.052` n `113` status `ready` deltaP `2.6103` edge `0.0836` maxDD `-3.7602`
- `market_context_high->fx_1h` score `-0.3748` n `113` status `ready` deltaP `-0.6319` edge `0.0037` maxDD `-0.1244`
- `market_context_high->commodity_1h` score `-0.5566` n `113` status `ready` deltaP `-1.0678` edge `-0.0017` maxDD `-3.3365`
- `market_context_high->metal_1h` score `-0.8278` n `113` status `ready` deltaP `-2.1727` edge `-0.0029` maxDD `-3.4325`
- `market_context_high->unknown_1h` score `-1.0861` n `113` status `ready` deltaP `1.7368` edge `-0.029` maxDD `-3.1801`
- `market_context_high->crypto_major_4h` score `-1.1702` n `113` status `ready` deltaP `10.5035` edge `0.2925` maxDD `-33.6701`
- `market_context_high->fx_4h` score `-1.2902` n `113` status `ready` deltaP `-4.9266` edge `0.0032` maxDD `-0.5631`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
