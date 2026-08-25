# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T17:22:24.115199+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `44.3235` n `51` status `ready` deltaP `5.2083` edge `3.6589` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.5484` n `53` status `ready` deltaP `24.0652` edge `0.8952` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `8.1546` n `51` status `ready` deltaP `31.73` edge `0.5611` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.2149` n `51` status `ready` deltaP `42.0037` edge `0.0864` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.155` n `53` status `ready` deltaP `16.0123` edge `0.1917` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0136` n `53` status `ready` deltaP `35.7254` edge `0.0264` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.5898` n `133` status `ready` deltaP `22.2068` edge `0.1086` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.7653` n `53` status `ready` deltaP `20.4987` edge `0.0875` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.2004` n `53` status `ready` deltaP `16.5179` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.4909` n `53` status `ready` deltaP `14.1227` edge `0.0052` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3565` n `53` status `ready` deltaP `10.078` edge `-0.0062` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.2548` n `53` status `ready` deltaP `8.1857` edge `0.0064` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.1374` n `133` status `ready` deltaP `11.5719` edge `-0.0208` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.0488` n `53` status `ready` deltaP `4.299` edge `0.0004` maxDD `-0.1583`
- `news_risk_high->metal_24h` score `-0.1148` n `51` status `ready` deltaP `24.7753` edge `-0.1705` maxDD `-0.0053`
- `news_risk_high->crypto_alt_24h` score `-0.3495` n `51` status `ready` deltaP `21.7014` edge `-0.1738` maxDD `0.0`
- `market_context_high->fx_1h` score `-0.4109` n `133` status `ready` deltaP `3.0976` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.4546` n `53` status `ready` deltaP `-0.6129` edge `-0.0112` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.4894` n `53` status `ready` deltaP `5.1196` edge `-0.0218` maxDD `-0.249`
- `market_context_high->metal_4h` score `-0.9898` n `133` status `ready` deltaP `4.1124` edge `-0.0462` maxDD `-2.4293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
