# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T21:37:24.884325+00:00`
- Price records: `672`
- Market context records: `7071`
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

- `market_context_high->fx_4h` score `0.7023` n `180` status `ready` deltaP `17.4492` edge `0.0122` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.1631` n `180` status `ready` deltaP `0.6853` edge `0.0377` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.1632` n `180` status `ready` deltaP `4.338` edge `0.0026` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.3338` n `180` status `ready` deltaP `1.5369` edge `0.0334` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5919` n `180` status `ready` deltaP `3.8024` edge `0.034` maxDD `-7.1523`
- `market_context_high->index_1h` score `-0.7263` n `180` status `ready` deltaP `-0.9348` edge `-0.0041` maxDD `-2.2895`
- `market_context_high->unknown_4h` score `-0.7523` n `180` status `ready` deltaP `-5.0474` edge `0.1344` maxDD `-4.742`
- `market_context_high->commodity_1h` score `-0.8674` n `180` status `ready` deltaP `-4.511` edge `-0.0195` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.3783` n `180` status `ready` deltaP `-5.1863` edge `-0.0035` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.6579` n `180` status `ready` deltaP `-7.5779` edge `-0.046` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.8826` n `180` status `ready` deltaP `4.3845` edge `-0.0283` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.2643` n `180` status `ready` deltaP `2.0562` edge `-0.0341` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.4573` n `180` status `ready` deltaP `-2.6389` edge `-0.0563` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.9691` n `180` status `ready` deltaP `0.1185` edge `-0.0029` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.0849` n `180` status `ready` deltaP `2.5271` edge `0.0161` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.6251` n `180` status `ready` deltaP `-0.9722` edge `-0.0129` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-3.7035` n `180` status `ready` deltaP `-0.9011` edge `-0.0043` maxDD `-5.5324`
- `market_context_high->unknown_24h` score `-4.3482` n `180` status `ready` deltaP `-16.6319` edge `0.0681` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.9274` n `180` status `ready` deltaP `4.126` edge `-0.1568` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.7181` n `180` status `ready` deltaP `-22.1527` edge `-0.1028` maxDD `-44.4154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
