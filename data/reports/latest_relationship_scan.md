# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T05:37:36.039094+00:00`
- Price records: `672`
- Market context records: `8272`
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

- `news_risk_high->unknown_24h` score `6930.8798` n `48` status `ready` deltaP `39.0625` edge `577.3129` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.2767` n `54` status `ready` deltaP `26.3832` edge `0.4902` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1373` n `54` status `ready` deltaP `22.128` edge `0.1448` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7619` n `54` status `ready` deltaP `22.8771` edge `0.0967` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1277` n `54` status `ready` deltaP `10.4788` edge `0.2723` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8831` n `54` status `ready` deltaP `14.7039` edge `0.1023` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6042` n `54` status `ready` deltaP `10.6066` edge `0.1027` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4463` n `54` status `ready` deltaP `16.6215` edge `0.2138` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.0914` n `54` status `ready` deltaP `9.8916` edge `0.0718` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.5046` n `54` status `ready` deltaP `7.2023` edge `0.0229` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.2281` n `54` status `ready` deltaP `8.045` edge `0.0037` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0616` n `54` status `ready` deltaP `3.4043` edge `0.0125` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4105` n `54` status `ready` deltaP `5.3748` edge `0.0073` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1683` n `54` status `ready` deltaP `-8.9599` edge `-0.0424` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.5604` n `48` status `ready` deltaP `-19.6181` edge `-0.048` maxDD `-4.7664`
- `news_risk_high->metal_24h` score `-5.7257` n `48` status `ready` deltaP `-19.9653` edge `-0.0694` maxDD `-10.6379`
- `news_risk_high->commodity_4h` score `-8.9374` n `54` status `ready` deltaP `-32.0291` edge `-0.2005` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.1098` n `48` status `ready` deltaP `-25.5208` edge `-0.3328` maxDD `-26.4966`
- `news_risk_high->commodity_24h` score `-12.6271` n `48` status `ready` deltaP `-13.8889` edge `-0.3713` maxDD `-33.4029`
- `news_risk_high->equity_24h` score `-35.5607` n `48` status `ready` deltaP `-24.6527` edge `-1.1518` maxDD `-117.7795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
