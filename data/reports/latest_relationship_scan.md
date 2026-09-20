# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T19:52:28.308130+00:00`
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

- `news_risk_high->crypto_major_24h` score `23.8948` n `98` status `ready` deltaP `11.5753` edge `2.5999` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3938` n `98` status `ready` deltaP `15.2671` edge `2.0858` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `12.2302` n `43` status `ready` deltaP `-0.5743` edge `1.038` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `4.9606` n `101` status `ready` deltaP `21.6629` edge `0.3899` maxDD `-7.675`
- `market_context_high->commodity_4h` score `4.2317` n `43` status `ready` deltaP `37.9148` edge `0.1132` maxDD `-0.0659`
- `news_risk_high->crypto_major_4h` score `3.8957` n `101` status `ready` deltaP `20.7483` edge `0.3121` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.9249` n `101` status `ready` deltaP `16.8302` edge `0.1781` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1887` n `101` status `ready` deltaP `18.6266` edge `0.1105` maxDD `-2.8494`
- `market_context_high->fx_4h` score `1.7261` n `43` status `ready` deltaP `23.8869` edge `0.0106` maxDD `-0.0801`
- `news_risk_high->commodity_24h` score `1.037` n `98` status `ready` deltaP `22.775` edge `0.1117` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.8417` n `54` status `ready` deltaP `12.3254` edge `0.0059` maxDD `-0.1012`
- `market_context_high->commodity_1h` score `0.7229` n `54` status `ready` deltaP `13.0184` edge `0.0334` maxDD `-0.2012`
- `news_risk_high->metal_4h` score `0.6142` n `101` status `ready` deltaP `17.0988` edge `0.0426` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6053` n `101` status `ready` deltaP `14.2986` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->equity_24h` score `0.5218` n `98` status `ready` deltaP `16.3974` edge `0.0751` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.3168` n `54` status `ready` deltaP `8.2114` edge `0.0065` maxDD `-0.4538`
- `news_risk_high->equity_1h` score `0.228` n `101` status `ready` deltaP `5.364` edge `0.0238` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `0.1603` n `101` status `ready` deltaP `8.1834` edge `0.0224` maxDD `-0.421`
- `news_risk_high->metal_24h` score `0.13` n `98` status `ready` deltaP `14.9837` edge `0.0012` maxDD `-2.4203`
- `news_risk_high->fx_1h` score `-0.2927` n `101` status `ready` deltaP `2.0943` edge `0.006` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
