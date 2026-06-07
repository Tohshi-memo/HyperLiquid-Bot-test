# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T18:37:23.010554+00:00`
- Price records: `672`
- Market context records: `3206`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10906`

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

- `market_context_high->crypto_alt_24h` score `17.0471` n `97` status `ready` deltaP `11.9398` edge `2.3386` maxDD `-71.142`
- `market_context_high->commodity_24h` score `13.7051` n `97` status `ready` deltaP `47.4924` edge `0.8683` maxDD `-2.0927`
- `market_context_high->index_24h` score `6.0406` n `97` status `ready` deltaP `28.0784` edge `0.8427` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.5858` n `97` status `ready` deltaP `11.8109` edge `1.3508` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.4188` n `126` status `ready` deltaP `22.5005` edge `0.1807` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.6726` n `97` status `ready` deltaP `12.1187` edge `-0.001` maxDD `-0.5661`
- `market_context_high->unknown_4h` score `0.5627` n `126` status `ready` deltaP `11.0265` edge `0.1956` maxDD `-14.7778`
- `market_context_high->unknown_24h` score `0.5182` n `97` status `ready` deltaP `14.0911` edge `0.3938` maxDD `-31.371`
- `market_context_high->commodity_1h` score `0.3566` n `135` status `ready` deltaP `5.9969` edge `0.032` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.7029` n `135` status `ready` deltaP `6.1621` edge `0.1133` maxDD `-14.7034`
- `market_context_high->crypto_major_1h` score `-0.8135` n `135` status `ready` deltaP `5.6099` edge `0.0846` maxDD `-15.1032`
- `market_context_high->index_1h` score `-0.8407` n `135` status `ready` deltaP `3.6483` edge `0.0119` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-1.0853` n `135` status `ready` deltaP `-9.8348` edge `-0.0049` maxDD `-0.8278`
- `market_context_high->fx_4h` score `-1.149` n `126` status `ready` deltaP `-7.9994` edge `-0.0055` maxDD `-1.4115`
- `market_context_high->equity_1h` score `-1.3753` n `135` status `ready` deltaP `3.4908` edge `0.0107` maxDD `-8.8863`
- `market_context_high->index_4h` score `-1.4982` n `126` status `ready` deltaP `15.2632` edge `0.0643` maxDD `-17.6057`
- `market_context_high->metal_1h` score `-2.0195` n `135` status `ready` deltaP `-3.1836` edge `-0.0077` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.6785` n `135` status `ready` deltaP `1.8053` edge `-0.1176` maxDD `-17.0266`
- `market_context_high->crypto_alt_4h` score `-3.1599` n `126` status `ready` deltaP `13.4195` edge `0.3099` maxDD `-58.6918`
- `market_context_high->crypto_major_4h` score `-4.3681` n `126` status `ready` deltaP `6.7291` edge `0.1875` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
