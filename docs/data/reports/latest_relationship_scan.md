# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T22:52:30.216084+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9978`

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

- `risk_on_high->crypto_alt_24h` score `13.089` n `117` status `ready` deltaP `26.6293` edge `0.9362` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.089` n `117` status `ready` deltaP `26.6293` edge `0.9362` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `8.0415` n `241` status `ready` deltaP `19.2845` edge `0.6243` maxDD `-3.9523`
- `risk_on_high->crypto_major_24h` score `7.0963` n `117` status `ready` deltaP `22.3157` edge `1.1678` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.0963` n `117` status `ready` deltaP `22.3157` edge `1.1678` maxDD `-24.5429`
- `risk_on_high->crypto_alt_4h` score `6.6319` n `117` status `ready` deltaP `35.2082` edge `0.3551` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `6.6319` n `117` status `ready` deltaP `35.2082` edge `0.3551` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.6425` n `117` status `ready` deltaP `25.3713` edge `0.3036` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.6425` n `117` status `ready` deltaP `25.3713` edge `0.3036` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.698` n `117` status `ready` deltaP `26.9498` edge `0.0494` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.698` n `117` status `ready` deltaP `26.9498` edge `0.0494` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.9766` n `241` status `ready` deltaP `22.045` edge `0.0571` maxDD `-0.1483`
- `market_context_high->equity_24h` score `1.8809` n `241` status `ready` deltaP `10.4167` edge `0.0873` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.2212` n `117` status `ready` deltaP `4.6958` edge `0.1057` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.2212` n `117` status `ready` deltaP `4.6958` edge `0.1057` maxDD `-1.1521`
- `risk_on_high->equity_24h` score `1.1957` n `117` status `ready` deltaP `10.4167` edge `0.0302` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.1957` n `117` status `ready` deltaP `10.4167` edge `0.0302` maxDD `0.0`
- `risk_on_high->metal_24h` score `0.8035` n `117` status `ready` deltaP `19.7383` edge `0.087` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.8035` n `117` status `ready` deltaP `19.7383` edge `0.087` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.5072` n `117` status `ready` deltaP `14.9714` edge `-0.0044` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
