# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T05:22:24.604977+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `news_risk_high->unknown_24h` score `52.8157` n `50` status `ready` deltaP `11.6118` edge `4.3239` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `27.6992` n `50` status `ready` deltaP `37.7678` edge `2.1006` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6171` n `50` status `ready` deltaP `24.5936` edge `0.8974` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `5.3872` n `50` status `ready` deltaP `49.2998` edge `0.1245` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `5.2854` n `50` status `ready` deltaP `29.7539` edge `0.3349` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.8758` n `50` status `ready` deltaP `45.2725` edge `0.0302` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.3914` n `128` status `ready` deltaP `5.3618` edge `0.3201` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.9592` n `50` status `ready` deltaP `16.1734` edge `0.1744` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.7239` n `50` status `ready` deltaP `30.461` edge `0.039` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.1741` n `148` status `ready` deltaP `17.7558` edge `0.1035` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5816` n `50` status `ready` deltaP `21.1779` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.4082` n `50` status `ready` deltaP `18.6936` edge `0.0206` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.3558` n `50` status `ready` deltaP `21.5099` edge `0.0459` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.8358` n `148` status `ready` deltaP `8.4707` edge `0.0582` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5035` n `50` status `ready` deltaP `14.0747` edge `0.002` maxDD `-0.5024`
- `news_risk_high->metal_4h` score `0.3167` n `50` status `ready` deltaP `11.2055` edge `0.0048` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.193` n `50` status `ready` deltaP `8.6368` edge `0.0011` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1614` n `50` status `ready` deltaP `6.3737` edge `0.0008` maxDD `-0.1413`
- `news_risk_high->crypto_major_24h` score `0.1412` n `50` status `ready` deltaP `17.9688` edge `-0.0587` maxDD `-2.6128`
- `market_context_high->metal_24h` score `-0.0011` n `128` status `ready` deltaP `13.7998` edge `0.0722` maxDD `-3.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
