# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T17:32:28.395110+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `145.2703` n `125` status `ready` deltaP `-23.939` edge `12.5567` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.8771` n `32` status `ready` deltaP `-35.664` edge `4.656` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.8771` n `32` status `ready` deltaP `-35.664` edge `4.656` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.9851` n `36` status `ready` deltaP `26.6609` edge `0.9423` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.7725` n `36` status `ready` deltaP `40.3963` edge `0.3784` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.7736` n `125` status `ready` deltaP `33.8218` edge `0.2614` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.2665` n `32` status `ready` deltaP `36.2218` edge `0.1974` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.2665` n `32` status `ready` deltaP `36.2218` edge `0.1974` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.1683` n `32` status `ready` deltaP `27.8542` edge `0.4643` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.1683` n `32` status `ready` deltaP `27.8542` edge `0.4643` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.6883` n `36` status `ready` deltaP `30.8492` edge `0.1017` maxDD `0.0`
- `risk_on_high->commodity_4h` score `3.0107` n `32` status `ready` deltaP `21.875` edge `0.1233` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.0107` n `32` status `ready` deltaP `21.875` edge `0.1233` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.0131` n `125` status `ready` deltaP `19.75` edge `0.0832` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.9266` n `36` status `ready` deltaP `22.2053` edge `0.0257` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7957` n `36` status `ready` deltaP `8.8823` edge `0.1223` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3988` n `32` status `ready` deltaP `15.0075` edge `0.0398` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3988` n `32` status `ready` deltaP `15.0075` edge `0.0398` maxDD `-0.1957`
- `risk_on_high->equity_24h` score `0.7942` n `32` status `ready` deltaP `15.2026` edge `0.1784` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `0.7942` n `32` status `ready` deltaP `15.2026` edge `0.1784` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
