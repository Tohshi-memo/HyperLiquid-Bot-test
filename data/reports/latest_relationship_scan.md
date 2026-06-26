# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T18:52:56.609433+00:00`
- Price records: `672`
- Market context records: `4855`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7632`

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

- `market_context_high->unknown_1h` score `13.4993` n `110` status `ready` deltaP `10.6206` edge `1.0959` maxDD `-1.674`
- `market_context_high->unknown_4h` score `10.8201` n `105` status `ready` deltaP `27.2561` edge `0.7731` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `5.9762` n `105` status `ready` deltaP `18.9518` edge `0.5069` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `5.7862` n `105` status `ready` deltaP `16.0192` edge `0.4978` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.2098` n `91` status `ready` deltaP `25.8166` edge `0.2963` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.4955` n `105` status `ready` deltaP `11.1832` edge `0.1163` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.7903` n `105` status `ready` deltaP `10.9146` edge `0.1667` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.508` n `105` status `ready` deltaP `10.572` edge `0.0409` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4368` n `110` status `ready` deltaP `6.1704` edge `0.1187` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.395` n `110` status `ready` deltaP `7.8715` edge `0.1004` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2168` n `110` status `ready` deltaP `4.0855` edge `0.0603` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1861` n `110` status `ready` deltaP `0.5443` edge `0.0305` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.195` n `110` status `ready` deltaP `3.7316` edge `0.0161` maxDD `-1.278`
- `market_context_high->fx_4h` score `-0.3698` n `105` status `ready` deltaP `3.2956` edge `0.0063` maxDD `-1.0547`
- `market_context_high->index_1h` score `-0.4993` n `110` status `ready` deltaP `0.1606` edge `0.0104` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.7671` n `105` status `ready` deltaP `7.0326` edge `0.0064` maxDD `-4.377`
- `market_context_high->fx_1h` score `-1.3322` n `110` status `ready` deltaP `-6.8672` edge `-0.0039` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-2.0002` n `91` status `ready` deltaP `-7.8984` edge `-0.013` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.8937` n `91` status `ready` deltaP `-9.5754` edge `-0.155` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.5659` n `91` status `ready` deltaP `9.6382` edge `-0.0172` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
