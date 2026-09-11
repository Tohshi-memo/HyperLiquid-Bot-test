# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T05:52:25.516113+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12312`

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

- `news_risk_high->unknown_1h` score `775.1355` n `58` status `ready` deltaP `-6.7055` edge `64.6815` maxDD `-1.7068`
- `news_risk_high->unknown_4h` score `176.3326` n `48` status `ready` deltaP `-26.7277` edge `14.9619` maxDD `-4.1464`
- `risk_on_high->crypto_alt_24h` score `21.2024` n `91` status `ready` deltaP `37.3874` edge `1.5406` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `21.2024` n `91` status `ready` deltaP `37.3874` edge `1.5406` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `18.3621` n `184` status `ready` deltaP `34.1862` edge `1.385` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.9027` n `91` status `ready` deltaP `41.1837` edge `0.5045` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9027` n `91` status `ready` deltaP `41.1837` edge `0.5045` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.8532` n `184` status `ready` deltaP `31.9444` edge `0.5248` maxDD `0.0`
- `risk_on_high->equity_24h` score `7.9232` n `91` status `ready` deltaP `31.9444` edge `0.4473` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.9232` n `91` status `ready` deltaP `31.9444` edge `0.4473` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.6895` n `91` status `ready` deltaP `32.0491` edge `0.513` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.6895` n `91` status `ready` deltaP `32.0491` edge `0.513` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2885` n `91` status `ready` deltaP `25.021` edge `1.1744` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2885` n `91` status `ready` deltaP `25.021` edge `1.1744` maxDD `-24.5429`
- `risk_on_high->index_24h` score `5.138` n `91` status `ready` deltaP `47.745` edge `0.1141` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.138` n `91` status `ready` deltaP `47.745` edge `0.1141` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.1401` n `184` status `ready` deltaP `41.2591` edge `0.1093` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.737` n `91` status `ready` deltaP `34.5651` edge `0.0903` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.737` n `91` status `ready` deltaP `34.5651` edge `0.0903` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.5293` n `184` status `ready` deltaP `27.5715` edge `0.1125` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
