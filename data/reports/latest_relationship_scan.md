# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T07:07:24.710791+00:00`
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

- `market_context_high->equity_24h` score `9.5312` n `32` status `ready` deltaP `16.4931` edge `0.9216` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.4653` n `32` status `ready` deltaP `7.8125` edge `0.2121` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3725` n `32` status `ready` deltaP `16.6667` edge `0.1111` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.7639` n `32` status `ready` deltaP `11.4583` edge `-0.0039` maxDD `-0.0397`
- `market_context_high->metal_4h` score `0.5657` n `72` status `ready` deltaP `9.3834` edge `0.0625` maxDD `-1.2025`
- `market_context_high->commodity_4h` score `0.5213` n `72` status `ready` deltaP `3.6077` edge `0.0666` maxDD `-1.1102`
- `market_context_high->metal_1h` score `0.3074` n `84` status `ready` deltaP `7.1429` edge `0.0214` maxDD `-0.8057`
- `market_context_high->index_4h` score `-0.0275` n `72` status `ready` deltaP `9.7391` edge `0.0244` maxDD `-2.4279`
- `market_context_high->commodity_1h` score `-0.248` n `84` status `ready` deltaP `2.9513` edge `0.0073` maxDD `-1.7019`
- `market_context_high->equity_1h` score `-0.4632` n `84` status `ready` deltaP `-3.2578` edge `0.0987` maxDD `-5.5762`
- `market_context_high->index_1h` score `-0.5469` n `84` status `ready` deltaP `-3.1081` edge `0.0131` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-1.2643` n `84` status `ready` deltaP `4.3484` edge `-0.0018` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-1.3728` n `84` status `ready` deltaP `-15.7898` edge `-0.0066` maxDD `-0.7977`
- `market_context_high->metal_24h` score `-1.7351` n `32` status `ready` deltaP `-1.0417` edge `-0.1602` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.2877` n `72` status `ready` deltaP `-13.0589` edge `-0.0129` maxDD `-2.1332`
- `market_context_high->crypto_major_1h` score `-2.5579` n `84` status `ready` deltaP `-2.2099` edge `-0.0795` maxDD `-13.6964`
- `market_context_high->equity_4h` score `-3.1899` n `72` status `ready` deltaP `6.7582` edge `0.0671` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-4.5274` n `32` status `ready` deltaP `-4.8611` edge `0.0194` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-7.5612` n `72` status `ready` deltaP `3.1166` edge `-0.184` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-9.229` n `32` status `ready` deltaP `-18.75` edge `-0.1862` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
