# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T21:37:22.085254+00:00`
- Price records: `672`
- Market context records: `3008`
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

- `market_context_high->crypto_alt_24h` score `20.3346` n `98` status `ready` deltaP `7.894` edge `2.0336` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.6851` n `98` status `ready` deltaP `42.8147` edge `0.7827` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `12.3233` n `98` status `ready` deltaP `20.1318` edge `0.9392` maxDD `-1.7175`
- `market_context_high->equity_24h` score `10.4029` n `98` status `ready` deltaP `18.867` edge `0.9415` maxDD `-12.6963`
- `market_context_high->index_24h` score `6.4609` n `98` status `ready` deltaP `18.4772` edge `0.5133` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.4232` n `105` status `ready` deltaP `18.1127` edge `0.1459` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.5902` n `105` status `ready` deltaP `13.0082` edge `0.1694` maxDD `-12.1029`
- `market_context_high->index_4h` score `0.2957` n `105` status `ready` deltaP `17.8107` edge `0.0972` maxDD `-9.9084`
- `market_context_high->commodity_1h` score `-0.0906` n `112` status `ready` deltaP `0.7378` edge `0.0205` maxDD `-0.9706`
- `market_context_high->equity_1h` score `-0.2512` n `112` status `ready` deltaP `4.7423` edge `0.044` maxDD `-5.6254`
- `market_context_high->crypto_alt_4h` score `-0.3014` n `105` status `ready` deltaP `22.1182` edge `0.3687` maxDD `-38.7172`
- `market_context_high->index_1h` score `-0.4026` n `112` status `ready` deltaP `4.4696` edge `0.02` maxDD `-4.1126`
- `market_context_high->fx_1h` score `-0.4134` n `112` status `ready` deltaP `-2.5342` edge `0.0005` maxDD `-0.2615`
- `market_context_high->crypto_alt_1h` score `-0.6706` n `112` status `ready` deltaP `7.7363` edge `0.1055` maxDD `-14.7034`
- `market_context_high->crypto_major_1h` score `-0.9443` n `112` status `ready` deltaP `5.3732` edge `0.0694` maxDD `-15.1032`
- `market_context_high->unknown_1h` score `-1.1081` n `112` status `ready` deltaP `3.1116` edge `-0.04` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-1.1934` n `105` status `ready` deltaP `-10.9524` edge `-0.001` maxDD `-0.6521`
- `market_context_high->unknown_4h` score `-1.5973` n `105` status `ready` deltaP `-2.3055` edge `-0.0124` maxDD `-3.7602`
- `market_context_high->fx_24h` score `-1.8477` n `98` status `ready` deltaP `-6.133` edge `-0.0259` maxDD `-0.6418`
- `market_context_high->metal_1h` score `-1.8699` n `112` status `ready` deltaP `-2.6572` edge `-0.0063` maxDD `-6.8783`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
