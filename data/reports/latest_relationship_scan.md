# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T20:22:22.357830+00:00`
- Price records: `672`
- Market context records: `3002`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `19.4072` n `98` status `ready` deltaP `7.0259` edge `1.9621` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.5092` n `98` status `ready` deltaP `42.6411` edge `0.7692` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `12.0403` n `98` status `ready` deltaP `19.2638` edge `0.9214` maxDD `-1.7175`
- `market_context_high->equity_24h` score `9.5763` n `98` status `ready` deltaP `17.9989` edge `0.8784` maxDD `-12.6963`
- `market_context_high->index_24h` score `5.9246` n `98` status `ready` deltaP `17.6092` edge `0.4744` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.2849` n `102` status `ready` deltaP `17.1479` edge `0.1408` maxDD `-2.8438`
- `market_context_high->index_4h` score `1.5009` n `102` status `ready` deltaP `19.1057` edge `0.1261` maxDD `-5.9381`
- `market_context_high->equity_4h` score `1.1218` n `102` status `ready` deltaP `14.3592` edge `0.1901` maxDD `-9.0276`
- `market_context_high->commodity_1h` score `-0.0796` n `107` status `ready` deltaP `0.6534` edge `0.0184` maxDD `-0.9706`
- `market_context_high->index_1h` score `-0.1675` n `107` status `ready` deltaP `4.9541` edge `0.0219` maxDD `-3.1118`
- `market_context_high->equity_1h` score `-0.2218` n `107` status `ready` deltaP `4.8002` edge `0.0415` maxDD `-5.1553`
- `market_context_high->crypto_alt_4h` score `-0.2629` n `102` status `ready` deltaP `22.6536` edge `0.3654` maxDD `-38.3432`
- `market_context_high->fx_1h` score `-0.4261` n `107` status `ready` deltaP `-2.7855` edge `0.0005` maxDD `-0.2577`
- `market_context_high->crypto_alt_1h` score `-0.9935` n `107` status `ready` deltaP `6.5239` edge `0.0421` maxDD `-14.7034`
- `market_context_high->fx_4h` score `-1.1149` n `102` status `ready` deltaP `-9.8039` edge `0.0003` maxDD `-0.5631`
- `market_context_high->metal_1h` score `-1.2701` n `107` status `ready` deltaP `-3.4165` edge `-0.0118` maxDD `-6.5935`
- `market_context_high->unknown_4h` score `-1.3789` n `102` status `ready` deltaP `-1.0013` edge `-0.0029` maxDD `-3.7602`
- `market_context_high->crypto_major_1h` score `-1.4673` n `107` status `ready` deltaP `3.9104` edge `0.0121` maxDD `-15.1032`
- `market_context_high->unknown_1h` score `-1.7154` n `107` status `ready` deltaP `1.0255` edge `-0.0767` maxDD `-3.1801`
- `market_context_high->fx_24h` score `-1.9244` n `98` status `ready` deltaP `-7.0011` edge `-0.0265` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
