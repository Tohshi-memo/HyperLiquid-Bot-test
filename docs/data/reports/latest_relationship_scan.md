# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T15:22:43.139244+00:00`
- Price records: `672`
- Market context records: `4003`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10252`

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

- `risk_on_high->unknown_4h` score `146.8038` n `40` status `ready` deltaP `-3.1707` edge `12.436` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `146.8038` n `40` status `ready` deltaP `-3.1707` edge `12.436` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `48.7849` n `135` status `ready` deltaP `-2.8704` edge `4.4864` maxDD `-24.1486`
- `market_context_high->unknown_4h` score `26.308` n `147` status `ready` deltaP `3.2749` edge `2.7114` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `8.849` n `40` status `ready` deltaP `41.4931` edge `0.4608` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.849` n `40` status `ready` deltaP `41.4931` edge `0.4608` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.9624` n `40` status `ready` deltaP `37.8963` edge `0.0823` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.9624` n `40` status `ready` deltaP `37.8963` edge `0.0823` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.5635` n `135` status `ready` deltaP `26.9445` edge `0.1992` maxDD `-5.5496`
- `market_context_high->metal_24h` score `2.9391` n `135` status `ready` deltaP `15.1389` edge `0.2843` maxDD `-8.2238`
- `risk_on_high->index_24h` score `2.4965` n `40` status `ready` deltaP `29.1667` edge `0.0136` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.4965` n `40` status `ready` deltaP `29.1667` edge `0.0136` maxDD `0.0`
- `market_context_high->equity_4h` score `2.0291` n `147` status `ready` deltaP `19.9881` edge `0.1661` maxDD `-7.0879`
- `market_context_high->equity_24h` score `1.9042` n `135` status `ready` deltaP `17.0487` edge `0.348` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.4872` n `40` status `ready` deltaP `20.5183` edge `0.0537` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.4872` n `40` status `ready` deltaP `20.5183` edge `0.0537` maxDD `-2.6576`
- `market_context_high->metal_1h` score `1.1584` n `147` status `ready` deltaP `12.4221` edge `0.0612` maxDD `-1.7983`
- `risk_on_high->commodity_24h` score `1.0467` n `40` status `ready` deltaP `4.1667` edge `0.2876` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.0467` n `40` status `ready` deltaP `4.1667` edge `0.2876` maxDD `-12.9187`
- `market_context_high->crypto_major_1h` score `1.0005` n `147` status `ready` deltaP `10.1084` edge `0.0702` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
