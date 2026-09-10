# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T21:07:29.534218+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11770`

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

- `risk_on_high->crypto_alt_24h` score `20.108` n `91` status `ready` deltaP `36.1722` edge `1.4575` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.108` n `91` status `ready` deltaP `36.1722` edge `1.4575` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `15.5193` n `201` status `ready` deltaP `27.7364` edge `1.1911` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.9797` n `91` status `ready` deltaP `42.2507` edge `0.5038` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9797` n `91` status `ready` deltaP `42.2507` edge `0.5038` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.6817` n `91` status `ready` deltaP `32.5064` edge `0.5093` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.6817` n `91` status `ready` deltaP `32.5064` edge `0.5093` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2565` n `91` status `ready` deltaP `25.021` edge `1.1703` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2565` n `91` status `ready` deltaP `25.021` edge `1.1703` maxDD `-24.5429`
- `market_context_high->equity_24h` score `6.6534` n `201` status `ready` deltaP `25.8681` edge `0.382` maxDD `0.0`
- `risk_on_high->equity_24h` score `5.0574` n `91` status `ready` deltaP `25.8681` edge `0.249` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.0574` n `91` status `ready` deltaP `25.8681` edge `0.249` maxDD `0.0`
- `risk_on_high->index_24h` score `4.3195` n `91` status `ready` deltaP `41.6686` edge `0.0864` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.3195` n `91` status `ready` deltaP `41.6686` edge `0.0864` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.4478` n `201` status `ready` deltaP `36.0101` edge `0.0866` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.1499` n `91` status `ready` deltaP `30.6017` edge `0.0678` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.1499` n `91` status `ready` deltaP `30.6017` edge `0.0678` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.0253` n `201` status `ready` deltaP `23.7623` edge `0.0959` maxDD `-2.843`
- `risk_on_high->equity_1h` score `1.5052` n `91` status `ready` deltaP `19.9859` edge `0.02` maxDD `-0.2246`
- `risk_on_and_context->equity_1h` score `1.5052` n `91` status `ready` deltaP `19.9859` edge `0.02` maxDD `-0.2246`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
