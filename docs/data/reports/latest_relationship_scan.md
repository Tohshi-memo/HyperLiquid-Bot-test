# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T12:37:28.293948+00:00`
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

- `market_context_high->unknown_4h` score `36.0112` n `90` status `ready` deltaP `-5.8468` edge `3.0938` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.5775` n `62` status `ready` deltaP `36.4477` edge `0.6588` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.3486` n `62` status `ready` deltaP `23.8494` edge `0.5878` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.7706` n `62` status `ready` deltaP `27.2569` edge `0.1325` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.1771` n `62` status `ready` deltaP `8.1317` edge `0.2205` maxDD `-0.1298`
- `news_risk_high->index_4h` score `3.0217` n `62` status `ready` deltaP `33.5268` edge `0.0545` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.3605` n `62` status `ready` deltaP `9.4263` edge `0.1694` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.2557` n `62` status `ready` deltaP `19.3008` edge `0.1191` maxDD `-2.7837`
- `market_context_high->crypto_major_4h` score `2.0727` n `90` status `ready` deltaP `14.5122` edge `0.1724` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.0103` n `62` status `ready` deltaP `25.3236` edge `0.0137` maxDD `-0.1997`
- `market_context_high->crypto_major_24h` score `1.661` n `90` status `ready` deltaP `6.2152` edge `0.4689` maxDD `-16.7906`
- `news_risk_high->metal_4h` score `1.457` n `62` status `ready` deltaP `20.4858` edge `0.0918` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.2054` n `62` status `ready` deltaP `3.4576` edge `0.1293` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7897` n `90` status `ready` deltaP `12.994` edge `0.0034` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.7774` n `90` status `ready` deltaP `18.6246` edge `0.0153` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.676` n `90` status `ready` deltaP `18.7152` edge `0.1104` maxDD `-3.5466`
- `news_risk_high->commodity_24h` score `0.1789` n `62` status `ready` deltaP `24.9384` edge `0.0133` maxDD `-8.196`
- `news_risk_high->metal_1h` score `0.1784` n `62` status `ready` deltaP `7.2001` edge `0.0087` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `0.0692` n `90` status `ready` deltaP `9.3546` edge `0.0354` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `-0.0419` n `90` status `ready` deltaP `4.2315` edge `0.0059` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
