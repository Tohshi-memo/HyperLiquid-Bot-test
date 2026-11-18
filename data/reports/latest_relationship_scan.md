# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T17:52:33.035292+00:00`
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

- `market_context_high->unknown_24h` score `1365.7557` n `98` status `ready` deltaP `2.9514` edge `113.7933` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.9104` n `98` status `ready` deltaP `40.1148` edge `1.843` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.1195` n `98` status `ready` deltaP `25.6555` edge `1.5951` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2764` n `98` status `ready` deltaP `2.328` edge `0.0092` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.4827` n `98` status `ready` deltaP `1.6395` edge `0.2082` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.4897` n `98` status `ready` deltaP `15.3557` edge `0.1793` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.5378` n `98` status `ready` deltaP `11.9245` edge `0.0064` maxDD `-6.1238`
- `market_context_high->crypto_major_4h` score `-0.8799` n `98` status `ready` deltaP `-1.316` edge `0.2542` maxDD `-22.3259`
- `market_context_high->index_1h` score `-0.8947` n `98` status `ready` deltaP `-2.4747` edge `0.0005` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.0941` n `98` status `ready` deltaP `-1.2098` edge `0.0181` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3424` n `98` status `ready` deltaP `-8.4474` edge `-0.0009` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.9402` n `98` status `ready` deltaP `-0.0397` edge `0.0253` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.3959` n `98` status `ready` deltaP `-7.4726` edge `-0.0155` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.7809` n `98` status `ready` deltaP `-14.6248` edge `-0.0295` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-2.8409` n `98` status `ready` deltaP `1.607` edge `-0.0297` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.4927` n `98` status `ready` deltaP `-24.0823` edge `-0.0096` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7636` n `98` status `ready` deltaP `-18.8138` edge `-0.0073` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.2179` n `98` status `ready` deltaP `-22.5329` edge `-0.1052` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.8699` n `98` status `ready` deltaP `-14.1653` edge `-0.1025` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-11.5849` n `98` status `ready` deltaP `-13.2093` edge `-0.1953` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
