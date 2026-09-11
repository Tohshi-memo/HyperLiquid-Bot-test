# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T03:07:26.093565+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11394`

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

- `news_risk_high->unknown_1h` score `1020.3085` n `49` status `ready` deltaP `-9.8986` edge `85.1271` maxDD `-1.1656`
- `news_risk_high->unknown_4h` score `889.0944` n `37` status `ready` deltaP `-24.827` edge `74.3211` maxDD `-2.1509`
- `risk_on_high->crypto_alt_24h` score `20.6847` n `91` status `ready` deltaP `36.3458` edge `1.5044` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.6847` n `91` status `ready` deltaP `36.3458` edge `1.5044` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `17.0215` n `193` status `ready` deltaP `30.9595` edge `1.2948` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.0251` n `91` status `ready` deltaP `42.0983` edge `0.5086` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.0251` n `91` status `ready` deltaP `42.0983` edge `0.5086` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.3296` n `193` status `ready` deltaP `30.0347` edge `0.4939` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.8467` n `91` status `ready` deltaP `32.9637` edge `0.52` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.8467` n `91` status `ready` deltaP `32.9637` edge `0.52` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2682` n `91` status `ready` deltaP `25.021` edge `1.1718` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2682` n `91` status `ready` deltaP `25.021` edge `1.1718` maxDD `-24.5429`
- `risk_on_high->equity_24h` score `7.0732` n `91` status `ready` deltaP `30.0347` edge `0.3892` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.0732` n `91` status `ready` deltaP `30.0347` edge `0.3892` maxDD `0.0`
- `risk_on_high->index_24h` score `4.8917` n `91` status `ready` deltaP `45.8352` edge `0.1063` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8917` n `91` status `ready` deltaP `45.8352` edge `0.1063` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.947` n `193` status `ready` deltaP `39.8055` edge `0.1029` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.6048` n `91` status `ready` deltaP `33.4981` edge `0.0864` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.6048` n `91` status `ready` deltaP `33.4981` edge `0.0864` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.4766` n `193` status `ready` deltaP `27.1381` edge `0.111` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
