# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T00:37:31.029828+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->fx_24h` score `1.1181` n `145` status `ready` deltaP `20.4064` edge `0.0379` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.821` n `171` status `ready` deltaP `11.1565` edge `0.0655` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.5335` n `180` status `ready` deltaP `7.688` edge `0.0275` maxDD `-0.7439`
- `market_context_high->fx_1h` score `-0.0504` n `180` status `ready` deltaP `5.7452` edge `0.0004` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.0851` n `171` status `ready` deltaP `6.8829` edge `0.007` maxDD `-0.4647`
- `market_context_high->metal_1h` score `-1.2984` n `180` status `ready` deltaP `-5.2195` edge `-0.0098` maxDD `-2.0884`
- `market_context_high->index_1h` score `-1.3434` n `180` status `ready` deltaP `-7.0758` edge `-0.006` maxDD `-1.0359`
- `market_context_high->equity_1h` score `-1.4801` n `180` status `ready` deltaP `-6.0545` edge `-0.0217` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-1.527` n `145` status `ready` deltaP `2.5482` edge `-0.0118` maxDD `-2.9283`
- `market_context_high->index_24h` score `-1.6212` n `145` status `ready` deltaP `-6.526` edge `0.0274` maxDD `-6.6723`
- `market_context_high->index_4h` score `-1.8924` n `171` status `ready` deltaP `-7.3572` edge `-0.0182` maxDD `-1.5693`
- `market_context_high->crypto_alt_1h` score `-2.8625` n `180` status `ready` deltaP `-11.1377` edge `-0.0457` maxDD `-6.4874`
- `market_context_high->metal_4h` score `-3.2156` n `171` status `ready` deltaP `-7.7816` edge `-0.0397` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.8613` n `180` status `ready` deltaP `-11.0479` edge `-0.0577` maxDD `-11.9002`
- `market_context_high->commodity_24h` score `-4.2061` n `145` status `ready` deltaP `4.1618` edge `0.0067` maxDD `-34.2283`
- `market_context_high->equity_4h` score `-4.4913` n `171` status `ready` deltaP `-16.7389` edge `-0.1533` maxDD `-15.8728`
- `market_context_high->crypto_major_24h` score `-5.5322` n `145` status `ready` deltaP `-9.1113` edge `-0.1539` maxDD `-29.2361`
- `market_context_high->equity_24h` score `-6.9886` n `145` status `ready` deltaP `-6.3706` edge `-0.1255` maxDD `-45.574`
- `market_context_high->crypto_alt_4h` score `-7.1654` n `171` status `ready` deltaP `-15.4667` edge `-0.1592` maxDD `-20.1177`
- `market_context_high->crypto_alt_24h` score `-8.6217` n `145` status `ready` deltaP `-12.8226` edge `-0.2214` maxDD `-24.2609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
