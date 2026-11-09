# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T04:37:23.947378+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6588`

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

- `market_context_high->equity_24h` score `10.4748` n `32` status `ready` deltaP `17.1875` edge `0.9956` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.6979` n `32` status `ready` deltaP `8.6806` edge `0.2257` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.4554` n `32` status `ready` deltaP `17.3611` edge `0.1171` maxDD `-2.3671`
- `market_context_high->metal_1h` score `0.9433` n `74` status `ready` deltaP `11.7131` edge `0.0333` maxDD `-0.6226`
- `market_context_high->metal_4h` score `0.8682` n `62` status `ready` deltaP `11.8115` edge `0.0851` maxDD `-1.2025`
- `market_context_high->fx_24h` score `0.682` n `32` status `ready` deltaP `10.7639` edge `-0.0061` maxDD `-0.0397`
- `market_context_high->commodity_4h` score `0.6629` n `62` status `ready` deltaP `4.2535` edge `0.0741` maxDD `-1.1102`
- `market_context_high->equity_1h` score `0.6368` n `74` status `ready` deltaP `2.3952` edge `0.1568` maxDD `-5.5762`
- `market_context_high->commodity_1h` score `0.2829` n `74` status `ready` deltaP `8.8728` edge `0.0232` maxDD `-1.7019`
- `market_context_high->index_4h` score `0.257` n `62` status `ready` deltaP `13.7539` edge `0.0341` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.2791` n `74` status `ready` deltaP `2.0958` edge `0.0211` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-0.5485` n `74` status `ready` deltaP `10.9443` edge `0.046` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-0.9294` n `74` status `ready` deltaP `-11.4015` edge `-0.0037` maxDD `-0.4893`
- `market_context_high->metal_24h` score `-1.5536` n `32` status `ready` deltaP `0.6944` edge `-0.1485` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-1.566` n `62` status `ready` deltaP `-7.8629` edge `-0.0055` maxDD `-1.4278`
- `market_context_high->equity_4h` score `-1.6306` n `62` status `ready` deltaP `9.5004` edge `0.1056` maxDD `-24.9053`
- `market_context_high->crypto_major_1h` score `-1.7116` n `74` status `ready` deltaP `3.7425` edge `-0.0345` maxDD `-11.7911`
- `market_context_high->crypto_major_24h` score `-4.6882` n `32` status `ready` deltaP `-4.8611` edge `0.006` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-6.3041` n `62` status `ready` deltaP `8.6005` edge `-0.1158` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-9.0214` n `32` status `ready` deltaP `-18.75` edge `-0.1689` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
