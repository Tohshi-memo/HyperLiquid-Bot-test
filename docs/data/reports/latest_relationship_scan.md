# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T06:37:24.160063+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8724`

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

- `market_context_high->equity_24h` score `9.6968` n `32` status `ready` deltaP `16.4931` edge `0.9354` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.4905` n `32` status `ready` deltaP `7.8125` edge `0.2142` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3803` n `32` status `ready` deltaP `16.6667` edge `0.1121` maxDD `-2.3671`
- `market_context_high->commodity_4h` score `0.7614` n `70` status `ready` deltaP `5.2744` edge `0.0755` maxDD `-1.1102`
- `market_context_high->fx_24h` score `0.7277` n `32` status `ready` deltaP `11.1111` edge `-0.0046` maxDD `-0.0397`
- `market_context_high->metal_4h` score `0.7111` n `70` status `ready` deltaP `11.0104` edge `0.0703` maxDD `-1.2025`
- `market_context_high->metal_1h` score `0.5955` n `82` status `ready` deltaP `8.5366` edge `0.0255` maxDD `-0.6226`
- `market_context_high->index_4h` score `0.0976` n `70` status `ready` deltaP `11.4851` edge `0.0288` maxDD `-2.4279`
- `market_context_high->commodity_1h` score `-0.2413` n `82` status `ready` deltaP `4.1953` edge `0.0107` maxDD `-1.7019`
- `market_context_high->equity_1h` score `-0.2527` n `82` status `ready` deltaP `-2.1834` edge `0.1102` maxDD `-5.5762`
- `market_context_high->index_1h` score `-0.4492` n `82` status `ready` deltaP `-2.0337` edge `0.0143` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-1.101` n `82` status `ready` deltaP `5.5389` edge `0.0112` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-1.2619` n `82` status `ready` deltaP `-15.1891` edge `-0.0059` maxDD `-0.7031`
- `market_context_high->metal_24h` score `-1.6976` n `32` status `ready` deltaP `-0.6944` edge `-0.1577` maxDD `-1.4245`
- `market_context_high->equity_4h` score `-1.7442` n `70` status `ready` deltaP `8.3058` edge `0.099` maxDD `-24.9053`
- `market_context_high->fx_4h` score `-2.152` n `70` status `ready` deltaP `-12.1734` edge `-0.0116` maxDD `-1.9844`
- `market_context_high->crypto_major_1h` score `-2.2968` n `82` status `ready` deltaP `-1.1355` edge `-0.0681` maxDD `-12.5032`
- `market_context_high->crypto_major_24h` score `-4.5778` n `32` status `ready` deltaP `-4.8611` edge `0.0152` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-7.1628` n `70` status `ready` deltaP `4.3467` edge `-0.159` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-9.2074` n `32` status `ready` deltaP `-18.75` edge `-0.1844` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
