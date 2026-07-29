# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T11:52:26.839644+00:00`
- Price records: `672`
- Market context records: `8299`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5892`

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

- `news_risk_high->unknown_24h` score `5951.4626` n `54` status `ready` deltaP `35.4745` edge `495.7608` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.8071` n `54` status `ready` deltaP `25.1637` edge `0.4592` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9167` n `54` status `ready` deltaP `21.0801` edge `0.1334` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.549` n `54` status `ready` deltaP `21.5052` edge `0.0881` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0006` n `54` status `ready` deltaP `9.5642` edge `0.2621` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8939` n `54` status `ready` deltaP `14.8536` edge `0.1022` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.587` n `54` status `ready` deltaP `17.841` edge `0.2237` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.567` n `54` status `ready` deltaP `10.6066` edge `0.0996` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `1.157` n `54` status `ready` deltaP `10.5013` edge `0.0732` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3429` n `54` status `ready` deltaP `5.7053` edge `0.0194` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.144` n `54` status `ready` deltaP `6.548` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0521` n `54` status `ready` deltaP `3.554` edge `0.0123` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5055` n `54` status `ready` deltaP `3.698` edge `0.0063` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.13` n `54` status `ready` deltaP `-8.6605` edge `-0.0412` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0428` n `54` status `ready` deltaP `-20.544` edge `-0.0489` maxDD `-5.4165`
- `news_risk_high->metal_24h` score `-5.8278` n `54` status `ready` deltaP `-21.9908` edge `-0.062` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7942` n `54` status `ready` deltaP `-30.8096` edge `-0.1967` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-10.8542` n `54` status `ready` deltaP `-5.9606` edge `-0.2708` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-11.9337` n `54` status `ready` deltaP `-23.206` edge `-0.2895` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-32.1765` n `54` status `ready` deltaP `-12.7315` edge `-1.144` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
