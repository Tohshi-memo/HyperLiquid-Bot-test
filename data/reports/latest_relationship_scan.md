# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T01:52:20.666176+00:00`
- Price records: `672`
- Market context records: `2924`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6927`

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

- `market_context_high->crypto_alt_24h` score `14.1691` n `142` status `ready` deltaP `13.6395` edge `1.4815` maxDD `-22.6673`
- `market_context_high->equity_24h` score `6.9829` n `142` status `ready` deltaP `15.8524` edge `0.6766` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.1417` n `142` status `ready` deltaP `13.8864` edge `0.4657` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.4077` n `142` status `ready` deltaP `11.6271` edge `0.2212` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8408` n `142` status `ready` deltaP `15.5516` edge `0.3591` maxDD `-12.4171`
- `market_context_high->equity_4h` score `0.6617` n `142` status `ready` deltaP `7.7551` edge `0.1414` maxDD `-5.7037`
- `market_context_high->index_4h` score `0.6256` n `142` status `ready` deltaP `14.0631` edge `0.0706` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.0499` n `142` status `ready` deltaP `3.899` edge `0.0835` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0326` n `143` status `ready` deltaP `4.0985` edge `0.0179` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.0421` n `142` status `ready` deltaP `15.1` edge `0.3299` maxDD `-28.7261`
- `market_context_high->unknown_1h` score `-0.426` n `143` status `ready` deltaP `3.5981` edge `0.0136` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-0.4339` n `143` status `ready` deltaP `0.3047` edge `0.0451` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.5226` n `143` status `ready` deltaP `5.7452` edge `0.0707` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.559` n `143` status `ready` deltaP `-0.7966` edge `0.0031` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6396` n `143` status `ready` deltaP `0.3967` edge `0.0041` maxDD `-3.4325`
- `market_context_high->commodity_1h` score `-0.6641` n `143` status `ready` deltaP `-1.3954` edge `-0.0005` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.6991` n `143` status `ready` deltaP `5.4929` edge `0.0607` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.0092` n `142` status `ready` deltaP `-1.9237` edge `0.0066` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2607` n `142` status `ready` deltaP `2.1427` edge `0.0161` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.284` n `142` status `ready` deltaP `-1.7116` edge `-0.0084` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
