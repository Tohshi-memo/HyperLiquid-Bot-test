# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T00:07:34.339781+00:00`
- Price records: `672`
- Market context records: `8461`
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

- `news_risk_high->unknown_24h` score `6263.3249` n `52` status `ready` deltaP `44.0438` edge `521.6922` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.0296` n `58` status `ready` deltaP `23.4703` edge `0.4057` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9321` n `61` status `ready` deltaP `20.7618` edge `0.1368` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1787` n `58` status `ready` deltaP `19.2021` edge `0.0726` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5697` n `61` status `ready` deltaP `12.4521` edge `0.0912` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.2922` n `58` status `ready` deltaP `7.191` edge `0.1871` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.2028` n `61` status `ready` deltaP `9.1587` edge `0.0789` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.1372` n `58` status `ready` deltaP `15.8221` edge `0.1795` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.5251` n `61` status `ready` deltaP `9.7722` edge `0.0067` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.5078` n `61` status `ready` deltaP `7.6617` edge `0.0201` maxDD `-0.3089`
- `news_risk_high->metal_1h` score `-0.0392` n `61` status `ready` deltaP `4.5254` edge `0.0069` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.0675` n `58` status `ready` deltaP `10.471` edge `0.0173` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `-0.1324` n `58` status `ready` deltaP `0.8936` edge `0.0298` maxDD `-0.7433`
- `news_risk_high->commodity_1h` score `-1.4851` n `61` status `ready` deltaP `-2.1449` edge `-0.0309` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5873` n `52` status `ready` deltaP `-27.7244` edge `-0.0486` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.4048` n `58` status `ready` deltaP `-18.0772` edge `-0.1658` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.1856` n `52` status `ready` deltaP `-36.6186` edge `-0.2443` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.8428` n `52` status `ready` deltaP `-12.954` edge `-0.3899` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.8181` n `52` status `ready` deltaP `-32.5855` edge `-0.384` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-39.7183` n `52` status `ready` deltaP `-27.9246` edge `-1.6712` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
