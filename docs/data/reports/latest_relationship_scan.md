# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T02:37:36.586711+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7026`

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

- `news_risk_high->unknown_24h` score `1332.0256` n `132` status `ready` deltaP `1.9097` edge `110.9894` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.6484` n `132` status `ready` deltaP `31.2973` edge `1.533` maxDD `-1.0093`
- `news_risk_high->crypto_major_24h` score `9.5857` n `132` status `ready` deltaP `26.2784` edge `0.939` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `9.2399` n `132` status `ready` deltaP `30.7923` edge `0.7996` maxDD `-9.4579`
- `news_risk_high->index_24h` score `4.2345` n `132` status `ready` deltaP `37.1527` edge `0.153` maxDD `-0.4916`
- `news_risk_high->equity_4h` score `2.9072` n `135` status `ready` deltaP `29.3236` edge `0.2069` maxDD `-9.143`
- `news_risk_high->metal_24h` score `2.5538` n `132` status `ready` deltaP `28.7564` edge `0.2631` maxDD `-2.192`
- `news_risk_high->crypto_alt_4h` score `2.087` n `135` status `ready` deltaP `12.0269` edge `0.3597` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.0646` n `135` status `ready` deltaP `9.1018` edge `0.1191` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.9044` n `135` status `ready` deltaP `9.4012` edge `0.075` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.4957` n `135` status `ready` deltaP `8.8179` edge `0.0113` maxDD `-0.302`
- `news_risk_high->index_4h` score `-0.0894` n `135` status `ready` deltaP `7.4063` edge `0.0285` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4814` n `135` status `ready` deltaP `1.1577` edge `0.0151` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5216` n `135` status `ready` deltaP `2.4894` edge `0.0682` maxDD `-7.2607`
- `news_risk_high->metal_4h` score `-1.235` n `135` status `ready` deltaP `-7.2369` edge `0.0307` maxDD `-2.9297`
- `news_risk_high->crypto_major_4h` score `-1.4266` n `135` status `ready` deltaP `-3.226` edge `0.1101` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.4859` n `135` status `ready` deltaP `6.0084` edge `-0.0092` maxDD `-3.0414`
- `news_risk_high->commodity_1h` score `-1.8086` n `135` status `ready` deltaP `-8.3688` edge `-0.0086` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.8912` n `135` status `ready` deltaP `-9.8037` edge `-0.0042` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2284` n `135` status `ready` deltaP `-8.54` edge `0.0131` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
