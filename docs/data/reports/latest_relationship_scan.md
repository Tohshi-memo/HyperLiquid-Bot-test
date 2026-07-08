# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T10:52:30.623459+00:00`
- Price records: `672`
- Market context records: `6079`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11147`

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

- `news_risk_high->fx_24h` score `8.1618` n `30` status `ready` deltaP `72.7431` edge `0.1952` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `4.8644` n `30` status `ready` deltaP `31.0069` edge `0.2134` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.3601` n `32` status `ready` deltaP `45.3506` edge `0.0656` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4722` n `32` status `ready` deltaP `29.6407` edge `0.0223` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.7671` n `206` status `ready` deltaP `9.2514` edge `0.1773` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.1567` n `32` status `ready` deltaP `13.3795` edge `0.1058` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `0.857` n `30` status `ready` deltaP `19.4792` edge `-0.0379` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.6556` n `32` status `ready` deltaP `9.2253` edge `0.0687` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1` n `30` status `ready` deltaP `9.2361` edge `0.0384` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3285` n `206` status `ready` deltaP `4.0288` edge `0.0109` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.4947` n `206` status `ready` deltaP `0.7572` edge `-0.0006` maxDD `-0.6538`
- `market_context_high->metal_4h` score `-0.5957` n `206` status `ready` deltaP `5.4005` edge `0.0331` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.7248` n `32` status `ready` deltaP `-1.7964` edge `-0.0312` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.7578` n `206` status `ready` deltaP `-1.9824` edge `-0.0053` maxDD `-0.5708`
- `market_context_high->crypto_alt_1h` score `-0.7612` n `206` status `ready` deltaP `4.7047` edge `0.0463` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8301` n `206` status `ready` deltaP `4.5506` edge `0.04` maxDD `-9.807`
- `market_context_high->equity_1h` score `-0.8394` n `206` status `ready` deltaP `1.8284` edge `0.0307` maxDD `-4.3608`
- `market_context_high->index_4h` score `-0.8826` n `206` status `ready` deltaP `2.2629` edge `0.0251` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-0.9504` n `32` status `ready` deltaP `-7.4289` edge `-0.016` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1792` n `206` status `ready` deltaP `-1.9374` edge `0.0045` maxDD `-1.1879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
