# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T16:37:21.010455+00:00`
- Price records: `672`
- Market context records: `2057`
- Flow alert records: `7814`
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

- `market_context_high->crypto_major_4h` score `9.5168` n `205` status `ready` deltaP `33.3842` edge `0.6235` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.8076` n `205` status `ready` deltaP `25.6098` edge `0.6777` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.3847` n `205` status `ready` deltaP `20.3658` edge `0.4712` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `3.9088` n `205` status `ready` deltaP `17.8606` edge `0.7387` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.3942` n `205` status `ready` deltaP `18.7805` edge `0.2671` maxDD `-5.0894`
- `market_context_high->index_4h` score `1.9432` n `205` status `ready` deltaP `14.9086` edge `0.1309` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.6987` n `206` status `ready` deltaP `13.4062` edge `0.1508` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.2857` n `206` status `ready` deltaP `10.2625` edge `0.1501` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.2515` n `205` status `ready` deltaP `18.7399` edge `0.4692` maxDD `-33.1875`
- `market_context_high->index_24h` score `1.1117` n `205` status `ready` deltaP `7.2419` edge `0.1672` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.4069` n `206` status `ready` deltaP `8.2714` edge `0.0576` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.2976` n `206` status `ready` deltaP `4.959` edge `0.0637` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.1019` n `206` status `ready` deltaP `3.9068` edge `0.0245` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.3645` n `205` status `ready` deltaP `12.6795` edge `0.0244` maxDD `-2.811`
- `market_context_high->crypto_major_24h` score `-0.3915` n `205` status `ready` deltaP `18.9535` edge `0.6996` maxDD `-62.3533`
- `market_context_high->metal_4h` score `-0.6561` n `205` status `ready` deltaP `11.1586` edge `0.1332` maxDD `-11.9812`
- `market_context_high->fx_1h` score `-0.7903` n `206` status `ready` deltaP `-0.5988` edge `0.0009` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.8063` n `206` status `ready` deltaP `3.9969` edge `0.0249` maxDD `-5.166`
- `market_context_high->fx_4h` score `-1.4308` n `205` status `ready` deltaP `-4.6037` edge `-0.0004` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.9395` n `206` status `ready` deltaP `1.9417` edge `-0.0058` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
