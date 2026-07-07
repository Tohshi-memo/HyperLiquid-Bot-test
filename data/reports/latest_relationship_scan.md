# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T19:37:31.899517+00:00`
- Price records: `672`
- Market context records: `6011`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11122`

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

- `news_risk_high->fx_24h` score `7.629` n `30` status `ready` deltaP `69.0972` edge `0.1751` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1761` n `30` status `ready` deltaP `43.2012` edge `0.0646` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.6626` n `30` status `ready` deltaP `30.0695` edge `0.1253` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2442` n `30` status `ready` deltaP `26.9261` edge `0.0214` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.0818` n `216` status `ready` deltaP `7.1082` edge `0.1522` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8528` n `30` status `ready` deltaP `10.6387` edge `0.0851` maxDD `-2.0691`
- `market_context_high->equity_24h` score `0.714` n `190` status `ready` deltaP `25.7456` edge `0.433` maxDD `-31.6107`
- `news_risk_high->crypto_alt_1h` score `0.2208` n `30` status `ready` deltaP `5.4691` edge `0.038` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1312` n `30` status `ready` deltaP `9.2361` edge `0.0424` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.4016` n `30` status `ready` deltaP `1.5369` edge `-0.0251` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4204` n `216` status `ready` deltaP `3.2962` edge `0.004` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.565` n `216` status `ready` deltaP `1.9212` edge `0.0276` maxDD `-4.3608`
- `market_context_high->commodity_1h` score `-0.6524` n `216` status `ready` deltaP `-1.2253` edge `0.0002` maxDD `-0.7117`
- `market_context_high->fx_1h` score `-0.7119` n `216` status `ready` deltaP `-1.0368` edge `-0.0016` maxDD `-0.7314`
- `news_risk_high->index_1h` score `-1.0345` n `30` status `ready` deltaP `-9.4012` edge `-0.0185` maxDD `-1.1161`
- `market_context_high->crypto_alt_1h` score `-1.125` n `216` status `ready` deltaP `2.0431` edge `0.0174` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-1.1276` n `216` status `ready` deltaP `2.398` edge `0.0162` maxDD `-9.807`
- `market_context_high->index_4h` score `-1.1375` n `216` status `ready` deltaP `0.638` edge `0.0153` maxDD `-2.8979`
- `market_context_high->commodity_4h` score `-1.1912` n `216` status `ready` deltaP `-2.36` edge `-0.0074` maxDD `-3.0339`
- `market_context_high->index_1h` score `-1.2611` n `216` status `ready` deltaP `-2.6419` edge `0.0026` maxDD `-1.2065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
