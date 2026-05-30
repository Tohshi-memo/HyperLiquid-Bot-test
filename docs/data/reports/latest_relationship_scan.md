# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T01:37:24.498013+00:00`
- Price records: `672`
- Market context records: `2301`
- Flow alert records: `8515`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9290`

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

- `news_risk_high->crypto_alt_24h` score `20.6077` n `43` status `ready` deltaP `50.0363` edge `1.4426` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.6891` n `43` status `ready` deltaP `40.9036` edge `1.0787` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.5823` n `43` status `ready` deltaP `29.7925` edge `0.9647` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.3382` n `43` status `ready` deltaP `19.7674` edge `0.7878` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `7.5009` n `159` status `ready` deltaP `24.4611` edge `0.7299` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.4919` n `159` status `ready` deltaP `29.2836` edge `0.6101` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `7.2709` n `115` status `ready` deltaP `23.7696` edge `0.4886` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `6.8344` n `43` status `ready` deltaP `27.8141` edge `0.4067` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.5914` n `159` status `ready` deltaP `22.3079` edge `0.3782` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `4.9982` n `115` status `ready` deltaP `13.4783` edge `0.9402` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.8969` n `43` status `ready` deltaP `32.6148` edge `0.3493` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.737` n `43` status `ready` deltaP `11.5351` edge `0.2764` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.4287` n `43` status `ready` deltaP `36.0142` edge `0.0641` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3473` n `115` status `ready` deltaP `13.3349` edge `0.2418` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.1314` n `43` status `ready` deltaP `4.4614` edge `0.3129` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.2318` n `43` status `ready` deltaP `28.3465` edge `0.0154` maxDD `-0.1382`
- `market_context_high->index_4h` score `2.2262` n `159` status `ready` deltaP `21.7192` edge `0.1233` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.9874` n `159` status `ready` deltaP `12.7735` edge `0.1992` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.7728` n `159` status `ready` deltaP `13.0729` edge `0.18` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.7471` n `159` status `ready` deltaP `16.2506` edge `0.1777` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
