# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T04:37:32.312075+00:00`
- Price records: `672`
- Market context records: `4793`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7548`

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

- `market_context_high->unknown_4h` score `7.7265` n `122` status `ready` deltaP `18.8725` edge `0.6391` maxDD `-4.6834`
- `market_context_high->unknown_1h` score `7.4653` n `122` status `ready` deltaP `12.4301` edge `0.581` maxDD `-1.674`
- `market_context_high->unknown_24h` score `2.1477` n `110` status `ready` deltaP `12.3611` edge `0.1889` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `0.1417` n `122` status `ready` deltaP `5.8309` edge `0.0317` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.055` n `122` status `ready` deltaP `11.8153` edge `0.0455` maxDD `-4.377`
- `market_context_high->equity_4h` score `-0.0942` n `122` status `ready` deltaP `8.3867` edge `0.1006` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.3528` n `122` status `ready` deltaP `7.1472` edge `0.014` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.4424` n `122` status `ready` deltaP `2.8214` edge `0.0021` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.7391` n `122` status `ready` deltaP `1.4185` edge `0.0057` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.91` n `122` status `ready` deltaP `-1.1829` edge `-0.003` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3788` n `122` status `ready` deltaP `-1.3473` edge `-0.0055` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.2143` n `110` status `ready` deltaP `19.334` edge `0.0981` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2509` n `122` status `ready` deltaP `-0.7976` edge `-0.0657` maxDD `-14.0715`
- `market_context_high->crypto_alt_1h` score `-3.164` n `122` status `ready` deltaP `0.8982` edge `-0.0457` maxDD `-15.2495`
- `market_context_high->fx_24h` score `-3.3105` n `110` status `ready` deltaP `-14.8517` edge `-0.0219` maxDD `-3.3968`
- `market_context_high->crypto_major_1h` score `-4.5043` n `122` status `ready` deltaP `0.6847` edge `-0.0709` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-4.7406` n `122` status `ready` deltaP `5.0505` edge `0.001` maxDD `-46.0617`
- `market_context_high->index_24h` score `-6.1493` n `110` status `ready` deltaP `-6.6067` edge `-0.1133` maxDD `-20.408`
- `market_context_high->crypto_major_4h` score `-8.0347` n `122` status `ready` deltaP `3.811` edge `-0.1324` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.3094` n `122` status `ready` deltaP `6.5349` edge `-0.2848` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
