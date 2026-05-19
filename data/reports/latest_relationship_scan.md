# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T09:22:20.536493+00:00`
- Price records: `672`
- Market context records: `1206`
- Flow alert records: `5378`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.5666` n `132` status `ready` deltaP `44.1762` edge `1.3659` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.3038` n `132` status `ready` deltaP `22.0329` edge `0.6634` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `6.3276` n `132` status `ready` deltaP `3.4876` edge `0.6257` maxDD `-6.7322`
- `market_context_high->metal_24h` score `4.4256` n `132` status `ready` deltaP `-3.5827` edge `0.5594` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `4.2194` n `132` status `ready` deltaP `-3.4249` edge `0.6034` maxDD `-13.3158`
- `market_context_high->equity_4h` score `2.7895` n `132` status `ready` deltaP `14.3986` edge `0.2028` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.1746` n `132` status `ready` deltaP `17.6925` edge `0.1719` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.792` n `132` status `ready` deltaP `17.9135` edge `0.343` maxDD `-14.2815`
- `market_context_high->index_4h` score `0.9204` n `132` status `ready` deltaP `10.3197` edge `0.0762` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.6003` n `132` status `ready` deltaP `9.012` edge `0.0552` maxDD `-1.8872`
- `market_context_high->index_1h` score `0.4979` n `132` status `ready` deltaP `8.4875` edge `0.0166` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3816` n `132` status `ready` deltaP `3.9693` edge `0.0431` maxDD `-1.3546`
- `market_context_high->metal_1h` score `-0.0959` n `132` status `ready` deltaP `9.472` edge `-0.0101` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.1628` n `132` status `ready` deltaP `4.7405` edge `0.0004` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1876` n `132` status `ready` deltaP `5.7696` edge `0.1296` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.3713` n `132` status `ready` deltaP `0.6714` edge `0.0322` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.3764` n `132` status `ready` deltaP `3.3479` edge `0.006` maxDD `-4.1256`
- `market_context_high->unknown_24h` score `-0.7272` n `132` status `ready` deltaP `0.805` edge `0.207` maxDD `-10.1706`
- `market_context_high->commodity_1h` score `-0.7689` n `132` status `ready` deltaP `-2.2637` edge `0.0125` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.8819` n `132` status `ready` deltaP `9.3357` edge `-0.0322` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
