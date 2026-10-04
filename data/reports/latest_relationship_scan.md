# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T14:37:26.953000+00:00`
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

- `market_context_high->unknown_4h` score `104.2674` n `88` status `ready` deltaP `2.8963` edge `8.7008` maxDD `-0.4928`
- `market_context_high->unknown_1h` score `95.7428` n `97` status `ready` deltaP `-0.6096` edge `8.0241` maxDD `-0.9839`
- `market_context_high->crypto_alt_24h` score `10.581` n `46` status `ready` deltaP `26.9626` edge `0.8293` maxDD `-8.1838`
- `news_risk_high->crypto_major_4h` score `10.5373` n `65` status `ready` deltaP `37.4297` edge `0.6489` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `10.3049` n `46` status `ready` deltaP `33.4012` edge `0.7013` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `8.576` n `65` status `ready` deltaP `24.4018` edge `0.562` maxDD `-0.1344`
- `news_risk_high->crypto_alt_4h` score `7.2959` n `65` status `ready` deltaP `24.3598` edge `0.58` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `5.2711` n `88` status `ready` deltaP `22.3947` edge `0.3603` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.998` n `65` status `ready` deltaP `27.4306` edge `0.1503` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.814` n `65` status `ready` deltaP `25.9123` edge `0.2061` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.1038` n `65` status `ready` deltaP `33.743` edge `0.0599` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8932` n `65` status `ready` deltaP `12.561` edge `0.1929` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.5878` n `65` status `ready` deltaP `22.2796` edge `0.1087` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.1548` n `97` status `ready` deltaP `15.4794` edge `0.1214` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.0962` n `65` status `ready` deltaP `25.7669` edge `0.0179` maxDD `-0.1997`
- `market_context_high->equity_24h` score `2.0347` n `46` status `ready` deltaP `4.4686` edge `0.2389` maxDD `-6.264`
- `news_risk_high->crypto_alt_1h` score `1.5103` n `65` status `ready` deltaP `5.0184` edge `0.1443` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.4912` n `88` status `ready` deltaP `4.5871` edge `0.2726` maxDD `-7.6465`
- `market_context_high->fx_4h` score `1.3893` n `88` status `ready` deltaP `24.6812` edge `0.0269` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3607` n `46` status `ready` deltaP `25.536` edge `0.106` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
