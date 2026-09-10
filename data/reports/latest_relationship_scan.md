# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T15:03:15.872212+00:00`
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

- `risk_on_high->crypto_alt_24h` score `18.8216` n `91` status `ready` deltaP `36.1722` edge `1.3503` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `18.8216` n `91` status `ready` deltaP `36.1722` edge `1.3503` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.2329` n `201` status `ready` deltaP `27.7364` edge `1.0839` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.9487` n `91` status `ready` deltaP `42.4032` edge `0.5002` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9487` n `91` status `ready` deltaP `42.4032` edge `0.5002` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.5121` n `91` status `ready` deltaP `32.2015` edge `0.4972` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.5121` n `91` status `ready` deltaP `32.2015` edge `0.4972` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `6.8954` n `91` status `ready` deltaP `25.021` edge `1.124` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.8954` n `91` status `ready` deltaP `25.021` edge `1.124` maxDD `-24.5429`
- `market_context_high->equity_24h` score `4.6161` n `201` status `ready` deltaP `21.7014` edge `0.24` maxDD `0.0`
- `risk_on_high->index_24h` score `3.7426` n `91` status `ready` deltaP `37.5019` edge `0.0661` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.7426` n `91` status `ready` deltaP `37.5019` edge `0.0661` maxDD `-0.0051`
- `risk_on_high->equity_24h` score `3.0225` n `91` status `ready` deltaP `21.7014` edge `0.1072` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.0225` n `91` status `ready` deltaP `21.7014` edge `0.1072` maxDD `0.0`
- `market_context_high->index_24h` score `2.8708` n `201` status `ready` deltaP `31.8434` edge `0.0663` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.866` n `91` status `ready` deltaP `29.2298` edge `0.0533` maxDD `-0.0796`
- `risk_on_and_context->equity_4h` score `2.866` n `91` status `ready` deltaP `29.2298` edge `0.0533` maxDD `-0.0796`
- `market_context_high->equity_4h` score `1.7404` n `201` status `ready` deltaP `22.3904` edge `0.0813` maxDD `-2.843`
- `risk_on_high->crypto_alt_1h` score `1.3979` n `91` status `ready` deltaP `5.2988` edge `0.1164` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.3979` n `91` status `ready` deltaP `5.2988` edge `0.1164` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
