# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T04:52:26.671467+00:00`
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

- `market_context_high->equity_24h` score `10.3637` n `32` status `ready` deltaP `17.0139` edge `0.9875` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.66` n `32` status `ready` deltaP `8.5069` edge `0.2237` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.4417` n `32` status `ready` deltaP `17.1875` edge `0.1165` maxDD `-2.3671`
- `market_context_high->metal_1h` score `0.968` n `75` status `ready` deltaP `12.0679` edge `0.033` maxDD `-0.6226`
- `market_context_high->metal_4h` score `0.9054` n `63` status `ready` deltaP `12.4516` edge `0.0856` maxDD `-1.2025`
- `market_context_high->commodity_4h` score `0.7352` n `63` status `ready` deltaP `4.7668` edge `0.0767` maxDD `-1.1102`
- `market_context_high->fx_24h` score `0.6832` n `32` status `ready` deltaP `10.7639` edge `-0.006` maxDD `-0.0397`
- `market_context_high->equity_1h` score `0.3371` n `75` status `ready` deltaP `1.7285` edge `0.1514` maxDD `-5.5762`
- `market_context_high->commodity_1h` score `0.3159` n `75` status `ready` deltaP `9.2096` edge `0.0237` maxDD `-1.7019`
- `market_context_high->index_4h` score `0.2908` n `63` status `ready` deltaP `14.1648` edge `0.0357` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.3301` n `75` status `ready` deltaP `1.5788` edge `0.0203` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-0.6087` n `75` status `ready` deltaP `10.2056` edge `0.0432` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-0.9595` n `75` status `ready` deltaP `-11.9601` edge `-0.0038` maxDD `-0.4919`
- `market_context_high->equity_4h` score `-1.4926` n `63` status `ready` deltaP `10.0392` edge `0.1197` maxDD `-24.9053`
- `market_context_high->metal_24h` score `-1.5712` n `32` status `ready` deltaP `0.5208` edge `-0.1496` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-1.6386` n `63` status `ready` deltaP `-8.4786` edge `-0.006` maxDD `-1.4712`
- `market_context_high->crypto_major_1h` score `-1.7705` n `75` status `ready` deltaP `3.0758` edge `-0.0376` maxDD `-11.7911`
- `market_context_high->crypto_major_24h` score `-4.6906` n `32` status `ready` deltaP `-4.8611` edge `0.0058` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-6.2219` n `63` status `ready` deltaP `9.2673` edge `-0.1134` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-9.0658` n `32` status `ready` deltaP `-18.75` edge `-0.1726` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
