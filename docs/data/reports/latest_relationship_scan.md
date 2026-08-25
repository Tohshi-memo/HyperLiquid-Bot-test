# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T17:52:26.247627+00:00`
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

- `news_risk_high->unknown_24h` score `44.398` n `51` status `ready` deltaP `5.5556` edge `3.6628` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.546` n `53` status `ready` deltaP `24.0652` edge `0.895` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `8.0356` n `51` status `ready` deltaP `31.3828` edge `0.5535` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.1775` n `51` status `ready` deltaP `41.6564` edge `0.0856` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1742` n `53` status `ready` deltaP `16.162` edge `0.1923` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.038` n `53` status `ready` deltaP `36.0303` edge `0.0264` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.5874` n `133` status `ready` deltaP `22.2068` edge `0.1084` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.7277` n `53` status `ready` deltaP `20.1939` edge `0.0864` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.2004` n `53` status `ready` deltaP `16.5179` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.4933` n `53` status `ready` deltaP `14.1227` edge `0.0055` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3697` n `53` status `ready` deltaP `10.2277` edge `-0.0061` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.256` n `53` status `ready` deltaP `8.1857` edge `0.0065` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.1566` n `133` status `ready` deltaP `11.7216` edge `-0.0202` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.048` n `53` status `ready` deltaP `4.299` edge `0.0005` maxDD `-0.1583`
- `news_risk_high->metal_24h` score `-0.0673` n `51` status `ready` deltaP `24.9489` edge `-0.1677` maxDD `-0.0053`
- `news_risk_high->crypto_alt_24h` score `-0.2065` n `51` status `ready` deltaP `22.0486` edge `-0.1642` maxDD `0.0`
- `market_context_high->fx_1h` score `-0.4109` n `133` status `ready` deltaP `3.0976` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.4546` n `53` status `ready` deltaP `-0.6129` edge `-0.0112` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.5294` n `53` status `ready` deltaP `4.8147` edge `-0.0231` maxDD `-0.249`
- `market_context_high->metal_4h` score `-1.0298` n `133` status `ready` deltaP `3.8075` edge `-0.0475` maxDD `-2.4293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
