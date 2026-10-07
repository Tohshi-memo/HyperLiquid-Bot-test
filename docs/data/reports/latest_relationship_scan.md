# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T03:37:29.611058+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

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

- `market_context_high->unknown_24h` score `1382.4244` n `117` status `ready` deltaP `11.3782` edge `115.1642` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `29.4725` n `117` status `ready` deltaP `-0.2058` edge `2.5113` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.6876` n `62` status `ready` deltaP `34.9233` edge `0.5948` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.9855` n `62` status `ready` deltaP `21.1055` edge `0.4925` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.0734` n `62` status `ready` deltaP `21.5278` edge `0.1126` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.9428` n `117` status `ready` deltaP `14.7827` edge `0.2431` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.6728` n `62` status `ready` deltaP `30.0207` edge `0.0488` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.1327` n `62` status `ready` deltaP `7.9293` edge `0.1604` maxDD `-1.5096`
- `news_risk_high->equity_24h` score `1.9091` n `62` status `ready` deltaP `3.097` edge `0.1484` maxDD `-0.1298`
- `news_risk_high->index_1h` score `1.9001` n `62` status `ready` deltaP `24.126` edge `0.0125` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6516` n `62` status `ready` deltaP `16.0996` edge `0.0901` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.2221` n `62` status `ready` deltaP `17.5895` edge `0.081` maxDD `-0.993`
- `market_context_high->crypto_major_24h` score `1.0005` n `117` status `ready` deltaP `7.2383` edge `0.3325` maxDD `-16.7906`
- `news_risk_high->crypto_alt_1h` score `0.9871` n `62` status `ready` deltaP `2.8588` edge `0.1151` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.9151` n `62` status `ready` deltaP `29.1051` edge `0.0799` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.874` n `117` status `ready` deltaP `19.3507` edge `0.0195` maxDD `-0.3868`
- `market_context_high->crypto_alt_4h` score `0.8607` n `117` status `ready` deltaP `0.1929` edge `0.2428` maxDD `-7.1222`
- `market_context_high->fx_1h` score `0.724` n `117` status `ready` deltaP `12.5429` edge `0.0051` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.5282` n `117` status `ready` deltaP `12.3333` edge `0.0318` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.3379` n `117` status `ready` deltaP `8.3129` edge `0.0124` maxDD `-0.5059`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
