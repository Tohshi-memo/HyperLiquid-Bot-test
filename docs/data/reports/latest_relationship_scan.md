# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T19:52:57.841960+00:00`
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

- `market_context_high->unknown_24h` score `1508.7015` n `117` status `ready` deltaP `11.1819` edge `125.6886` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `28.7139` n `117` status `ready` deltaP `-0.3583` edge `2.4491` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.2308` n `62` status `ready` deltaP `33.3989` edge `0.5669` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.386` n `62` status `ready` deltaP `19.5811` edge `0.4527` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.1185` n `62` status `ready` deltaP `21.8966` edge `0.1139` maxDD `0.0`
- `news_risk_high->equity_24h` score `2.6158` n `62` status `ready` deltaP `7.3415` edge `0.179` maxDD `-0.1298`
- `news_risk_high->index_4h` score `2.5718` n `62` status `ready` deltaP `28.9536` edge `0.0475` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.486` n `117` status `ready` deltaP `13.2583` edge `0.2152` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `1.9708` n `62` status `ready` deltaP `7.6299` edge `0.1489` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8726` n `62` status `ready` deltaP `23.8266` edge `0.0122` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.5296` n `62` status `ready` deltaP `15.4898` edge `0.084` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.2048` n `62` status `ready` deltaP `17.437` edge `0.0798` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `0.9829` n `62` status `ready` deltaP `29.2548` edge `0.0876` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8812` n `117` status `ready` deltaP `19.3507` edge `0.0201` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.7939` n `62` status `ready` deltaP `3.0085` edge `0.098` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7024` n `117` status `ready` deltaP `12.2435` edge `0.0053` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.662` n `117` status `ready` deltaP `12.7906` edge `0.0399` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.441` n `117` status `ready` deltaP `9.3608` edge `0.014` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.2611` n `117` status `ready` deltaP `-1.3315` edge `0.203` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0851` n `62` status `ready` deltaP `4.5055` edge `0.0047` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
