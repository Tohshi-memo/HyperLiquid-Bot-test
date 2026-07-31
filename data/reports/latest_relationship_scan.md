# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T04:22:24.655380+00:00`
- Price records: `672`
- Market context records: `8479`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5828`

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

- `news_risk_high->unknown_24h` score `6268.2581` n `52` status `ready` deltaP `44.0438` edge `522.1033` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.2435` n `61` status `ready` deltaP `22.4385` edge `0.4304` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.1984` n `61` status `ready` deltaP `18.3226` edge `0.0801` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7385` n `64` status `ready` deltaP `16.1022` edge `0.0852` maxDD `-2.4803`
- `news_risk_high->crypto_alt_4h` score `1.3826` n `61` status `ready` deltaP `17.5555` edge `0.1994` maxDD `-5.8012`
- `news_risk_high->crypto_major_4h` score `1.381` n `61` status `ready` deltaP `7.7594` edge `0.1947` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `0.6121` n `64` status `ready` deltaP `10.058` edge `0.0641` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3407` n `64` status `ready` deltaP `6.9143` edge `0.0488` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1243` n `64` status `ready` deltaP `6.0348` edge `0.0038` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0416` n `61` status `ready` deltaP `11.6429` edge `0.0216` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0293` n `64` status `ready` deltaP `4.07` edge `0.0083` maxDD `-0.5338`
- `news_risk_high->metal_1h` score `-0.2701` n `64` status `ready` deltaP `1.9087` edge `0.0051` maxDD `-0.5599`
- `news_risk_high->metal_4h` score `-0.3744` n `61` status `ready` deltaP `-1.312` edge `0.0248` maxDD `-0.7801`
- `news_risk_high->commodity_1h` score `-1.5261` n `64` status `ready` deltaP `-2.6572` edge `-0.0309` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5501` n `52` status `ready` deltaP `-27.7244` edge `-0.0455` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.4212` n `61` status `ready` deltaP `-18.5526` edge `-0.164` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.2948` n `52` status `ready` deltaP `-36.6186` edge `-0.2534` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.951` n `52` status `ready` deltaP `-13.3013` edge `-0.3966` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-14.5222` n `52` status `ready` deltaP `-35.5369` edge `-0.423` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-40.5652` n `52` status `ready` deltaP `-30.876` edge `-1.7221` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
