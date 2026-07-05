# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T07:37:27.711553+00:00`
- Price records: `672`
- Market context records: `5749`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8664`

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

- `market_context_high->equity_24h` score `0.8537` n `218` status `ready` deltaP `14.6614` edge `0.5196` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.175` n `285` status `ready` deltaP `7.6728` edge `0.1273` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.1964` n `287` status `ready` deltaP `3.2585` edge `0.0012` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4671` n `287` status `ready` deltaP `1.2659` edge `-0.0008` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.6449` n `287` status `ready` deltaP `0.0683` edge `0.0037` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6543` n `287` status `ready` deltaP `2.8454` edge `0.0272` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7761` n `287` status `ready` deltaP `-1.9628` edge `-0.0057` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.8104` n `287` status `ready` deltaP `3.1114` edge `0.0352` maxDD `-5.5448`
- `market_context_high->crypto_alt_1h` score `-0.8761` n `287` status `ready` deltaP `1.9628` edge `0.0343` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-0.9897` n `218` status `ready` deltaP `13.118` edge `0.044` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1536` n `285` status `ready` deltaP `1.4752` edge `0.011` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2207` n `285` status `ready` deltaP `3.3189` edge `0.0059` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6044` n `285` status `ready` deltaP `-7.0839` edge `-0.0491` maxDD `-11.6719`
- `market_context_high->crypto_major_4h` score `-2.6611` n `285` status `ready` deltaP `8.2168` edge `0.154` maxDD `-25.1094`
- `market_context_high->index_24h` score `-3.0456` n `218` status `ready` deltaP `-0.5097` edge `0.0274` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7041` n `285` status `ready` deltaP `-2.0587` edge `-0.0274` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-3.7245` n `218` status `ready` deltaP `9.453` edge `0.0723` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `-3.803` n `285` status `ready` deltaP `6.5543` edge `0.1084` maxDD `-26.1874`
- `market_context_high->metal_24h` score `-7.8677` n `218` status `ready` deltaP `-10.38` edge `-0.251` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.9277` n `218` status `ready` deltaP `-13.873` edge `-0.0875` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
