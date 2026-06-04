# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T23:07:28.011647+00:00`
- Price records: `672`
- Market context records: `2912`
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

- `market_context_high->crypto_alt_24h` score `12.5391` n `142` status `ready` deltaP `11.7298` edge `1.3584` maxDD `-22.6673`
- `market_context_high->equity_24h` score `6.3874` n `142` status `ready` deltaP `13.9426` edge `0.6397` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.6284` n `142` status `ready` deltaP `12.1503` edge `0.4345` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.1862` n `142` status `ready` deltaP `10.2382` edge `0.212` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7808` n `142` status `ready` deltaP `15.5516` edge `0.3541` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.4821` n `142` status `ready` deltaP `13.1484` edge `0.0583` maxDD `-2.3986`
- `market_context_high->equity_4h` score `0.2675` n `142` status `ready` deltaP `6.3831` edge `0.1177` maxDD `-5.7037`
- `market_context_high->unknown_4h` score `0.1155` n `142` status `ready` deltaP `4.5087` edge `0.0849` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0461` n `142` status `ready` deltaP `4.0483` edge `0.0165` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.2073` n `142` status `ready` deltaP `15.4049` edge `0.3141` maxDD `-28.7261`
- `market_context_high->unknown_1h` score `-0.3133` n `142` status `ready` deltaP `4.0314` edge `0.0201` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-0.416` n `142` status `ready` deltaP `0.544` edge `0.045` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4746` n `142` status `ready` deltaP `5.9944` edge `0.0752` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5526` n `142` status `ready` deltaP `-0.6873` edge `0.0029` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6015` n `142` status `ready` deltaP `-0.5819` edge `0.0021` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.6333` n `142` status `ready` deltaP `5.8721` edge `0.0666` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6715` n `142` status `ready` deltaP `-0.3163` edge `0.0006` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-0.9874` n `142` status `ready` deltaP `-1.7713` edge `0.0074` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2417` n `142` status `ready` deltaP `2.4476` edge `0.0165` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.2792` n `142` status `ready` deltaP `-1.7116` edge `-0.008` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
