# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T04:52:27.435938+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12256`

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

- `news_risk_high->unknown_1h` score `819.2142` n `56` status `ready` deltaP `-7.6026` edge `68.3607` maxDD `-1.7068`
- `news_risk_high->unknown_4h` score `387.7269` n `44` status `ready` deltaP `-29.3792` edge `32.5934` maxDD `-3.9573`
- `risk_on_high->crypto_alt_24h` score `20.9753` n `91` status `ready` deltaP `36.693` edge `1.5263` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.9753` n `91` status `ready` deltaP `36.693` edge `1.5263` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `18.0093` n `187` status `ready` deltaP `33.6314` edge `1.3593` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.8739` n `91` status `ready` deltaP `41.1837` edge `0.5021` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.8739` n `91` status `ready` deltaP `41.1837` edge `0.5021` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.6632` n `187` status `ready` deltaP `31.25` edge `0.5136` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.6979` n `91` status `ready` deltaP `32.0491` edge `0.5137` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.6979` n `91` status `ready` deltaP `32.0491` edge `0.5137` maxDD `-3.8693`
- `risk_on_high->equity_24h` score `7.6264` n `91` status `ready` deltaP `31.25` edge `0.4272` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.6264` n `91` status `ready` deltaP `31.25` edge `0.4272` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.29` n `91` status `ready` deltaP `25.021` edge `1.1746` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.29` n `91` status `ready` deltaP `25.021` edge `1.1746` maxDD `-24.5429`
- `risk_on_high->index_24h` score `5.0525` n `91` status `ready` deltaP `47.0505` edge `0.1116` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.0525` n `91` status `ready` deltaP `47.0505` edge `0.1116` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.0683` n `187` status `ready` deltaP `40.7215` edge `0.1069` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.7322` n `91` status `ready` deltaP `34.5651` edge `0.0899` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.7322` n `91` status `ready` deltaP `34.5651` edge `0.0899` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.5491` n `187` status `ready` deltaP `27.7895` edge `0.1127` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
