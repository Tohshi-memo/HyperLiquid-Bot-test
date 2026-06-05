# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T00:07:24.541019+00:00`
- Price records: `672`
- Market context records: `2917`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `13.1814` n `142` status `ready` deltaP `12.4242` edge `1.4073` maxDD `-22.6673`
- `market_context_high->equity_24h` score `6.5389` n `142` status `ready` deltaP `14.6371` edge `0.6477` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.8688` n `142` status `ready` deltaP `12.8447` edge `0.4499` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.206` n `142` status `ready` deltaP `10.4118` edge `0.2125` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8012` n `142` status `ready` deltaP `15.5516` edge `0.3558` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.5016` n `142` status `ready` deltaP `13.1484` edge `0.0608` maxDD `-2.3986`
- `market_context_high->equity_4h` score `0.3687` n `142` status `ready` deltaP `6.688` edge `0.1241` maxDD `-5.7037`
- `market_context_high->unknown_4h` score `0.1527` n `142` status `ready` deltaP `4.5087` edge `0.088` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0305` n `142` status `ready` deltaP `4.198` edge `0.0175` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.0921` n `142` status `ready` deltaP `15.4049` edge `0.3237` maxDD `-28.7261`
- `market_context_high->unknown_1h` score `-0.2726` n `142` status `ready` deltaP `4.3308` edge `0.0215` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-0.3692` n `142` status `ready` deltaP `0.8434` edge `0.0469` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4489` n `142` status `ready` deltaP `6.2938` edge `0.0765` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5251` n `142` status `ready` deltaP `-0.3879` edge `0.0032` maxDD `-0.2164`
- `market_context_high->crypto_major_1h` score `-0.6131` n `142` status `ready` deltaP `6.1715` edge `0.0672` maxDD `-9.622`
- `market_context_high->commodity_1h` score `-0.6319` n `142` status `ready` deltaP `-1.031` edge `0.0012` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6388` n `142` status `ready` deltaP `0.1328` edge `0.0018` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-0.9716` n `142` status `ready` deltaP `-1.6188` edge `0.0077` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2551` n `142` status `ready` deltaP `2.2951` edge `0.0158` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.2708` n `142` status `ready` deltaP `-1.7116` edge `-0.0073` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
