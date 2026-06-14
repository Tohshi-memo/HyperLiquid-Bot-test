# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T16:55:23.071071+00:00`
- Price records: `672`
- Market context records: `3911`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11374`

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

- `risk_on_high->unknown_4h` score `50.0984` n `69` status `ready` deltaP `5.152` edge `6.6027` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `50.0984` n `69` status `ready` deltaP `5.152` edge `6.6027` maxDD `-13.467`
- `risk_on_high->equity_24h` score `21.2351` n `40` status `ready` deltaP `42.0139` edge `1.4895` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `21.2351` n `40` status `ready` deltaP `42.0139` edge `1.4895` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `19.5427` n `40` status `ready` deltaP `10.1042` edge `1.713` maxDD `-8.1441`
- `risk_on_and_context->crypto_major_24h` score `19.5427` n `40` status `ready` deltaP `10.1042` edge `1.713` maxDD `-8.1441`
- `risk_on_high->index_24h` score `8.614` n `40` status `ready` deltaP `30.0347` edge `0.5176` maxDD `0.0`
- `risk_on_and_context->index_24h` score `8.614` n `40` status `ready` deltaP `30.0347` edge `0.5176` maxDD `0.0`
- `market_context_high->unknown_4h` score `7.0975` n `205` status `ready` deltaP `-1.5854` edge `1.4614` maxDD `-35.6052`
- `risk_on_high->crypto_major_4h` score `6.7682` n `69` status `ready` deltaP `23.6081` edge `0.4977` maxDD `-4.6192`
- `risk_on_and_context->crypto_major_4h` score `6.7682` n `69` status `ready` deltaP `23.6081` edge `0.4977` maxDD `-4.6192`
- `market_context_high->equity_24h` score `5.9724` n `165` status `ready` deltaP `20.8018` edge `0.662` maxDD `-14.5715`
- `risk_on_high->crypto_alt_24h` score `5.0615` n `40` status `ready` deltaP `8.0208` edge `0.8435` maxDD `-15.8446`
- `risk_on_and_context->crypto_alt_24h` score `5.0615` n `40` status `ready` deltaP `8.0208` edge `0.8435` maxDD `-15.8446`
- `market_context_high->index_24h` score `4.5384` n `165` status `ready` deltaP `25.7923` edge `0.3202` maxDD `-7.1159`
- `risk_on_high->equity_4h` score `3.7462` n `69` status `ready` deltaP `28.5724` edge `0.1982` maxDD `-3.7865`
- `risk_on_and_context->equity_4h` score `3.7462` n `69` status `ready` deltaP `28.5724` edge `0.1982` maxDD `-3.7865`
- `market_context_high->crypto_major_4h` score `3.0153` n `205` status `ready` deltaP `17.9878` edge `0.3078` maxDD `-9.4488`
- `market_context_high->metal_24h` score `2.6553` n `165` status `ready` deltaP `18.0272` edge `0.2526` maxDD `-9.1203`
- `market_context_high->equity_4h` score `1.3906` n `205` status `ready` deltaP `14.7866` edge `0.1877` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
