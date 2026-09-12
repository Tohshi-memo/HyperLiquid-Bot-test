# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T16:22:25.817587+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12636`

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

- `market_context_high->unknown_24h` score `6725.7912` n `90` status `ready` deltaP `13.2292` edge `560.3996` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `4538.8981` n `45` status `ready` deltaP `15.4514` edge `378.1385` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `4538.8981` n `45` status `ready` deltaP `15.4514` edge `378.1385` maxDD `0.0`
- `news_risk_high->unknown_1h` score `382.9888` n `82` status `ready` deltaP `-5.4002` edge `31.9939` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `23.2576` n `62` status `ready` deltaP `52.0778` edge `1.681` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `17.11` n `45` status `ready` deltaP `39.0625` edge `1.1884` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `17.11` n `45` status `ready` deltaP `39.0625` edge `1.1884` maxDD `-0.8386`
- `news_risk_high->crypto_alt_24h` score `17.0371` n `62` status `ready` deltaP `27.593` edge `1.2846` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `15.1468` n `90` status `ready` deltaP `32.3958` edge `1.129` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `11.4652` n `62` status `ready` deltaP `31.8661` edge `0.7707` maxDD `-1.2164`
- `risk_on_high->equity_24h` score `9.4452` n `45` status `ready` deltaP `39.9306` edge `0.5209` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.4452` n `45` status `ready` deltaP `39.9306` edge `0.5209` maxDD `0.0`
- `market_context_high->equity_24h` score `9.0912` n `90` status `ready` deltaP `39.9306` edge `0.4914` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.5397` n `45` status `ready` deltaP `41.6565` edge `0.4711` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.5397` n `45` status `ready` deltaP `41.6565` edge `0.4711` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `7.7458` n `62` status `ready` deltaP `49.6752` edge `0.3302` maxDD `-0.2708`
- `news_risk_high->index_24h` score `7.411` n `62` status `ready` deltaP `48.0119` edge `0.311` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.8776` n `45` status `ready` deltaP `49.4097` edge `0.0813` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8776` n `45` status `ready` deltaP `49.4097` edge `0.0813` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.1298` n `45` status `ready` deltaP `36.3855` edge `0.1109` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
