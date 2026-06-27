# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T20:37:30.716543+00:00`
- Price records: `672`
- Market context records: `4970`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `17.4625` n `100` status `ready` deltaP `7.6048` edge `1.4546` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.6734` n `91` status `ready` deltaP `29.7055` edge `0.9095` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.4897` n `91` status `ready` deltaP `21.638` edge `0.6023` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.1652` n `91` status `ready` deltaP `22.159` edge `0.5846` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.9322` n `88` status `ready` deltaP `27.541` edge `0.345` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7513` n `91` status `ready` deltaP `13.8887` edge `0.1915` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.5206` n `91` status `ready` deltaP `11.6524` edge `0.1236` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.9172` n `91` status `ready` deltaP `11.5955` edge `0.0453` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.8507` n `100` status `ready` deltaP `8.1497` edge `0.0739` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.5013` n `100` status `ready` deltaP `5.6407` edge `0.1305` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4042` n `100` status `ready` deltaP `7.5988` edge `0.1034` maxDD `-5.5126`
- `market_context_high->metal_1h` score `-0.0454` n `100` status `ready` deltaP `2.9401` edge `0.0346` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.3804` n `100` status `ready` deltaP `2.1018` edge `0.0127` maxDD `-0.7054`
- `market_context_high->commodity_1h` score `-0.4075` n `100` status `ready` deltaP `0.994` edge `0.0071` maxDD `-1.278`
- `market_context_high->fx_4h` score `-1.1303` n `91` status `ready` deltaP `-6.6856` edge `-0.0033` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.1322` n `91` status `ready` deltaP `5.7575` edge `-0.0082` maxDD `-4.9624`
- `market_context_high->fx_24h` score `-1.2307` n `88` status `ready` deltaP `-1.1048` edge `-0.011` maxDD `-2.4023`
- `market_context_high->fx_1h` score `-1.4963` n `100` status `ready` deltaP `-9.1078` edge `-0.004` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-4.3377` n `88` status `ready` deltaP `17.8503` edge `0.0304` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-7.0197` n `88` status `ready` deltaP `-9.3434` edge `0.0228` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
