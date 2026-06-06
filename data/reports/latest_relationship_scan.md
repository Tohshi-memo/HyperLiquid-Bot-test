# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T07:52:24.970236+00:00`
- Price records: `672`
- Market context records: `3052`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6969`

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

- `market_context_high->crypto_alt_24h` score `25.5767` n `99` status `ready` deltaP `14.1098` edge `2.429` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `13.5246` n `99` status `ready` deltaP `44.8075` edge `0.8524` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.5035` n `99` status `ready` deltaP `24.6686` edge `1.0073` maxDD `-1.7175`
- `market_context_high->equity_24h` score `10.093` n `99` status `ready` deltaP `25.2841` edge `1.4006` maxDD `-18.3486`
- `market_context_high->index_24h` score `9.5524` n `99` status `ready` deltaP `23.8321` edge `0.7627` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.6537` n `130` status `ready` deltaP `18.0535` edge `0.1655` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.1661` n `136` status `ready` deltaP `1.0083` edge `0.0217` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.4494` n `130` status `ready` deltaP `2.0379` edge `0.0543` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.5444` n `136` status `ready` deltaP `2.9676` edge `0.0167` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.5444` n `136` status `ready` deltaP `-4.8345` edge `-0.0003` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.5676` n `136` status `ready` deltaP `6.0585` edge `0.0998` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.8063` n `136` status `ready` deltaP `2.4789` edge `0.0255` maxDD `-8.6319`
- `market_context_high->unknown_1h` score `-0.9073` n `136` status `ready` deltaP `4.6319` edge `-0.0334` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.9161` n `136` status `ready` deltaP `4.6407` edge `0.0779` maxDD `-15.1032`
- `market_context_high->index_4h` score `-1.0646` n `130` status `ready` deltaP `11.8082` edge `0.0608` maxDD `-17.0804`
- `market_context_high->fx_4h` score `-1.0717` n `130` status `ready` deltaP `-7.561` edge `-0.0035` maxDD `-1.0127`
- `market_context_high->metal_1h` score `-1.1442` n `136` status `ready` deltaP `-1.2417` edge `-0.0016` maxDD `-7.278`
- `market_context_high->fx_24h` score `-1.1735` n `99` status `ready` deltaP `0.2841` edge `-0.0125` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-3.032` n `130` status `ready` deltaP `9.5357` edge `0.0502` maxDD `-34.8653`
- `market_context_high->crypto_alt_4h` score `-3.116` n `130` status `ready` deltaP `18.5085` edge `0.2816` maxDD `-58.6918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
