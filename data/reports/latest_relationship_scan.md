# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T14:22:35.236295+00:00`
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

- `risk_on_high->crypto_alt_24h` score `18.5864` n `91` status `ready` deltaP `36.1722` edge `1.3307` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `18.5864` n `91` status `ready` deltaP `36.1722` edge `1.3307` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `13.9977` n `201` status `ready` deltaP `27.7364` edge `1.0643` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.7897` n `91` status `ready` deltaP `41.9459` edge `0.49` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.7897` n `91` status `ready` deltaP `41.9459` edge `0.49` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.3471` n `91` status `ready` deltaP `31.7442` edge `0.4865` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.3471` n `91` status `ready` deltaP `31.7442` edge `0.4865` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `6.8018` n `91` status `ready` deltaP `25.021` edge `1.112` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.8018` n `91` status `ready` deltaP `25.021` edge `1.112` maxDD `-24.5429`
- `market_context_high->equity_24h` score `4.3392` n `201` status `ready` deltaP `21.1806` edge `0.2204` maxDD `0.0`
- `risk_on_high->index_24h` score `3.6637` n `91` status `ready` deltaP `36.9811` edge `0.063` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.6637` n `91` status `ready` deltaP `36.9811` edge `0.063` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.792` n `201` status `ready` deltaP `31.3226` edge `0.0632` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.7503` n `91` status `ready` deltaP `28.7725` edge `0.0467` maxDD `-0.0796`
- `risk_on_and_context->equity_4h` score `2.7503` n `91` status `ready` deltaP `28.7725` edge `0.0467` maxDD `-0.0796`
- `risk_on_high->equity_24h` score `2.7456` n `91` status `ready` deltaP `21.1806` edge `0.0876` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.7456` n `91` status `ready` deltaP `21.1806` edge `0.0876` maxDD `0.0`
- `market_context_high->equity_4h` score `1.6246` n `201` status `ready` deltaP `21.9331` edge `0.0747` maxDD `-2.843`
- `market_context_high->commodity_24h` score `1.4664` n `201` status `ready` deltaP `16.3687` edge `0.027` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.4503` n `91` status `ready` deltaP `16.0352` edge `0.0233` maxDD `-0.0811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
