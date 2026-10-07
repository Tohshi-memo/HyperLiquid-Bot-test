# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T02:37:32.858403+00:00`
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

- `market_context_high->unknown_24h` score `1389.6964` n `117` status `ready` deltaP `11.3782` edge `115.7702` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `29.3177` n `117` status `ready` deltaP `-0.2058` edge `2.4984` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.5374` n `62` status `ready` deltaP `34.7709` edge `0.5833` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.7571` n `62` status `ready` deltaP `20.8006` edge `0.4755` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.0408` n `62` status `ready` deltaP `21.1806` edge `0.1122` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.7926` n `117` status `ready` deltaP `14.6303` edge `0.2316` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.6436` n `62` status `ready` deltaP `29.7158` edge `0.0484` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.1111` n `62` status `ready` deltaP `7.9293` edge `0.1586` maxDD `-1.5096`
- `news_risk_high->equity_24h` score `1.9314` n `62` status `ready` deltaP `3.2706` edge `0.1491` maxDD `-0.1298`
- `news_risk_high->index_1h` score `1.9265` n `62` status `ready` deltaP `24.4254` edge `0.0127` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.624` n `62` status `ready` deltaP `16.0996` edge `0.0878` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1977` n `62` status `ready` deltaP `17.2846` edge `0.0799` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `0.9749` n `62` status `ready` deltaP `29.6259` edge `0.0841` maxDD `-8.196`
- `news_risk_high->crypto_alt_1h` score `0.9631` n `62` status `ready` deltaP `2.8588` edge `0.1131` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.8618` n `117` status `ready` deltaP `19.1982` edge `0.0195` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.7396` n `117` status `ready` deltaP `12.6926` edge `0.0054` maxDD `-0.271`
- `market_context_high->crypto_major_24h` score `0.6893` n `117` status `ready` deltaP `6.5438` edge `0.3112` maxDD `-16.7906`
- `market_context_high->crypto_alt_4h` score `0.6323` n `117` status `ready` deltaP `-0.112` edge `0.2258` maxDD `-7.1222`
- `market_context_high->commodity_4h` score `0.5536` n `117` status `ready` deltaP `12.4857` edge `0.0329` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.3655` n `117` status `ready` deltaP `8.6123` edge `0.0127` maxDD `-0.5059`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
