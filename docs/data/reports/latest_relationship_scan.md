# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T23:22:24.467720+00:00`
- Price records: `672`
- Market context records: `3016`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `21.4134` n `98` status `ready` deltaP `9.1093` edge `2.1154` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.9476` n `98` status `ready` deltaP `43.3355` edge `0.8011` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `12.7049` n `98` status `ready` deltaP `21.3471` edge `0.9629` maxDD `-1.7175`
- `market_context_high->equity_24h` score `11.5105` n `98` status `ready` deltaP `20.0822` edge `1.0257` maxDD `-12.6963`
- `market_context_high->index_24h` score `7.1785` n `98` status `ready` deltaP `19.6925` edge `0.565` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.4408` n `107` status `ready` deltaP `18.1516` edge `0.1471` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.7135` n `107` status `ready` deltaP `14.0885` edge `0.178` maxDD `-12.1029`
- `market_context_high->index_4h` score `0.2245` n `107` status `ready` deltaP `17.3823` edge `0.0976` maxDD `-10.4423`
- `market_context_high->crypto_alt_4h` score `0.0672` n `107` status `ready` deltaP `22.9827` edge `0.4102` maxDD `-38.7172`
- `market_context_high->commodity_1h` score `-0.0894` n `119` status `ready` deltaP `1.502` edge `0.0248` maxDD `-1.7142`
- `market_context_high->equity_1h` score `-0.3116` n `119` status `ready` deltaP `3.8495` edge `0.0422` maxDD `-5.6254`
- `market_context_high->index_1h` score `-0.3659` n `119` status `ready` deltaP `4.6797` edge `0.0233` maxDD `-4.1126`
- `market_context_high->crypto_alt_1h` score `-0.6087` n `119` status `ready` deltaP `6.4522` edge `0.0919` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-0.66` n `119` status `ready` deltaP `-2.8493` edge `0.0006` maxDD `-0.2615`
- `market_context_high->unknown_1h` score `-0.9592` n `119` status `ready` deltaP `3.6079` edge `-0.0309` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-1.0836` n `119` status `ready` deltaP `4.1048` edge `0.06` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.15` n `107` status `ready` deltaP `-10.118` edge `-0.001` maxDD `-0.6521`
- `market_context_high->metal_1h` score `-1.1753` n `119` status `ready` deltaP `-2.2606` edge `-0.0038` maxDD `-6.8783`
- `market_context_high->unknown_4h` score `-1.5232` n `107` status `ready` deltaP `-2.429` edge `-0.0054` maxDD `-3.7602`
- `market_context_high->fx_24h` score `-1.7397` n `98` status `ready` deltaP `-4.9178` edge `-0.025` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
