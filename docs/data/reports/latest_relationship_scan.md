# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T00:07:30.462794+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11823`

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

- `market_context_high->unknown_24h` score `16.4304` n `85` status `ready` deltaP `17.3999` edge `1.2575` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.5189` n `90` status `ready` deltaP `1.7479` edge `0.5478` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.6466` n `90` status `ready` deltaP `17.8422` edge `0.1029` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.313` n `85` status `ready` deltaP `2.2447` edge `0.2702` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.0212` n `85` status `ready` deltaP `25.1245` edge `0.084` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3097` n `90` status `ready` deltaP `5.9414` edge `0.0278` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1135` n `90` status `ready` deltaP `7.1557` edge `-0.0034` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0616` n `90` status `ready` deltaP `13.0048` edge `0.0072` maxDD `-1.8797`
- `market_context_high->crypto_alt_24h` score `-0.5152` n `85` status `ready` deltaP `6.6237` edge `0.0341` maxDD `-4.5445`
- `market_context_high->metal_1h` score `-0.5215` n `90` status `ready` deltaP `-1.3074` edge `-0.0087` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5635` n `90` status `ready` deltaP `-0.1563` edge `-0.0178` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.6658` n `90` status `ready` deltaP `3.9465` edge `0.0118` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.6985` n `90` status `ready` deltaP `-2.0093` edge `-0.0051` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.035` n `90` status `ready` deltaP `3.0284` edge `-0.0139` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.6517` n `90` status `ready` deltaP `4.3513` edge `-0.0872` maxDD `-10.619`
- `market_context_high->index_24h` score `-1.7042` n `85` status `ready` deltaP `-5.3554` edge `0.0367` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.045` n `90` status `ready` deltaP `-11.8259` edge `-0.0579` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-3.3145` n `90` status `ready` deltaP `-10.8117` edge `-0.0668` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4072` n `90` status `ready` deltaP `2.0492` edge `-0.2529` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.5737` n `85` status `ready` deltaP `4.6589` edge `-0.1404` maxDD `-45.6753`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
