# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T16:37:26.499353+00:00`
- Price records: `672`
- Market context records: `4951`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9472`

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

- `market_context_high->unknown_1h` score `19.9773` n `94` status `ready` deltaP `10.5205` edge `1.6364` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.5576` n `91` status `ready` deltaP `28.4224` edge `0.9084` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.4653` n `91` status `ready` deltaP `22.159` edge `0.5968` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.2575` n `91` status `ready` deltaP `22.8324` edge `0.5878` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.9233` n `91` status `ready` deltaP `28.0144` edge `0.3411` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.8393` n `91` status `ready` deltaP `14.8989` edge `0.1921` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.7782` n `91` status `ready` deltaP `13.5772` edge `0.1239` maxDD `-1.9651`
- `market_context_high->index_4h` score `1.02` n `91` status `ready` deltaP `12.9105` edge `0.0451` maxDD `-0.6938`
- `market_context_high->equity_1h` score `1.0043` n `94` status `ready` deltaP `9.1254` edge `0.0802` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.988` n `94` status `ready` deltaP `9.8261` edge `0.165` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.7689` n `94` status `ready` deltaP `10.6383` edge `0.1299` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.1878` n `94` status `ready` deltaP `5.4051` edge `0.0376` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.3509` n `94` status `ready` deltaP `2.6086` edge `0.0131` maxDD `-0.7054`
- `market_context_high->commodity_1h` score `-0.3542` n `94` status `ready` deltaP `1.9302` edge `0.0077` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.8538` n `91` status `ready` deltaP `7.6822` edge `-0.0037` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-1.1841` n `91` status `ready` deltaP `-7.4796` edge `-0.0049` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.3719` n `91` status `ready` deltaP `-0.4349` edge `-0.0104` maxDD `-2.749`
- `market_context_high->fx_1h` score `-1.534` n `94` status `ready` deltaP `-9.4885` edge `-0.0046` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-3.9923` n `91` status `ready` deltaP `19.6485` edge `0.0472` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.8746` n `91` status `ready` deltaP `-8.8199` edge `0.0314` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
