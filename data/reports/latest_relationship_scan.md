# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T02:22:28.638070+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11257`

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

- `news_risk_high->unknown_1h` score `383.1348` n `82` status `ready` deltaP `-3.3044` edge `31.9921` maxDD `-1.7068`
- `market_context_high->unknown_24h` score `98.4142` n `146` status `ready` deltaP `14.0815` edge `8.1125` maxDD `-0.082`
- `risk_on_high->crypto_alt_24h` score `25.2403` n `91` status `ready` deltaP `43.1166` edge `1.8389` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `25.2403` n `91` status `ready` deltaP `43.1166` edge `1.8389` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `23.1382` n `50` status `ready` deltaP `53.2847` edge `1.663` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `21.4029` n `146` status `ready` deltaP `37.6522` edge `1.6153` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `15.4058` n `50` status `ready` deltaP `26.6111` edge `1.1552` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `11.2622` n `50` status `ready` deltaP `32.9792` edge `0.7285` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.2595` n `91` status `ready` deltaP `36.9792` edge `0.5251` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2595` n `91` status `ready` deltaP `36.9792` edge `0.5251` maxDD `0.0`
- `market_context_high->equity_24h` score `8.9499` n `146` status `ready` deltaP `36.9792` edge `0.4993` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.9374` n `91` status `ready` deltaP `43.9276` edge `0.4891` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9374` n `91` status `ready` deltaP `43.9276` edge `0.4891` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.0949` n `50` status `ready` deltaP `51.0417` edge `0.3343` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.9304` n `91` status `ready` deltaP `25.021` edge `1.2567` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.9304` n `91` status `ready` deltaP `25.021` edge `1.2567` maxDD `-24.5429`
- `news_risk_high->index_24h` score `7.8701` n `50` status `ready` deltaP `50.8611` edge `0.3261` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `6.8003` n `91` status `ready` deltaP `32.0491` edge `0.4389` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.8003` n `91` status `ready` deltaP `32.0491` edge `0.4389` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.2936` n `91` status `ready` deltaP `51.5644` edge `0.1016` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
