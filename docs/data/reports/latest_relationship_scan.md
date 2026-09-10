# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T16:07:32.478495+00:00`
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

- `risk_on_high->crypto_alt_24h` score `19.0448` n `91` status `ready` deltaP `36.1722` edge `1.3689` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `19.0448` n `91` status `ready` deltaP `36.1722` edge `1.3689` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.4561` n `201` status `ready` deltaP `27.7364` edge `1.1025` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.1138` n `91` status `ready` deltaP `43.0129` edge `0.5099` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.1138` n `91` status `ready` deltaP `43.0129` edge `0.5099` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.7229` n `91` status `ready` deltaP `32.8113` edge `0.5107` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.7229` n `91` status `ready` deltaP `32.8113` edge `0.5107` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `6.978` n `91` status `ready` deltaP `25.021` edge `1.1346` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.978` n `91` status `ready` deltaP `25.021` edge `1.1346` maxDD `-24.5429`
- `market_context_high->equity_24h` score `4.9213` n `201` status `ready` deltaP `22.3958` edge `0.2608` maxDD `0.0`
- `risk_on_high->index_24h` score `3.8341` n `91` status `ready` deltaP `38.1964` edge `0.0691` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.8341` n `91` status `ready` deltaP `38.1964` edge `0.0691` maxDD `-0.0051`
- `risk_on_high->equity_24h` score `3.3277` n `91` status `ready` deltaP `22.3958` edge `0.128` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.3277` n `91` status `ready` deltaP `22.3958` edge `0.128` maxDD `0.0`
- `risk_on_high->equity_4h` score `2.964` n `91` status `ready` deltaP `29.8395` edge `0.0574` maxDD `-0.0796`
- `risk_on_and_context->equity_4h` score `2.964` n `91` status `ready` deltaP `29.8395` edge `0.0574` maxDD `-0.0796`
- `market_context_high->index_24h` score `2.9624` n `201` status `ready` deltaP `32.5379` edge `0.0693` maxDD `-0.1483`
- `market_context_high->equity_4h` score `1.8384` n `201` status `ready` deltaP `23.0001` edge `0.0854` maxDD `-2.843`
- `risk_on_high->crypto_alt_1h` score `1.4554` n `91` status `ready` deltaP `5.7479` edge `0.1182` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.4554` n `91` status `ready` deltaP `5.7479` edge `0.1182` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
