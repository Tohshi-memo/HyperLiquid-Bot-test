# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T04:52:31.100381+00:00`
- Price records: `672`
- Market context records: `8482`
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

- `news_risk_high->unknown_24h` score `6268.8329` n `52` status `ready` deltaP `44.0438` edge `522.1512` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.2761` n `61` status `ready` deltaP `22.5909` edge `0.4321` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.2264` n `61` status `ready` deltaP `18.6275` edge `0.0804` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7289` n `64` status `ready` deltaP `16.1022` edge `0.0844` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.4195` n `61` status `ready` deltaP `8.0642` edge `0.1976` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `1.4187` n `61` status `ready` deltaP `17.8604` edge `0.202` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.623` n `64` status `ready` deltaP `10.2077` edge `0.0645` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3407` n `64` status `ready` deltaP `6.9143` edge `0.0488` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1243` n `64` status `ready` deltaP `6.0348` edge `0.0038` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0392` n `61` status `ready` deltaP `11.6429` edge `0.0214` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0208` n `64` status `ready` deltaP `3.9203` edge `0.0082` maxDD `-0.5338`
- `news_risk_high->metal_1h` score `-0.2845` n `64` status `ready` deltaP `1.759` edge `0.0049` maxDD `-0.5599`
- `news_risk_high->metal_4h` score `-0.3392` n `61` status `ready` deltaP `-1.0071` edge `0.0257` maxDD `-0.7801`
- `news_risk_high->commodity_1h` score `-1.5249` n `64` status `ready` deltaP `-2.6572` edge `-0.0308` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5501` n `52` status `ready` deltaP `-27.7244` edge `-0.0455` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.4224` n `61` status `ready` deltaP `-18.5526` edge `-0.1641` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.314` n `52` status `ready` deltaP `-36.6186` edge `-0.255` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.9618` n `52` status `ready` deltaP `-13.3013` edge `-0.3975` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-14.6039` n `52` status `ready` deltaP `-35.8841` edge `-0.4275` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-40.6734` n `52` status `ready` deltaP `-31.2232` edge `-1.7288` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
