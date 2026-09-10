# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T12:22:30.276849+00:00`
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

- `risk_on_high->crypto_alt_24h` score `17.5117` n `91` status `ready` deltaP `34.7833` edge `1.2504` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `17.5117` n `91` status `ready` deltaP `34.7833` edge `1.2504` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `12.923` n `201` status `ready` deltaP `26.3475` edge `0.984` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.2229` n `91` status `ready` deltaP `40.7264` edge `0.4509` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.2229` n `91` status `ready` deltaP `40.7264` edge `0.4509` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `6.6004` n `91` status `ready` deltaP `30.5247` edge `0.4324` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.6004` n `91` status `ready` deltaP `30.5247` edge `0.4324` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `6.1477` n `91` status `ready` deltaP `23.6321` edge `1.0374` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.1477` n `91` status `ready` deltaP `23.6321` edge `1.0374` maxDD `-24.5429`
- `market_context_high->equity_24h` score `3.5945` n `201` status `ready` deltaP `19.7917` edge `0.1676` maxDD `0.0`
- `risk_on_high->index_24h` score `3.453` n `91` status `ready` deltaP `35.5922` edge `0.0547` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.453` n `91` status `ready` deltaP `35.5922` edge `0.0547` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.5813` n `201` status `ready` deltaP `29.9337` edge `0.0549` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.3106` n `91` status `ready` deltaP `27.5529` edge `0.0182` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `2.3106` n `91` status `ready` deltaP `27.5529` edge `0.0182` maxDD `-0.0802`
- `risk_on_high->equity_24h` score `1.9889` n `91` status `ready` deltaP `19.7917` edge `0.0338` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.9889` n `91` status `ready` deltaP `19.7917` edge `0.0338` maxDD `0.0`
- `market_context_high->commodity_24h` score `1.7275` n `201` status `ready` deltaP `17.7576` edge `0.0395` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.7114` n `91` status `ready` deltaP `17.4241` edge `0.0358` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.7114` n `91` status `ready` deltaP `17.4241` edge `0.0358` maxDD `-0.0811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
