# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T18:22:28.953880+00:00`
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

- `market_context_high->unknown_24h` score `1365.9004` n `98` status `ready` deltaP `3.125` edge `113.8042` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.8109` n `98` status `ready` deltaP `39.9412` edge `1.8314` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.9961` n `98` status `ready` deltaP `25.3083` edge `1.5816` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2858` n `98` status `ready` deltaP `2.1783` edge `0.009` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.4749` n `98` status `ready` deltaP `1.6395` edge `0.2092` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.4813` n `98` status `ready` deltaP `15.3557` edge `0.18` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.5378` n `98` status `ready` deltaP `11.9245` edge `0.0064` maxDD `-6.1238`
- `market_context_high->crypto_major_4h` score `-0.8581` n `98` status `ready` deltaP `-1.316` edge `0.257` maxDD `-22.3259`
- `market_context_high->index_1h` score `-0.8775` n `98` status `ready` deltaP `-2.1753` edge `0.0007` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.0894` n `98` status `ready` deltaP `-1.2098` edge `0.0187` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3556` n `98` status `ready` deltaP `-8.5971` edge `-0.001` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.9378` n `98` status `ready` deltaP `-0.0397` edge `0.0255` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.3935` n `98` status `ready` deltaP `-7.4726` edge `-0.0153` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.8157` n `98` status `ready` deltaP `1.7567` edge `-0.0286` maxDD `-11.0868`
- `market_context_high->commodity_1h` score `-2.8168` n `98` status `ready` deltaP `-14.9242` edge `-0.0305` maxDD `-3.7125`
- `market_context_high->fx_4h` score `-4.4927` n `98` status `ready` deltaP `-24.0823` edge `-0.0096` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7612` n `98` status `ready` deltaP `-18.8138` edge `-0.0071` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.2191` n `98` status `ready` deltaP `-22.5329` edge `-0.1053` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.9037` n `98` status `ready` deltaP `-14.5125` edge `-0.103` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-11.5717` n `98` status `ready` deltaP `-13.2093` edge `-0.1942` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
