# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T17:52:27.829120+00:00`
- Price records: `672`
- Market context records: `2062`
- Flow alert records: `7830`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9145`

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

- `market_context_high->crypto_major_4h` score `9.5699` n `206` status `ready` deltaP `33.5676` edge `0.6267` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.886` n `206` status `ready` deltaP `25.8406` edge `0.6827` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.4467` n `206` status `ready` deltaP `20.7657` edge `0.4737` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `4.77` n `205` status `ready` deltaP `18.7257` edge `0.8047` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.515` n `206` status `ready` deltaP `19.1496` edge `0.2747` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.0316` n `206` status `ready` deltaP `15.2943` edge `0.1357` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.8366` n `206` status `ready` deltaP `14.1547` edge `0.1573` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.5007` n `205` status `ready` deltaP `19.605` edge `0.4842` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `1.462` n `206` status `ready` deltaP `11.011` edge `0.1598` maxDD `-4.9097`
- `market_context_high->index_24h` score `1.2877` n `205` status `ready` deltaP `8.107` edge `0.1761` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.4908` n `206` status `ready` deltaP `8.7205` edge `0.0616` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.3407` n `206` status `ready` deltaP `5.2584` edge `0.0653` maxDD `-3.0902`
- `market_context_high->crypto_major_24h` score `0.0017` n `205` status `ready` deltaP `19.8186` edge `0.7266` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.048` n `206` status `ready` deltaP `4.3559` edge `0.026` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.3158` n `205` status `ready` deltaP `13.1986` edge `0.025` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.5948` n `206` status `ready` deltaP `11.3693` edge `0.1369` maxDD `-11.9812`
- `market_context_high->metal_1h` score `-0.7224` n `206` status `ready` deltaP `4.446` edge `0.0289` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8287` n `206` status `ready` deltaP `-1.0479` edge `0.0007` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.4103` n `206` status `ready` deltaP `-4.3926` edge `-0.0001` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.9642` n `205` status `ready` deltaP `10.5359` edge `0.1562` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
