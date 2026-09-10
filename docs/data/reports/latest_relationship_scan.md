# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T15:22:31.994230+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11967`

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

- `risk_on_high->crypto_alt_24h` score `18.8756` n `91` status `ready` deltaP `36.1722` edge `1.3548` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `18.8756` n `91` status `ready` deltaP `36.1722` edge `1.3548` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.2869` n `201` status `ready` deltaP `27.7364` edge `1.0884` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.9993` n `91` status `ready` deltaP `42.5556` edge `0.5034` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9993` n `91` status `ready` deltaP `42.5556` edge `0.5034` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.5675` n `91` status `ready` deltaP `32.3539` edge `0.5008` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.5675` n `91` status `ready` deltaP `32.3539` edge `0.5008` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `6.9125` n `91` status `ready` deltaP `25.021` edge `1.1262` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.9125` n `91` status `ready` deltaP `25.021` edge `1.1262` maxDD `-24.5429`
- `market_context_high->equity_24h` score `4.6924` n `201` status `ready` deltaP `21.875` edge `0.2452` maxDD `0.0`
- `risk_on_high->index_24h` score `3.7661` n `91` status `ready` deltaP `37.6755` edge `0.0669` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.7661` n `91` status `ready` deltaP `37.6755` edge `0.0669` maxDD `-0.0051`
- `risk_on_high->equity_24h` score `3.0988` n `91` status `ready` deltaP `21.875` edge `0.1124` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.0988` n `91` status `ready` deltaP `21.875` edge `0.1124` maxDD `0.0`
- `market_context_high->index_24h` score `2.8943` n `201` status `ready` deltaP `32.017` edge `0.0671` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.8938` n `91` status `ready` deltaP `29.3822` edge `0.0546` maxDD `-0.0796`
- `risk_on_and_context->equity_4h` score `2.8938` n `91` status `ready` deltaP `29.3822` edge `0.0546` maxDD `-0.0796`
- `market_context_high->equity_4h` score `1.7682` n `201` status `ready` deltaP `22.5428` edge `0.0826` maxDD `-2.843`
- `risk_on_high->crypto_alt_1h` score `1.4027` n `91` status `ready` deltaP `5.2988` edge `0.1168` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.4027` n `91` status `ready` deltaP `5.2988` edge `0.1168` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
