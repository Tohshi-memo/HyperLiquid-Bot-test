# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T07:52:29.382972+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9292`

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

- `news_risk_high->crypto_major_24h` score `41.23` n `81` status `ready` deltaP `17.8048` edge `3.4839` maxDD `-10.3413`
- `news_risk_high->crypto_alt_24h` score `37.3658` n `81` status `ready` deltaP `28.6844` edge `3.0605` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `6.8795` n `71` status `ready` deltaP `35.2211` edge `0.391` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.2338` n `98` status `ready` deltaP `23.4476` edge `0.4841` maxDD `-7.675`
- `news_risk_high->equity_24h` score `6.0868` n `81` status `ready` deltaP `33.2755` edge `0.299` maxDD `-0.4217`
- `news_risk_high->crypto_major_4h` score `4.7578` n `98` status `ready` deltaP `22.9902` edge `0.369` maxDD `-8.0625`
- `market_context_high->unknown_4h` score `4.5488` n `74` status `ready` deltaP `2.3483` edge `0.3784` maxDD `-0.5326`
- `market_context_high->commodity_4h` score `4.1726` n `74` status `ready` deltaP `36.7707` edge `0.1159` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.2942` n `99` status `ready` deltaP `18.1607` edge `0.2` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.5075` n `99` status `ready` deltaP `20.2565` edge `0.1262` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.3455` n `74` status `ready` deltaP `30.8256` edge `0.0073` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `1.9756` n `74` status `ready` deltaP `21.48` edge `0.0383` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.3537` n `81` status `ready` deltaP `21.3349` edge `0.055` maxDD `-2.4203`
- `market_context_high->fx_24h` score `1.132` n `71` status `ready` deltaP `15.6054` edge `-0.0055` maxDD `-0.0027`
- `news_risk_high->metal_4h` score `0.854` n `98` status `ready` deltaP `19.5868` edge `0.046` maxDD `-2.0994`
- `market_context_high->fx_1h` score `0.8281` n `74` status `ready` deltaP `13.5297` edge `0.0046` maxDD `-0.063`
- `news_risk_high->metal_1h` score `0.6631` n `99` status `ready` deltaP `14.9459` edge `0.0158` maxDD `-0.8144`
- `news_risk_high->commodity_24h` score `0.3653` n `81` status `ready` deltaP `17.2068` edge `0.0627` maxDD `-3.4467`
- `news_risk_high->equity_1h` score `0.3242` n `99` status `ready` deltaP `5.7416` edge `0.0293` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `-0.0805` n `98` status `ready` deltaP `5.2327` edge `0.022` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
