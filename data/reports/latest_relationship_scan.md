# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T09:07:15.989192+00:00`
- Price records: `672`
- Market context records: `1205`
- Flow alert records: `5375`
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

- `market_context_high->crypto_major_24h` score `18.5582` n `132` status `ready` deltaP `44.1762` edge `1.3652` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.2642` n `132` status `ready` deltaP `22.0329` edge `0.6601` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `6.3082` n `132` status `ready` deltaP `3.3352` edge `0.6251` maxDD `-6.7322`
- `market_context_high->metal_24h` score `4.3445` n `132` status `ready` deltaP `-3.7563` edge `0.5538` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `4.2957` n `132` status `ready` deltaP `-3.2513` edge `0.6086` maxDD `-13.3158`
- `market_context_high->equity_4h` score `2.7835` n `132` status `ready` deltaP `14.3986` edge `0.2023` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.1055` n `132` status `ready` deltaP `17.5189` edge `0.1673` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.7268` n `132` status `ready` deltaP `17.7399` edge `0.3358` maxDD `-14.2815`
- `market_context_high->index_4h` score `0.9022` n `132` status `ready` deltaP `10.1673` edge `0.0757` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.6298` n `132` status `ready` deltaP `9.1856` edge `0.0565` maxDD `-1.8872`
- `market_context_high->index_1h` score `0.4787` n `132` status `ready` deltaP `8.3378` edge `0.016` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.36` n `132` status `ready` deltaP `3.8196` edge `0.0423` maxDD `-1.3546`
- `market_context_high->metal_1h` score `-0.1115` n `132` status `ready` deltaP `9.3223` edge `-0.0104` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.164` n `132` status `ready` deltaP `4.7405` edge `0.0003` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1962` n `132` status `ready` deltaP `5.7696` edge `0.1285` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.3861` n `132` status `ready` deltaP `0.5217` edge `0.0313` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.3943` n `132` status `ready` deltaP `3.1982` edge `0.0047` maxDD `-4.1256`
- `market_context_high->commodity_1h` score `-0.7545` n `132` status `ready` deltaP `-2.114` edge `0.0127` maxDD `-2.252`
- `market_context_high->unknown_24h` score `-0.798` n `132` status `ready` deltaP `0.805` edge `0.2011` maxDD `-10.1706`
- `market_context_high->metal_4h` score `-0.8811` n `132` status `ready` deltaP `9.3357` edge `-0.0321` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
