# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T02:22:42.522301+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4173`

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

- `market_context_high->unknown_24h` score `1489.8918` n `98` status `ready` deltaP `3.4722` edge `124.1345` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.3905` n `98` status `ready` deltaP `46.0176` edge `1.9934` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.28` n `98` status `ready` deltaP `31.3847` edge `1.8339` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.4415` n `98` status `ready` deltaP `-0.0672` edge `0.004` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.8357` n `98` status `ready` deltaP `-0.7996` edge `0.1792` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.8929` n `98` status `ready` deltaP `15.3557` edge `0.1457` maxDD `-15.7982`
- `market_context_high->index_1h` score `-1.0107` n `98` status `ready` deltaP `-4.4208` edge `-0.0014` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-1.1778` n `98` status `ready` deltaP `6.894` edge `-0.0134` maxDD `-6.1238`
- `market_context_high->crypto_alt_1h` score `-1.183` n `98` status `ready` deltaP `-1.8086` edge `0.0107` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3053` n `98` status `ready` deltaP `-7.9983` edge `-0.0008` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.571` n `98` status `ready` deltaP `-4.0599` edge `0.1839` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.2878` n `98` status `ready` deltaP `-2.1355` edge `0.0103` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.8559` n `98` status `ready` deltaP `-11.5885` edge `-0.0264` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9798` n `98` status `ready` deltaP `-16.2715` edge `-0.0351` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.3763` n `98` status `ready` deltaP `-0.6385` edge `-0.0585` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.612` n `98` status `ready` deltaP `-25.4542` edge `-0.0104` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.754` n `98` status `ready` deltaP `-18.8138` edge `-0.0065` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.7527` n `98` status `ready` deltaP `-26.9537` edge `-0.1203` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.4622` n `98` status `ready` deltaP `-9.9986` edge `-0.0963` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.6388` n `98` status `ready` deltaP `-18.5447` edge `-0.3275` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
