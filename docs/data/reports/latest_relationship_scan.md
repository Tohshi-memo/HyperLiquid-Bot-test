# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T23:37:25.247242+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10313`

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

- `risk_on_high->unknown_24h` score `4004.4962` n `117` status `ready` deltaP `20.3125` edge `333.5726` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `4004.4962` n `117` status `ready` deltaP `20.3125` edge `333.5726` maxDD `0.0`
- `market_context_high->unknown_24h` score `2961.8223` n `238` status `ready` deltaP `19.4722` edge `246.6939` maxDD `-0.0819`
- `risk_on_high->crypto_alt_24h` score `9.5165` n `117` status `ready` deltaP `25.414` edge `0.6466` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `9.5165` n `117` status `ready` deltaP `25.414` edge `0.6466` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.8924` n `117` status `ready` deltaP `31.2448` edge `0.3199` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.8924` n `117` status `ready` deltaP `31.2448` edge `0.3199` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.339` n `117` status `ready` deltaP `21.1005` edge `0.9506` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.339` n `117` status `ready` deltaP `21.1005` edge `0.9506` maxDD `-24.5429`
- `market_context_high->crypto_alt_24h` score `5.1407` n `238` status `ready` deltaP `19.1833` edge `0.358` maxDD `-2.5998`
- `risk_on_high->crypto_major_4h` score `4.8433` n `117` status `ready` deltaP `25.6762` edge `0.3183` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8433` n `117` status `ready` deltaP `25.6762` edge `0.3183` maxDD `-3.8693`
- `market_context_high->equity_24h` score `2.399` n `238` status `ready` deltaP `12.1528` edge `0.1189` maxDD `0.0`
- `risk_on_high->equity_24h` score `1.6658` n `117` status `ready` deltaP `12.1528` edge `0.0578` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.6658` n `117` status `ready` deltaP `12.1528` edge `0.0578` maxDD `0.0`
- `risk_on_high->index_24h` score `1.4926` n `117` status `ready` deltaP `14.1026` edge `0.0346` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.4926` n `117` status `ready` deltaP `14.1026` edge `0.0346` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `1.04` n `117` status `ready` deltaP `4.6958` edge `0.0906` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.04` n `117` status `ready` deltaP `4.6958` edge `0.0906` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.7697` n `238` status `ready` deltaP `9.1037` edge `0.0428` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
