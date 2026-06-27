# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T14:07:25.843207+00:00`
- Price records: `672`
- Market context records: `4941`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9408`

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

- `market_context_high->unknown_1h` score `19.9917` n `94` status `ready` deltaP `11.4346` edge `1.6315` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.169` n `94` status `ready` deltaP `28.2596` edge `0.8771` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.2945` n `94` status `ready` deltaP `21.1339` edge `0.5894` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.0379` n `94` status `ready` deltaP `21.7372` edge `0.5768` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.8764` n `86` status `ready` deltaP `26.5141` edge `0.3472` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7906` n `94` status `ready` deltaP `14.8903` edge `0.1881` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.6877` n `94` status `ready` deltaP `13.0903` edge `0.1196` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.9737` n `94` status `ready` deltaP `12.4676` edge `0.0442` maxDD `-0.6938`
- `market_context_high->crypto_major_1h` score `0.7143` n `94` status `ready` deltaP `7.2334` edge `0.1472` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.5218` n `94` status `ready` deltaP `8.1953` edge `0.1145` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.5203` n `94` status `ready` deltaP `7.1474` edge `0.0764` maxDD `-2.5875`
- `market_context_high->metal_1h` score `0.0486` n `94` status `ready` deltaP `3.8763` edge `0.0362` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.3697` n `94` status `ready` deltaP `1.6308` edge `0.0077` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4445` n `94` status `ready` deltaP `0.9301` edge `0.0123` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.9215` n `94` status `ready` deltaP `6.8662` edge `-0.0039` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-1.1381` n `94` status `ready` deltaP `-6.6846` edge `-0.0043` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.5746` n `94` status `ready` deltaP `-9.6382` edge `-0.0057` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-1.6454` n `86` status `ready` deltaP `-3.0725` edge `-0.0156` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-4.6082` n `86` status `ready` deltaP `16.9291` edge `0.014` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-7.0986` n `86` status `ready` deltaP `-9.2498` edge `0.0156` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
