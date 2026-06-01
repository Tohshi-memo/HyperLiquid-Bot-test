# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T05:07:20.707970+00:00`
- Price records: `672`
- Market context records: `2531`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9312`

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

- `market_context_high->crypto_alt_4h` score `5.0316` n `160` status `ready` deltaP `23.4451` edge `0.5309` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `4.6601` n `117` status `ready` deltaP `19.4044` edge `0.2918` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.5374` n `160` status `ready` deltaP `16.753` edge `0.3641` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.702` n `117` status `ready` deltaP `12.7137` edge `0.6186` maxDD `-23.222`
- `market_context_high->unknown_4h` score `1.9143` n `160` status `ready` deltaP `11.2043` edge `0.1898` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1728` n `160` status `ready` deltaP `9.506` edge `0.1531` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.7323` n `160` status `ready` deltaP `8.4057` edge `0.1244` maxDD `-4.2199`
- `market_context_high->equity_24h` score `0.0644` n `117` status `ready` deltaP `17.9087` edge `0.0243` maxDD `-6.3993`
- `market_context_high->crypto_alt_24h` score `0.014` n `117` status `ready` deltaP `0.641` edge `0.6867` maxDD `-43.1346`
- `market_context_high->index_4h` score `-0.0687` n `160` status `ready` deltaP `6.7683` edge `0.0333` maxDD `-2.3986`
- `market_context_high->index_24h` score `-0.1176` n `117` status `ready` deltaP `2.711` edge `0.0702` maxDD `-2.5127`
- `market_context_high->commodity_1h` score `-0.3139` n `160` status `ready` deltaP `4.6033` edge `0.0169` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4008` n `160` status `ready` deltaP `2.5524` edge `0.0186` maxDD `-2.8543`
- `market_context_high->index_1h` score `-0.4127` n `160` status `ready` deltaP `1.3361` edge `0.0061` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.4778` n `160` status `ready` deltaP `0.8982` edge `0.0087` maxDD `-3.0759`
- `market_context_high->fx_1h` score `-0.5012` n `160` status `ready` deltaP `1.1265` edge `0.0042` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.8257` n `160` status `ready` deltaP `-0.1272` edge `0.0159` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8292` n `160` status `ready` deltaP `0.6555` edge `0.0125` maxDD `-0.8774`
- `market_context_high->metal_4h` score `-0.8807` n `160` status `ready` deltaP `3.3079` edge `0.0433` maxDD `-4.7664`
- `market_context_high->fx_24h` score `-0.8818` n `117` status `ready` deltaP `2.6976` edge `0.0039` maxDD `-2.4611`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
