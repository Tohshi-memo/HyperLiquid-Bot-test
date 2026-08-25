# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T17:02:52.173453+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14776`

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

- `news_risk_high->unknown_24h` score `44.2832` n `51` status `ready` deltaP `5.0347` edge `3.6567` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.546` n `53` status `ready` deltaP `24.0652` edge `0.895` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `8.2141` n `51` status `ready` deltaP `31.9036` edge `0.5649` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.2336` n `51` status `ready` deltaP `42.1773` edge `0.0868` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1526` n `53` status `ready` deltaP `16.0123` edge `0.1915` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0002` n `53` status `ready` deltaP `35.573` edge `0.0263` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.5874` n `133` status `ready` deltaP `22.2068` edge `0.1084` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.7907` n `53` status `ready` deltaP `20.6512` edge `0.0886` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.2004` n `53` status `ready` deltaP `16.5179` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.4917` n `53` status `ready` deltaP `14.1227` edge `0.0053` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3577` n `53` status `ready` deltaP `10.078` edge `-0.0061` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.2548` n `53` status `ready` deltaP `8.1857` edge `0.0064` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.135` n `133` status `ready` deltaP `11.5719` edge `-0.021` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.0488` n `53` status `ready` deltaP `4.299` edge `0.0004` maxDD `-0.1583`
- `news_risk_high->metal_24h` score `-0.1467` n `51` status `ready` deltaP `24.6017` edge `-0.172` maxDD `-0.0053`
- `market_context_high->fx_1h` score `-0.4109` n `133` status `ready` deltaP `3.0976` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->crypto_alt_24h` score `-0.4282` n `51` status `ready` deltaP `21.5278` edge `-0.1792` maxDD `0.0`
- `news_risk_high->metal_1h` score `-0.4415` n `53` status `ready` deltaP `-0.4632` edge `-0.0111` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.4676` n `53` status `ready` deltaP `5.2721` edge `-0.021` maxDD `-0.249`
- `market_context_high->metal_4h` score `-0.968` n `133` status `ready` deltaP `4.2649` edge `-0.0454` maxDD `-2.4293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
