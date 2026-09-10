# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T20:38:06.139147+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11858`

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

- `risk_on_high->crypto_alt_24h` score `20.0492` n `91` status `ready` deltaP `36.1722` edge `1.4526` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.0492` n `91` status `ready` deltaP `36.1722` edge `1.4526` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `15.4605` n `201` status `ready` deltaP `27.7364` edge `1.1862` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.0353` n `91` status `ready` deltaP `42.5556` edge `0.5064` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.0353` n `91` status `ready` deltaP `42.5556` edge `0.5064` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.7385` n `91` status `ready` deltaP `32.8113` edge `0.512` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.7385` n `91` status `ready` deltaP `32.8113` edge `0.512` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2573` n `91` status `ready` deltaP `25.021` edge `1.1704` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2573` n `91` status `ready` deltaP `25.021` edge `1.1704` maxDD `-24.5429`
- `market_context_high->equity_24h` score `6.4697` n `201` status `ready` deltaP `25.5208` edge `0.369` maxDD `0.0`
- `risk_on_high->equity_24h` score `4.8737` n `91` status `ready` deltaP `25.5208` edge `0.236` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.8737` n `91` status `ready` deltaP `25.5208` edge `0.236` maxDD `0.0`
- `risk_on_high->index_24h` score `4.2689` n `91` status `ready` deltaP `41.3214` edge `0.0845` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.2689` n `91` status `ready` deltaP `41.3214` edge `0.0845` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.3972` n `201` status `ready` deltaP `35.6629` edge `0.0847` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.0943` n `91` status `ready` deltaP `30.2968` edge `0.0652` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.0943` n `91` status `ready` deltaP `30.2968` edge `0.0652` maxDD `-0.079`
- `market_context_high->equity_4h` score `1.9697` n `201` status `ready` deltaP `23.4574` edge `0.0933` maxDD `-2.843`
- `risk_on_high->crypto_alt_1h` score `1.5213` n `91` status `ready` deltaP `6.197` edge `0.1207` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.5213` n `91` status `ready` deltaP `6.197` edge `0.1207` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
