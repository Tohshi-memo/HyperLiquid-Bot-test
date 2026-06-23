# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T03:22:26.901215+00:00`
- Price records: `672`
- Market context records: `4477`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11059`

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

- `risk_on_high->unknown_4h` score `124.0486` n `49` status `ready` deltaP `3.111` edge `10.4997` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.0486` n `49` status `ready` deltaP `3.111` edge `10.4997` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `32.3406` n `230` status `ready` deltaP `3.7048` edge `2.8209` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `14.6841` n `230` status `ready` deltaP `3.8919` edge `1.7442` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `4.0492` n `49` status `ready` deltaP `38.7195` edge `0.0793` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `4.0492` n `49` status `ready` deltaP `38.7195` edge `0.0793` maxDD `0.0`
- `risk_on_high->metal_24h` score `3.3189` n `44` status `ready` deltaP `-13.2733` edge `0.5754` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.3189` n `44` status `ready` deltaP `-13.2733` edge `0.5754` maxDD `-1.9133`
- `risk_on_high->unknown_24h` score `2.7854` n `44` status `ready` deltaP `14.3466` edge `0.2168` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.7854` n `44` status `ready` deltaP `14.3466` edge `0.2168` maxDD `-5.0928`
- `risk_on_high->equity_24h` score `2.7762` n `44` status `ready` deltaP `23.4375` edge `0.0751` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.7762` n `44` status `ready` deltaP `23.4375` edge `0.0751` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `2.5537` n `49` status `ready` deltaP `20.7846` edge `0.1408` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.5537` n `49` status `ready` deltaP `20.7846` edge `0.1408` maxDD `-2.6576`
- `risk_on_high->index_24h` score `2.3597` n `44` status `ready` deltaP `25.5208` edge `0.0265` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.3597` n `44` status `ready` deltaP `25.5208` edge `0.0265` maxDD `0.0`
- `risk_on_high->metal_4h` score `1.4962` n `49` status `ready` deltaP `12.5622` edge `0.0745` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.4962` n `49` status `ready` deltaP `12.5622` edge `0.0745` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.0882` n `49` status `ready` deltaP `14.5424` edge `0.028` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.0882` n `49` status `ready` deltaP `14.5424` edge `0.028` maxDD `-0.7415`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
