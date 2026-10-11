# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T20:52:35.227868+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8948`

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

- `market_context_high->unknown_24h` score `1380.7353` n `40` status `ready` deltaP `-22.5694` edge `115.2481` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `51.0364` n `92` status `ready` deltaP `-3.6917` edge `4.3357` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.7924` n `40` status `ready` deltaP `27.6736` edge `0.5911` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.4024` n `40` status `ready` deltaP `52.4306` edge `0.184` maxDD `0.0`
- `market_context_high->unknown_1h` score `5.5485` n `104` status `ready` deltaP `-3.7655` edge `0.5211` maxDD `-1.0231`
- `market_context_high->fx_24h` score `3.1039` n `40` status `ready` deltaP `35.2083` edge `0.0369` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.4044` n `40` status `ready` deltaP `-21.1111` edge `0.5726` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.8928` n `92` status `ready` deltaP `14.2298` edge `0.0079` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.5516` n `92` status `ready` deltaP `12.4205` edge `0.0165` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `0.325` n `104` status `ready` deltaP `6.7481` edge `0.1001` maxDD `-4.9401`
- `market_context_high->commodity_1h` score `0.305` n `104` status `ready` deltaP `7.0475` edge `0.0068` maxDD `-0.6025`
- `market_context_high->crypto_major_4h` score `0.1838` n `92` status `ready` deltaP `1.7895` edge `0.2222` maxDD `-11.1784`
- `market_context_high->metal_4h` score `0.1727` n `92` status `ready` deltaP `9.6699` edge `0.0222` maxDD `-1.1153`
- `market_context_high->fx_1h` score `0.0511` n `104` status `ready` deltaP `4.0765` edge `0.0013` maxDD `-0.271`
- `market_context_high->crypto_alt_4h` score `0.0134` n `92` status `ready` deltaP `-0.5302` edge `0.2611` maxDD `-13.8008`
- `market_context_high->metal_1h` score `-0.0822` n `104` status `ready` deltaP `7.2202` edge `0.0039` maxDD `-0.7107`
- `market_context_high->crypto_major_1h` score `-0.2299` n `104` status `ready` deltaP `0.5124` edge `0.056` maxDD `-3.7778`
- `market_context_high->index_4h` score `-0.4679` n `92` status `ready` deltaP `0.517` edge `0.0066` maxDD `-0.9364`
- `market_context_high->index_1h` score `-0.7181` n `104` status `ready` deltaP `-3.8692` edge `-0.0012` maxDD `-0.5392`
- `market_context_high->equity_1h` score `-0.9028` n `104` status `ready` deltaP `-4.8134` edge `0.0033` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
