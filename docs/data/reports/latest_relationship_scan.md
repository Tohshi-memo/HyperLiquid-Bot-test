# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T03:07:18.787032+00:00`
- Price records: `672`
- Market context records: `2417`
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

- `news_risk_high->crypto_alt_24h` score `20.1066` n `43` status `ready` deltaP `46.2169` edge `1.4263` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.4671` n `43` status `ready` deltaP `50.2786` edge `1.2477` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.1411` n `43` status `ready` deltaP `29.7925` edge `1.0946` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.7608` n `43` status `ready` deltaP `18.8993` edge `0.8288` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.0311` n `43` status `ready` deltaP `27.2932` edge `0.5099` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.8771` n `103` status `ready` deltaP `24.1774` edge `0.3614` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.2308` n `43` status `ready` deltaP `11.1879` edge `0.4032` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.6989` n `126` status `ready` deltaP `22.2271` edge `0.4244` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.6585` n `126` status `ready` deltaP `22.8006` edge `0.5041` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.5988` n `43` status `ready` deltaP `37.7504` edge `0.0667` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2866` n `43` status `ready` deltaP `30.3282` edge `0.2863` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.7531` n `103` status `ready` deltaP `11.2678` edge `0.6671` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.6853` n `126` status `ready` deltaP `13.6712` edge `0.1936` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.4738` n `103` status `ready` deltaP `13.6715` edge `0.1407` maxDD `-0.3888`
- `news_risk_high->fx_4h` score `2.139` n `43` status `ready` deltaP `27.127` edge `0.0158` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7977` n `43` status `ready` deltaP `16.1444` edge `0.1145` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2247` n `126` status `ready` deltaP `11.4414` edge `0.1452` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.0306` n `43` status `ready` deltaP `19.9972` edge `-0.0005` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0088` n `126` status `ready` deltaP `8.6256` edge `0.1453` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.56` n `43` status `ready` deltaP `9.4172` edge `0.077` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
