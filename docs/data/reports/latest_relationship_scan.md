# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T18:22:28.853644+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4888`

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

- `market_context_high->unknown_1h` score `358.9954` n `50` status `ready` deltaP `10.8743` edge `29.8487` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.5253` n `50` status `ready` deltaP `10.3659` edge `24.308` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.6847` n `73` status `ready` deltaP `39.9686` edge `1.0615` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `9.3594` n `50` status `ready` deltaP `16.7083` edge `0.8389` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `8.9598` n `50` status `ready` deltaP `31.8264` edge `0.6761` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.9321` n `73` status `ready` deltaP `32.0586` edge `0.5791` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.1797` n `50` status `ready` deltaP `17.5427` edge `0.5517` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.1956` n `50` status `ready` deltaP `15.7317` edge `0.457` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `5.0166` n `116` status `ready` deltaP `21.5938` edge `0.4085` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.1378` n `50` status `ready` deltaP `14.6527` edge `0.2301` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.042` n `50` status `ready` deltaP `14.2994` edge `0.2032` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7519` n `50` status `ready` deltaP `30.7073` edge `0.0381` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.4747` n `116` status `ready` deltaP `22.0984` edge `0.1285` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.6325` n `50` status `ready` deltaP `8.2778` edge `0.3403` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.4887` n `73` status `ready` deltaP `5.9908` edge `0.4663` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4232` n `50` status `ready` deltaP `20.0419` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3402` n `73` status `ready` deltaP `13.009` edge `0.2125` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `1.2362` n `116` status `ready` deltaP `14.1979` edge `0.2948` maxDD `-10.477`
- `news_risk_high->crypto_alt_1h` score `0.9903` n `116` status `ready` deltaP `5.5493` edge `0.1016` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.7805` n `50` status `ready` deltaP `17.0347` edge `0.0883` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
