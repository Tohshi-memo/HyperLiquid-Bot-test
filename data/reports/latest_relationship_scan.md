# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T14:52:33.798343+00:00`
- Price records: `672`
- Market context records: `4733`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7448`

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

- `market_context_high->unknown_1h` score `79.3614` n `141` status `ready` deltaP `15.0911` edge `6.5546` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.3271` n `141` status `ready` deltaP `14.3801` edge `0.4691` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.4098` n `132` status `ready` deltaP `17.1875` edge `0.2619` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3277` n `141` status `ready` deltaP `2.1584` edge `0.0232` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.579` n `141` status `ready` deltaP `5.2197` edge `0.0004` maxDD `-5.7542`
- `market_context_high->fx_4h` score `-0.8653` n `141` status `ready` deltaP `-0.2422` edge `-0.0019` maxDD `-1.9274`
- `market_context_high->equity_1h` score `-0.9178` n `141` status `ready` deltaP `-1.2135` edge `-0.012` maxDD `-5.4726`
- `market_context_high->index_1h` score `-1.0107` n `141` status `ready` deltaP `-3.3093` edge `-0.0071` maxDD `-2.6999`
- `market_context_high->equity_4h` score `-1.0678` n `141` status `ready` deltaP `3.4434` edge `0.0129` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-1.4001` n `141` status `ready` deltaP `-6.3915` edge `-0.0061` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.5183` n `141` status `ready` deltaP `8.6457` edge `0.0266` maxDD `-9.1941`
- `market_context_high->metal_1h` score `-2.7456` n `141` status `ready` deltaP `-5.3829` edge `-0.0751` maxDD `-15.9475`
- `market_context_high->crypto_alt_1h` score `-2.867` n `141` status `ready` deltaP `0.1338` edge `-0.0539` maxDD `-21.1642`
- `market_context_high->crypto_major_1h` score `-3.5107` n `141` status `ready` deltaP `-0.4969` edge `-0.0727` maxDD `-27.2597`
- `market_context_high->commodity_24h` score `-4.1812` n `132` status `ready` deltaP `16.7614` edge `0.0646` maxDD `-28.6488`
- `market_context_high->fx_24h` score `-4.7607` n `132` status `ready` deltaP `-14.1572` edge `-0.0195` maxDD `-5.2943`
- `market_context_high->crypto_alt_4h` score `-7.2278` n `141` status `ready` deltaP `-1.0574` edge `-0.1086` maxDD `-59.5456`
- `market_context_high->index_24h` score `-8.1811` n `132` status `ready` deltaP `-11.7266` edge `-0.1038` maxDD `-27.3155`
- `market_context_high->metal_4h` score `-8.5514` n `141` status `ready` deltaP `1.8455` edge `-0.259` maxDD `-62.6377`
- `market_context_high->crypto_major_4h` score `-10.1464` n `141` status `ready` deltaP `-0.6465` edge `-0.2229` maxDD `-80.5555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
