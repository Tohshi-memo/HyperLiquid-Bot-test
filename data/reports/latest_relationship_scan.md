# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T16:52:45.839386+00:00`
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

- `market_context_high->unknown_24h` score `1365.3115` n `98` status `ready` deltaP `2.6042` edge `113.7586` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.0887` n `98` status `ready` deltaP `40.2884` edge `1.8647` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.381` n `98` status `ready` deltaP `26.3499` edge `1.624` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2476` n `98` status `ready` deltaP `2.7771` edge `0.0099` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.4913` n `98` status `ready` deltaP `1.6395` edge `0.2071` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.5005` n `98` status `ready` deltaP `15.3557` edge `0.1784` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.5354` n `98` status `ready` deltaP `11.9245` edge `0.0066` maxDD `-6.1238`
- `market_context_high->index_1h` score `-0.8939` n `98` status `ready` deltaP `-2.4747` edge `0.0006` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-0.9409` n `98` status `ready` deltaP `-1.4684` edge `0.2474` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.0645` n `98` status `ready` deltaP `-1.0601` edge `0.0209` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3173` n `98` status `ready` deltaP `-8.148` edge `-0.0008` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.9066` n `98` status `ready` deltaP `-0.0397` edge `0.0281` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.4555` n `98` status `ready` deltaP `-8.0824` edge `-0.0164` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.7797` n `98` status `ready` deltaP `-14.6248` edge `-0.0294` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-2.8456` n `98` status `ready` deltaP `1.4573` edge `-0.0291` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.5206` n `98` status `ready` deltaP `-24.3871` edge `-0.0099` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7684` n `98` status `ready` deltaP `-18.8138` edge `-0.0077` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.2107` n `98` status `ready` deltaP `-22.5329` edge `-0.1046` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.8012` n `98` status `ready` deltaP `-13.4708` edge `-0.1014` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-11.7005` n `98` status `ready` deltaP `-13.5142` edge `-0.2029` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
