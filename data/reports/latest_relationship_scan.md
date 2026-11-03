# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T06:37:28.936985+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4520`

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

- `news_risk_high->crypto_alt_4h` score `0.2121` n `146` status `ready` deltaP `5.7802` edge `0.2523` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4223` n `146` status `ready` deltaP `2.1819` edge `0.0541` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6194` n `146` status `ready` deltaP `-1.0253` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9442` n `146` status `ready` deltaP `0.7485` edge `-0.0037` maxDD `-1.3981`
- `news_risk_high->metal_24h` score `-0.953` n `134` status `ready` deltaP `11.4039` edge `0.1274` maxDD `-14.0483`
- `news_risk_high->fx_4h` score `-1.2254` n `146` status `ready` deltaP `-3.2012` edge `-0.0106` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3024` n `146` status `ready` deltaP `-5.2477` edge `-0.0098` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.09` n `146` status `ready` deltaP `-3.4268` edge `-0.015` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.1625` n `134` status `ready` deltaP `-2.8271` edge `0.0258` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.3763` n `134` status `ready` deltaP `-17.413` edge `-0.0177` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.3804` n `146` status `ready` deltaP `-9.0764` edge `-0.0012` maxDD `-3.2657`
- `news_risk_high->crypto_alt_24h` score `-2.6343` n `134` status `ready` deltaP `21.0381` edge `0.8013` maxDD `-89.0097`
- `news_risk_high->equity_1h` score `-2.7155` n `146` status `ready` deltaP `-7.0851` edge `-0.0333` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2247` n `146` status `ready` deltaP `-8.1556` edge `-0.0418` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7868` n `146` status `ready` deltaP `-12.1701` edge `0.001` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-4.1299` n `134` status `ready` deltaP `16.177` edge `0.5575` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.8587` n `146` status `ready` deltaP `-7.6052` edge `-0.0337` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0382` n `146` status `ready` deltaP `-14.2312` edge `-0.0897` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-11.4064` n `134` status `ready` deltaP `-12.7695` edge `0.0456` maxDD `-59.5472`
- `news_risk_high->equity_4h` score `-11.6772` n `146` status `ready` deltaP `-2.0548` edge `-0.1233` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
