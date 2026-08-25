# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T09:37:27.141108+00:00`
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

- `news_risk_high->unknown_24h` score `43.668` n `51` status `ready` deltaP `2.4306` edge `3.6228` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.9836` n `51` status `ready` deltaP `25.6307` edge `0.9157` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `10.1439` n `51` status `ready` deltaP `37.112` edge `0.691` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.7306` n `51` status `ready` deltaP `46.1703` edge `0.1016` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.0804` n `52` status `ready` deltaP `15.35` edge `0.1899` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0753` n `51` status `ready` deltaP `36.406` edge `0.027` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.6185` n `51` status `ready` deltaP `23.5743` edge `0.1381` maxDD `-2.164`
- `market_context_high->unknown_4h` score `1.9895` n `133` status `ready` deltaP `20.0727` edge `0.0728` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1629` n `52` status `ready` deltaP `16.064` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.733` n `52` status `ready` deltaP `16.5131` edge `0.0203` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.501` n `51` status `ready` deltaP `10.3479` edge `0.0125` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.2188` n `52` status `ready` deltaP `8.7172` edge `-0.0086` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.0354` n `52` status `ready` deltaP `5.7232` edge `0.0017` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `0.0055` n `133` status `ready` deltaP `11.2725` edge `-0.0298` maxDD `-1.5916`
- `news_risk_high->metal_4h` score `-0.2593` n `51` status `ready` deltaP `6.3008` edge `-0.0105` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.3882` n `52` status `ready` deltaP `-0.1727` edge `-0.0086` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.5067` n `133` status `ready` deltaP `1.3012` edge `-0.0004` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.6471` n `133` status `ready` deltaP `6.5514` edge `-0.0339` maxDD `-2.4293`
- `news_risk_high->metal_24h` score `-0.6576` n `51` status `ready` deltaP `21.6503` edge `-0.1949` maxDD `-0.0053`
- `market_context_high->index_1h` score `-1.182` n `133` status `ready` deltaP `-5.7719` edge `-0.0062` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
