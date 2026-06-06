# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T14:22:22.547299+00:00`
- Price records: `672`
- Market context records: `3081`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6911`

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

- `market_context_high->crypto_alt_24h` score `17.3904` n `87` status `ready` deltaP `12.3922` edge `2.5386` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `15.3085` n `87` status `ready` deltaP `47.3359` edge `0.9891` maxDD `-1.6506`
- `market_context_high->unknown_24h` score `14.2246` n `87` status `ready` deltaP `23.1681` edge `1.0774` maxDD `-1.7175`
- `market_context_high->index_24h` score `12.762` n `87` status `ready` deltaP `33.5848` edge `0.9569` maxDD `-7.0507`
- `market_context_high->equity_24h` score `10.7071` n `87` status `ready` deltaP `24.1559` edge `1.5396` maxDD `-22.2351`
- `market_context_high->commodity_4h` score `2.7833` n `123` status `ready` deltaP `17.2256` edge `0.1629` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `-0.117` n `123` status `ready` deltaP `2.998` edge `0.0756` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.2465` n `125` status `ready` deltaP `0.0024` edge `0.0217` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.6079` n `125` status `ready` deltaP `2.3461` edge `0.0127` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.7309` n `125` status `ready` deltaP `4.1473` edge `0.0916` maxDD `-14.7034`
- `market_context_high->unknown_1h` score `-1.0059` n `125` status `ready` deltaP `1.509` edge `-0.0208` maxDD `-3.1801`
- `market_context_high->fx_24h` score `-1.086` n `87` status `ready` deltaP `0.0658` edge `-0.0042` maxDD `-0.6057`
- `market_context_high->fx_1h` score `-1.1018` n `125` status `ready` deltaP `-7.8527` edge `-0.0022` maxDD `-0.3147`
- `market_context_high->equity_1h` score `-1.2631` n `125` status `ready` deltaP `-2.0` edge `-0.0013` maxDD `-8.7845`
- `market_context_high->fx_4h` score `-1.3205` n `123` status `ready` deltaP `-11.8395` edge `-0.006` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4215` n `123` status `ready` deltaP `8.9939` edge `0.0487` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.954` n `125` status `ready` deltaP `0.3389` edge `0.0612` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.2084` n `125` status `ready` deltaP `-5.8084` edge `-0.0085` maxDD `-7.278`
- `market_context_high->crypto_alt_4h` score `-3.119` n `123` status `ready` deltaP `17.5813` edge `0.2874` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.7865` n `123` status `ready` deltaP `7.2155` edge `-0.0097` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
