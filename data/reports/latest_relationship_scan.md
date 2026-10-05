# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T08:52:29.340057+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8300`

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

- `market_context_high->unknown_1h` score `75.4192` n `122` status `ready` deltaP `-0.8098` edge `6.3318` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `59.3076` n `110` status `ready` deltaP `-0.1995` edge `4.9868` maxDD `-1.4538`
- `market_context_high->crypto_major_24h` score `10.8953` n `79` status `ready` deltaP `29.7094` edge `0.7235` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3191` n `65` status `ready` deltaP `32.5516` edge `0.5799` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `7.1614` n `79` status `ready` deltaP `25.1165` edge `0.4913` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.7984` n `65` status `ready` deltaP `19.7866` edge `0.4857` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.3893` n `110` status `ready` deltaP `14.7894` edge `0.2636` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.3433` n `65` status `ready` deltaP `23.6111` edge `0.1212` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.2313` n `65` status `ready` deltaP `11.7281` edge `0.2011` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.8999` n `65` status `ready` deltaP `31.9137` edge `0.0551` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.4926` n `65` status `ready` deltaP `20.1196` edge `0.1346` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.3765` n `65` status `ready` deltaP `9.4173` edge `0.1708` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0207` n `65` status `ready` deltaP `25.0184` edge `0.0166` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9114` n `65` status `ready` deltaP `17.8588` edge `0.0818` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.3397` n `110` status `ready` deltaP `24.3016` edge `0.0253` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.0306` n `65` status `ready` deltaP `2.9226` edge `0.1183` maxDD `-2.4854`
- `market_context_high->crypto_major_1h` score `0.995` n `122` status `ready` deltaP `11.2963` edge `0.0965` maxDD `-3.7778`
- `news_risk_high->commodity_24h` score `0.5589` n `65` status `ready` deltaP `24.9119` edge `0.1087` maxDD `-10.9169`
- `market_context_high->fx_1h` score `0.5416` n `122` status `ready` deltaP `13.878` edge `0.0053` maxDD `-0.271`
- `market_context_high->crypto_alt_4h` score `0.4282` n `110` status `ready` deltaP `1.6048` edge `0.2039` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
