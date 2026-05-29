# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T10:22:19.922359+00:00`
- Price records: `672`
- Market context records: `2235`
- Flow alert records: `8328`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9203`

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

- `news_risk_high->crypto_alt_24h` score `25.2644` n `33` status `ready` deltaP `55.745` edge `1.7926` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `14.2702` n `33` status `ready` deltaP `46.1016` edge `0.9258` maxDD `-3.1836`
- `market_context_high->crypto_alt_4h` score `12.9871` n `131` status `ready` deltaP `37.1695` edge `0.9281` maxDD `-5.1574`
- `news_risk_high->equity_24h` score `12.0768` n `33` status `ready` deltaP `37.0739` edge `0.7907` maxDD `-2.1831`
- `market_context_high->crypto_major_4h` score `11.7435` n `131` status `ready` deltaP `42.2129` edge `0.7502` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.1563` n `33` status `ready` deltaP `36.6477` edge `0.5413` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `7.1766` n `33` status `ready` deltaP `18.5922` edge `0.8542` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `5.998` n `131` status `ready` deltaP `23.2824` edge `0.39` maxDD `-1.6306`
- `market_context_high->unknown_24h` score `4.2878` n `127` status `ready` deltaP `25.3855` edge `0.5116` maxDD `-21.8818`
- `market_context_high->equity_4h` score `4.2839` n `131` status `ready` deltaP `24.3705` edge `0.2462` maxDD `-2.1345`
- `news_risk_high->commodity_4h` score `3.9623` n `43` status `ready` deltaP `33.377` edge `0.3526` maxDD `-3.0367`
- `market_context_high->index_4h` score `3.6908` n `131` status `ready` deltaP `27.8754` edge `0.1647` maxDD `-0.7707`
- `market_context_high->crypto_major_1h` score `3.0445` n `143` status `ready` deltaP `16.8335` edge `0.1892` maxDD `-1.817`
- `news_risk_high->fx_24h` score `2.9544` n `33` status `ready` deltaP `31.0606` edge `0.0576` maxDD `-0.1442`
- `market_context_high->crypto_alt_1h` score `2.8167` n `143` status `ready` deltaP `15.7343` edge `0.2162` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `2.3013` n `127` status `ready` deltaP `15.4664` edge `0.8533` maxDD `-46.9097`
- `news_risk_high->commodity_24h` score `2.2631` n `33` status `ready` deltaP `-2.4622` edge `0.2867` maxDD `-3.202`
- `market_context_high->index_24h` score `2.2264` n `127` status `ready` deltaP `10.0339` edge `0.2072` maxDD `-3.0845`
- `news_risk_high->fx_4h` score `2.15` n `43` status `ready` deltaP `27.2794` edge `0.0157` maxDD `-0.1382`
- `market_context_high->metal_4h` score `1.3606` n `131` status `ready` deltaP `17.4793` edge `0.1356` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
