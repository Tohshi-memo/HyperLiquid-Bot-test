# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T05:52:33.842860+00:00`
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

- `market_context_high->unknown_24h` score `1191.6459` n `98` status `ready` deltaP `5.2083` edge `99.2691` maxDD `0.0`
- `market_context_high->unknown_1h` score `408.2163` n `109` status `ready` deltaP `0.6483` edge `34.0335` maxDD `-0.9174`
- `market_context_high->crypto_major_24h` score `12.9294` n `98` status `ready` deltaP `39.594` edge `1.7207` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `10.9121` n `98` status `ready` deltaP `23.5722` edge `1.4542` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.2317` n `98` status `ready` deltaP `15.3557` edge `0.2008` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.3994` n `109` status `ready` deltaP `2.9844` edge `0.0133` maxDD `-2.6517`
- `market_context_high->metal_4h` score `-0.687` n `98` status `ready` deltaP `10.705` edge `0.0021` maxDD `-6.1238`
- `market_context_high->index_1h` score `-0.8448` n `109` status `ready` deltaP `-1.7717` edge `0.0022` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.8824` n `109` status `ready` deltaP `1.9173` edge `0.0608` maxDD `-10.2705`
- `market_context_high->crypto_alt_1h` score `-1.0387` n `109` status `ready` deltaP `-1.5835` edge `0.0277` maxDD `-7.6911`
- `market_context_high->crypto_alt_4h` score `-1.1644` n `98` status `ready` deltaP `-2.1715` edge `0.1462` maxDD `-17.1476`
- `market_context_high->fx_1h` score `-1.3215` n `109` status `ready` deltaP `-8.1937` edge `-0.0006` maxDD `-0.392`
- `market_context_high->crypto_major_4h` score `-1.4068` n `98` status `ready` deltaP `-4.5172` edge `0.208` maxDD `-22.3259`
- `market_context_high->commodity_1h` score `-2.7127` n `109` status `ready` deltaP `-13.1915` edge `-0.0303` maxDD `-3.9584`
- `market_context_high->index_4h` score `-2.7966` n `98` status `ready` deltaP `-11.1312` edge `-0.0245` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.9233` n `109` status `ready` deltaP `0.2321` edge `-0.0274` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.5764` n `98` status `ready` deltaP `-24.8445` edge `-0.0115` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7149` n `98` status `ready` deltaP `-18.6402` edge `-0.0044` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.4728` n `98` status `ready` deltaP `-24.8195` edge `-0.1112` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0913` n `98` status `ready` deltaP `-16.4222` edge `-0.1059` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
