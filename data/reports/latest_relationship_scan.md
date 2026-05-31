# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T03:52:20.890314+00:00`
- Price records: `672`
- Market context records: `2420`
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

- `news_risk_high->crypto_alt_24h` score `19.9521` n `43` status `ready` deltaP `45.696` edge `1.4169` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.564` n `43` status `ready` deltaP `50.7994` edge `1.2523` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.0967` n `43` status `ready` deltaP `29.7925` edge `1.0909` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.6077` n `43` status `ready` deltaP `18.7257` edge `0.8172` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.8706` n `43` status `ready` deltaP `26.7724` edge `0.5` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.7166` n `103` status `ready` deltaP `23.6566` edge `0.3515` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.1724` n `43` status `ready` deltaP `10.667` edge `0.4018` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.6206` n `126` status `ready` deltaP `21.9222` edge `0.4199` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.5391` n `126` status `ready` deltaP `22.3432` edge `0.4972` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.5523` n `43` status `ready` deltaP `37.2295` edge `0.0663` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.255` n `43` status `ready` deltaP `29.8709` edge `0.2853` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.6536` n `103` status `ready` deltaP `11.0942` edge `0.6555` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.6191` n `126` status `ready` deltaP `13.5187` edge `0.1891` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.4153` n `103` status `ready` deltaP `13.1506` edge `0.1393` maxDD `-0.3888`
- `news_risk_high->fx_4h` score `2.1256` n `43` status `ready` deltaP `26.9746` edge `0.0157` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7315` n `43` status `ready` deltaP `15.9919` edge `0.11` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2056` n `126` status `ready` deltaP `11.2917` edge `0.1446` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.033` n `43` status `ready` deltaP `19.9972` edge `-0.0003` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `0.986` n `126` status `ready` deltaP `8.4759` edge `0.1444` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5686` n `43` status `ready` deltaP `9.5669` edge `0.0771` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
