# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T16:07:30.288521+00:00`
- Price records: `672`
- Market context records: `4843`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7616`

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

- `market_context_high->unknown_1h` score `13.5018` n `110` status `ready` deltaP `10.4709` edge `1.0971` maxDD `-1.674`
- `market_context_high->unknown_4h` score `10.8766` n `98` status `ready` deltaP `25.0062` edge `0.8183` maxDD `-2.623`
- `market_context_high->unknown_24h` score `4.7672` n `92` status `ready` deltaP `22.8034` edge `0.2795` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `3.6528` n `98` status `ready` deltaP `16.1741` edge `0.3318` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `2.3739` n `98` status `ready` deltaP `12.444` edge `0.3438` maxDD `-7.1265`
- `market_context_high->metal_4h` score `1.4119` n `98` status `ready` deltaP `11.4578` edge `0.1075` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.2751` n `110` status `ready` deltaP `4.6516` edge `0.1081` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.227` n `110` status `ready` deltaP `6.6521` edge `0.087` maxDD `-5.5126`
- `market_context_high->index_4h` score `0.2007` n `98` status `ready` deltaP `6.8255` edge `0.0269` maxDD `-0.7334`
- `market_context_high->equity_1h` score `0.0973` n `110` status `ready` deltaP `3.4758` edge `0.0509` maxDD `-2.928`
- `market_context_high->fx_4h` score `-0.077` n `98` status `ready` deltaP `7.6002` edge `0.0111` maxDD `-0.788`
- `market_context_high->equity_4h` score `-0.1104` n `98` status `ready` deltaP `8.8197` edge `0.0652` maxDD `-6.3852`
- `market_context_high->metal_1h` score `-0.1406` n `110` status `ready` deltaP `1.1649` edge `0.0322` maxDD `-1.3057`
- `market_context_high->commodity_4h` score `-0.2919` n `98` status `ready` deltaP `10.3192` edge `0.011` maxDD `-4.377`
- `market_context_high->commodity_1h` score `-0.3246` n `110` status `ready` deltaP `1.9134` edge `0.0116` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.6087` n `110` status `ready` deltaP `-1.6576` edge `0.0085` maxDD `-0.7054`
- `market_context_high->fx_1h` score `-1.2179` n `110` status `ready` deltaP `-5.4981` edge `-0.0035` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.7961` n `92` status `ready` deltaP `-5.8122` edge `-0.0099` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-3.3948` n `92` status `ready` deltaP `11.5866` edge `-0.0016` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.7375` n `92` status `ready` deltaP `-8.5523` edge `-0.1493` maxDD `-24.085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
