# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T01:37:29.078570+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4662`

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

- `market_context_high->unknown_1h` score `360.8357` n `52` status `ready` deltaP `11.573` edge `29.9974` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `321.7042` n `50` status `ready` deltaP `12.9573` edge `26.7223` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.2528` n `50` status `ready` deltaP `29.286` edge `1.0795` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.1214` n `50` status `ready` deltaP `35.2062` edge `0.8337` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.5142` n `62` status `ready` deltaP `28.2244` edge `0.7365` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.4313` n `68` status `ready` deltaP `37.7242` edge `0.6381` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.1431` n `68` status `ready` deltaP `25.0897` edge `0.5624` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.0314` n `50` status `ready` deltaP `16.0183` edge `0.5495` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.4264` n `50` status `ready` deltaP `14.2073` edge `0.4864` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.4089` n `62` status `ready` deltaP `31.5564` edge `0.1729` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8303` n `68` status `ready` deltaP `26.9637` edge `0.2007` maxDD `-2.9013`
- `news_risk_high->index_4h` score `2.9851` n `68` status `ready` deltaP `32.6937` edge `0.057` maxDD `-0.4296`
- `market_context_high->fx_4h` score `2.9456` n `50` status `ready` deltaP `32.9939` edge `0.039` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.9067` n `68` status `ready` deltaP `12.9095` edge `0.1917` maxDD `-1.5096`
- `market_context_high->crypto_alt_1h` score `2.6314` n `52` status `ready` deltaP `10.4675` edge `0.2158` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.4998` n `52` status `ready` deltaP `9.7421` edge `0.1884` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3613` n `68` status `ready` deltaP `19.9875` edge `0.1051` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.0078` n `68` status `ready` deltaP `24.7975` edge `0.017` maxDD `-0.1997`
- `market_context_high->equity_24h` score `1.4064` n `50` status `ready` deltaP `7.5147` edge `0.3164` maxDD `-11.8957`
- `news_risk_high->crypto_alt_1h` score `1.4023` n `68` status `ready` deltaP `4.3589` edge `0.1397` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
