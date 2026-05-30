# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T07:37:21.912882+00:00`
- Price records: `672`
- Market context records: `2327`
- Flow alert records: `8589`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9168`

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

- `news_risk_high->crypto_alt_24h` score `20.7517` n `43` status `ready` deltaP `50.0363` edge `1.4546` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.4001` n `43` status `ready` deltaP `43.1605` edge `1.1229` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.1043` n `43` status `ready` deltaP `29.7925` edge `1.0082` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.4462` n `43` status `ready` deltaP `19.7674` edge `0.7968` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `7.4712` n `124` status `ready` deltaP `24.0536` edge `0.5034` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `6.9734` n `43` status `ready` deltaP `27.4669` edge `0.4206` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `6.9439` n `159` status `ready` deltaP `23.3941` edge `0.6906` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.9169` n `159` status `ready` deltaP `27.3019` edge `0.5754` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `5.7023` n `124` status `ready` deltaP `16.129` edge `1.0128` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.2649` n `159` status `ready` deltaP `21.2408` edge `0.3581` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.2352` n `43` status `ready` deltaP `11.8823` edge `0.3156` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0042` n `43` status `ready` deltaP `33.9868` edge `0.3539` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.4517` n `124` status `ready` deltaP `14.2641` edge `0.2443` maxDD `-1.4737`
- `news_risk_high->fx_24h` score `3.4071` n `43` status `ready` deltaP `36.0142` edge `0.0623` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `2.183` n `43` status `ready` deltaP `27.7368` edge `0.0154` maxDD `-0.1382`
- `market_context_high->index_4h` score `2.1206` n `159` status `ready` deltaP `20.8045` edge `0.1206` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.9071` n `159` status `ready` deltaP `12.4741` edge `0.1945` maxDD `-6.1656`
- `news_risk_high->commodity_24h` score `1.8107` n `43` status `ready` deltaP `4.2878` edge `0.204` maxDD `-3.202`
- `market_context_high->equity_24h` score `1.7427` n `124` status `ready` deltaP `18.4084` edge `0.1752` maxDD `-6.8828`
- `market_context_high->crypto_major_1h` score `1.6469` n `159` status `ready` deltaP `12.4741` edge `0.1735` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
