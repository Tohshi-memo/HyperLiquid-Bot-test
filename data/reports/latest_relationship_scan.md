# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T05:37:27.077080+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8814`

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

- `market_context_high->equity_24h` score `10.0388` n `32` status `ready` deltaP `16.4931` edge `0.9639` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.562` n `32` status `ready` deltaP `7.9861` edge `0.219` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3982` n `32` status `ready` deltaP `16.6667` edge `0.1144` maxDD `-2.3671`
- `market_context_high->metal_4h` score `0.9821` n `66` status `ready` deltaP `14.2553` edge `0.0834` maxDD `-1.2025`
- `market_context_high->commodity_4h` score `0.8979` n `66` status `ready` deltaP `6.1854` edge `0.0808` maxDD `-1.1102`
- `market_context_high->metal_1h` score `0.8574` n `78` status `ready` deltaP `11.0894` edge `0.0303` maxDD `-0.6226`
- `market_context_high->fx_24h` score `0.6868` n `32` status `ready` deltaP `10.7639` edge `-0.0057` maxDD `-0.0397`
- `market_context_high->index_4h` score `0.355` n `66` status `ready` deltaP `15.2947` edge `0.0364` maxDD `-2.4279`
- `market_context_high->equity_1h` score `0.1043` n `78` status `ready` deltaP `-0.1689` edge `0.1342` maxDD `-5.5762`
- `market_context_high->commodity_1h` score `0.047` n `78` status `ready` deltaP `6.7481` edge `0.0177` maxDD `-1.7019`
- `market_context_high->index_1h` score `-0.4795` n `78` status `ready` deltaP `-0.0192` edge `0.0185` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-0.8577` n `78` status `ready` deltaP `8.103` edge `0.0253` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-1.0521` n `78` status `ready` deltaP `-13.5498` edge `-0.0044` maxDD `-0.5451`
- `market_context_high->equity_4h` score `-1.2279` n `66` status `ready` deltaP `11.5299` edge `0.1437` maxDD `-24.9053`
- `market_context_high->metal_24h` score `-1.6248` n `32` status `ready` deltaP `0.0` edge `-0.153` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-1.8687` n `66` status `ready` deltaP `-10.1857` edge `-0.0088` maxDD `-1.6965`
- `market_context_high->crypto_major_1h` score `-1.9978` n `78` status `ready` deltaP `1.1784` edge `-0.0541` maxDD `-11.7911`
- `market_context_high->crypto_major_24h` score `-4.6642` n `32` status `ready` deltaP `-4.8611` edge `0.008` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-6.4764` n `66` status `ready` deltaP `7.0307` edge `-0.1197` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-9.1438` n `32` status `ready` deltaP `-18.75` edge `-0.1791` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
