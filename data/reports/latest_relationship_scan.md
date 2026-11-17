# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T20:37:23.344218+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4041`

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

- `market_context_high->unknown_24h` score `1490.8998` n `98` status `ready` deltaP `3.4722` edge `124.2185` maxDD `0.0`
- `news_risk_high->equity_24h` score `53.4293` n `35` status `ready` deltaP `66.1904` edge `4.0818` maxDD `-3.6503`
- `news_risk_high->equity_4h` score `20.338` n `35` status `ready` deltaP `55.6402` edge `1.3239` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `15.4901` n `35` status `ready` deltaP `29.0179` edge `1.9068` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `15.4359` n `98` status `ready` deltaP `46.3648` edge `1.9969` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.5975` n `98` status `ready` deltaP `32.5999` edge `1.8665` maxDD `-13.3222`
- `news_risk_high->index_24h` score `8.7666` n `35` status `ready` deltaP `57.5099` edge `0.3775` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.6841` n `35` status `ready` deltaP `54.8611` edge `0.2746` maxDD `0.0`
- `news_risk_high->metal_4h` score `6.8799` n `35` status `ready` deltaP `55.6795` edge `0.2066` maxDD `-0.0246`
- `news_risk_high->equity_1h` score `5.889` n `35` status `ready` deltaP `27.13` edge `0.3317` maxDD `-0.4122`
- `news_risk_high->crypto_alt_24h` score `5.1794` n `35` status `ready` deltaP `9.5387` edge `1.051` maxDD `-29.0448`
- `news_risk_high->crypto_major_4h` score `5.1549` n `35` status `ready` deltaP `20.9364` edge `0.3327` maxDD `-1.7491`
- `news_risk_high->crypto_alt_4h` score `5.04` n `35` status `ready` deltaP `32.365` edge `0.5071` maxDD `-4.137`
- `news_risk_high->index_4h` score `4.3275` n `35` status `ready` deltaP `36.7814` edge `0.1379` maxDD `-0.1319`
- `news_risk_high->crypto_alt_1h` score `2.9496` n `35` status `ready` deltaP `21.4157` edge `0.1557` maxDD `-2.5469`
- `news_risk_high->metal_1h` score `2.7715` n `35` status `ready` deltaP `29.6878` edge `0.0548` maxDD `-0.0743`
- `news_risk_high->crypto_major_1h` score `2.6724` n `35` status `ready` deltaP `17.5107` edge `0.1411` maxDD `-1.4777`
- `news_risk_high->index_1h` score `1.8731` n `35` status `ready` deltaP `21.8648` edge `0.0321` maxDD `-0.0751`
- `news_risk_high->commodity_4h` score `1.5851` n `35` status `ready` deltaP `26.7247` edge `0.0504` maxDD `-0.3611`
- `news_risk_high->commodity_1h` score `-0.2745` n `35` status `ready` deltaP `-1.5911` edge `0.0212` maxDD `-0.3438`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
