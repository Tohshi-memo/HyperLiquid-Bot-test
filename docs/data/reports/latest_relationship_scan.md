# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T20:22:24.818221+00:00`
- Price records: `672`
- Market context records: `2072`
- Flow alert records: `7861`
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

- `market_context_high->crypto_major_4h` score `9.7332` n `206` status `ready` deltaP `34.6347` edge `0.6332` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `9.1084` n `206` status `ready` deltaP `27.0601` edge `0.6931` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.722` n `206` status `ready` deltaP `22.1377` edge `0.4875` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `6.5572` n `205` status `ready` deltaP `20.4558` edge `0.9421` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.5139` n `206` status `ready` deltaP `19.302` edge `0.2736` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.033` n `206` status `ready` deltaP `15.4467` edge `0.1348` maxDD `-1.8022`
- `market_context_high->equity_24h` score `1.8628` n `205` status `ready` deltaP `21.1621` edge `0.504` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `1.8054` n `206` status `ready` deltaP `13.8553` edge `0.1567` maxDD `-3.2225`
- `market_context_high->index_24h` score `1.5677` n `205` status `ready` deltaP `9.8371` edge `0.1879` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.474` n `206` status `ready` deltaP `11.011` edge `0.1608` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `0.6807` n `205` status `ready` deltaP `21.3757` edge `0.7728` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `0.4667` n `206` status `ready` deltaP `5.5578` edge `0.0738` maxDD `-3.0902`
- `market_context_high->equity_1h` score `0.4309` n `206` status `ready` deltaP `8.1217` edge `0.0606` maxDD `-2.6402`
- `market_context_high->index_1h` score `-0.0564` n `206` status `ready` deltaP `4.3559` edge `0.0253` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.231` n `205` status `ready` deltaP `14.0636` edge `0.0263` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.5814` n `206` status `ready` deltaP `11.5217` edge `0.137` maxDD `-11.9812`
- `market_context_high->metal_1h` score `-0.7344` n `206` status `ready` deltaP `4.2963` edge `0.0289` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8406` n `206` status `ready` deltaP `-1.1976` edge `0.0007` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.4627` n `206` status `ready` deltaP `-5.0024` edge `-0.0004` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.7288` n `205` status `ready` deltaP `11.2279` edge `0.1712` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
