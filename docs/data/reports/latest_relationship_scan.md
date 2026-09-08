# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T00:52:25.033789+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10313`

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

- `market_context_high->unknown_24h` score `3224.7957` n `241` status `ready` deltaP `19.1354` edge `268.6106` maxDD `-0.0819`
- `risk_on_high->unknown_24h` score `3195.4872` n `117` status `ready` deltaP `19.9653` edge `266.1575` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `3195.4872` n `117` status `ready` deltaP `19.9653` edge `266.1575` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `9.4618` n `117` status `ready` deltaP `25.2404` edge `0.6432` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `9.4618` n `117` status `ready` deltaP `25.2404` edge `0.6432` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.9468` n `117` status `ready` deltaP `31.5497` edge `0.3224` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.9468` n `117` status `ready` deltaP `31.5497` edge `0.3224` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.3132` n `117` status `ready` deltaP `21.1005` edge `0.9473` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.3132` n `117` status `ready` deltaP `21.1005` edge `0.9473` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8699` n `117` status `ready` deltaP `25.8287` edge `0.3195` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8699` n `117` status `ready` deltaP `25.8287` edge `0.3195` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `4.4144` n `241` status `ready` deltaP `17.8956` edge `0.3313` maxDD `-3.9523`
- `market_context_high->equity_24h` score `2.0224` n `241` status `ready` deltaP `11.2847` edge `0.0933` maxDD `0.0`
- `risk_on_high->index_24h` score `1.3788` n `117` status `ready` deltaP `13.2345` edge `0.0309` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.3788` n `117` status `ready` deltaP `13.2345` edge `0.0309` maxDD `-0.0051`
- `risk_on_high->equity_24h` score `1.3372` n `117` status `ready` deltaP `11.2847` edge `0.0362` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.3372` n `117` status `ready` deltaP `11.2847` edge `0.0362` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `0.9801` n `117` status `ready` deltaP `4.2467` edge `0.0886` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9801` n `117` status `ready` deltaP `4.2467` edge `0.0886` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.6573` n `241` status `ready` deltaP `8.3297` edge `0.0386` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
