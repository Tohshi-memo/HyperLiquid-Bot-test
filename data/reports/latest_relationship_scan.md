# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T21:37:40.989990+00:00`
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

- `market_context_high->unknown_24h` score `1459.3888` n `117` status `ready` deltaP `11.3782` edge `121.5779` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `28.3751` n `117` status `ready` deltaP `-0.6632` edge `2.4229` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.2938` n `62` status `ready` deltaP `33.8562` edge `0.5691` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.4138` n `62` status `ready` deltaP `19.7335` edge `0.454` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.1549` n `62` status `ready` deltaP `22.3958` edge `0.1136` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6716` n `62` status `ready` deltaP `30.0207` edge `0.0487` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.549` n `117` status `ready` deltaP `13.7156` edge `0.2174` maxDD `-4.047`
- `news_risk_high->equity_24h` score `2.4411` n `62` status `ready` deltaP `6.222` edge `0.1719` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `1.93` n `62` status `ready` deltaP `7.3305` edge `0.1475` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8738` n `62` status `ready` deltaP `23.8266` edge `0.0123` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.657` n `62` status `ready` deltaP `16.5569` edge `0.0875` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.2087` n `62` status `ready` deltaP `17.437` edge `0.0803` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `1.0209` n `62` status `ready` deltaP `29.6259` edge `0.09` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8934` n `117` status `ready` deltaP `19.5031` edge `0.0201` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.7795` n `62` status `ready` deltaP `2.8588` edge `0.0978` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7264` n `117` status `ready` deltaP `12.5429` edge `0.0053` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.6054` n `117` status `ready` deltaP `12.6381` edge `0.0362` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.3703` n `117` status `ready` deltaP `8.6123` edge `0.0131` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.2889` n `117` status `ready` deltaP `-1.1791` edge `0.2043` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0181` n `62` status `ready` deltaP `5.254` edge `0.0053` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
