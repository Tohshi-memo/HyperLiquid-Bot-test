# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T03:22:23.480638+00:00`
- Price records: `672`
- Market context records: `2418`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `news_risk_high->crypto_alt_24h` score `20.0627` n `43` status `ready` deltaP `46.0432` edge `1.4238` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.5026` n `43` status `ready` deltaP `50.4522` edge `1.2495` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.1279` n `43` status `ready` deltaP `29.7925` edge `1.0935` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.7212` n `43` status `ready` deltaP `18.8993` edge `0.8255` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.9812` n `43` status `ready` deltaP `27.1196` edge `0.5069` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.8272` n `103` status `ready` deltaP `24.0038` edge `0.3584` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.2121` n `43` status `ready` deltaP `11.0142` edge `0.4028` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.6857` n `126` status `ready` deltaP `22.2271` edge `0.4233` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.6271` n `126` status `ready` deltaP `22.6481` edge `0.5025` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.5837` n `43` status `ready` deltaP `37.5767` edge `0.0666` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2764` n `43` status `ready` deltaP `30.1758` edge `0.286` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.7273` n `103` status `ready` deltaP `11.2678` edge `0.6638` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.6745` n `126` status `ready` deltaP `13.6712` edge `0.1927` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.4551` n `103` status `ready` deltaP `13.4978` edge `0.1403` maxDD `-0.3888`
- `news_risk_high->fx_4h` score `2.139` n `43` status `ready` deltaP `27.127` edge `0.0158` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7869` n `43` status `ready` deltaP `16.1444` edge `0.1136` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2427` n `126` status `ready` deltaP `11.5911` edge `0.1457` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.0342` n `43` status `ready` deltaP `19.9972` edge `-0.0002` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.028` n `126` status `ready` deltaP `8.7753` edge `0.1459` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.56` n `43` status `ready` deltaP `9.4172` edge `0.077` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
