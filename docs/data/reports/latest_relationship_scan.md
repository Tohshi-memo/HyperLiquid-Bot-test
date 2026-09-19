# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T12:52:28.669668+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8522`

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

- `news_risk_high->crypto_major_24h` score `53.3213` n `72` status `ready` deltaP `32.4652` edge `4.3162` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `46.763` n `72` status `ready` deltaP `36.9792` edge `3.7883` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.0369` n `144` status `ready` deltaP `-2.185` edge `3.1243` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `10.6003` n `72` status `ready` deltaP `42.0139` edge `0.6075` maxDD `-0.0053`
- `risk_on_high->unknown_4h` score `8.2843` n `52` status `ready` deltaP `-9.076` edge `0.7734` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.2843` n `52` status `ready` deltaP `-9.076` edge `0.7734` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.2364` n `52` status `ready` deltaP `44.9653` edge `0.3866` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2364` n `52` status `ready` deltaP `44.9653` edge `0.3866` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.0182` n `144` status `ready` deltaP `38.0209` edge `0.3839` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.6247` n `84` status `ready` deltaP `23.7588` edge `0.5146` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5765` n `84` status `ready` deltaP `20.9786` edge `0.3673` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.541` n `96` status `ready` deltaP `20.7959` edge `0.203` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.6611` n `52` status `ready` deltaP `31.6252` edge `0.0459` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6611` n `52` status `ready` deltaP `31.6252` edge `0.0459` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5091` n `144` status `ready` deltaP `27.4051` edge `0.0682` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.4989` n `96` status `ready` deltaP `20.8084` edge `0.1218` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.9185` n `72` status `ready` deltaP `24.4792` edge `0.0811` maxDD `-2.4203`
- `news_risk_high->fx_4h` score `1.1556` n `84` status `ready` deltaP `13.1678` edge `0.0304` maxDD `-0.084`
- `market_context_high->commodity_1h` score `1.0896` n `144` status `ready` deltaP `15.9598` edge `0.0221` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `0.7636` n `96` status `ready` deltaP `10.4229` edge `0.0347` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
