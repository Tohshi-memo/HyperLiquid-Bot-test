# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T21:37:17.290187+00:00`
- Price records: `672`
- Market context records: `2078`
- Flow alert records: `7877`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_major_4h` score `10.0109` n `201` status `ready` deltaP `35.6609` edge `0.6495` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `9.4966` n `201` status `ready` deltaP `28.6874` edge `0.7146` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `7.1079` n `201` status `ready` deltaP `23.3755` edge `0.5114` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `5.8073` n `200` status `ready` deltaP `20.9671` edge `0.8762` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.6817` n `201` status `ready` deltaP `19.8542` edge `0.2839` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.1088` n `201` status `ready` deltaP `15.9144` edge `0.138` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.9968` n `201` status `ready` deltaP `14.9276` edge `0.1655` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.8066` n `200` status `ready` deltaP `21.2543` edge `0.4987` maxDD `-33.1875`
- `market_context_high->index_24h` score `1.6706` n `200` status `ready` deltaP `10.2388` edge `0.1938` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.6148` n `201` status `ready` deltaP `11.5858` edge `0.1687` maxDD `-4.9097`
- `market_context_high->equity_1h` score `0.5355` n `201` status `ready` deltaP `8.9791` edge `0.0636` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.4666` n `201` status `ready` deltaP `5.0168` edge `0.0774` maxDD `-3.0902`
- `market_context_high->crypto_major_24h` score `0.3993` n `200` status `ready` deltaP `21.1142` edge `0.7511` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.1258` n `201` status `ready` deltaP `3.7135` edge `0.0238` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.1994` n `200` status `ready` deltaP `14.2336` edge `0.0278` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.3639` n `201` status `ready` deltaP `12.1321` edge `0.1433` maxDD `-11.3602`
- `market_context_high->fx_1h` score `-0.5971` n `201` status `ready` deltaP `-2.142` edge `0.0005` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.744` n `201` status `ready` deltaP `4.2817` edge `0.0282` maxDD `-5.166`
- `market_context_high->fx_4h` score `-1.4026` n `201` status `ready` deltaP `-4.3563` edge `0.0003` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.6207` n `200` status `ready` deltaP `11.154` edge `0.1807` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
