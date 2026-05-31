# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T02:52:22.688217+00:00`
- Price records: `672`
- Market context records: `2416`
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

- `news_risk_high->crypto_alt_24h` score `20.133` n `43` status `ready` deltaP `46.2169` edge `1.4285` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.4317` n `43` status `ready` deltaP `50.105` edge `1.2459` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.1519` n `43` status `ready` deltaP `29.7925` edge `1.0955` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.7944` n `43` status `ready` deltaP `18.8993` edge `0.8316` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.0774` n `43` status `ready` deltaP `27.4669` edge `0.5126` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.9234` n `103` status `ready` deltaP `24.3511` edge `0.3641` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.2507` n `43` status `ready` deltaP `11.3615` edge `0.4037` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.7109` n `126` status `ready` deltaP `22.2271` edge `0.4254` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.6863` n `126` status `ready` deltaP `22.953` edge `0.5054` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.6` n `43` status `ready` deltaP `37.7504` edge `0.0668` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2882` n `43` status `ready` deltaP `30.3282` edge `0.2865` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.7749` n `103` status `ready` deltaP `11.2678` edge `0.6699` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.6925` n `126` status `ready` deltaP `13.6712` edge `0.1942` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.4937` n `103` status `ready` deltaP `13.8451` edge `0.1412` maxDD `-0.3888`
- `news_risk_high->fx_4h` score `2.139` n `43` status `ready` deltaP `27.127` edge `0.0158` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.8049` n `43` status `ready` deltaP `16.1444` edge `0.1151` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2175` n `126` status `ready` deltaP `11.4414` edge `0.1446` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.033` n `43` status `ready` deltaP `19.9972` edge `-0.0003` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `0.992` n `126` status `ready` deltaP `8.4759` edge `0.1449` maxDD `-6.1656`
- `market_context_high->crypto_alt_24h` score `0.5653` n `103` status `ready` deltaP `1.3535` edge `0.7592` maxDD `-43.6595`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
