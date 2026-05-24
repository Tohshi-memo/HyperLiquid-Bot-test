# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T00:07:15.731217+00:00`
- Price records: `672`
- Market context records: `1681`
- Flow alert records: `6748`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `8.3969` n `153` status `ready` deltaP `27.201` edge `0.761` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.2402` n `195` status `ready` deltaP `22.8901` edge `0.5505` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8873` n `153` status `ready` deltaP `18.6659` edge `0.3373` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `3.4771` n `195` status `ready` deltaP `19.7162` edge `0.4292` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.8114` n `195` status `ready` deltaP `15.3651` edge `0.2413` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.0579` n `153` status `ready` deltaP `14.3599` edge `0.6078` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.902` n `153` status `ready` deltaP `17.7816` edge `0.5298` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.5496` n `204` status `ready` deltaP `5.6798` edge `0.1103` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.4373` n `153` status `ready` deltaP `25.1634` edge `1.0496` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.1434` n `195` status `ready` deltaP `6.0373` edge `0.0806` maxDD `-3.7119`
- `market_context_high->crypto_major_24h` score `-0.0289` n `153` status `ready` deltaP `23.9524` edge `0.6952` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.0985` n `204` status `ready` deltaP `3.6809` edge `0.0481` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.3898` n `204` status `ready` deltaP `3.2553` edge `0.0732` maxDD `-5.5244`
- `market_context_high->metal_1h` score `-0.5504` n `204` status `ready` deltaP `7.0682` edge `0.0159` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.586` n `204` status `ready` deltaP `-0.0088` edge `0.0144` maxDD `-1.7205`
- `market_context_high->fx_24h` score `-0.5989` n `153` status `ready` deltaP `5.94` edge `0.0154` maxDD `-1.3925`
- `market_context_high->metal_4h` score `-0.6081` n `195` status `ready` deltaP `12.6469` edge `0.1342` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.8842` n `204` status `ready` deltaP `-1.224` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.2228` n `195` status `ready` deltaP `-7.9621` edge `-0.0108` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.1368` n `204` status `ready` deltaP `0.4638` edge `-0.0316` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
