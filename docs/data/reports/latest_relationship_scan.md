# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T08:52:24.102073+00:00`
- Price records: `672`
- Market context records: `2954`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `17.2265` n `128` status `ready` deltaP `13.8021` edge `1.7352` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `8.1509` n `128` status `ready` deltaP `16.6667` edge `0.6146` maxDD `-1.7175`
- `market_context_high->equity_24h` score `8.1326` n `128` status `ready` deltaP `18.4028` edge `0.7554` maxDD `-12.6963`
- `market_context_high->commodity_24h` score `5.4056` n `128` status `ready` deltaP `23.0035` edge `0.4637` maxDD `-5.6606`
- `market_context_high->index_24h` score `3.1542` n `128` status `ready` deltaP `14.1493` edge `0.2666` maxDD `-2.5127`
- `market_context_high->equity_4h` score `2.5947` n `129` status `ready` deltaP `14.0137` edge `0.1874` maxDD `-2.8349`
- `market_context_high->crypto_alt_4h` score `1.5728` n `129` status `ready` deltaP `20.3996` edge `0.4512` maxDD `-30.8239`
- `market_context_high->unknown_4h` score `0.726` n `129` status `ready` deltaP `5.8399` edge `0.1269` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.692` n `129` status `ready` deltaP `13.8708` edge `0.0804` maxDD `-2.3986`
- `market_context_high->index_1h` score `0.0526` n `129` status `ready` deltaP `5.2418` edge `0.0212` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.166` n `129` status `ready` deltaP `1.6224` edge `0.0508` maxDD `-2.0358`
- `market_context_high->fx_1h` score `-0.2071` n `129` status `ready` deltaP `1.4193` edge `0.004` maxDD `-0.1244`
- `market_context_high->crypto_alt_1h` score `-0.4174` n `129` status `ready` deltaP `5.1885` edge `0.0879` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.5225` n `129` status `ready` deltaP `-0.7566` edge `0.0006` maxDD `-3.3365`
- `market_context_high->metal_1h` score `-0.6409` n `129` status `ready` deltaP `0.4305` edge `0.0037` maxDD `-3.4325`
- `market_context_high->fx_4h` score `-0.6915` n `129` status `ready` deltaP `1.5067` edge `0.0102` maxDD `-0.5631`
- `market_context_high->crypto_major_1h` score `-0.6929` n `129` status `ready` deltaP `4.3065` edge `0.0694` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-0.749` n `129` status `ready` deltaP `6.0964` edge `0.0423` maxDD `-8.9839`
- `market_context_high->unknown_1h` score `-0.8577` n `129` status `ready` deltaP `0.9168` edge `-0.0045` maxDD `-3.1801`
- `market_context_high->crypto_major_4h` score `-0.961` n `129` status `ready` deltaP `10.2961` edge `0.3207` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
