# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T05:52:35.578459+00:00`
- Price records: `672`
- Market context records: `8273`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5924`

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

- `news_risk_high->unknown_24h` score `6750.5882` n `49` status `ready` deltaP `39.0625` edge `562.2886` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.2683` n `54` status `ready` deltaP `26.3832` edge `0.4895` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.0954` n `54` status `ready` deltaP `21.9783` edge `0.1423` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7619` n `54` status `ready` deltaP `22.8771` edge `0.0967` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1073` n `54` status `ready` deltaP `10.3264` edge `0.2707` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8543` n `54` status `ready` deltaP `14.5542` edge `0.1009` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.5682` n `54` status `ready` deltaP `10.4569` edge `0.1007` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4518` n `54` status `ready` deltaP `16.6215` edge `0.2145` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.0756` n `54` status `ready` deltaP `9.7391` edge `0.0715` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4879` n `54` status `ready` deltaP `7.0526` edge `0.0225` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.2195` n `54` status `ready` deltaP `7.8953` edge `0.0036` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0628` n `54` status `ready` deltaP `3.4043` edge `0.0124` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4097` n `54` status `ready` deltaP `5.3748` edge `0.0074` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1803` n `54` status `ready` deltaP `-9.1096` edge `-0.0424` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.656` n `49` status `ready` deltaP `-19.7881` edge `-0.0489` maxDD `-4.9074`
- `news_risk_high->metal_24h` score `-5.5643` n `49` status `ready` deltaP `-18.6083` edge `-0.065` maxDD `-10.6379`
- `news_risk_high->commodity_4h` score `-8.9168` n `54` status `ready` deltaP `-31.8767` edge `-0.1998` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.1682` n `49` status `ready` deltaP `-25.5598` edge `-0.3286` maxDD `-26.868`
- `news_risk_high->commodity_24h` score `-12.5374` n `49` status `ready` deltaP `-13.8429` edge `-0.3611` maxDD `-33.6451`
- `news_risk_high->crypto_major_24h` score `-35.3161` n `49` status `ready` deltaP `-18.0024` edge `-1.3705` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
