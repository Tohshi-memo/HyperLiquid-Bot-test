# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T21:07:41.477019+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8706`

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

- `market_context_high->unknown_24h` score `1494.6244` n `117` status `ready` deltaP `11.3782` edge `124.5142` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `28.3295` n `117` status `ready` deltaP `-0.6632` edge `2.4191` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.278` n `62` status `ready` deltaP `33.7038` edge `0.5688` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.4198` n `62` status `ready` deltaP `19.7335` edge `0.4545` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.1398` n `62` status `ready` deltaP `22.2222` edge `0.1135` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6436` n `62` status `ready` deltaP `29.7158` edge `0.0484` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.5332` n `117` status `ready` deltaP `13.5632` edge `0.2171` maxDD `-4.047`
- `news_risk_high->equity_24h` score `2.4917` n `62` status `ready` deltaP `6.5692` edge `0.1738` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `1.9096` n `62` status `ready` deltaP `7.1808` edge `0.1468` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8738` n `62` status `ready` deltaP `23.8266` edge `0.0123` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6194` n `62` status `ready` deltaP `16.252` edge `0.0864` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.208` n `62` status `ready` deltaP `17.437` edge `0.0802` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `1.0209` n `62` status `ready` deltaP `29.6259` edge `0.09` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.9056` n `117` status `ready` deltaP `19.6555` edge `0.0201` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.7663` n `62` status `ready` deltaP `2.8588` edge `0.0967` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7264` n `117` status `ready` deltaP `12.5429` edge `0.0053` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.615` n `117` status `ready` deltaP `12.6381` edge `0.037` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.3715` n `117` status `ready` deltaP `8.6123` edge `0.0132` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.2949` n `117` status `ready` deltaP `-1.1791` edge `0.2048` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0193` n `62` status `ready` deltaP `5.254` edge `0.0052` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
