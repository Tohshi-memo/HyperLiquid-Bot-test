# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T02:22:31.346102+00:00`
- Price records: `672`
- Market context records: `7093`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.4509` n `162` status `ready` deltaP `17.0562` edge `0.0141` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1372` n `162` status `ready` deltaP `4.6019` edge `0.003` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.3479` n `162` status `ready` deltaP `-0.8594` edge `0.0326` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.3928` n `162` status `ready` deltaP `1.1218` edge `0.0286` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.418` n `162` status `ready` deltaP `2.0034` edge `-0.005` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.5671` n `162` status `ready` deltaP `3.8904` edge `0.0366` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8589` n `162` status `ready` deltaP `-4.3783` edge `-0.0193` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.4131` n `162` status `ready` deltaP `-5.441` edge `-0.0047` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.4425` n `162` status `ready` deltaP `-5.58` edge `-0.0442` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-1.7333` n `162` status `ready` deltaP `-8.3126` edge `-0.0066` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.0005` n `162` status `ready` deltaP `3.5558` edge `-0.0379` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.2952` n `162` status `ready` deltaP `2.2414` edge `-0.0393` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.9119` n `162` status `ready` deltaP `-5.517` edge `-0.075` maxDD `-4.4704`
- `market_context_high->crypto_major_4h` score `-2.9484` n `162` status `ready` deltaP `4.7783` edge `0.0186` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.1753` n `162` status `ready` deltaP `-1.4322` edge `-0.019` maxDD `-22.2831`
- `market_context_high->fx_24h` score `-4.1173` n `162` status `ready` deltaP `-6.4043` edge `-0.0177` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-4.1498` n `162` status `ready` deltaP `-5.7739` edge `-0.009` maxDD `-5.5324`
- `market_context_high->equity_4h` score `-8.2981` n `162` status `ready` deltaP `2.0814` edge `-0.1907` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-8.802` n `162` status `ready` deltaP `-23.0131` edge `-0.0654` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-15.1803` n `162` status `ready` deltaP `-24.3634` edge `-0.1285` maxDD `-43.5947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
