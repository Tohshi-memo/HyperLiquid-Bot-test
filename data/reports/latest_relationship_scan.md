# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T15:52:31.944422+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `121.8207` n `134` status `ready` deltaP `-33.3799` edge `10.6655` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.8218` n `32` status `ready` deltaP `-45.8333` edge `4.5885` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.8218` n `32` status `ready` deltaP `-45.8333` edge `4.5885` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.8312` n `36` status `ready` deltaP `10.9375` edge `0.7843` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.3108` n `36` status `ready` deltaP `38.7195` edge `0.3511` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7558` n `32` status `ready` deltaP `32.1181` edge `0.1822` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7558` n `32` status `ready` deltaP `32.1181` edge `0.1822` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.0228` n `134` status `ready` deltaP `25.4017` edge `0.2089` maxDD `-1.4406`
- `risk_on_high->commodity_4h` score `2.8994` n `32` status `ready` deltaP `20.1982` edge `0.1252` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8994` n `32` status `ready` deltaP `20.1982` edge `0.1252` maxDD `-0.1258`
- `risk_on_high->crypto_major_24h` score `2.194` n `32` status `ready` deltaP `17.1875` edge `0.2823` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.194` n `32` status `ready` deltaP `17.1875` edge `0.2823` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.1418` n `36` status `ready` deltaP `14.7569` edge `0.0801` maxDD `0.0`
- `news_risk_high->equity_1h` score `1.7849` n `36` status `ready` deltaP `9.032` edge `0.1204` maxDD `-0.5496`
- `news_risk_high->index_4h` score `1.7285` n `36` status `ready` deltaP `20.2235` edge `0.0224` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.3474` n `134` status `ready` deltaP `15.2075` edge `0.0686` maxDD `-1.616`
- `risk_on_high->commodity_1h` score `1.2935` n `32` status `ready` deltaP `13.6602` edge `0.04` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2935` n `32` status `ready` deltaP `13.6602` edge `0.04` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.1568` n `32` status `ready` deltaP `13.7153` edge `0.0234` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1568` n `32` status `ready` deltaP `13.7153` edge `0.0234` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
