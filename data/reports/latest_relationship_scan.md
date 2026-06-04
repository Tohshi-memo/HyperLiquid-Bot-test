# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T20:28:10.305580+00:00`
- Price records: `672`
- Market context records: `2900`
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

- `market_context_high->crypto_alt_24h` score `10.8512` n `142` status `ready` deltaP `10.3409` edge `1.227` maxDD `-22.6673`
- `market_context_high->equity_24h` score `5.8722` n `142` status `ready` deltaP `12.0329` edge `0.6095` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.2461` n `142` status `ready` deltaP `10.7614` edge `0.4119` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.1994` n `142` status `ready` deltaP `10.2382` edge `0.2131` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7424` n `142` status `ready` deltaP `15.5516` edge `0.3509` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.4578` n `142` status `ready` deltaP `12.996` edge `0.0562` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.1883` n `142` status `ready` deltaP `5.1185` edge `0.0869` maxDD `-3.7602`
- `market_context_high->equity_4h` score `-0.0365` n `142` status `ready` deltaP `5.1636` edge `0.1005` maxDD `-5.7037`
- `market_context_high->index_1h` score `-0.082` n `142` status `ready` deltaP `3.5992` edge `0.0149` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2294` n `142` status `ready` deltaP `4.7799` edge `0.0221` maxDD `-3.1801`
- `market_context_high->fx_1h` score `-0.5646` n `142` status `ready` deltaP `-0.837` edge `0.0029` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.5798` n `142` status `ready` deltaP `5.3956` edge `0.0657` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.5906` n `142` status `ready` deltaP `-0.4322` edge `0.0025` maxDD `-4.3601`
- `market_context_high->equity_1h` score `-0.5982` n `142` status `ready` deltaP `-0.8033` edge `0.0388` maxDD `-2.6634`
- `market_context_high->crypto_alt_4h` score `-0.6527` n `142` status `ready` deltaP `14.3378` edge `0.2841` maxDD `-28.7261`
- `market_context_high->crypto_major_1h` score `-0.6816` n `142` status `ready` deltaP `5.5727` edge `0.0624` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6933` n `142` status `ready` deltaP `-0.6157` edge `-0.0002` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-1.1407` n `142` status `ready` deltaP `-3.4481` edge `0.0058` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.1427` n `142` status `ready` deltaP `3.3622` edge `0.0231` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.3243` n `142` status `ready` deltaP `-1.8852` edge `-0.0106` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
