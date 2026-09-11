# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T16:22:27.555551+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12499`

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

- `news_risk_high->unknown_1h` score `727.5677` n `60` status `ready` deltaP `-5.5788` edge `60.71` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `23.2075` n `91` status `ready` deltaP `41.9013` edge `1.6776` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `23.2075` n `91` status `ready` deltaP `41.9013` edge `1.6776` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `20.549` n `153` status `ready` deltaP `36.9383` edge `1.5489` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `9.5703` n `91` status `ready` deltaP `36.9792` edge `0.551` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.5703` n `91` status `ready` deltaP `36.9792` edge `0.551` maxDD `0.0`
- `market_context_high->equity_24h` score `9.3051` n `153` status `ready` deltaP `36.9792` edge `0.5289` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.1069` n `91` status `ready` deltaP `41.0312` edge `0.4392` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.1069` n `91` status `ready` deltaP `41.0312` edge `0.4392` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `7.2705` n `91` status `ready` deltaP `25.021` edge `1.1721` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2705` n `91` status `ready` deltaP `25.021` edge `1.1721` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `6.2996` n `91` status `ready` deltaP `30.8296` edge `0.4053` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.2996` n `91` status `ready` deltaP `30.8296` edge `0.4053` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.5247` n `91` status `ready` deltaP `51.738` edge `0.1197` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.5247` n `91` status `ready` deltaP `51.738` edge `0.1197` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.3676` n `153` status `ready` deltaP `43.9236` edge `0.1105` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.5876` n `91` status `ready` deltaP `34.1078` edge `0.0809` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.5876` n `91` status `ready` deltaP `34.1078` edge `0.0809` maxDD `-0.079`
- `market_context_high->crypto_alt_4h` score `3.3856` n `153` status `ready` deltaP `23.8582` edge `0.2936` maxDD `-7.6417`
- `market_context_high->equity_4h` score `1.9892` n `153` status `ready` deltaP `26.9757` edge `0.0686` maxDD `-2.6138`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
