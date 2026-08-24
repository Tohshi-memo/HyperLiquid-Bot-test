# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T07:52:30.265254+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `50.0907` n `51` status `ready` deltaP `17.0139` edge `4.0608` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.2879` n `51` status `ready` deltaP `40.237` edge `1.0155` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9681` n `51` status `ready` deltaP `23.8014` edge `0.9266` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.7484` n `51` status `ready` deltaP `48.9481` edge `0.1679` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.7728` n `51` status `ready` deltaP `27.2328` edge `0.2099` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6473` n `51` status `ready` deltaP `17.0834` edge `0.2205` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2236` n `51` status `ready` deltaP `37.9304` edge `0.0292` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.8772` n `145` status `ready` deltaP `20.245` edge `0.0579` maxDD `-0.5816`
- `news_risk_high->metal_24h` score `1.6881` n `51` status `ready` deltaP `33.9767` edge `-0.0816` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2302` n `51` status `ready` deltaP `16.8457` edge `0.0072` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9888` n `51` status `ready` deltaP `18.9415` edge `0.0369` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9727` n `51` status `ready` deltaP `14.1589` edge `0.0264` maxDD `-0.1788`
- `market_context_high->unknown_24h` score `0.4821` n `90` status `ready` deltaP `4.7917` edge `0.0589` maxDD `-1.0533`
- `news_risk_high->index_1h` score `0.2753` n `51` status `ready` deltaP `9.8714` edge `0.0048` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1919` n `51` status `ready` deltaP `8.5388` edge `-0.0101` maxDD `-0.4666`
- `news_risk_high->crypto_alt_24h` score `0.1021` n `51` status `ready` deltaP `23.6111` edge `-0.1489` maxDD `0.0`
- `news_risk_high->metal_1h` score `-0.1224` n `51` status `ready` deltaP `2.043` edge `-0.007` maxDD `-0.1184`
- `market_context_high->metal_4h` score `-0.1421` n `145` status `ready` deltaP `7.9825` edge `-0.015` maxDD `-1.3378`
- `news_risk_high->metal_4h` score `-0.1863` n `51` status `ready` deltaP `7.063` edge `-0.0095` maxDD `-0.249`
- `market_context_high->unknown_1h` score `-0.1921` n `146` status `ready` deltaP `9.388` edge `-0.0337` maxDD `-1.5916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
