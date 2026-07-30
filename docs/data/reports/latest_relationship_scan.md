# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T18:52:46.815098+00:00`
- Price records: `672`
- Market context records: `8437`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5742`

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

- `news_risk_high->unknown_24h` score `6257.2263` n `52` status `ready` deltaP `43.6966` edge `521.1863` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.2015` n `52` status `ready` deltaP `23.0183` edge `0.3397` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.2444` n `52` status `ready` deltaP `18.7356` edge `0.093` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1197` n `52` status `ready` deltaP `18.75` edge `0.0707` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5176` n `52` status `ready` deltaP `12.1603` edge `0.0888` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.2046` n `52` status `ready` deltaP `8.7172` edge `0.082` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.146` n `52` status `ready` deltaP `4.0338` edge `0.1894` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.9887` n `52` status `ready` deltaP `13.5202` edge `0.1758` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.1833` n `52` status `ready` deltaP `6.9899` edge `0.005` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0058` n `52` status `ready` deltaP `1.841` edge `0.035` maxDD `-0.7433`
- `news_risk_high->index_1h` score `-0.0395` n `52` status `ready` deltaP `1.9001` edge `0.0129` maxDD `-0.3089`
- `news_risk_high->fx_4h` score `-0.3202` n `52` status `ready` deltaP `6.1797` edge `0.0135` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.5044` n `52` status `ready` deltaP `-0.3454` edge `0.0006` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.883` n `52` status `ready` deltaP `-5.7232` edge `-0.0402` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6869` n `52` status `ready` deltaP `-27.7244` edge `-0.0569` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.527` n `52` status `ready` deltaP `-27.2748` edge `-0.198` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.7784` n `52` status `ready` deltaP `-34.7088` edge `-0.2231` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.709` n `52` status `ready` deltaP `-12.7804` edge `-0.3799` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.9492` n `52` status `ready` deltaP `-28.9396` edge `-0.3359` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-37.6962` n `52` status `ready` deltaP `-27.0299` edge `-1.1736` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
