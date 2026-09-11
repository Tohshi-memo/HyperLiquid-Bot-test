# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T22:07:31.184200+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11333`

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

- `news_risk_high->unknown_1h` score `473.7031` n `74` status `ready` deltaP `-4.8713` edge `39.5499` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `24.3491` n `91` status `ready` deltaP `42.5958` edge `1.7681` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `24.3491` n `91` status `ready` deltaP `42.5958` edge `1.7681` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `22.3165` n `33` status `ready` deltaP `49.1635` edge `1.622` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `21.4395` n `151` status `ready` deltaP `37.4943` edge `1.6194` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `13.5127` n `33` status `ready` deltaP `23.8479` edge `1.0117` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `9.7161` n `33` status `ready` deltaP `30.9186` edge `0.6134` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.4443` n `91` status `ready` deltaP `36.9792` edge `0.5405` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.4443` n `91` status `ready` deltaP `36.9792` edge `0.5405` maxDD `0.0`
- `market_context_high->equity_24h` score `9.1551` n `151` status `ready` deltaP `36.9792` edge `0.5164` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.6091` n `91` status `ready` deltaP `42.4032` edge `0.4719` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.6091` n `91` status `ready` deltaP `42.4032` edge `0.4719` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `7.8657` n `33` status `ready` deltaP `51.0417` edge `0.3152` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.6668` n `91` status `ready` deltaP `25.021` edge `1.2229` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.6668` n `91` status `ready` deltaP `25.021` edge `1.2229` maxDD `-24.5429`
- `news_risk_high->index_24h` score `7.5769` n `33` status `ready` deltaP `48.8005` edge `0.3154` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `6.6434` n `91` status `ready` deltaP `31.2869` edge `0.4309` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.6434` n `91` status `ready` deltaP `31.2869` edge `0.4309` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.3836` n `91` status `ready` deltaP `51.5644` edge `0.1091` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.3836` n `91` status `ready` deltaP `51.5644` edge `0.1091` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
