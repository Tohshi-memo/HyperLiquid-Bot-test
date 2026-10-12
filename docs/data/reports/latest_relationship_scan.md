# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T00:37:35.031862+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9488`

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

- `market_context_high->unknown_24h` score `1285.9633` n `42` status `ready` deltaP `-21.3789` edge `107.3425` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `40.1648` n `107` status `ready` deltaP `-8.9226` edge `3.4771` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.1037` n `42` status `ready` deltaP `28.745` edge `0.6099` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.3904` n `42` status `ready` deltaP `52.4306` edge `0.183` maxDD `0.0`
- `market_context_high->fx_24h` score `2.5713` n `42` status `ready` deltaP `29.241` edge `0.0323` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `2.4266` n `42` status `ready` deltaP `-17.0635` edge `0.6308` maxDD `-17.8526`
- `risk_on_high->crypto_alt_1h` score `2.2845` n `40` status `ready` deltaP `15.2096` edge `0.1445` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `2.2845` n `40` status `ready` deltaP `15.2096` edge `0.1445` maxDD `-2.4421`
- `market_context_high->unknown_1h` score `1.9458` n `119` status `ready` deltaP `-3.6192` edge `0.2199` maxDD `-1.0231`
- `risk_on_high->crypto_major_1h` score `1.3625` n `40` status `ready` deltaP `12.3503` edge `0.0965` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.3625` n `40` status `ready` deltaP `12.3503` edge `0.0965` maxDD `-3.2233`
- `risk_on_high->metal_1h` score `1.2214` n `40` status `ready` deltaP `15.2545` edge `0.024` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `1.2214` n `40` status `ready` deltaP `15.2545` edge `0.024` maxDD `-0.2466`
- `risk_on_high->equity_1h` score `0.4982` n `40` status `ready` deltaP `3.8623` edge `0.0403` maxDD `-0.296`
- `risk_on_and_context->equity_1h` score `0.4982` n `40` status `ready` deltaP `3.8623` edge `0.0403` maxDD `-0.296`
- `market_context_high->crypto_alt_1h` score `0.2767` n `119` status `ready` deltaP `6.5541` edge `0.0952` maxDD `-4.9401`
- `market_context_high->metal_4h` score `0.094` n `107` status `ready` deltaP `8.746` edge `0.0218` maxDD `-1.1153`
- `market_context_high->commodity_4h` score `0.0574` n `107` status `ready` deltaP `9.5552` edge `-0.0004` maxDD `-1.8092`
- `risk_on_high->commodity_1h` score `0.0505` n `40` status `ready` deltaP `12.4102` edge `-0.0292` maxDD `-1.7651`
- `risk_on_and_context->commodity_1h` score `0.0505` n `40` status `ready` deltaP `12.4102` edge `-0.0292` maxDD `-1.7651`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
