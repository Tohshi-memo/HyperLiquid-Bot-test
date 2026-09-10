# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T14:07:35.543162+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11908`

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

- `risk_on_high->crypto_alt_24h` score `18.4693` n `91` status `ready` deltaP `35.9986` edge `1.3221` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `18.4693` n `91` status `ready` deltaP `35.9986` edge `1.3221` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `13.8806` n `201` status `ready` deltaP `27.5628` edge `1.0557` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.7247` n `91` status `ready` deltaP `41.7934` edge `0.4856` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.7247` n `91` status `ready` deltaP `41.7934` edge `0.4856` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.2677` n `91` status `ready` deltaP `31.5918` edge `0.4809` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.2677` n `91` status `ready` deltaP `31.5918` edge `0.4809` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `6.7405` n `91` status `ready` deltaP `24.8474` edge `1.1053` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.7405` n `91` status `ready` deltaP `24.8474` edge `1.1053` maxDD `-24.5429`
- `market_context_high->equity_24h` score `4.2402` n `201` status `ready` deltaP `21.0069` edge `0.2133` maxDD `0.0`
- `risk_on_high->index_24h` score `3.6366` n `91` status `ready` deltaP `36.8075` edge `0.0619` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.6366` n `91` status `ready` deltaP `36.8075` edge `0.0619` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.7649` n `201` status `ready` deltaP `31.149` edge `0.0621` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.7009` n `91` status `ready` deltaP `28.62` edge `0.0436` maxDD `-0.0796`
- `risk_on_and_context->equity_4h` score `2.7009` n `91` status `ready` deltaP `28.62` edge `0.0436` maxDD `-0.0796`
- `risk_on_high->equity_24h` score `2.6466` n `91` status `ready` deltaP `21.0069` edge `0.0805` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.6466` n `91` status `ready` deltaP `21.0069` edge `0.0805` maxDD `0.0`
- `market_context_high->equity_4h` score `1.5752` n `201` status `ready` deltaP `21.7806` edge `0.0716` maxDD `-2.843`
- `market_context_high->commodity_24h` score `1.4971` n `201` status `ready` deltaP `16.5423` edge `0.0284` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.4809` n `91` status `ready` deltaP `16.2088` edge `0.0247` maxDD `-0.0811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
