# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T08:37:27.777426+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10712`

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

- `market_context_high->commodity_4h` score `1.1166` n `169` status `ready` deltaP `13.6067` edge `0.0738` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.8373` n `136` status `ready` deltaP `18.9367` edge `0.0243` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7943` n `169` status `ready` deltaP `10.619` edge `0.0297` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.0931` n `169` status `ready` deltaP `8.7055` edge `0.0097` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1241` n `169` status `ready` deltaP `4.2669` edge `0.0008` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.6099` n `136` status `ready` deltaP `1.6528` edge `0.0913` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.829` n `169` status `ready` deltaP `-2.8762` edge `-0.0022` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.8296` n `169` status `ready` deltaP `-4.9578` edge `-0.0097` maxDD `-2.0884`
- `market_context_high->index_4h` score `-1.0946` n `169` status `ready` deltaP `-0.7295` edge `-0.0081` maxDD `-1.26`
- `market_context_high->metal_24h` score `-1.2462` n `136` status `ready` deltaP `-2.7742` edge `0.0428` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-1.2663` n `169` status `ready` deltaP `-2.2056` edge `-0.0038` maxDD `-4.6286`
- `market_context_high->equity_24h` score `-1.282` n `136` status `ready` deltaP `-0.7366` edge `0.2124` maxDD `-21.1456`
- `market_context_high->crypto_alt_1h` score `-1.5762` n `169` status `ready` deltaP `-9.1282` edge `-0.0391` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.916` n `169` status `ready` deltaP `-5.7524` edge `-0.0309` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.0793` n `169` status `ready` deltaP `-10.4005` edge `-0.1129` maxDD `-8.0039`
- `market_context_high->crypto_major_1h` score `-3.6414` n `169` status `ready` deltaP `-10.5401` edge `-0.0598` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.9258` n `169` status `ready` deltaP `-11.7533` edge `-0.1492` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.4423` n `136` status `ready` deltaP `-11.9075` edge `-0.1465` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.7879` n `136` status `ready` deltaP `-2.8902` edge `-0.1303` maxDD `-14.2873`
- `market_context_high->commodity_24h` score `-8.569` n `136` status `ready` deltaP `-5.3752` edge `-0.1912` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
