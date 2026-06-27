# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T12:22:30.004860+00:00`
- Price records: `672`
- Market context records: `4933`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9400`

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

- `market_context_high->unknown_1h` score `17.4081` n `101` status `ready` deltaP `10.5798` edge `1.4219` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.5381` n `101` status `ready` deltaP `29.4343` edge `0.8167` maxDD `-1.7801`
- `market_context_high->crypto_alt_4h` score `7.233` n `101` status `ready` deltaP `23.8016` edge `0.5793` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.9617` n `101` status `ready` deltaP `20.5279` edge `0.5657` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `6.0252` n `86` status `ready` deltaP `26.5141` edge `0.3596` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.6688` n `101` status `ready` deltaP `14.4319` edge `0.181` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.3252` n `101` status `ready` deltaP `9.6398` edge `0.1124` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.7757` n `101` status `ready` deltaP `10.3975` edge `0.0415` maxDD `-0.6938`
- `market_context_high->crypto_major_1h` score `0.5584` n `101` status `ready` deltaP `6.2755` edge `0.1336` maxDD `-5.6406`
- `market_context_high->equity_1h` score `0.3943` n `101` status `ready` deltaP `5.8946` edge `0.0686` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.3701` n `101` status `ready` deltaP `6.9425` edge `0.1034` maxDD `-5.5126`
- `market_context_high->metal_1h` score `-0.0344` n `101` status `ready` deltaP `3.2134` edge `0.0337` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2988` n `101` status `ready` deltaP `2.3493` edge `0.012` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5076` n `101` status `ready` deltaP `-0.1038` edge `0.0111` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.8345` n `101` status `ready` deltaP `7.1285` edge `0.0016` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-0.9598` n `101` status `ready` deltaP `-3.5408` edge `-0.0024` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.4595` n `101` status `ready` deltaP `-8.3343` edge `-0.0048` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-1.89` n `86` status `ready` deltaP `-6.0401` edge `-0.0162` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-5.1` n `86` status `ready` deltaP `12.9724` edge `-0.0006` maxDD `-27.5371`
- `market_context_high->index_24h` score `-7.5821` n `86` status `ready` deltaP `-9.9281` edge `-0.1571` maxDD `-24.6845`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
