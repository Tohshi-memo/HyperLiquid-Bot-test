# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T19:52:35.549670+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9700`

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

- `risk_on_high->commodity_24h` score `6.9996` n `54` status `ready` deltaP `38.8502` edge `0.3243` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.9996` n `54` status `ready` deltaP `38.8502` edge `0.3243` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `1.2303` n `174` status `ready` deltaP `13.4515` edge `0.3422` maxDD `-14.6817`
- `risk_on_high->crypto_major_4h` score `0.5935` n `90` status `ready` deltaP `16.5549` edge `0.2027` maxDD `-10.6246`
- `risk_on_and_context->crypto_major_4h` score `0.5935` n `90` status `ready` deltaP `16.5549` edge `0.2027` maxDD `-10.6246`
- `market_context_high->crypto_major_1h` score `0.4346` n `174` status `ready` deltaP `4.9212` edge `0.0923` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.0375` n `90` status `ready` deltaP `5.4054` edge `0.0055` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0375` n `90` status `ready` deltaP `5.4054` edge `0.0055` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `0.035` n `174` status `ready` deltaP `7.5917` edge `0.1023` maxDD `-7.3329`
- `market_context_high->index_1h` score `-0.2054` n `174` status `ready` deltaP `6.5548` edge `0.0048` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.235` n `90` status `ready` deltaP `1.6216` edge `-0.0029` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.235` n `90` status `ready` deltaP `1.6216` edge `-0.0029` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3323` n `174` status `ready` deltaP `5.4666` edge `0.0079` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.3931` n `174` status `ready` deltaP `9.8581` edge `0.0376` maxDD `-7.2977`
- `risk_on_high->equity_1h` score `-0.4507` n `90` status `ready` deltaP `9.8198` edge `0.0266` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4507` n `90` status `ready` deltaP `9.8198` edge `0.0266` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.5204` n `90` status `ready` deltaP `0.4092` edge `0.0037` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5204` n `90` status `ready` deltaP `0.4092` edge `0.0037` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.5718` n `174` status `ready` deltaP `6.1922` edge `0.0406` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.7387` n `174` status `ready` deltaP `-1.1753` edge `-0.0016` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
