# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T01:52:24.380819+00:00`
- Price records: `672`
- Market context records: `3027`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6987`

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

- `market_context_high->crypto_alt_24h` score `22.2286` n `99` status `ready` deltaP `10.464` edge `2.1743` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `12.7282` n `99` status `ready` deltaP `22.238` edge `0.9589` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `12.6497` n `99` status `ready` deltaP `42.3769` edge `0.7957` maxDD `-1.2589`
- `market_context_high->equity_24h` score `7.3858` n `99` status `ready` deltaP `21.1175` edge `1.0813` maxDD `-18.3486`
- `market_context_high->index_24h` score `7.2156` n `99` status `ready` deltaP `20.7071` edge `0.5888` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.6917` n `117` status `ready` deltaP `19.0236` edge `0.1622` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.2222` n `117` status `ready` deltaP `13.373` edge `0.1568` maxDD `-15.0636`
- `market_context_high->index_4h` score `0.1746` n `117` status `ready` deltaP `16.3892` edge `0.1029` maxDD `-10.8483`
- `market_context_high->crypto_alt_4h` score `0.1573` n `117` status `ready` deltaP `23.0639` edge `0.4212` maxDD `-38.7172`
- `market_context_high->commodity_1h` score `0.0553` n `129` status `ready` deltaP `2.5902` edge `0.0296` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4279` n `129` status `ready` deltaP `3.7878` edge `0.0213` maxDD `-4.1126`
- `market_context_high->equity_1h` score `-0.5323` n `129` status `ready` deltaP `3.4188` edge `0.0305` maxDD `-6.7232`
- `market_context_high->fx_1h` score `-0.5571` n `129` status `ready` deltaP `-5.1885` edge `0.0` maxDD `-0.2801`
- `market_context_high->crypto_alt_1h` score `-0.6114` n `129` status `ready` deltaP `6.0867` edge `0.094` maxDD `-14.7034`
- `market_context_high->unknown_4h` score `-0.7246` n `117` status `ready` deltaP `0.1877` edge `0.0437` maxDD `-3.7602`
- `market_context_high->unknown_1h` score `-0.7925` n `129` status `ready` deltaP `4.0709` edge `-0.0201` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-1.0293` n `129` status `ready` deltaP `4.1301` edge `0.0668` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-1.1661` n `129` status `ready` deltaP `-2.0981` edge `-0.0037` maxDD `-6.8783`
- `market_context_high->fx_4h` score `-1.5238` n `117` status `ready` deltaP `-7.0201` edge `-0.0012` maxDD `-0.6521`
- `market_context_high->fx_24h` score `-1.6329` n `99` status `ready` deltaP `-3.8825` edge `-0.023` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
