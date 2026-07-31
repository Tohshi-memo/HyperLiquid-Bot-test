# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T06:52:30.506665+00:00`
- Price records: `672`
- Market context records: `8490`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5860`

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

- `news_risk_high->unknown_24h` score `6271.1117` n `52` status `ready` deltaP `44.0438` edge `522.3411` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.0524` n `64` status `ready` deltaP `22.1799` edge `0.4162` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0351` n `64` status `ready` deltaP `16.8064` edge `0.0766` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.6978` n `64` status `ready` deltaP `15.8028` edge `0.0838` maxDD `-2.4803`
- `news_risk_high->crypto_alt_4h` score `1.0387` n `64` status `ready` deltaP `15.3963` edge `0.1697` maxDD `-5.8012`
- `news_risk_high->crypto_major_4h` score `0.9814` n `64` status `ready` deltaP `5.9832` edge `0.1635` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.6183` n `64` status `ready` deltaP `10.058` edge `0.0649` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.343` n `64` status `ready` deltaP `6.9143` edge `0.0491` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1617` n `64` status `ready` deltaP `6.6336` edge `0.0046` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0682` n `64` status `ready` deltaP `12.0808` edge `0.0209` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0021` n `64` status `ready` deltaP `3.6209` edge `0.0078` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.1667` n `64` status `ready` deltaP `-0.1143` edge `0.027` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.2545` n `64` status `ready` deltaP `2.0584` edge `0.0054` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.5872` n `64` status `ready` deltaP `-3.256` edge `-0.032` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5393` n `52` status `ready` deltaP `-27.7244` edge `-0.0446` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.5663` n `64` status `ready` deltaP `-19.8552` edge `-0.1654` maxDD `-13.2872`
- `news_risk_high->metal_24h` score `-9.398` n `52` status `ready` deltaP `-36.6186` edge `-0.262` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.9426` n `52` status `ready` deltaP `-13.3013` edge `-0.3959` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-14.9587` n `52` status `ready` deltaP `-37.273` edge `-0.4478` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-41.1337` n `52` status `ready` deltaP `-32.6121` edge `-1.7579` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
