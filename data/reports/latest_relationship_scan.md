# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T04:37:31.086977+00:00`
- Price records: `672`
- Market context records: `3959`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11179`

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

- `risk_on_high->unknown_4h` score `148.1984` n `40` status `ready` deltaP `1.7073` edge `12.5197` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `148.1984` n `40` status `ready` deltaP `1.7073` edge `12.5197` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `31.1258` n `148` status `ready` deltaP `-7.8876` edge `3.3777` maxDD `-50.1708`
- `market_context_high->unknown_4h` score `21.5665` n `159` status `ready` deltaP `0.8111` edge `2.3327` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `8.8547` n `40` status `ready` deltaP `42.0139` edge `0.4578` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.8547` n `40` status `ready` deltaP `42.0139` edge `0.4578` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4077` n `40` status `ready` deltaP `37.5915` edge `0.0381` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.4077` n `40` status `ready` deltaP `37.5915` edge `0.0381` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.1548` n `148` status `ready` deltaP `25.807` edge `0.2048` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.1392` n `148` status `ready` deltaP `16.4556` edge `0.3034` maxDD `-9.1203`
- `risk_on_high->index_24h` score `2.6661` n `40` status `ready` deltaP `29.8611` edge `0.0231` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.6661` n `40` status `ready` deltaP `29.8611` edge `0.0231` maxDD `0.0`
- `market_context_high->equity_24h` score `2.4367` n `148` status `ready` deltaP `18.3653` edge `0.3836` maxDD `-14.5715`
- `market_context_high->equity_4h` score `2.3034` n `159` status `ready` deltaP `19.3368` edge `0.1933` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.2882` n `159` status `ready` deltaP `19.7164` edge `0.2159` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.6864` n `40` status `ready` deltaP `20.5183` edge `0.0703` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6864` n `40` status `ready` deltaP `20.5183` edge `0.0703` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.6337` n `168` status `ready` deltaP `12.639` edge `0.1061` maxDD `-2.3372`
- `risk_on_high->commodity_24h` score `1.0395` n `40` status `ready` deltaP `4.1667` edge `0.287` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.0395` n `40` status `ready` deltaP `4.1667` edge `0.287` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
