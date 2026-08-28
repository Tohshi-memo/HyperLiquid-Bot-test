# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T07:37:27.136444+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11607`

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

- `news_risk_high->unknown_24h` score `53.0377` n `50` status `ready` deltaP `11.6118` edge `4.3424` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `29.0024` n `50` status `ready` deltaP `37.7678` edge `2.2092` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.7454` n `50` status `ready` deltaP `25.5068` edge `0.902` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.3455` n `50` status `ready` deltaP `30.1005` edge `0.3376` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `5.3337` n `50` status `ready` deltaP `49.1265` edge `0.1212` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9207` n `50` status `ready` deltaP `45.7291` edge `0.0309` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.4397` n `129` status `ready` deltaP `5.4102` edge `0.3238` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.9264` n `50` status `ready` deltaP `16.2275` edge `0.1713` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.595` n `50` status `ready` deltaP `29.0745` edge `0.0375` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.3023` n `148` status `ready` deltaP `18.669` edge `0.1081` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.6533` n `50` status `ready` deltaP `22.0` edge `0.0081` maxDD `-0.0257`
- `news_risk_high->equity_4h` score `1.6478` n `50` status `ready` deltaP `22.8798` edge `0.0611` maxDD `-2.105`
- `news_risk_high->equity_1h` score `1.4771` n `50` status `ready` deltaP `19.0599` edge `0.0239` maxDD `-0.2301`
- `news_risk_high->crypto_major_24h` score `1.1924` n `50` status `ready` deltaP `17.9688` edge `0.0289` maxDD `-2.6128`
- `market_context_high->unknown_1h` score `0.803` n `148` status `ready` deltaP `8.5248` edge `0.0551` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5533` n `50` status `ready` deltaP `14.8982` edge `0.0029` maxDD `-0.5024`
- `news_risk_high->metal_4h` score `0.3227` n `50` status `ready` deltaP `11.2055` edge `0.0053` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.1989` n `50` status `ready` deltaP `8.7066` edge `0.0014` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1544` n `50` status `ready` deltaP `6.4491` edge `-0.0006` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.0861` n `50` status `ready` deltaP `6.8584` edge `0.0011` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
