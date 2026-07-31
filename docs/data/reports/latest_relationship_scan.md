# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T14:22:38.251405+00:00`
- Price records: `672`
- Market context records: `8522`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `6279.1701` n `52` status `ready` deltaP `44.7383` edge `523.008` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.5014` n `64` status `ready` deltaP `21.1128` edge `0.3774` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.9829` n `64` status `ready` deltaP `16.3491` edge `0.0753` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.6834` n `64` status `ready` deltaP `15.8028` edge `0.0826` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.8157` n `64` status `ready` deltaP `5.5259` edge `0.1453` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7726` n `64` status `ready` deltaP `14.3293` edge `0.1427` maxDD `-5.8012`
- `market_context_high->crypto_alt_4h` score `0.7144` n `38` status `ready` deltaP `9.724` edge `0.1082` maxDD `-4.5146`
- `news_risk_high->crypto_alt_1h` score `0.5139` n `64` status `ready` deltaP `9.0101` edge `0.0585` maxDD `-1.8813`
- `market_context_high->crypto_major_4h` score `0.4882` n `38` status `ready` deltaP `5.6081` edge `0.1093` maxDD `-3.7278`
- `news_risk_high->crypto_major_1h` score `0.2838` n `64` status `ready` deltaP `6.1658` edge `0.0465` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1243` n `64` status `ready` deltaP `5.8851` edge `0.0048` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.048` n `64` status `ready` deltaP `4.3694` edge `0.0087` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `0.0367` n `64` status `ready` deltaP `2.4771` edge `0.0358` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `0.0242` n `64` status `ready` deltaP `11.471` edge `0.0213` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.082` n `64` status `ready` deltaP `3.7051` edge `0.0088` maxDD `-0.5599`
- `market_context_high->fx_4h` score `-0.1249` n `38` status `ready` deltaP `4.6453` edge `0.0057` maxDD `-0.5474`
- `market_context_high->commodity_1h` score `-0.1977` n `50` status `ready` deltaP `4.3952` edge `0.0079` maxDD `-2.0038`
- `market_context_high->index_4h` score `-0.5441` n `38` status `ready` deltaP `0.3129` edge `-0.0199` maxDD `-1.4887`
- `market_context_high->commodity_4h` score `-0.5736` n `38` status `ready` deltaP `5.2551` edge `0.0429` maxDD `-5.4508`
- `market_context_high->metal_4h` score `-0.7654` n `38` status `ready` deltaP `5.1909` edge `-0.0391` maxDD `-2.4907`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
