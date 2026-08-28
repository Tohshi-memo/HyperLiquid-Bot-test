# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T16:37:26.818255+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11634`

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

- `news_risk_high->unknown_24h` score `53.9428` n `50` status `ready` deltaP `12.305` edge `4.4132` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.0386` n `50` status `ready` deltaP `43.1404` edge `2.4264` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.2214` n `56` status `ready` deltaP `23.5845` edge `0.7921` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.5867` n `50` status `ready` deltaP `30.1005` edge `0.3577` maxDD `-4.7584`
- `news_risk_high->crypto_major_24h` score `4.7531` n `50` status `ready` deltaP `22.1282` edge `0.2979` maxDD `-2.6128`
- `news_risk_high->metal_24h` score `4.3206` n `50` status `ready` deltaP `43.4073` edge `0.0749` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0407` n `56` status `ready` deltaP `46.973` edge `0.0326` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `3.6356` n `61` status `ready` deltaP `12.9847` edge `0.2521` maxDD `-0.8558`
- `market_context_high->unknown_24h` score `3.2515` n `120` status `ready` deltaP `5.6383` edge `0.3066` maxDD `-3.1917`
- `market_context_high->metal_24h` score `3.1378` n `120` status `ready` deltaP `28.7406` edge `0.1718` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.7876` n `120` status `ready` deltaP `18.4655` edge `0.1499` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.3638` n `50` status `ready` deltaP `26.9948` edge `0.0321` maxDD `-0.2064`
- `news_risk_high->fx_1h` score `1.4327` n `61` status `ready` deltaP `19.3016` edge `0.0077` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `0.9647` n `120` status `ready` deltaP `9.2416` edge `0.0638` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.8837` n `56` status `ready` deltaP `20.0566` edge `0.0559` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.7039` n `56` status `ready` deltaP `14.1551` edge `0.0174` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.4001` n `61` status `ready` deltaP `12.003` edge `0.0033` maxDD `-0.5618`
- `news_risk_high->index_4h` score `0.1329` n `56` status `ready` deltaP `7.5566` edge `0.0006` maxDD `-0.1919`
- `market_context_high->metal_4h` score `-0.0545` n `120` status `ready` deltaP `12.8455` edge `-0.0009` maxDD `-3.3377`
- `news_risk_high->metal_1h` score `-0.163` n `61` status `ready` deltaP `4.2481` edge `-0.0119` maxDD `-1.3186`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
