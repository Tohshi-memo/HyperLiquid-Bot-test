# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T18:07:40.674706+00:00`
- Price records: `672`
- Market context records: `4014`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10566`

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

- `risk_on_high->unknown_4h` score `146.8054` n `40` status `ready` deltaP `-4.7527` edge `12.4471` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `146.8054` n `40` status `ready` deltaP `-4.7527` edge `12.4471` maxDD `-10.864`
- `market_context_high->unknown_24h` score `48.203` n `135` status `ready` deltaP `-3.9181` edge `4.4459` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `26.3643` n `146` status `ready` deltaP `2.1309` edge `2.7251` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `7.2454` n `40` status `ready` deltaP `39.688` edge `0.3392` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.2454` n `40` status `ready` deltaP `39.688` edge `0.3392` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.5517` n `40` status `ready` deltaP `36.465` edge `0.0576` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.5517` n `40` status `ready` deltaP `36.465` edge `0.0576` maxDD `-0.0446`
- `market_context_high->index_24h` score `3.4498` n `135` status `ready` deltaP `25.9015` edge `0.1633` maxDD `-3.2125`
- `market_context_high->metal_24h` score `2.6214` n `135` status `ready` deltaP `14.0779` edge `0.2435` maxDD `-6.5125`
- `market_context_high->equity_4h` score `1.7395` n `146` status `ready` deltaP `19.102` edge `0.1457` maxDD `-6.9137`
- `risk_on_high->index_24h` score `1.6002` n `40` status `ready` deltaP `27.383` edge `-0.0492` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.6002` n `40` status `ready` deltaP `27.383` edge `-0.0492` maxDD `0.0`
- `market_context_high->equity_1h` score `1.2441` n `149` status `ready` deltaP `8.5862` edge `0.1024` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `1.1731` n `40` status `ready` deltaP `19.532` edge `0.0341` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.1731` n `40` status `ready` deltaP `19.532` edge `0.0341` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.0295` n `149` status `ready` deltaP `10.1706` edge `0.0722` maxDD `-2.3372`
- `risk_on_high->commodity_24h` score `0.9836` n `40` status `ready` deltaP `4.2028` edge `0.2821` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.9836` n `40` status `ready` deltaP `4.2028` edge `0.2821` maxDD `-12.9187`
- `market_context_high->equity_24h` score `0.9522` n `135` status `ready` deltaP `15.9843` edge `0.2726` maxDD `-14.318`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
