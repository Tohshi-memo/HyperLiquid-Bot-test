# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T19:37:29.753789+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10148`

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

- `risk_on_high->crypto_alt_24h` score `11.142` n `117` status `ready` deltaP `24.3723` edge `0.789` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `11.142` n `117` status `ready` deltaP `24.3723` edge `0.789` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `6.0946` n `241` status `ready` deltaP `17.0275` edge `0.4771` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `5.9193` n `117` status `ready` deltaP `33.5314` edge `0.3069` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.9193` n `117` status `ready` deltaP `33.5314` edge `0.3069` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.784` n `117` status `ready` deltaP `20.0588` edge `1.0146` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.784` n `117` status `ready` deltaP `20.0588` edge `1.0146` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.1078` n `117` status `ready` deltaP `23.847` edge `0.2692` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.1078` n `117` status `ready` deltaP `23.847` edge `0.2692` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.4347` n `117` status `ready` deltaP `24.6928` edge `0.0425` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.4347` n `117` status `ready` deltaP `24.6928` edge `0.0425` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.7132` n `241` status `ready` deltaP `19.788` edge `0.0502` maxDD `-0.1483`
- `market_context_high->equity_24h` score `1.2036` n `241` status `ready` deltaP `8.1597` edge `0.0459` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `0.9693` n `117` status `ready` deltaP `4.097` edge `0.0887` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9693` n `117` status `ready` deltaP `4.097` edge `0.0887` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.7559` n `117` status `ready` deltaP `19.7383` edge `0.0809` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.7559` n `117` status `ready` deltaP `19.7383` edge `0.0809` maxDD `-0.9131`
- `risk_on_high->equity_24h` score `0.5184` n `117` status `ready` deltaP `8.1597` edge `-0.0112` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.5184` n `117` status `ready` deltaP `8.1597` edge `-0.0112` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.3658` n `117` status `ready` deltaP `13.7738` edge `-0.0082` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
