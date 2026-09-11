# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T05:37:27.902174+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12302`

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

- `news_risk_high->unknown_1h` score `775.4463` n `58` status `ready` deltaP `-6.5558` edge `64.7064` maxDD `-1.7068`
- `news_risk_high->unknown_4h` score `221.9654` n `47` status `ready` deltaP `-27.7276` edge `18.7713` maxDD `-4.1464`
- `risk_on_high->crypto_alt_24h` score `21.1309` n `91` status `ready` deltaP `37.2138` edge `1.5358` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `21.1309` n `91` status `ready` deltaP `37.2138` edge `1.5358` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `18.2775` n `185` status `ready` deltaP `34.0597` edge `1.3788` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.8907` n `91` status `ready` deltaP `41.1837` edge `0.5035` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.8907` n `91` status `ready` deltaP `41.1837` edge `0.5035` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.8213` n `185` status `ready` deltaP `31.7708` edge `0.5233` maxDD `0.0`
- `risk_on_high->equity_24h` score `7.8505` n `91` status `ready` deltaP `31.7708` edge `0.4424` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.8505` n `91` status `ready` deltaP `31.7708` edge `0.4424` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.6907` n `91` status `ready` deltaP `32.0491` edge `0.5131` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.6907` n `91` status `ready` deltaP `32.0491` edge `0.5131` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2846` n `91` status `ready` deltaP `25.021` edge `1.1739` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2846` n `91` status `ready` deltaP `25.021` edge `1.1739` maxDD `-24.5429`
- `risk_on_high->index_24h` score `5.1169` n `91` status `ready` deltaP `47.5714` edge `0.1135` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.1169` n `91` status `ready` deltaP `47.5714` edge `0.1135` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.1244` n `185` status `ready` deltaP `41.1384` edge `0.1088` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.737` n `91` status `ready` deltaP `34.5651` edge `0.0903` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.737` n `91` status `ready` deltaP `34.5651` edge `0.0903` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.5448` n `185` status `ready` deltaP `27.645` edge `0.1133` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
