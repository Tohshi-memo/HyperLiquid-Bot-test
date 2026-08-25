# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T09:22:29.007474+00:00`
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

- `news_risk_high->unknown_24h` score `43.6728` n `51` status `ready` deltaP `2.4306` edge `3.6232` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.9654` n `51` status `ready` deltaP `25.4782` edge `0.9152` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `10.1974` n `51` status `ready` deltaP `37.2856` edge `0.6943` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.7493` n `51` status `ready` deltaP `46.3439` edge `0.102` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.0765` n `51` status `ready` deltaP `36.406` edge `0.0271` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `3.0612` n `52` status `ready` deltaP `15.2003` edge `0.1893` maxDD `-0.8426`
- `news_risk_high->equity_4h` score `2.6257` n `51` status `ready` deltaP `23.5743` edge `0.1387` maxDD `-2.164`
- `market_context_high->unknown_4h` score `1.9713` n `133` status `ready` deltaP `19.9202` edge `0.0723` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1748` n `52` status `ready` deltaP `16.2137` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.7447` n `52` status `ready` deltaP `16.6628` edge `0.0208` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.5022` n `51` status `ready` deltaP `10.3479` edge `0.0126` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.214` n `52` status `ready` deltaP `8.7172` edge `-0.009` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.044` n `52` status `ready` deltaP `5.8729` edge `0.0018` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `-0.0137` n `133` status `ready` deltaP `11.1228` edge `-0.0304` maxDD `-1.5916`
- `news_risk_high->metal_4h` score `-0.2739` n `51` status `ready` deltaP `6.1484` edge `-0.0107` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.3894` n `52` status `ready` deltaP `-0.1727` edge `-0.0087` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4989` n `133` status `ready` deltaP `1.4509` edge `-0.0004` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.6516` n `51` status `ready` deltaP `21.6503` edge `-0.1944` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.6617` n `133` status `ready` deltaP `6.399` edge `-0.0341` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.1688` n `133` status `ready` deltaP `-5.6222` edge `-0.0061` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
