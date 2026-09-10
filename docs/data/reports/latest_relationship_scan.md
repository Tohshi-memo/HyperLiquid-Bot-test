# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T06:52:28.156869+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10942`

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

- `risk_on_high->crypto_alt_24h` score `14.0813` n `91` status `ready` deltaP `30.9638` edge `0.99` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `14.0813` n `91` status `ready` deltaP `30.9638` edge `0.99` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `10.2682` n `213` status `ready` deltaP `23.3128` edge `0.783` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.4682` n `91` status `ready` deltaP `37.9824` edge `0.4063` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.4682` n `91` status `ready` deltaP `37.9824` edge `0.4063` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.5577` n `91` status `ready` deltaP `27.7808` edge `0.3638` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.5577` n `91` status `ready` deltaP `27.7808` edge `0.3638` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `3.8618` n `91` status `ready` deltaP `19.8127` edge `0.7698` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `3.8618` n `91` status `ready` deltaP `19.8127` edge `0.7698` maxDD `-24.5429`
- `risk_on_high->index_24h` score `2.8535` n `91` status `ready` deltaP `31.7727` edge `0.0302` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.8535` n `91` status `ready` deltaP `31.7727` edge `0.0302` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.701` n `213` status `ready` deltaP `15.9722` edge `0.1186` maxDD `0.0`
- `market_context_high->index_24h` score `2.4013` n `213` status `ready` deltaP `26.6187` edge `0.062` maxDD `-0.1483`
- `risk_on_high->commodity_24h` score `1.9217` n `91` status `ready` deltaP `18.1185` edge `0.0487` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.9217` n `91` status `ready` deltaP `18.1185` edge `0.0487` maxDD `-0.0811`
- `risk_on_high->equity_4h` score `1.9151` n `91` status `ready` deltaP `26.0286` edge `-0.0046` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `1.9151` n `91` status `ready` deltaP `26.0286` edge `-0.0046` maxDD `-0.0802`
- `risk_on_high->equity_1h` score `1.0803` n `91` status `ready` deltaP `17.441` edge `0.0016` maxDD `-0.228`
- `risk_on_and_context->equity_1h` score `1.0803` n `91` status `ready` deltaP `17.441` edge `0.0016` maxDD `-0.228`
- `risk_on_high->crypto_alt_1h` score `1.0621` n `91` status `ready` deltaP `4.2509` edge `0.0954` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
