# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T15:37:34.683659+00:00`
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

- `risk_on_high->crypto_alt_24h` score `18.9236` n `91` status `ready` deltaP `36.1722` edge `1.3588` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `18.9236` n `91` status `ready` deltaP `36.1722` edge `1.3588` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.3349` n `201` status `ready` deltaP `27.7364` edge `1.0924` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.0415` n `91` status `ready` deltaP `42.7081` edge `0.5059` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.0415` n `91` status `ready` deltaP `42.7081` edge `0.5059` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.6229` n `91` status `ready` deltaP `32.5064` edge `0.5044` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.6229` n `91` status `ready` deltaP `32.5064` edge `0.5044` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `6.9344` n `91` status `ready` deltaP `25.021` edge `1.129` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.9344` n `91` status `ready` deltaP `25.021` edge `1.129` maxDD `-24.5429`
- `market_context_high->equity_24h` score `4.7615` n `201` status `ready` deltaP `22.0486` edge `0.2498` maxDD `0.0`
- `risk_on_high->index_24h` score `3.7872` n `91` status `ready` deltaP `37.8491` edge `0.0675` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.7872` n `91` status `ready` deltaP `37.8491` edge `0.0675` maxDD `-0.0051`
- `risk_on_high->equity_24h` score `3.1679` n `91` status `ready` deltaP `22.0486` edge `0.117` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.1679` n `91` status `ready` deltaP `22.0486` edge `0.117` maxDD `0.0`
- `risk_on_high->equity_4h` score `2.9192` n `91` status `ready` deltaP `29.5346` edge `0.0557` maxDD `-0.0796`
- `risk_on_and_context->equity_4h` score `2.9192` n `91` status `ready` deltaP `29.5346` edge `0.0557` maxDD `-0.0796`
- `market_context_high->index_24h` score `2.9154` n `201` status `ready` deltaP `32.1906` edge `0.0677` maxDD `-0.1483`
- `market_context_high->equity_4h` score `1.7936` n `201` status `ready` deltaP `22.6952` edge `0.0837` maxDD `-2.843`
- `risk_on_high->crypto_alt_1h` score `1.4183` n `91` status `ready` deltaP `5.4485` edge `0.1171` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.4183` n `91` status `ready` deltaP `5.4485` edge `0.1171` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
