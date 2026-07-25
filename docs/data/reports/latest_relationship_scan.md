# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T17:37:25.538442+00:00`
- Price records: `672`
- Market context records: `7902`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14745`

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

- `market_context_high->equity_24h` score `15.2253` n `98` status `ready` deltaP `29.6343` edge `1.2054` maxDD `-6.0681`
- `market_context_high->metal_24h` score `6.3359` n `98` status `ready` deltaP `31.1976` edge `0.3563` maxDD `-0.2364`
- `market_context_high->equity_4h` score `5.7211` n `104` status `ready` deltaP `20.8716` edge `0.4269` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `1.9301` n `98` status `ready` deltaP `21.3435` edge `0.1769` maxDD `-7.0012`
- `market_context_high->index_4h` score `1.8763` n `104` status `ready` deltaP `20.8716` edge `0.0657` maxDD `-0.8791`
- `market_context_high->metal_4h` score `1.7287` n `104` status `ready` deltaP `15.8889` edge `0.1087` maxDD `-0.979`
- `market_context_high->crypto_alt_4h` score `1.7025` n `104` status `ready` deltaP `12.8987` edge `0.1676` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.5408` n `104` status `ready` deltaP `14.7162` edge `0.2021` maxDD `-6.7444`
- `market_context_high->equity_1h` score `1.5136` n `107` status `ready` deltaP `13.1683` edge `0.1201` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.2752` n `98` status `ready` deltaP `33.638` edge `0.048` maxDD `-3.0343`
- `market_context_high->crypto_major_1h` score `1.2583` n `107` status `ready` deltaP `14.3727` edge `0.0499` maxDD `-1.6021`
- `market_context_high->index_24h` score `1.0176` n `98` status `ready` deltaP `5.0985` edge `0.1345` maxDD `-1.3621`
- `market_context_high->index_1h` score `0.6789` n `107` status `ready` deltaP `11.9825` edge `0.0197` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.4501` n `107` status `ready` deltaP `5.8887` edge `0.0415` maxDD `-1.4603`
- `market_context_high->metal_1h` score `0.3357` n `107` status `ready` deltaP `6.002` edge `0.0258` maxDD `-0.6936`
- `market_context_high->commodity_4h` score `-0.1561` n `104` status `ready` deltaP `6.1221` edge `0.0206` maxDD `-2.2874`
- `market_context_high->fx_1h` score `-0.2108` n `107` status `ready` deltaP `1.3345` edge `0.0008` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.3071` n `104` status `ready` deltaP `4.4548` edge `0.0057` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.4186` n `107` status `ready` deltaP `2.7715` edge `0.0035` maxDD `-1.5486`
- `market_context_high->unknown_1h` score `-1.4695` n `107` status `ready` deltaP `6.1111` edge `-0.1868` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
