# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T07:22:31.129364+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5004`

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

- `market_context_high->unknown_4h` score `242.5256` n `59` status `ready` deltaP `7.5496` edge `20.1745` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `189.5729` n `71` status `ready` deltaP `1.7838` edge `15.8273` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `14.2167` n `46` status `ready` deltaP `31.9079` edge `1.0993` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `13.0097` n `46` status `ready` deltaP `38.3505` edge `0.8937` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `11.1532` n `59` status `ready` deltaP `28.7489` edge `0.7478` maxDD `-0.1353`
- `news_risk_high->crypto_major_4h` score `11.1168` n `65` status `ready` deltaP `40.1736` edge `0.6789` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.559` n `65` status `ready` deltaP `24.6646` edge `0.5999` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.2349` n `59` status `ready` deltaP `20.7473` edge `0.4516` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.7779` n `59` status `ready` deltaP `32.409` edge `0.1821` maxDD `0.0`
- `market_context_high->equity_24h` score `4.1791` n `46` status `ready` deltaP `9.4416` edge `0.385` maxDD `-6.3081`
- `news_risk_high->equity_4h` score `3.9409` n `65` status `ready` deltaP `27.1318` edge `0.2088` maxDD `-2.9013`
- `market_context_high->crypto_alt_4h` score `3.4371` n `59` status `ready` deltaP `19.2409` edge `0.4413` maxDD `-7.6465`
- `news_risk_high->index_4h` score `3.1818` n `65` status `ready` deltaP `34.6576` edge `0.0603` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `3.0035` n `65` status `ready` deltaP `13.1598` edge `0.1981` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.6899` n `71` status `ready` deltaP `17.4285` edge `0.153` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.5768` n `65` status `ready` deltaP `22.1271` edge `0.1088` maxDD `-0.993`
- `market_context_high->crypto_alt_1h` score `2.1719` n `71` status `ready` deltaP `12.6044` edge `0.1716` maxDD `-3.6376`
- `news_risk_high->index_1h` score `2.1573` n `65` status `ready` deltaP `26.5154` edge `0.018` maxDD `-0.1997`
- `market_context_high->fx_4h` score `1.6052` n `59` status `ready` deltaP `21.3828` edge `0.0318` maxDD `-0.2468`
- `news_risk_high->crypto_alt_1h` score `1.5667` n `65` status `ready` deltaP `4.8687` edge `0.15` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
