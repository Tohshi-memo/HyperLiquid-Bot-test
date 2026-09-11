# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T21:21:55.661196+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11415`

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

- `news_risk_high->unknown_1h` score `512.4928` n `71` status `ready` deltaP `-4.6049` edge `42.7806` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `24.1029` n `91` status `ready` deltaP `42.2486` edge `1.7499` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `24.1029` n `91` status `ready` deltaP `42.2486` edge `1.7499` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `22.5231` n `30` status `ready` deltaP `47.9514` edge `1.6473` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `21.1933` n `151` status `ready` deltaP `37.1471` edge `1.6012` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `14.4759` n `30` status `ready` deltaP `27.7431` edge `1.066` maxDD `-2.2369`
- `risk_on_high->equity_24h` score `9.4755` n `91` status `ready` deltaP `36.9792` edge `0.5431` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.4755` n `91` status `ready` deltaP `36.9792` edge `0.5431` maxDD `0.0`
- `news_risk_high->equity_24h` score `9.3856` n `30` status `ready` deltaP `30.3125` edge `0.5899` maxDD `-0.1212`
- `market_context_high->equity_24h` score `9.1863` n `151` status `ready` deltaP `36.9792` edge `0.519` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.4897` n `91` status `ready` deltaP `41.9459` edge `0.465` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.4897` n `91` status `ready` deltaP `41.9459` edge `0.465` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `7.7637` n `30` status `ready` deltaP `51.0417` edge `0.3067` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.5927` n `91` status `ready` deltaP `25.021` edge `1.2134` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.5927` n `91` status `ready` deltaP `25.021` edge `1.2134` maxDD `-24.5429`
- `news_risk_high->index_24h` score `7.4936` n `30` status `ready` deltaP `48.1944` edge `0.3125` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `6.5732` n `91` status `ready` deltaP `30.8296` edge `0.4281` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.5732` n `91` status `ready` deltaP `30.8296` edge `0.4281` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.3992` n `91` status `ready` deltaP `51.5644` edge `0.1104` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.3992` n `91` status `ready` deltaP `51.5644` edge `0.1104` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
