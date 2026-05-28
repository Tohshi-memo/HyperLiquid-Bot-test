# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T00:52:16.736796+00:00`
- Price records: `672`
- Market context records: `2093`
- Flow alert records: `7918`
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

- `market_context_high->crypto_alt_4h` score `10.5049` n `188` status `ready` deltaP `30.7764` edge `0.7847` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.4302` n `188` status `ready` deltaP `36.8514` edge `0.6765` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.7924` n `188` status `ready` deltaP `24.1567` edge `0.4799` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.144` n `188` status `ready` deltaP `22.0777` edge `0.3076` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `3.8414` n `187` status `ready` deltaP `22.2083` edge `0.7041` maxDD `-35.8966`
- `market_context_high->index_4h` score `2.5175` n `188` status `ready` deltaP `18.5035` edge `0.1548` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.3245` n `188` status `ready` deltaP `16.4734` edge `0.1825` maxDD `-3.2225`
- `market_context_high->index_24h` score `2.1001` n `187` status `ready` deltaP `11.167` edge `0.2234` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `2.0699` n `188` status `ready` deltaP `13.6291` edge `0.193` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.7848` n `187` status `ready` deltaP `22.2869` edge `0.49` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.8728` n `188` status `ready` deltaP `11.2148` edge `0.0768` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.677` n `188` status `ready` deltaP `6.1314` edge `0.0875` maxDD `-3.0902`
- `market_context_high->index_1h` score `0.159` n `188` status `ready` deltaP `6.1632` edge `0.0312` maxDD `-1.3898`
- `market_context_high->crypto_major_24h` score `0.1313` n `187` status `ready` deltaP `21.1387` edge `0.7286` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.119` n `187` status `ready` deltaP `14.8632` edge `0.0303` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.1618` n `188` status `ready` deltaP `13.1585` edge `0.1533` maxDD `-11.3602`
- `market_context_high->metal_1h` score `-0.2811` n `188` status `ready` deltaP `6.5327` edge `0.0351` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8322` n `188` status `ready` deltaP `-1.1976` edge `0.0014` maxDD `-0.3548`
- `market_context_high->metal_24h` score `-1.2565` n `187` status `ready` deltaP `10.7266` edge `0.2139` maxDD `-23.2095`
- `market_context_high->fx_4h` score `-1.4214` n `188` status `ready` deltaP `-4.5764` edge `0.0002` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
