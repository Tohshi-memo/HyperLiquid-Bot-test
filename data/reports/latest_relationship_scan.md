# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T16:07:29.810786+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2298`

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

- `market_context_high->unknown_24h` score `1365.1764` n `98` status `ready` deltaP `2.4306` edge `113.7485` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.1652` n `98` status `ready` deltaP `40.2884` edge `1.8745` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.4964` n `98` status `ready` deltaP `26.3499` edge `1.6388` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.25` n `98` status `ready` deltaP `2.7771` edge `0.0096` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.5149` n `98` status `ready` deltaP `15.3557` edge `0.1772` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.5342` n `98` status `ready` deltaP `11.9245` edge `0.0067` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.5553` n `98` status `ready` deltaP `1.487` edge `0.1999` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9235` n `98` status `ready` deltaP `-2.9238` edge `-0.0002` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-1.0747` n `98` status `ready` deltaP `-1.9257` edge `0.2333` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.1417` n `98` status `ready` deltaP `-1.5092` edge `0.014` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3568` n `98` status `ready` deltaP `-8.5971` edge `-0.0011` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-2.0481` n `98` status `ready` deltaP `-0.4888` edge `0.0193` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.5136` n `98` status `ready` deltaP `-8.5397` edge `-0.0182` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.8312` n `98` status `ready` deltaP `-15.0739` edge `-0.0307` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-2.9896` n `98` status `ready` deltaP `1.0082` edge `-0.0381` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.5608` n `98` status `ready` deltaP `-24.8445` edge `-0.0102` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7768` n `98` status `ready` deltaP `-18.8138` edge `-0.0084` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.2119` n `98` status `ready` deltaP `-22.5329` edge `-0.1047` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.7686` n `98` status `ready` deltaP `-13.1236` edge `-0.101` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-11.9519` n `98` status `ready` deltaP `-13.9715` edge `-0.2208` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
