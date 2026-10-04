# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T13:52:26.969168+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5016`

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

- `market_context_high->unknown_4h` score `114.1009` n `85` status `ready` deltaP `2.4551` edge `9.5232` maxDD `-0.4928`
- `market_context_high->unknown_1h` score `95.5112` n `97` status `ready` deltaP `-0.6096` edge `8.0048` maxDD `-0.9839`
- `market_context_high->crypto_alt_24h` score `10.8807` n `46` status `ready` deltaP `27.4834` edge `0.8508` maxDD `-8.1838`
- `news_risk_high->crypto_major_4h` score `10.5433` n `65` status `ready` deltaP `37.4297` edge `0.6494` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `10.529` n `46` status `ready` deltaP `33.9221` edge `0.7165` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `8.812` n `65` status `ready` deltaP `24.9226` edge `0.5782` maxDD `-0.1344`
- `news_risk_high->crypto_alt_4h` score `7.2523` n `65` status `ready` deltaP `24.0549` edge `0.5784` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `5.7329` n `85` status `ready` deltaP `25.122` edge `0.3806` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.0565` n `65` status `ready` deltaP `27.9514` edge `0.1517` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8116` n `65` status `ready` deltaP `25.9123` edge `0.2059` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.066` n `65` status `ready` deltaP `33.2857` edge `0.0598` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9208` n `65` status `ready` deltaP `12.561` edge `0.1952` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.5634` n `65` status `ready` deltaP `21.9747` edge `0.1087` maxDD `-0.993`
- `market_context_high->equity_24h` score `2.2708` n `46` status `ready` deltaP `4.9894` edge `0.2551` maxDD `-6.264`
- `market_context_high->crypto_major_1h` score `2.1824` n `97` status `ready` deltaP `15.4794` edge `0.1237` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.0962` n `65` status `ready` deltaP `25.7669` edge `0.0179` maxDD `-0.1997`
- `market_context_high->crypto_alt_4h` score `1.7483` n `85` status `ready` deltaP `5.2314` edge `0.2814` maxDD `-7.6465`
- `news_risk_high->crypto_alt_1h` score `1.557` n `65` status `ready` deltaP `5.1681` edge `0.1472` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.3599` n `46` status `ready` deltaP `25.536` edge `0.1059` maxDD `-1.8102`
- `market_context_high->fx_4h` score `1.2922` n `85` status `ready` deltaP `23.4379` edge `0.0271` maxDD `-0.3868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
