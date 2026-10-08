# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T08:22:32.759692+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `39.4363` n `90` status `ready` deltaP `-2.7981` edge `3.3589` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `11.1392` n `62` status `ready` deltaP `39.344` edge `0.6863` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `7.4153` n `62` status `ready` deltaP `19.1097` edge `0.5005` maxDD `-0.1298`
- `news_risk_high->crypto_alt_4h` score `7.1798` n `62` status `ready` deltaP `23.2396` edge `0.5778` maxDD `-6.4195`
- `market_context_high->crypto_major_24h` score `5.2582` n `90` status `ready` deltaP `13.5924` edge `0.8809` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.1931` n `62` status `ready` deltaP `37.8238` edge `0.1806` maxDD `0.0`
- `news_risk_high->index_4h` score `3.1461` n `62` status `ready` deltaP `34.1365` edge `0.0608` maxDD `-0.4296`
- `market_context_high->equity_24h` score `2.9107` n `90` status `ready` deltaP `16.6724` edge `0.1743` maxDD `-1.0977`
- `news_risk_high->equity_4h` score `2.6385` n `62` status `ready` deltaP `19.3008` edge `0.151` maxDD `-2.7837`
- `market_context_high->crypto_major_4h` score `2.6344` n `90` status `ready` deltaP `17.4085` edge `0.1999` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.587` n `62` status `ready` deltaP `10.7736` edge `0.1793` maxDD `-1.5096`
- `news_risk_high->unknown_4h` score `2.2159` n `62` status `ready` deltaP `-5.7731` edge `0.3477` maxDD `-5.6309`
- `news_risk_high->index_1h` score `2.117` n `62` status `ready` deltaP `26.2218` edge `0.0166` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4419` n `62` status `ready` deltaP `21.0956` edge `0.0858` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.2635` n `90` status `ready` deltaP `21.5371` edge `0.1669` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.2533` n `62` status `ready` deltaP `3.9067` edge `0.1303` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.9671` n `90` status `ready` deltaP `20.6063` edge `0.0179` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6124` n `90` status `ready` deltaP `10.7485` edge `0.0036` maxDD `-0.271`
- `market_context_high->crypto_alt_24h` score `0.4323` n `90` status `ready` deltaP `8.7508` edge `0.5909` maxDD `-34.5048`
- `market_context_high->crypto_major_1h` score `0.2165` n `90` status `ready` deltaP `10.7019` edge `0.0453` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
