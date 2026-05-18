# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T08:22:18.115069+00:00`
- Price records: `672`
- Market context records: `1099`
- Flow alert records: `5070`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->crypto_major_24h` score `16.9763` n `150` status `ready` deltaP `36.8611` edge `1.2153` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `6.3114` n `150` status `ready` deltaP `13.2222` edge `0.5612` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.0851` n `150` status `ready` deltaP `15.6527` edge `0.4524` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.2302` n `150` status `ready` deltaP `-2.9305` edge `0.6221` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.8273` n `150` status `ready` deltaP `15.1319` edge `0.3322` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.9968` n `168` status `ready` deltaP `11.4039` edge `0.1567` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.0353` n `168` status `ready` deltaP `9.3568` edge `0.0922` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4917` n `168` status `ready` deltaP `7.6454` edge `0.0217` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2848` n `168` status `ready` deltaP `2.5805` edge `0.0443` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1388` n `168` status `ready` deltaP `8.3155` edge `0.0017` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0334` n `168` status `ready` deltaP `6.9825` edge `0.0328` maxDD `-4.1256`
- `market_context_high->crypto_major_4h` score `0.0128` n `168` status `ready` deltaP `8.3043` edge `0.1384` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.2028` n `168` status `ready` deltaP `6.9504` edge `-0.0022` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.3173` n `168` status `ready` deltaP `2.6447` edge `0.0402` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.685` n `168` status `ready` deltaP `-1.0265` edge `-0.0002` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.6977` n `168` status `ready` deltaP `1.3937` edge `0.0009` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.1407` n `168` status `ready` deltaP `4.7765` edge `0.1184` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.2229` n `168` status `ready` deltaP `7.6147` edge `-0.0406` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1274` n `168` status `ready` deltaP `-10.6635` edge `-0.0131` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.2295` n `150` status `ready` deltaP `2.9097` edge `-0.0258` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
