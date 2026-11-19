# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T05:37:26.848096+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2478`

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

- `market_context_high->unknown_24h` score `1347.0111` n `98` status `ready` deltaP `5.2083` edge `112.2162` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `12.977` n `98` status `ready` deltaP `39.594` edge `1.7268` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `10.9495` n `98` status `ready` deltaP `23.5722` edge `1.459` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.2329` n `98` status `ready` deltaP `15.3557` edge `0.2007` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.4548` n `108` status `ready` deltaP `2.5172` edge `0.0118` maxDD `-2.6517`
- `market_context_high->metal_4h` score `-0.6858` n `98` status `ready` deltaP `10.705` edge `0.0022` maxDD `-6.1238`
- `market_context_high->crypto_major_1h` score `-0.852` n `108` status `ready` deltaP `2.3675` edge `0.0617` maxDD `-10.2705`
- `market_context_high->index_1h` score `-0.864` n `108` status `ready` deltaP `-2.1402` edge `0.0022` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.0049` n `108` status `ready` deltaP `-1.3085` edge `0.0302` maxDD `-7.6911`
- `market_context_high->crypto_alt_4h` score `-1.1472` n `98` status `ready` deltaP `-2.0191` edge `0.1474` maxDD `-17.1476`
- `market_context_high->fx_1h` score `-1.3569` n `108` status `ready` deltaP `-8.6217` edge `-0.0007` maxDD `-0.392`
- `market_context_high->crypto_major_4h` score `-1.3817` n `98` status `ready` deltaP `-4.3647` edge `0.2102` maxDD `-22.3259`
- `market_context_high->commodity_1h` score `-2.7574` n `108` status `ready` deltaP `-13.6449` edge `-0.031` maxDD `-3.9584`
- `market_context_high->index_4h` score `-2.782` n `98` status `ready` deltaP `-10.9787` edge `-0.0243` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.9483` n `108` status `ready` deltaP `-0.1109` edge `-0.0272` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.591` n `98` status `ready` deltaP `-24.9969` edge `-0.0117` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7173` n `98` status `ready` deltaP `-18.6402` edge `-0.0046` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.4946` n `98` status `ready` deltaP `-24.972` edge `-0.112` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0774` n `98` status `ready` deltaP `-16.2486` edge `-0.1059` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.882` n `98` status `ready` deltaP `-16.8678` edge `-0.279` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
