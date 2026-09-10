# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T09:07:31.188106+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11876`

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

- `risk_on_high->crypto_alt_24h` score `15.4471` n `91` status `ready` deltaP `32.5263` edge `1.0934` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `15.4471` n `91` status `ready` deltaP `32.5263` edge `1.0934` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `11.164` n `204` status `ready` deltaP `24.2953` edge `0.8511` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.6518` n `91` status `ready` deltaP `38.8971` edge `0.4155` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.6518` n `91` status `ready` deltaP `38.8971` edge `0.4155` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.7616` n `91` status `ready` deltaP `28.6954` edge `0.3747` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.7616` n `91` status `ready` deltaP `28.6954` edge `0.3747` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.7885` n `91` status `ready` deltaP `21.3752` edge `0.8782` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.7885` n `91` status `ready` deltaP `21.3752` edge `0.8782` maxDD `-24.5429`
- `risk_on_high->index_24h` score `3.0685` n `91` status `ready` deltaP `33.3352` edge `0.0377` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.0685` n `91` status `ready` deltaP `33.3352` edge `0.0377` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.7888` n `204` status `ready` deltaP `17.5347` edge `0.1155` maxDD `0.0`
- `market_context_high->index_24h` score `2.4592` n `204` status `ready` deltaP `27.8084` edge `0.0589` maxDD `-0.1483`
- `risk_on_high->commodity_24h` score `1.9363` n `91` status `ready` deltaP `18.4657` edge `0.0476` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.9363` n `91` status `ready` deltaP `18.4657` edge `0.0476` maxDD `-0.0811`
- `risk_on_high->equity_4h` score `1.8775` n `91` status `ready` deltaP `25.7237` edge `-0.0057` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `1.8775` n `91` status `ready` deltaP `25.7237` edge `-0.0057` maxDD `-0.0802`
- `market_context_high->commodity_24h` score `1.4823` n `204` status `ready` deltaP `17.453` edge `0.0448` maxDD `-1.01`
- `risk_on_high->equity_1h` score `1.1222` n `91` status `ready` deltaP `17.8901` edge `0.0021` maxDD `-0.228`
- `risk_on_and_context->equity_1h` score `1.1222` n `91` status `ready` deltaP `17.8901` edge `0.0021` maxDD `-0.228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
