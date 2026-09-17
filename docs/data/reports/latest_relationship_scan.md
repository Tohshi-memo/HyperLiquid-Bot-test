# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T17:22:33.306473+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8862`

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

- `news_risk_high->unknown_4h` score `422.4615` n `77` status `ready` deltaP `-20.8821` edge `35.4338` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `9.7251` n `77` status `ready` deltaP `29.8251` edge `0.7495` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `9.5414` n `77` status `ready` deltaP `21.4218` edge `0.8518` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.4141` n `52` status `ready` deltaP `50.5208` edge `0.4477` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.4141` n `52` status `ready` deltaP `50.5208` edge `0.4477` maxDD `0.0`
- `market_context_high->commodity_24h` score `8.1149` n `149` status `ready` deltaP `43.8094` edge `0.4367` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `7.932` n `77` status `ready` deltaP `29.8521` edge `0.6394` maxDD `-6.5262`
- `news_risk_high->index_24h` score `5.5393` n `77` status `ready` deltaP `37.2768` edge `0.2307` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.6911` n `77` status `ready` deltaP `28.4565` edge `0.1633` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.9263` n `52` status `ready` deltaP `32.5399` edge `0.0619` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9263` n `52` status `ready` deltaP `32.5399` edge `0.0619` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.826` n `149` status `ready` deltaP `29.0422` edge `0.0837` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.0668` n `52` status `ready` deltaP `28.2852` edge `-0.0121` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.0668` n `52` status `ready` deltaP `28.2852` edge `-0.0121` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.9319` n `149` status `ready` deltaP `25.5103` edge `0.0125` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1193` n `149` status `ready` deltaP `16.0612` edge `0.0239` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5843` n `77` status `ready` deltaP `10.9776` edge `0.0221` maxDD `-0.3938`
- `risk_on_high->commodity_1h` score `0.4961` n `52` status `ready` deltaP `9.1433` edge `0.0156` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4961` n `52` status `ready` deltaP `9.1433` edge `0.0156` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.1961` n `149` status `ready` deltaP `10.1909` edge `0.0048` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
