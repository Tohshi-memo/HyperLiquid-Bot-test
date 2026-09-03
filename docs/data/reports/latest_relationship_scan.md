# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T22:52:27.009999+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11523`

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

- `risk_on_high->unknown_4h` score `27.0783` n `133` status `ready` deltaP `10.5229` edge `2.2482` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `27.0783` n `133` status `ready` deltaP `10.5229` edge `2.2482` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `20.3132` n `167` status `ready` deltaP `12.1212` edge `1.6815` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `14.8914` n `133` status `ready` deltaP `0.144` edge `1.2977` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `14.8914` n `133` status `ready` deltaP `0.144` edge `1.2977` maxDD `-1.95`
- `market_context_high->unknown_1h` score `10.4116` n `167` status `ready` deltaP `0.5988` edge `0.9267` maxDD `-2.0446`
- `market_context_high->equity_24h` score `0.5713` n `127` status `ready` deltaP `15.9558` edge `0.3758` maxDD `-20.7654`
- `news_risk_high->commodity_4h` score `0.3493` n `67` status `ready` deltaP `6.4047` edge `0.038` maxDD `-0.8733`
- `risk_on_high->equity_24h` score `0.0884` n `107` status `ready` deltaP `11.202` edge `0.3472` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.0884` n `107` status `ready` deltaP `11.202` edge `0.3472` maxDD `-19.828`
- `risk_on_high->metal_1h` score `0.0789` n `133` status `ready` deltaP `11.9637` edge `0.0016` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0789` n `133` status `ready` deltaP `11.9637` edge `0.0016` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0508` n `67` status `ready` deltaP `4.7748` edge `-0.003` maxDD `-0.8275`
- `news_risk_high->fx_4h` score `-0.0711` n `67` status `ready` deltaP `8.4319` edge `0.0035` maxDD `-1.2507`
- `risk_on_high->index_1h` score `-0.089` n `133` status `ready` deltaP `5.19` edge `-0.0015` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.089` n `133` status `ready` deltaP `5.19` edge `-0.0015` maxDD `-0.5605`
- `risk_on_high->fx_24h` score `-0.1314` n `107` status `ready` deltaP `25.7075` edge `0.0815` maxDD `-4.2453`
- `risk_on_and_context->fx_24h` score `-0.1314` n `107` status `ready` deltaP `25.7075` edge `0.0815` maxDD `-4.2453`
- `news_risk_high->equity_24h` score `-0.1439` n `67` status `ready` deltaP `3.6277` edge `0.2041` maxDD `-15.4056`
- `news_risk_high->commodity_1h` score `-0.149` n `67` status `ready` deltaP `4.7569` edge `0.0005` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
