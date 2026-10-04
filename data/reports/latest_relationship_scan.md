# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T16:07:32.070626+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5032`

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

- `market_context_high->unknown_1h` score `96.1208` n `97` status `ready` deltaP `-0.6096` edge `8.0556` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `86.3915` n `94` status `ready` deltaP `2.7828` edge `7.2119` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.6181` n `65` status `ready` deltaP `37.7345` edge `0.6536` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `9.9241` n `46` status `ready` deltaP `25.9209` edge `0.7815` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `9.8292` n `46` status `ready` deltaP `32.3596` edge `0.6686` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `8.0198` n `65` status `ready` deltaP `23.3601` edge `0.5226` maxDD `-0.1344`
- `news_risk_high->crypto_alt_4h` score `7.445` n `65` status `ready` deltaP `24.6646` edge `0.5904` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `5.0493` n `94` status `ready` deltaP `22.0225` edge `0.3443` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.8945` n `65` status `ready` deltaP `26.7361` edge `0.1463` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8406` n `65` status `ready` deltaP `26.0647` edge `0.2073` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.1818` n `65` status `ready` deltaP `34.6576` edge `0.0603` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.886` n `65` status `ready` deltaP `12.561` edge `0.1923` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.6268` n `65` status `ready` deltaP `22.7369` edge `0.1089` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1585` n `65` status `ready` deltaP `26.5154` edge `0.0181` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.1476` n `97` status `ready` deltaP `15.4794` edge `0.1208` maxDD `-2.2692`
- `market_context_high->fx_4h` score `1.562` n `94` status `ready` deltaP `26.9298` edge `0.0263` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.5438` n `65` status `ready` deltaP `5.1681` edge `0.1461` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.5401` n `94` status `ready` deltaP `5.3029` edge `0.2719` maxDD `-7.6465`
- `market_context_high->equity_24h` score `1.4786` n `46` status `ready` deltaP `3.4269` edge `0.1995` maxDD `-6.264`
- `market_context_high->fx_24h` score `1.3622` n `46` status `ready` deltaP `25.536` edge `0.1062` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
