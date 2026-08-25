# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T16:52:50.045357+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14776`

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

- `news_risk_high->unknown_24h` score `44.2417` n `51` status `ready` deltaP `4.8611` edge `3.6544` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.5448` n `53` status `ready` deltaP `24.0652` edge `0.8949` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `8.27` n `51` status `ready` deltaP `32.0772` edge `0.5684` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.2511` n `51` status `ready` deltaP `42.3509` edge `0.0871` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1502` n `53` status `ready` deltaP `16.0123` edge `0.1913` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `2.988` n `53` status `ready` deltaP `35.4205` edge `0.0263` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.5862` n `133` status `ready` deltaP `22.2068` edge `0.1083` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.8209` n `53` status `ready` deltaP `20.8036` edge `0.0901` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1872` n `53` status `ready` deltaP `16.3682` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.4956` n `53` status `ready` deltaP `14.1227` edge `0.0058` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3697` n `53` status `ready` deltaP `10.2277` edge `-0.0061` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.256` n `53` status `ready` deltaP `8.1857` edge `0.0065` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.1326` n `133` status `ready` deltaP `11.5719` edge `-0.0212` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.048` n `53` status `ready` deltaP `4.299` edge `0.0005` maxDD `-0.1583`
- `news_risk_high->metal_24h` score `-0.1797` n `51` status `ready` deltaP `24.4281` edge `-0.1736` maxDD `-0.0053`
- `market_context_high->fx_1h` score `-0.4195` n `133` status `ready` deltaP `2.9479` edge `-0.0002` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.4403` n `53` status `ready` deltaP `-0.4632` edge `-0.011` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.4482` n `53` status `ready` deltaP `5.4245` edge `-0.0204` maxDD `-0.249`
- `news_risk_high->crypto_alt_24h` score `-0.5201` n `51` status `ready` deltaP `21.3542` edge `-0.1857` maxDD `0.0`
- `market_context_high->metal_4h` score `-0.9486` n `133` status `ready` deltaP `4.4173` edge `-0.0448` maxDD `-2.4293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
