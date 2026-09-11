# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T21:37:30.805111+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11417`

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

- `news_risk_high->unknown_1h` score `495.9066` n `72` status `ready` deltaP `-5.6221` edge `41.4052` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `24.1629` n `91` status `ready` deltaP `42.2486` edge `1.7549` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `24.1629` n `91` status `ready` deltaP `42.2486` edge `1.7549` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `22.5539` n `31` status `ready` deltaP `48.3815` edge `1.647` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `21.2533` n `151` status `ready` deltaP `37.1471` edge `1.6062` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `14.4327` n `31` status `ready` deltaP `28.3883` edge `1.0581` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `9.5084` n `31` status `ready` deltaP `30.5276` edge `0.5987` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.4647` n `91` status `ready` deltaP `36.9792` edge `0.5422` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.4647` n `91` status `ready` deltaP `36.9792` edge `0.5422` maxDD `0.0`
- `market_context_high->equity_24h` score `9.1755` n `151` status `ready` deltaP `36.9792` edge `0.5181` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.5283` n `91` status `ready` deltaP `42.0983` edge `0.4672` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.5283` n `91` status `ready` deltaP `42.0983` edge `0.4672` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `7.7937` n `31` status `ready` deltaP `51.0417` edge `0.3092` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.6114` n `91` status `ready` deltaP `25.021` edge `1.2158` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.6114` n `91` status `ready` deltaP `25.021` edge `1.2158` maxDD `-24.5429`
- `news_risk_high->index_24h` score `7.5192` n `31` status `ready` deltaP `48.4095` edge `0.3132` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `6.5974` n `91` status `ready` deltaP `30.982` edge `0.4291` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.5974` n `91` status `ready` deltaP `30.982` edge `0.4291` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.3932` n `91` status `ready` deltaP `51.5644` edge `0.1099` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.3932` n `91` status `ready` deltaP `51.5644` edge `0.1099` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
