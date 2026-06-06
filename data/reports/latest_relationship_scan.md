# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T18:52:18.673053+00:00`
- Price records: `672`
- Market context records: `3102`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6921`

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

- `market_context_high->crypto_alt_24h` score `16.4967` n `83` status `ready` deltaP `13.7696` edge `2.5542` maxDD `-33.816`
- `market_context_high->commodity_24h` score `15.1239` n `83` status `ready` deltaP `45.233` edge `1.0016` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.8551` n `83` status `ready` deltaP `23.2681` edge `1.1316` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.5816` n `83` status `ready` deltaP `32.1431` edge `0.9167` maxDD `-15.6019`
- `market_context_high->equity_24h` score `7.4173` n `83` status `ready` deltaP `18.2794` edge `1.3658` maxDD `-36.9377`
- `market_context_high->commodity_4h` score `3.0653` n `118` status `ready` deltaP `18.4115` edge `0.1785` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `-0.059` n `120` status `ready` deltaP `1.5369` edge `0.0271` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.3187` n `118` status `ready` deltaP `5.7488` edge `0.0579` maxDD `-7.4891`
- `market_context_high->index_1h` score `-0.4605` n `120` status `ready` deltaP `4.5958` edge `0.0166` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.6394` n `83` status `ready` deltaP `3.3864` edge `-0.0031` maxDD `-0.4876`
- `market_context_high->fx_1h` score `-0.6768` n `120` status `ready` deltaP `-7.0509` edge `-0.0025` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.8411` n `120` status `ready` deltaP `2.9291` edge `0.0856` maxDD `-14.7034`
- `market_context_high->fx_4h` score `-1.3275` n `118` status `ready` deltaP `-12.2727` edge `-0.004` maxDD `-1.0829`
- `market_context_high->equity_1h` score `-1.3323` n `120` status `ready` deltaP `-3.0339` edge `-0.002` maxDD `-8.8863`
- `market_context_high->index_4h` score `-1.4067` n `118` status `ready` deltaP `9.999` edge `0.0439` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-2.2481` n `120` status `ready` deltaP `-1.1477` edge `0.0466` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.436` n `120` status `ready` deltaP `-7.6248` edge `-0.0128` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.689` n `120` status `ready` deltaP `3.3084` edge `-0.0617` maxDD `-12.7554`
- `market_context_high->crypto_alt_4h` score `-3.899` n `118` status `ready` deltaP `12.4819` edge `0.2214` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.1614` n `118` status `ready` deltaP `5.1519` edge `-0.0373` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
