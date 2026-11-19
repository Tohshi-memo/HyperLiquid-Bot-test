# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T07:37:26.672822+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2632`

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

- `market_context_high->unknown_1h` score `11501.3142` n `112` status `ready` deltaP `1.1175` edge `958.4552` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7790.4124` n `104` status `ready` deltaP `0.0821` edge `649.2289` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `12.5854` n `98` status `ready` deltaP `39.594` edge `1.6766` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `10.6217` n `98` status `ready` deltaP `22.8777` edge `1.4216` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2521` n `112` status `ready` deltaP `3.1437` edge `0.0132` maxDD `-2.6517`
- `market_context_high->metal_24h` score `-0.2521` n `98` status `ready` deltaP `15.3557` edge `0.1991` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.4626` n `104` status `ready` deltaP `11.9489` edge `0.0128` maxDD `-6.1475`
- `market_context_high->crypto_major_4h` score `-0.648` n `104` status `ready` deltaP `-1.5947` edge `0.2858` maxDD `-22.3259`
- `market_context_high->crypto_alt_4h` score `-0.7028` n `104` status `ready` deltaP `0.4808` edge `0.1877` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.8058` n `112` status `ready` deltaP `-1.1709` edge `0.0032` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.8396` n `112` status `ready` deltaP `2.3952` edge `0.0631` maxDD `-10.2705`
- `market_context_high->crypto_alt_1h` score `-1.0408` n `112` status `ready` deltaP `-1.6253` edge `0.0277` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3806` n `112` status `ready` deltaP `-8.9019` edge `-0.0008` maxDD `-0.392`
- `market_context_high->index_4h` score `-2.3814` n `104` status `ready` deltaP `-7.7861` edge `-0.0122` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.5654` n `112` status `ready` deltaP `-11.7408` edge `-0.0277` maxDD `-3.9584`
- `market_context_high->equity_1h` score `-2.7672` n `112` status `ready` deltaP `1.2083` edge `-0.0209` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.1909` n `104` status `ready` deltaP `-20.4972` edge `-0.0083` maxDD `-2.0104`
- `market_context_high->fx_24h` score `-6.616` n `98` status `ready` deltaP `-17.5985` edge `-0.0031` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.3387` n `104` status `ready` deltaP `-22.7486` edge `-0.1005` maxDD `-14.7522`
- `market_context_high->index_24h` score `-9.1419` n `98` status `ready` deltaP `-16.7694` edge `-0.1078` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
