# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T00:52:15.282445+00:00`
- Price records: `672`
- Market context records: `2407`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9202`

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

- `news_risk_high->crypto_alt_24h` score `20.5235` n `43` status `ready` deltaP `47.2585` edge `1.4541` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.1937` n `43` status `ready` deltaP `49.4105` edge `1.2307` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.2587` n `43` status `ready` deltaP `29.7925` edge `1.1044` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.0644` n `43` status `ready` deltaP `18.8993` edge `0.8541` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2211` n `43` status `ready` deltaP `27.9877` edge `0.5211` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.5436` n `111` status `ready` deltaP `22.729` edge `0.3516` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.3592` n `43` status `ready` deltaP `12.4031` edge `0.4058` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.8835` n `134` status `ready` deltaP `23.6485` edge `0.4303` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.0905` n `134` status `ready` deltaP `20.486` edge `0.4722` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.6079` n `43` status `ready` deltaP `37.924` edge `0.0663` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2647` n `43` status `ready` deltaP `30.1758` edge `0.2845` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `3.0596` n `111` status `ready` deltaP `13.9968` edge `0.6882` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.5209` n `134` status `ready` deltaP `13.1917` edge `0.1831` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.1658` n `43` status `ready` deltaP `27.4319` edge `0.016` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7105` n `43` status `ready` deltaP `15.5346` edge `0.1113` maxDD `-2.7857`
- `market_context_high->index_24h` score `1.6468` n `111` status `ready` deltaP `10.8108` edge `0.1129` maxDD `-1.1522`
- `market_context_high->crypto_major_1h` score `1.4745` n `134` status `ready` deltaP `13.4239` edge `0.1528` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1337` n `43` status `ready` deltaP `20.2966` edge `0.0061` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0744` n `134` status `ready` deltaP `9.3999` edge `0.1456` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.7065` n `134` status `ready` deltaP `12.9687` edge `0.055` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
