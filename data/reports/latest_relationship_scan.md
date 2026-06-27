# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T19:22:32.942052+00:00`
- Price records: `672`
- Market context records: `4964`
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

- `market_context_high->unknown_1h` score `18.212` n `98` status `ready` deltaP `7.8089` edge `1.5157` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.1237` n `94` status `ready` deltaP `28.7137` edge `0.8703` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.3696` n `94` status `ready` deltaP `21.8928` edge `0.5906` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.0888` n `94` status `ready` deltaP `22.3437` edge `0.577` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.7823` n `91` status `ready` deltaP `26.9727` edge `0.3363` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7409` n `94` status `ready` deltaP `14.2838` edge `0.188` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.5387` n `94` status `ready` deltaP `12.3281` edge `0.1206` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `1.2998` n `98` status `ready` deltaP `8.2732` edge `0.157` maxDD `-5.6406`
- `market_context_high->equity_1h` score `1.1195` n `98` status `ready` deltaP `10.7754` edge `0.0788` maxDD `-2.5875`
- `market_context_high->index_4h` score `0.9508` n `94` status `ready` deltaP `12.166` edge `0.0443` maxDD `-0.6938`
- `market_context_high->crypto_alt_1h` score `0.6901` n `98` status `ready` deltaP `9.6328` edge `0.1265` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.1699` n `98` status `ready` deltaP `5.3617` edge `0.0364` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.3695` n `98` status `ready` deltaP `2.3127` edge `0.0127` maxDD `-0.7054`
- `market_context_high->commodity_1h` score `-0.4456` n `98` status `ready` deltaP `0.2322` edge `0.0073` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-1.0087` n `94` status `ready` deltaP `6.8662` edge `-0.0053` maxDD `-4.9624`
- `market_context_high->fx_4h` score `-1.116` n `94` status `ready` deltaP `-6.2306` edge `-0.0045` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.5235` n `98` status `ready` deltaP `-9.3731` edge `-0.0045` maxDD `-0.4646`
- `market_context_high->fx_24h` score `-1.542` n `91` status `ready` deltaP `-2.171` edge `-0.013` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-3.9971` n `91` status `ready` deltaP `19.6485` edge `0.0468` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.9819` n `91` status `ready` deltaP `-9.8615` edge `0.0294` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
