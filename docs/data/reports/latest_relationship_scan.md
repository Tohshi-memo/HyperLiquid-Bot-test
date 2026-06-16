# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T00:37:32.364379+00:00`
- Price records: `672`
- Market context records: `4042`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10624`

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

- `risk_on_high->unknown_4h` score `145.6241` n `40` status `ready` deltaP `-7.7439` edge `12.3686` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.6241` n `40` status `ready` deltaP `-7.7439` edge `12.3686` maxDD `-10.864`
- `market_context_high->unknown_24h` score `46.5362` n `134` status `ready` deltaP `-7.7589` edge `4.3326` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `22.9101` n `156` status `ready` deltaP `2.0638` edge `2.4377` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `4.4898` n `40` status `ready` deltaP `35.182` edge `0.1396` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.4898` n `40` status `ready` deltaP `35.182` edge `0.1396` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.3445` n `40` status `ready` deltaP `36.8293` edge `0.0379` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.3445` n `40` status `ready` deltaP `36.8293` edge `0.0379` maxDD `-0.0446`
- `market_context_high->index_24h` score `2.5024` n `134` status `ready` deltaP `22.1306` edge `0.0822` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.6247` n `156` status `ready` deltaP `15.6114` edge `0.1594` maxDD `-6.9137`
- `market_context_high->metal_24h` score `1.3053` n `134` status `ready` deltaP `10.6612` edge `0.1364` maxDD `-4.8962`
- `market_context_high->equity_1h` score `0.9487` n `162` status `ready` deltaP `6.8437` edge `0.0894` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `0.8993` n `40` status `ready` deltaP `18.689` edge `0.0169` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.8993` n `40` status `ready` deltaP `18.689` edge `0.0169` maxDD `-2.6576`
- `risk_on_high->equity_1h` score `0.368` n `40` status `ready` deltaP `10.7635` edge `-0.002` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.368` n `40` status `ready` deltaP `10.7635` edge `-0.002` maxDD `-0.7937`
- `risk_on_high->commodity_24h` score `0.3599` n `40` status `ready` deltaP `1.7764` edge `0.2463` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.3599` n `40` status `ready` deltaP `1.7764` edge `0.2463` maxDD `-12.9187`
- `market_context_high->metal_1h` score `0.3105` n `162` status `ready` deltaP `9.372` edge `0.0436` maxDD `-3.3018`
- `market_context_high->crypto_major_1h` score `0.27` n `162` status `ready` deltaP `7.3316` edge `0.0458` maxDD `-3.7739`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
