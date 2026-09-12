# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T04:22:25.979044+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11349`

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

- `market_context_high->unknown_24h` score `873.5275` n `138` status `ready` deltaP `14.0021` edge `72.7058` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.3473` n `82` status `ready` deltaP `-3.6038` edge `32.0118` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `24.322` n `86` status `ready` deltaP `42.7971` edge `1.7645` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `24.322` n `86` status `ready` deltaP `42.7971` edge `1.7645` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `23.7497` n `58` status `ready` deltaP `54.3881` edge `1.7066` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `20.3105` n `138` status `ready` deltaP `37.0169` edge `1.5285` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.1857` n `58` status `ready` deltaP `29.6456` edge `1.2833` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.0887` n `58` status `ready` deltaP `33.5309` edge `0.7937` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0819` n `86` status `ready` deltaP `36.9792` edge `0.5103` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0819` n `86` status `ready` deltaP `36.9792` edge `0.5103` maxDD `0.0`
- `market_context_high->equity_24h` score `8.7699` n `138` status `ready` deltaP `36.9792` edge `0.4843` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.5894` n `86` status `ready` deltaP `43.672` edge `0.4618` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.5894` n `86` status `ready` deltaP `43.672` edge `0.4618` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.1861` n `58` status `ready` deltaP `51.0417` edge `0.3419` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9539` n `58` status `ready` deltaP `51.4128` edge `0.3294` maxDD `-0.0797`
- `risk_on_high->crypto_major_24h` score `6.9994` n `86` status `ready` deltaP `22.9126` edge `1.1514` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.9994` n `86` status `ready` deltaP `22.9126` edge `1.1514` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `6.5895` n `86` status `ready` deltaP `30.8991` edge `0.429` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.5895` n `86` status `ready` deltaP `30.8991` edge `0.429` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.2171` n `86` status `ready` deltaP `51.3727` edge `0.0965` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
