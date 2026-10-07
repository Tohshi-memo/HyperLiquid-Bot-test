# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T11:52:27.814003+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8718`

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

- `market_context_high->unknown_4h` score `36.8007` n `91` status `ready` deltaP `-5.5782` edge `3.1578` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.5367` n `62` status `ready` deltaP `36.4477` edge `0.6554` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.279` n `62` status `ready` deltaP `23.8494` edge `0.582` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.6929` n `62` status `ready` deltaP `26.7361` edge `0.1295` maxDD `0.0`
- `news_risk_high->equity_24h` score `2.9962` n `62` status `ready` deltaP `7.6109` edge `0.2089` maxDD `-0.1298`
- `news_risk_high->index_4h` score `2.9683` n `62` status `ready` deltaP `33.0695` edge `0.0531` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.3269` n `62` status `ready` deltaP `9.1269` edge `0.1686` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.1749` n `62` status `ready` deltaP `18.9959` edge `0.1144` maxDD `-2.7837`
- `news_risk_high->index_1h` score `2.0103` n `62` status `ready` deltaP `25.3236` edge `0.0137` maxDD `-0.1997`
- `market_context_high->crypto_major_4h` score `1.9296` n `91` status `ready` deltaP `13.743` edge `0.1656` maxDD `-4.047`
- `news_risk_high->metal_4h` score `1.4507` n `62` status `ready` deltaP `20.4858` edge `0.091` maxDD `-0.993`
- `market_context_high->crypto_major_24h` score `1.4138` n `91` status `ready` deltaP `5.3457` edge `0.443` maxDD `-16.7906`
- `news_risk_high->crypto_alt_1h` score `1.2126` n `62` status `ready` deltaP `3.6073` edge `0.1289` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7877` n `91` status `ready` deltaP `12.9845` edge `0.0033` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.71` n `91` status `ready` deltaP `17.9409` edge `0.0148` maxDD `-0.3528`
- `market_context_high->metal_24h` score `0.5899` n `91` status `ready` deltaP `18.0193` edge `0.104` maxDD `-3.5466`
- `news_risk_high->commodity_24h` score `0.2739` n `62` status `ready` deltaP `25.4593` edge `0.022` maxDD `-8.196`
- `news_risk_high->metal_1h` score `0.188` n `62` status `ready` deltaP `7.3498` edge `0.0085` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `0.0779` n `91` status `ready` deltaP `9.446` edge `0.0359` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `-0.0416` n `91` status `ready` deltaP `4.2953` edge `0.0055` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
