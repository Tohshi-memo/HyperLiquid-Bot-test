# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T14:22:32.167895+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3479`

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

- `news_risk_high->unknown_1h` score `3229.4688` n `31` status `ready` deltaP `1.7819` edge `269.1281` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3218.9563` n `31` status `ready` deltaP `3.4815` edge `268.2288` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `34.1379` n `31` status `ready` deltaP `42.7083` edge `2.5601` maxDD `0.0`
- `news_risk_high->equity_24h` score `33.178` n `31` status `ready` deltaP `41.8403` edge `2.4859` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `28.1411` n `31` status `ready` deltaP `42.0139` edge `2.065` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.4555` n `31` status `ready` deltaP `25.9982` edge `0.785` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.146` n `31` status `ready` deltaP `38.1393` edge `0.6393` maxDD `-2.178`
- `news_risk_high->metal_24h` score `8.1045` n `31` status `ready` deltaP `28.3883` edge `0.5136` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.8412` n `31` status `ready` deltaP `19.0647` edge `0.8917` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.5931` n `31` status `ready` deltaP `43.2292` edge `0.1779` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.8854` n `31` status `ready` deltaP `41.017` edge `0.1465` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7866` n `31` status `ready` deltaP `20.5862` edge `0.197` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3636` n `31` status `ready` deltaP `36.7673` edge `0.0612` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7704` n `31` status `ready` deltaP `32.741` edge `0.0211` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4876` n `31` status `ready` deltaP `9.8609` edge `0.2993` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2448` n `31` status `ready` deltaP `12.7052` edge `0.2388` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4511` n `31` status `ready` deltaP `28.5348` edge `0.0237` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.982` n `31` status `ready` deltaP `15.5586` edge `0.0779` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.4287` n `31` status `ready` deltaP `12.4852` edge `0.0115` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4011` n `31` status `ready` deltaP `-2.3614` edge `0.0085` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
