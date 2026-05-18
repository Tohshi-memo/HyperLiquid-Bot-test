# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T08:39:46.634278+00:00`
- Price records: `672`
- Market context records: `1101`
- Flow alert records: `5073`
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

- `market_context_high->crypto_major_24h` score `17.0681` n `150` status `ready` deltaP `37.0348` edge `1.2218` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `6.4249` n `150` status `ready` deltaP `13.3958` edge `0.5695` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.1019` n `150` status `ready` deltaP `15.6527` edge `0.4538` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.2506` n `150` status `ready` deltaP `-2.9305` edge `0.6238` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.8417` n `150` status `ready` deltaP `15.1319` edge `0.3334` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.9618` n `168` status `ready` deltaP `11.2515` edge `0.1548` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.0135` n `168` status `ready` deltaP `9.2044` edge `0.0914` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4738` n `168` status `ready` deltaP `7.4957` edge `0.0212` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2597` n `168` status `ready` deltaP `2.4308` edge `0.0432` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1388` n `168` status `ready` deltaP `8.3155` edge `0.0017` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0418` n `168` status `ready` deltaP `6.9825` edge `0.0335` maxDD `-4.1256`
- `market_context_high->crypto_major_4h` score `0.0278` n `168` status `ready` deltaP `8.4567` edge `0.1393` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.2208` n `168` status `ready` deltaP `6.8007` edge `-0.0027` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.3006` n `168` status `ready` deltaP `2.7944` edge `0.0406` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.6827` n `168` status `ready` deltaP `-1.0265` edge `0.0001` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.6969` n `168` status `ready` deltaP `1.3937` edge `0.001` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.1196` n `168` status `ready` deltaP `4.9289` edge `0.1201` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.2447` n `168` status `ready` deltaP `7.4622` edge `-0.0414` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1243` n `168` status `ready` deltaP `-10.6635` edge `-0.0127` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.2401` n `150` status `ready` deltaP `2.7361` edge `-0.026` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
