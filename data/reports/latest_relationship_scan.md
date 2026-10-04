# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T05:37:42.019130+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5068`

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

- `market_context_high->unknown_4h` score `299.7551` n `52` status `ready` deltaP `8.4076` edge `24.9379` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `228.0955` n `64` status `ready` deltaP `0.8421` edge `19.0438` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `14.9737` n `46` status `ready` deltaP `33.1211` edge `1.1543` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `13.5807` n `46` status `ready` deltaP `39.5637` edge `0.9332` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `11.5539` n `59` status `ready` deltaP `29.9621` edge `0.7731` maxDD `-0.1353`
- `news_risk_high->crypto_major_4h` score `11.0592` n `65` status `ready` deltaP `40.1736` edge `0.6741` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.5494` n `65` status `ready` deltaP `24.6646` edge `0.5991` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.106` n `52` status `ready` deltaP `17.0967` edge `0.4652` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.905` n `59` status `ready` deltaP `33.6222` edge `0.1846` maxDD `0.0`
- `market_context_high->equity_24h` score `4.5798` n `46` status `ready` deltaP `10.6548` edge `0.4103` maxDD `-6.3081`
- `news_risk_high->equity_4h` score `3.9277` n `65` status `ready` deltaP `27.1318` edge `0.2077` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.1538` n `65` status `ready` deltaP `34.3528` edge `0.06` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9963` n `65` status `ready` deltaP `13.3095` edge `0.1965` maxDD `-1.5096`
- `market_context_high->crypto_alt_4h` score `2.9955` n `52` status `ready` deltaP `15.8184` edge `0.4075` maxDD `-7.6465`
- `news_risk_high->metal_4h` score `2.5524` n `65` status `ready` deltaP `21.8223` edge `0.1088` maxDD `-0.993`
- `market_context_high->fx_4h` score `2.5033` n `52` status `ready` deltaP `29.5967` edge `0.0376` maxDD `-0.1043`
- `market_context_high->crypto_major_1h` score `2.4887` n `64` status `ready` deltaP `14.3432` edge `0.1568` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.0962` n `65` status `ready` deltaP `25.7669` edge `0.0179` maxDD `-0.1997`
- `market_context_high->crypto_alt_1h` score `2.0516` n `64` status `ready` deltaP `10.32` edge `0.1768` maxDD `-3.6376`
- `news_risk_high->crypto_alt_1h` score `1.5079` n `65` status `ready` deltaP `4.719` edge `0.1461` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
