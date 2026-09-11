# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T01:52:26.056024+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11374`

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

- `news_risk_high->unknown_1h` score `1213.6318` n `44` status `ready` deltaP `-4.9673` edge `101.2045` maxDD `-1.1656`
- `news_risk_high->unknown_4h` score `320.9791` n `32` status `ready` deltaP `-23.9329` edge `26.9722` maxDD `-2.1509`
- `risk_on_high->crypto_alt_24h` score `20.4872` n `91` status `ready` deltaP `36.1722` edge `1.4891` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.4872` n `91` status `ready` deltaP `36.1722` edge `1.4891` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `16.25` n `198` status `ready` deltaP `29.0404` edge `1.2433` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.0287` n `91` status `ready` deltaP `42.0983` edge `0.5089` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.0287` n `91` status `ready` deltaP `42.0983` edge `0.5089` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.1533` n `198` status `ready` deltaP `29.1667` edge `0.485` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.7959` n `91` status `ready` deltaP `32.6588` edge `0.5178` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.7959` n `91` status `ready` deltaP `32.6588` edge `0.5178` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2409` n `91` status `ready` deltaP `25.021` edge `1.1683` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2409` n `91` status `ready` deltaP `25.021` edge `1.1683` maxDD `-24.5429`
- `risk_on_high->equity_24h` score `6.6869` n `91` status `ready` deltaP `29.1667` edge `0.3628` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.6869` n `91` status `ready` deltaP `29.1667` edge `0.3628` maxDD `0.0`
- `risk_on_high->index_24h` score `4.7742` n `91` status `ready` deltaP `44.9672` edge `0.1023` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.7742` n `91` status `ready` deltaP `44.9672` edge `0.1023` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.8748` n `198` status `ready` deltaP `39.173` edge `0.1011` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.5502` n `91` status `ready` deltaP `33.0407` edge `0.0849` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.5502` n `91` status `ready` deltaP `33.0407` edge `0.0849` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.3626` n `198` status `ready` deltaP `25.9977` edge `0.1091` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
