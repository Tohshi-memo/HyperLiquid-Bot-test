# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T19:37:29.041092+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10418`

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

- `news_risk_high->crypto_major_24h` score `23.8246` n `98` status `ready` deltaP `11.4017` edge `2.5952` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.389` n `98` status `ready` deltaP `15.2671` edge `2.0854` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `11.7825` n `42` status `ready` deltaP `-0.7405` edge `1.0018` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.0388` n `101` status `ready` deltaP `21.8154` edge `0.3954` maxDD `-7.675`
- `market_context_high->commodity_4h` score `4.2335` n `42` status `ready` deltaP `37.6379` edge `0.1152` maxDD `-0.0659`
- `news_risk_high->crypto_major_4h` score `3.9499` n `101` status `ready` deltaP `20.9007` edge `0.3156` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.9309` n `101` status `ready` deltaP `16.8302` edge `0.1786` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1923` n `101` status `ready` deltaP `18.6266` edge `0.1108` maxDD `-2.8494`
- `market_context_high->fx_4h` score `1.8824` n `42` status `ready` deltaP `25.617` edge `0.0118` maxDD `-0.0569`
- `news_risk_high->commodity_24h` score `1.0409` n `98` status `ready` deltaP `22.775` edge `0.1122` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.8297` n `54` status `ready` deltaP `12.1757` edge `0.0059` maxDD `-0.1012`
- `market_context_high->commodity_1h` score `0.7229` n `54` status `ready` deltaP `13.0184` edge `0.0334` maxDD `-0.2012`
- `news_risk_high->metal_4h` score `0.6288` n `101` status `ready` deltaP `17.2512` edge `0.0428` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6173` n `101` status `ready` deltaP `14.4483` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->equity_24h` score `0.5326` n `98` status `ready` deltaP `16.3974` edge `0.076` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.3288` n `54` status `ready` deltaP `8.3611` edge `0.0065` maxDD `-0.4538`
- `news_risk_high->equity_1h` score `0.2292` n `101` status `ready` deltaP `5.364` edge `0.0239` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `0.1481` n `101` status `ready` deltaP `8.0309` edge `0.0224` maxDD `-0.421`
- `news_risk_high->metal_24h` score `0.1363` n `98` status `ready` deltaP `14.9837` edge `0.002` maxDD `-2.4203`
- `news_risk_high->fx_1h` score `-0.3046` n `101` status `ready` deltaP `1.9446` edge `0.006` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
