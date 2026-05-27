# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T22:22:20.088533+00:00`
- Price records: `672`
- Market context records: `2081`
- Flow alert records: `7886`
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

- `market_context_high->crypto_major_4h` score `10.1308` n `198` status `ready` deltaP `35.9448` edge `0.6576` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `9.7334` n `198` status `ready` deltaP `29.1882` edge `0.731` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `7.3849` n `198` status `ready` deltaP `24.5288` edge `0.5268` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `5.3847` n `197` status `ready` deltaP `21.2654` edge `0.839` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.8172` n `198` status `ready` deltaP `20.6332` edge `0.29` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.2125` n `198` status `ready` deltaP `16.6405` edge `0.1418` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.0742` n `198` status `ready` deltaP `15.1893` edge `0.1702` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.8208` n `197` status `ready` deltaP `21.5069` edge `0.4982` maxDD `-33.1875`
- `market_context_high->index_24h` score `1.7658` n `197` status `ready` deltaP `10.4685` edge `0.2002` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.7359` n `198` status `ready` deltaP `11.84` edge `0.1771` maxDD `-4.9097`
- `market_context_high->equity_1h` score `0.5895` n `198` status `ready` deltaP `9.2936` edge `0.066` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.4686` n `198` status `ready` deltaP `5.0868` edge `0.0771` maxDD `-3.0902`
- `market_context_high->crypto_major_24h` score `0.3203` n `197` status `ready` deltaP `21.1459` edge `0.7443` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.1055` n `198` status `ready` deltaP `3.9074` edge `0.0242` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.1538` n `197` status `ready` deltaP `14.6532` edge `0.0288` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.2753` n `198` status `ready` deltaP `12.5493` edge `0.1479` maxDD `-11.3602`
- `market_context_high->metal_1h` score `-0.621` n `198` status `ready` deltaP `4.4336` edge `0.0291` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8951` n `198` status `ready` deltaP `-1.9083` edge `0.0009` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.3547` n `198` status `ready` deltaP `-3.8771` edge `0.0011` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.5193` n `197` status `ready` deltaP `11.0867` edge `0.1896` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
