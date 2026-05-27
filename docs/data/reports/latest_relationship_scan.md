# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T16:52:16.667959+00:00`
- Price records: `672`
- Market context records: `2058`
- Flow alert records: `7817`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9125`

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

- `market_context_high->crypto_major_4h` score `9.5554` n `205` status `ready` deltaP `33.5366` edge `0.6257` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.8534` n `205` status `ready` deltaP `25.7622` edge `0.6805` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.4221` n `205` status `ready` deltaP `20.5182` edge `0.4733` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `4.0774` n `205` status `ready` deltaP `18.0336` edge `0.7516` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.4376` n `205` status `ready` deltaP `18.9329` edge `0.2697` maxDD `-5.0894`
- `market_context_high->index_4h` score `1.9769` n `205` status `ready` deltaP `15.061` edge `0.1327` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.7263` n `206` status `ready` deltaP `13.5559` edge `0.1521` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.3217` n `206` status `ready` deltaP `10.4122` edge `0.1521` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.3049` n `205` status `ready` deltaP `18.913` edge `0.4725` maxDD `-33.1875`
- `market_context_high->index_24h` score `1.1519` n `205` status `ready` deltaP `7.415` edge `0.1694` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.4105` n `206` status `ready` deltaP `8.2714` edge `0.0579` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.3264` n `206` status `ready` deltaP `5.1087` edge `0.0651` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.1007` n `206` status `ready` deltaP `3.9068` edge `0.0246` maxDD `-1.3898`
- `market_context_high->crypto_major_24h` score `-0.3129` n `205` status `ready` deltaP `19.1265` edge `0.705` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.3494` n `205` status `ready` deltaP `12.8525` edge `0.0245` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.6381` n `205` status `ready` deltaP `11.1586` edge `0.1347` maxDD `-11.9812`
- `market_context_high->fx_1h` score `-0.7915` n `206` status `ready` deltaP `-0.5988` edge `0.0008` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.7955` n `206` status `ready` deltaP `3.9969` edge `0.0258` maxDD `-5.166`
- `market_context_high->fx_4h` score `-1.4174` n `205` status `ready` deltaP `-4.4512` edge `-0.0003` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.9481` n `206` status `ready` deltaP `1.9417` edge `-0.0069` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
