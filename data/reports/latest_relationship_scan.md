# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T02:07:27.739189+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5368`

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

- `market_context_high->unknown_1h` score `117.534` n `95` status `ready` deltaP `-0.0803` edge `9.8365` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `71.8288` n `95` status `ready` deltaP `2.4743` edge `6.0004` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.7174` n `52` status `ready` deltaP `30.5155` edge `0.7033` maxDD `-0.423`
- `market_context_high->crypto_alt_24h` score `9.9377` n `52` status `ready` deltaP `25.0802` edge `0.7229` maxDD `-2.9571`
- `news_risk_high->crypto_major_4h` score `9.4768` n `65` status `ready` deltaP `33.0089` edge `0.59` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.3974` n `65` status `ready` deltaP `20.8537` edge `0.5285` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.6923` n `65` status `ready` deltaP `16.4156` edge `0.2916` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.3696` n `95` status `ready` deltaP `18.5959` edge `0.3105` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.4594` n `65` status `ready` deltaP `24.1319` edge `0.1274` maxDD `0.0`
- `news_risk_high->index_4h` score `2.9157` n `65` status `ready` deltaP `32.0662` edge `0.0554` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.8928` n `65` status `ready` deltaP `21.4915` edge `0.1588` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.5804` n `65` status `ready` deltaP `10.6149` edge `0.1798` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.1886` n `95` status `ready` deltaP `14.9874` edge `0.1275` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.1003` n `65` status `ready` deltaP `19.2308` edge `0.0884` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.071` n `65` status `ready` deltaP `25.6172` edge `0.0168` maxDD `-0.1997`
- `market_context_high->fx_24h` score `2.0361` n `52` status `ready` deltaP `24.359` edge `0.0994` maxDD `-1.703`
- `market_context_high->equity_24h` score `1.6537` n `52` status `ready` deltaP `3.3386` edge `0.1358` maxDD `-0.6196`
- `market_context_high->fx_4h` score `1.4417` n `95` status `ready` deltaP `25.1717` edge `0.028` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.3808` n `65` status `ready` deltaP `4.4196` edge `0.1375` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.2772` n `95` status `ready` deltaP `4.0116` edge `0.2586` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
