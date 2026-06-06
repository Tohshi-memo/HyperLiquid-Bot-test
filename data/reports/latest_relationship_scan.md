# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T14:37:24.503734+00:00`
- Price records: `672`
- Market context records: `3082`
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

- `market_context_high->crypto_alt_24h` score `17.5074` n `86` status `ready` deltaP `12.7664` edge `2.5511` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `15.4313` n `86` status `ready` deltaP `47.4161` edge `0.9988` maxDD `-1.6506`
- `market_context_high->unknown_24h` score `14.4056` n `86` status `ready` deltaP `22.9409` edge `1.094` maxDD `-1.7175`
- `market_context_high->index_24h` score `12.9604` n `86` status `ready` deltaP `34.5203` edge `0.9672` maxDD `-7.0507`
- `market_context_high->equity_24h` score `10.7032` n `86` status `ready` deltaP `23.9018` edge `1.5408` maxDD `-22.2351`
- `market_context_high->commodity_4h` score `2.8658` n `122` status `ready` deltaP `17.6729` edge `0.1668` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `-0.0409` n `122` status `ready` deltaP `3.3187` edge `0.0798` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.2453` n `125` status `ready` deltaP `0.0024` edge `0.0218` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5632` n `125` status `ready` deltaP `2.9964` edge `0.0141` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.6589` n `125` status `ready` deltaP `4.7976` edge `0.0965` maxDD `-14.7034`
- `market_context_high->unknown_1h` score `-0.8471` n `125` status `ready` deltaP `2.1593` edge `-0.0119` maxDD `-3.1801`
- `market_context_high->fx_24h` score `-1.0145` n `86` status `ready` deltaP `0.8277` edge `-0.0036` maxDD `-0.5832`
- `market_context_high->fx_1h` score `-1.1538` n `125` status `ready` deltaP `-8.503` edge `-0.0022` maxDD `-0.3147`
- `market_context_high->equity_1h` score `-1.2207` n `125` status `ready` deltaP `-1.3497` edge `-0.0002` maxDD `-8.7845`
- `market_context_high->fx_4h` score `-1.3128` n `122` status `ready` deltaP `-11.7053` edge `-0.0059` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4094` n `122` status `ready` deltaP `9.3013` edge `0.0482` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.8515` n `125` status `ready` deltaP `0.9892` edge `0.0654` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.2821` n `125` status `ready` deltaP `-6.4587` edge `-0.01` maxDD `-7.3029`
- `market_context_high->crypto_alt_4h` score `-3.1782` n `122` status `ready` deltaP `17.2082` edge `0.2823` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.7905` n `122` status `ready` deltaP `7.5294` edge `-0.0123` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
