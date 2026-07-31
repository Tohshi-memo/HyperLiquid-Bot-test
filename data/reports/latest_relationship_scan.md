# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T08:37:26.601081+00:00`
- Price records: `672`
- Market context records: `8498`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5871`

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

- `news_risk_high->unknown_24h` score `6273.0869` n `52` status `ready` deltaP `44.0438` edge `522.5057` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.034` n `64` status `ready` deltaP `21.875` edge `0.4167` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0351` n `64` status `ready` deltaP `16.8064` edge `0.0766` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7218` n `64` status `ready` deltaP `15.8028` edge `0.0858` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.954` n `64` status `ready` deltaP `5.8308` edge `0.161` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.9444` n `64` status `ready` deltaP `14.6341` edge `0.1627` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.6074` n `64` status `ready` deltaP `9.9083` edge `0.0645` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3937` n `64` status `ready` deltaP `7.3634` edge `0.0526` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1687` n `64` status `ready` deltaP `6.7833` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.073` n `64` status `ready` deltaP `12.0808` edge `0.0213` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0223` n `64` status `ready` deltaP `3.9203` edge `0.0084` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.117` n `64` status `ready` deltaP `0.4954` edge `0.0293` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1934` n `64` status `ready` deltaP `2.6572` edge `0.0065` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.6351` n `64` status `ready` deltaP `-3.7051` edge `-0.033` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5237` n `52` status `ready` deltaP `-27.7244` edge `-0.0433` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.6355` n `64` status `ready` deltaP `-20.4649` edge `-0.1671` maxDD `-13.2872`
- `news_risk_high->metal_24h` score `-9.5021` n `52` status `ready` deltaP `-37.1394` edge `-0.2672` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.9126` n `52` status `ready` deltaP `-13.3013` edge `-0.3934` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-15.2719` n `52` status `ready` deltaP `-38.4883` edge `-0.4658` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-41.5405` n `52` status `ready` deltaP `-33.8274` edge `-1.7837` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
