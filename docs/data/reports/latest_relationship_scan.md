# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T12:52:32.451565+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11908`

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

- `risk_on_high->crypto_alt_24h` score `17.7783` n `91` status `ready` deltaP `35.1305` edge `1.2703` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `17.7783` n `91` status `ready` deltaP `35.1305` edge `1.2703` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `13.1895` n `201` status `ready` deltaP `26.6947` edge `1.0039` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.3577` n `91` status `ready` deltaP `41.0312` edge `0.4601` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.3577` n `91` status `ready` deltaP `41.0312` edge `0.4601` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `6.788` n `91` status `ready` deltaP `30.8296` edge `0.446` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.788` n `91` status `ready` deltaP `30.8296` edge `0.446` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `6.3202` n `91` status `ready` deltaP `23.9794` edge `1.0572` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.3202` n `91` status `ready` deltaP `23.9794` edge `1.0572` maxDD `-24.5429`
- `market_context_high->equity_24h` score `3.7519` n `201` status `ready` deltaP `20.1389` edge `0.1784` maxDD `0.0`
- `risk_on_high->index_24h` score `3.5` n `91` status `ready` deltaP `35.9394` edge `0.0563` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.5` n `91` status `ready` deltaP `35.9394` edge `0.0563` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.6282` n `201` status `ready` deltaP `30.2809` edge `0.0565` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.4214` n `91` status `ready` deltaP `27.8578` edge `0.0254` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `2.4214` n `91` status `ready` deltaP `27.8578` edge `0.0254` maxDD `-0.0802`
- `risk_on_high->equity_24h` score `2.1463` n `91` status `ready` deltaP `20.1389` edge `0.0446` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.1463` n `91` status `ready` deltaP `20.1389` edge `0.0446` maxDD `0.0`
- `market_context_high->commodity_24h` score `1.6649` n `201` status `ready` deltaP `17.4104` edge `0.0366` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.6488` n `91` status `ready` deltaP `17.0769` edge `0.0329` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.6488` n `91` status `ready` deltaP `17.0769` edge `0.0329` maxDD `-0.0811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
